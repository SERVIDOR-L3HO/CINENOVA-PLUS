#!/usr/bin/env python3
"""Replace CINENOVA's Firebase notification icon in an APK.

The recovered project does not contain the original Android source tree, so
this updates the five density-specific PNG entries directly in a copy of the
APK. Android renders a small notification icon as a monochrome alpha mask.
"""

from __future__ import annotations

import argparse
import subprocess
import tempfile
import zipfile
from pathlib import Path


ICON_PATHS = {
    "mdpi": ("res/drawable-mdpi/ic_stat_name.png", 24),
    "hdpi": ("res/drawable-hdpi/ic_stat_name.png", 36),
    "xhdpi": ("res/drawable-xhdpi/ic_stat_name.png", 48),
    "xxhdpi": ("res/drawable-xxhdpi/ic_stat_name.png", 72),
    "xxxhdpi": ("res/drawable-xxxhdpi/ic_stat_name.png", 96),
}


def build_icon(source: Path, destination: Path, size: int) -> None:
    """Create a white-on-transparent alpha-mask icon at one density."""
    subprocess.run(
        [
            "magick",
            str(source),
            "-resize",
            "88x82",
            "-gravity",
            "center",
            "-background",
            "none",
            "-extent",
            "96x96",
            "-colorspace",
            "gray",
            "(",
            "+clone",
            "-alpha",
            "off",
            ")",
            "-compose",
            "CopyOpacity",
            "-composite",
            "-fill",
            "white",
            "-colorize",
            "100",
            "-resize",
            f"{size}x{size}",
            str(destination),
        ],
        check=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_apk", type=Path)
    parser.add_argument("source_icon", type=Path)
    parser.add_argument("output_apk", type=Path)
    args = parser.parse_args()

    for path in (args.input_apk, args.source_icon):
        if not path.is_file():
            raise SystemExit(f"File not found: {path}")

    with tempfile.TemporaryDirectory(prefix="cinenova-notification-") as temporary:
        temporary_path = Path(temporary)
        icons = {}
        for density, (_, size) in ICON_PATHS.items():
            icon = temporary_path / f"{density}-ic_stat_name.png"
            build_icon(args.source_icon, icon, size)
            icons[density] = icon

        args.output_apk.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(args.input_apk, "r") as source:
            expected = {path for path, _ in ICON_PATHS.values()}
            found = {entry.filename for entry in source.infolist()}
            missing = expected - found
            if missing:
                raise SystemExit(
                    "Input APK is missing notification icon entries: "
                    + ", ".join(sorted(missing))
                )

        # Match by the complete APK resource path, not merely the basename.
        icon_by_apk_path = {
            path: icons[density] for density, (path, _) in ICON_PATHS.items()
        }
        with zipfile.ZipFile(args.input_apk, "r") as source, zipfile.ZipFile(
            args.output_apk, "w", compression=zipfile.ZIP_DEFLATED
        ) as destination:
            for entry in source.infolist():
                if entry.filename.startswith("META-INF/") and (
                    entry.filename.endswith(".SF")
                    or entry.filename.endswith(".RSA")
                    or entry.filename.endswith(".DSA")
                    or entry.filename == "META-INF/MANIFEST.MF"
                ):
                    continue
                data = icon_by_apk_path.get(entry.filename)
                destination.writestr(
                    entry,
                    data.read_bytes() if data else source.read(entry),
                )


if __name__ == "__main__":
    main()