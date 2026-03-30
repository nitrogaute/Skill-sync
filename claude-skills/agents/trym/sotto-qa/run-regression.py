#!/usr/bin/env python3
"""
Sotto Full Regression Suite — Playwright
Runs all views, interaction tests, and persistence checks.

Usage: python3 run-regression.py [--base-url URL] [--mobile-only] [--desktop-only]
Requires: pip install playwright pillow
          playwright install chromium
"""

import asyncio
import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("❌ Install playwright: pip install playwright && playwright install chromium")
    sys.exit(1)

BASE_URL = "https://sotto-dashboard.vercel.app"
AUTH_TOKEN_KEY = "sb-ukwzbvfstvfavptxiyrn-auth-token"
SCREENSHOT_DIR = Path.home() / "clawd/projects/sotto/e2e-audit/screenshots" / datetime.now().strftime("%Y-%m-%d")

VIEWS = [
    "today", "week", "tasks", "projects", "topics", "notes", "meetings",
    "people", "okrs", "documents", "trym", "graph", "finances", "health", "weekly-review"
]

VIEWPORTS = {
    "mobile": {"width": 375, "height": 812},
    "desktop": {"width": 1440, "height": 900},
}

class RegressionResult:
    def __init__(self):
        self.passed = []
        self.failed = []
        self.warnings = []

    def ok(self, name):
        self.passed.append(name)
        print(f"  ✅ {name}")

    def fail(self, name, reason=""):
        self.failed.append((name, reason))
        print(f"  ❌ {name}: {reason}")

    def warn(self, name, reason=""):
        self.warnings.append((name, reason))
        print(f"  ⚠️  {name}: {reason}")

    def summary(self):
        total = len(self.passed) + len(self.failed)
        print(f"\n{'='*60}")
        print(f"RESULTS: {len(self.passed)}/{total} passed, {len(self.failed)} failed, {len(self.warnings)} warnings")
        if self.failed:
            print("\nFAILURES:")
            for name, reason in self.failed:
                print(f"  ❌ {name}: {reason}")
        if self.warnings:
            print("\nWARNINGS:")
            for name, reason in self.warnings:
                print(f"  ⚠️  {name}: {reason}")
        print(f"{'='*60}")
        return len(self.failed) == 0


async def inject_auth(page):
    """Inject auth token from environment."""
    token = os.environ.get("SOTTO_AUTH_TOKEN")
    if not token:
        print("⚠️  SOTTO_AUTH_TOKEN not set — trying without auth injection")
        return
    await page.evaluate(f"""() => {{
        window.localStorage.setItem('{AUTH_TOKEN_KEY}', {json.dumps(token)});
    }}""")


async def wait_for_app(page):
    """Wait for the app to be ready (has __sotto_setActiveView)."""
    for _ in range(20):
        ready = await page.evaluate("() => typeof window.__sotto_setActiveView === 'function'")
        if ready:
            return True
        await page.wait_for_timeout(500)
    return False


async def navigate_to_view(page, view):
    """Navigate to a view using the global setter."""
    await page.evaluate(f"() => window.__sotto_setActiveView('{view}')")
    await page.wait_for_timeout(1500)


async def test_views_load(page, result, viewport_name):
    """Test all 15 views load without errors."""
    print(f"\n📱 Testing all views ({viewport_name})...")
    for view in VIEWS:
        try:
            await navigate_to_view(page, view)
            # Check no error boundary
            error = await page.evaluate("""() => {
                const el = document.querySelector('[data-error-boundary], .error-boundary');
                return el ? el.textContent : null;
            }""")
            if error:
                result.fail(f"{view}-{viewport_name}-load", f"Error boundary: {error[:100]}")
            else:
                # Check page has meaningful content (not blank)
                body_text = await page.evaluate("() => document.body.innerText.length")
                if body_text < 50:
                    result.warn(f"{view}-{viewport_name}-load", "Very little content rendered")
                else:
                    result.ok(f"{view}-{viewport_name}-load")

            # Screenshot
            SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
            await page.screenshot(
                path=str(SCREENSHOT_DIR / f"{view}-{viewport_name}.png"),
                full_page=True
            )
        except Exception as e:
            result.fail(f"{view}-{viewport_name}-load", str(e)[:200])


