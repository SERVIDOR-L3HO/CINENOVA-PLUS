#!/usr/bin/env python3
"""Apply CINENOVA's movie-themed server names and icon set to a decoded APK."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import sys


BRANDING_CLASS = "smali/com/dpsteam/filmplus/tools/ServerBranding.smali"


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text()
    if old not in text:
        if new in text:
            return
        raise SystemExit(f"Expected branding anchor was not found: {path}")
    path.write_text(text.replace(old, new, 1))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("decoded_apk_directory", type=Path)
    args = parser.parse_args()

    root = args.decoded_apk_directory.resolve()
    adapter = root / "smali/z3/j.smali"
    replace_once(
        adapter,
        """    invoke-virtual {v1, v0}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
""",
        """    invoke-static {v0}, Lcom/dpsteam/filmplus/tools/ServerBranding;->displayName(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v0
    invoke-virtual {v1, v0}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
""",
    )

    source = Path(__file__).resolve().parents[1] / "apk-edit" / BRANDING_CLASS
    destination = root / BRANDING_CLASS
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)

    generator = Path(__file__).with_name("generate-server-icons.py")
    subprocess.run(
        [sys.executable, str(generator), str(root / "res/drawable")],
        check=True,
    )


if __name__ == "__main__":
    main()