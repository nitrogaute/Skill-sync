#!/usr/bin/env python3
"""
Capture baseline screenshots for Sotto visual regression.
Saves to ~/clawd/projects/sotto/e2e-audit/baselines/

Usage: python3 take-baselines.py [--base-url URL]
Requires: pip install playwright && playwright install chromium
"""

import asyncio
import argparse
import json
import os
import sys
from pathlib import Path

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("❌ Install playwright: pip install playwright && playwright install chromium")
    sys.exit(1)

BASE_URL = "https://sotto-dashboard.vercel.app"
AUTH_TOKEN_KEY = "sb-ukwzbvfstvfavptxiyrn-auth-token"
BASELINE_DIR = Path.home() / "clawd/projects/sotto/e2e-audit/baselines"

VIEWS = [
    "today", "week", "tasks", "projects", "topics", "notes", "meetings",
    "people", "okrs", "documents", "trym", "graph", "finances", "health", "weekly-review"
]

VIEWPORTS = {
    "mobile": {"width": 375, "height": 812},
    "desktop": {"width": 1440, "height": 900},
}


async def run(base_url):
    BASELINE_DIR.mkdir(parents=True, exist_ok=True)
    token = os.environ.get("SOTTO_AUTH_TOKEN")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        for vp_name, vp_size in VIEWPORTS.items():
            print(f"\n📸 Capturing {vp_name} baselines ({vp_size['width']}×{vp_size['height']})...")

            context = await browser.new_context(
                viewport=vp_size,
                device_scale_factor=2 if vp_name == "mobile" else 1,
                is_mobile=vp_name == "mobile",
                has_touch=vp_name == "mobile",
                user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)" if vp_name == "mobile" else None,
            )
            page = await context.new_page()

            await page.goto(base_url, wait_until="domcontentloaded", timeout=30000)
            if token:
                await page.evaluate(f"() => window.localStorage.setItem('{AUTH_TOKEN_KEY}', {json.dumps(token)})")
                await page.goto(base_url, wait_until="networkidle", timeout=30000)
            await page.wait_for_timeout(3000)

            # Check app ready
            ready = False
            for _ in range(20):
                ready = await page.evaluate("() => typeof window.__sotto_setActiveView === 'function'")
                if ready:
                    break
                await page.wait_for_timeout(500)

            if not ready:
                print("❌ App not ready — __sotto_setActiveView not found")
                await context.close()
                continue

            for view in VIEWS:
                await page.evaluate(f"() => window.__sotto_setActiveView('{view}')")
                await page.wait_for_timeout(2000)
                path = BASELINE_DIR / f"{view}-{vp_name}.png"
                await page.screenshot(path=str(path), full_page=True)
                print(f"  ✅ {view}-{vp_name}.png")

            await context.close()

        await browser.close()

    print(f"\n✅ Baselines saved to {BASELINE_DIR}")


def main():
    parser = argparse.ArgumentParser(description="Capture Sotto baseline screenshots")
    parser.add_argument("--base-url", default=BASE_URL)
    args = parser.parse_args()
    asyncio.run(run(args.base_url))


if __name__ == "__main__":
    main()