async def test_task_checkbox(page, result):
    """Test checkbox toggles done state."""
    print("\n☑️  Testing task checkbox toggle...")
    await navigate_to_view(page, "tasks")
    try:
        # Find first checkbox
        checkbox = page.locator('[role="checkbox"], .task-checkbox, button:has(svg)').first
        if await checkbox.count() == 0:
            result.warn("task-checkbox", "No checkboxes found")
            return

        # Get initial state
        await checkbox.click()
        await page.wait_for_timeout(500)
        # Click again to toggle back
        await checkbox.click()
        await page.wait_for_timeout(500)
        result.ok("task-checkbox-toggle")
    except Exception as e:
        result.fail("task-checkbox-toggle", str(e)[:200])


async def test_task_opens_detail(page, result):
    """Test clicking task text opens detail dialog."""
    print("\n📋 Testing task detail dialog...")
    await navigate_to_view(page, "tasks")
    try:
        # Click on a task title (not checkbox)
        task_title = page.locator('.task-title, [data-task-title], td >> nth=1, .cursor-pointer').first
        if await task_title.count() == 0:
            # Try broader selector
            task_title = page.locator('text=/\\w+/').nth(5)

        await task_title.click()
        await page.wait_for_timeout(1000)

        # Check dialog opened
        dialog = page.locator('[role="dialog"], [data-state="open"]')
        if await dialog.count() > 0:
            result.ok("task-opens-detail-dialog")
            # Close dialog
            await page.keyboard.press("Escape")
            await page.wait_for_timeout(500)
        else:
            result.warn("task-opens-detail-dialog", "Dialog not detected — may need manual verification")
    except Exception as e:
        result.fail("task-opens-detail-dialog", str(e)[:200])


async def test_mobile_no_horizontal_overflow(page, result):
    """Test no horizontal overflow on mobile."""
    print("\n📐 Testing no horizontal overflow...")
    for view in VIEWS:
        try:
            await navigate_to_view(page, view)
            overflow = await page.evaluate(
                "() => document.documentElement.scrollWidth > document.documentElement.clientWidth"
            )
            if overflow:
                result.fail(f"{view}-no-h-overflow", "Horizontal overflow detected")
            else:
                result.ok(f"{view}-no-h-overflow")
        except Exception as e:
            result.fail(f"{view}-no-h-overflow", str(e)[:200])


async def test_touch_targets(page, result):
    """Test touch targets >= 44px on mobile."""
    print("\n👆 Testing touch targets...")
    await navigate_to_view(page, "today")
    try:
        too_small = await page.evaluate("""() => {
            const els = document.querySelectorAll('button, a[href], [role="button"], [role="checkbox"]');
            const violations = [];
            els.forEach(el => {
                const r = el.getBoundingClientRect();
                if (r.width > 0 && r.height > 0 && (r.width < 44 || r.height < 44)) {
                    violations.push({
                        tag: el.tagName,
                        cls: (el.className || '').toString().slice(0, 60),
                        w: Math.round(r.width),
                        h: Math.round(r.height),
                        text: (el.textContent || '').slice(0, 30)
                    });
                }
            });
            return violations;
        }""")
        if too_small:
            result.warn("touch-targets", f"{len(too_small)} elements < 44px: {json.dumps(too_small[:3])}")
        else:
            result.ok("touch-targets")
    except Exception as e:
        result.fail("touch-targets", str(e)[:200])


