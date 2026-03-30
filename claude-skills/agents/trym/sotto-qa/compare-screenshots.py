#!/usr/bin/env python3
"""
Visual diff tool — compares current screenshots against baselines.

Usage: python3 compare-screenshots.py [--current DIR] [--baseline DIR] [--threshold 5.0]
Requires: pip install Pillow
"""

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("❌ Install Pillow: pip install Pillow")
    sys.exit(1)

BASELINE_DIR = Path.home() / "clawd/projects/sotto/e2e-audit/baselines"


def pixel_diff_percent(img1_path, img2_path):
    """Calculate percentage of pixels that differ between two images."""
    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")

    # Resize to same dimensions if needed
    if img1.size != img2.size:
        img2 = img2.resize(img1.size, Image.LANCZOS)

    pixels1 = img1.load()
    pixels2 = img2.load()
    w, h = img1.size
    diff_count = 0
    total = w * h

    for y in range(h):
        for x in range(w):
            r1, g1, b1 = pixels1[x, y]
            r2, g2, b2 = pixels2[x, y]
            # Threshold per channel to ignore anti-aliasing
            if abs(r1 - r2) > 10 or abs(g1 - g2) > 10 or abs(b1 - b2) > 10:
                diff_count += 1

    return (diff_count / total) * 100


def main():
    parser = argparse.ArgumentParser(description="Sotto Visual Diff Tool")
    parser.add_argument("--current", type=Path, help="Directory with current screenshots")
    parser.add_argument("--baseline", type=Path, default=BASELINE_DIR)
    parser.add_argument("--threshold", type=float, default=5.0, help="Fail threshold (percent)")
    args = parser.parse_args()

    if not args.current:
        # Auto-detect latest screenshot dir
        screenshots_root = Path.home() / "clawd/projects/sotto/e2e-audit/screenshots"
        if screenshots_root.exists():
            dirs = sorted([d for d in screenshots_root.iterdir() if d.is_dir()])
            if dirs:
                args.current = dirs[-1]
                print(f"Using latest screenshots: {args.current}")

    if not args.current or not args.current.exists():
        print("❌ No current screenshots found. Run regression first.")
        sys.exit(1)

    if not args.baseline.exists():
        print("❌ No baselines found. Run take-baselines.py first.")
        sys.exit(1)

    passed = 0
    failed = 0
    reviewed = 0

    baselines = sorted(args.baseline.glob("*.png"))
    if not baselines:
        print("❌ No baseline images found")
        sys.exit(1)

    for baseline in baselines:
        current = args.current / baseline.name
        if not current.exists():
            print(f"  ⚠️  {baseline.name}: no current screenshot (SKIP)")
            continue

        diff = pixel_diff_percent(baseline, current)

        if diff < 1.0:
            print(f"  ✅ {baseline.name}: {diff:.2f}% diff (PASS)")
            passed += 1
        elif diff < args.threshold:
            print(f"  ⚠️  {baseline.name}: {diff:.2f}% diff (REVIEW)")
            reviewed += 1
        else:
            print(f"  ❌ {baseline.name}: {diff:.2f}% diff (FAIL)")
            failed += 1

    print(f"\n{'='*50}")
    print(f"RESULTS: {passed} pass, {reviewed} review, {failed} fail")
    print(f"{'='*50}")

    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
