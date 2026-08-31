#!/usr/bin/env python3
"""Replace the custom welcome-toast logo in a recovered CINENOVA APK."""

from __future__ import annotations

import argparse
import tempfile
import zipfile
from pathlib import Path
import subprocess


ASSET_PATH = "assets/ToastAndroForever.png"


def prepare_logo(source: Path, destination: Path) -> None:
    """Fit the supplied transparent logo into a square without distortion."""
    subprocess.run(
        [
            "magick",
            str(source),
            "-resize",
            "486x486",
            "-gravity",
            "center",
            "-background",
            "none",
            "-extent",
            "518x518",
            str(destination),
        ],
        check=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_apk", type=Path)
    parser.add_argument("source_logo", type=Path)
    parser.add_argument("output_apk", type=Path)
    args = parser.parse_args()

    for path in (args.input_apk, args.source_logo):
        if not path.is_file():
            raise SystemExit(f"File not found: {path}")

    with tempfile.TemporaryDirectory(prefix="cinenova-toast-logo-") as temporary:
        logo = Path(temporary) / "ToastAndroForever.png"
        prepare_logo(args.source_logo, logo)

        with zipfile.ZipFile(args.input_apk, "r") as source:
            entries = {entry.filename for entry in source.infolist()}
            if ASSET_PATH not in entries:
                raise SystemExit(f"Input APK is missing {ASSET_PATH}")

        args.output_apk.parent.mkdir(parents=True, exist_ok=True)
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
                destination.writestr(
                    entry,
                    logo.read_bytes() if entry.filename == ASSET_PATH else source.read(entry),
                )


if __name__ == "__main__":
    main()