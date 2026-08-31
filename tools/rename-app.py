#!/usr/bin/env python3
"""Rename the visible CINENOVA app and notification channel in a decoded APK."""

from __future__ import annotations

import argparse
from pathlib import Path


APP_NAME = "CINENOVA BLUE"


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text()
    if old not in text:
        if new in text:
            return
        raise SystemExit(f"Expected rename anchor was not found: {path}")
    path.write_text(text.replace(old, new, 1))


def replace_in_file(path: Path, old: str, new: str) -> None:
    text = path.read_text()
    updated = text.replace(old, new)
    if updated != text:
        path.write_text(updated)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("decoded_apk_directory", type=Path)
    args = parser.parse_args()

    root = args.decoded_apk_directory.resolve()
    strings = root / "res/values/strings.xml"
    replace_once(
        strings,
        '<string name="app_name">CINENOVA</string>',
        f'<string name="app_name">{APP_NAME}</string>',
    )
    replace_once(
        strings,
        '<string name="channel">PlusNotificationChannel375</string>',
        f'<string name="channel">{APP_NAME}</string>',
    )

    for relative in (
        "res/layout/fragment_dispositive.xml",
        "res/layout/fragment_more.xml",
        "res/layout/media_controller.xml",
        "res/layout/media_raw.xml",
        "smali/y3/e.smali",
        "smali/z3/b.smali",
        "smali/com/dpsteam/filmplus/tools/i1.smali",
        "smali/com/dpsteam/filmplus/activities/MediaActivity.smali",
    ):
        replace_in_file(root / relative, "CINENOVA", APP_NAME)


if __name__ == "__main__":
    main()