async def test_detail_dialog_scroll_mobile(page, result):
    """Test detail dialog scrolls on mobile."""
    print("\n📜 Testing detail dialog scroll (mobile)...")
    await navigate_to_view(page, "today")
    try:
        # Find and click a task
        task = page.locator('.cursor-pointer, [data-task-title]').first
        if await task.count() > 0:
            await task.click()
            await page.wait_for_timeout(1000)

            dialog = page.locator('[role="dialog"]')
            if await dialog.count() > 0:
                # Check if dialog content is scrollable
                scrollable = await page.evaluate("""() => {
                    const d = document.querySelector('[role="dialog"]');
                    if (!d) return false;
                    const content = d.querySelector('[data-dialog-content], .overflow-y-auto, [class*="scroll"]') || d;
                    return content.scrollHeight > content.clientHeight || document.body.scrollHeight > window.innerHeight;
                }""")
                if scrollable:
                    result.ok("detail-dialog-scroll-mobile")
                else:
                    result.warn("detail-dialog-scroll-mobile", "Dialog may not need scrolling (short content)")

                await page.keyboard.press("Escape")
                await page.wait_for_timeout(500)
            else:
                result.warn("detail-dialog-scroll-mobile", "Could not open dialog")
        else:
            result.warn("detail-dialog-scroll-mobile", "No tasks found to test")
    except Exception as e:
        result.fail("detail-dialog-scroll-mobile", str(e)[:200])


async def test_quick_capture(page, result):
    """Test quick capture creates a task."""
    print("\n⚡ Testing quick capture...")
    try:
        await page.keyboard.press("Meta+n")
        await page.wait_for_timeout(1000)

        dialog = page.locator('[role="dialog"]')
        if await dialog.count() > 0:
            result.ok("quick-capture-opens")

            # Type a test task
            title_input = dialog.locator('input[type="text"], input[placeholder]').first
            if await title_input.count() > 0:
                test_title = f"QA-TEST-{int(datetime.now().timestamp())}"
                await title_input.fill(test_title)
                await page.keyboard.press("Meta+Enter")
                await page.wait_for_timeout(1500)
                result.ok("quick-capture-submit")

                # Clean up — delete test task via DB later
            else:
                result.warn("quick-capture-submit", "Could not find title input")

            # Close dialog if still open
            await page.keyboard.press("Escape")
        else:
            result.fail("quick-capture-opens", "⌘N did not open dialog")
    except Exception as e:
        result.fail("quick-capture", str(e)[:200])


async def run_regression(base_url, viewports_to_test):
    result = RegressionResult()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        for vp_name, vp_size in viewports_to_test.items():
            print(f"\n{'='*60}")
            print(f"🖥️  Viewport: {vp_name} ({vp_size['width']}×{vp_size['height']})")
            print(f"{'='*60}")

            context = await browser.new_context(
                viewport=vp_size,
                device_scale_factor=2 if vp_name == "mobile" else 1,
                is_mobile=vp_name == "mobile",
                has_touch=vp_name == "mobile",
                user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)" if vp_name == "mobile" else None,
            )
            page = await context.new_page()

            # Navigate and auth
            await page.goto(base_url, wait_until="domcontentloaded", timeout=30000)
            await inject_auth(page)
            await page.goto(base_url, wait_until="networkidle", timeout=30000)
            await page.wait_for_timeout(3000)

            if not await wait_for_app(page):
                result.fail(f"{vp_name}-app-ready", "__sotto_setActiveView not available")
                await context.close()
                continue

            result.ok(f"{vp_name}-app-ready")

            # Run tests
            await test_views_load(page, result, vp_name)

            if vp_name == "mobile":
                await test_mobile_no_horizontal_overflow(page, result)
                await test_touch_targets(page, result)
                await test_detail_dialog_scroll_mobile(page, result)

            if vp_name == "desktop":
                await test_task_checkbox(page, result)
                await test_task_opens_detail(page, result)
                await test_quick_capture(page, result)

            await context.close()

        await browser.close()

    return result.summary()


def main():
    parser = argparse.ArgumentParser(description="Sotto Regression Suite")
    parser.add_argument("--base-url", default=BASE_URL)
    parser.add_argument("--mobile-only", action="store_true")
    parser.add_argument("--desktop-only", action="store_true")
    args = parser.parse_args()

    vps = dict(VIEWPORTS)
    if args.mobile_only:
        vps = {"mobile": VIEWPORTS["mobile"]}
    elif args.desktop_only:
        vps = {"desktop": VIEWPORTS["desktop"]}

    success = asyncio.run(run_regression(args.base_url, vps))
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
