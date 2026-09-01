#!/usr/bin/env python3
"""Generate the cohesive, movie-themed server icons used by CINENOVA."""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import tempfile


PALETTE = {
    "navy": "#0B1C2B",
    "blue": "#65D9FF",
    "ice": "#DDF7FF",
    "gold": "#FFC857",
    "pink": "#FF6B9A",
    "violet": "#A78BFA",
    "green": "#65E6B4",
}


def svg_icon(body: str) -> str:
    p = PALETTE
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{p["navy"]}"/>
    <stop offset="1" stop-color="#173C59"/>
  </linearGradient>
  <linearGradient id="blue" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{p["ice"]}"/>
    <stop offset="1" stop-color="{p["blue"]}"/>
  </linearGradient>
</defs>
<circle cx="256" cy="256" r="224" fill="url(#bg)" stroke="{p["blue"]}" stroke-width="12"/>
<circle cx="256" cy="256" r="204" fill="none" stroke="#9BEAFF" stroke-opacity=".16" stroke-width="3"/>
{body}
</svg>"""


ICONS = {
    "ic_ultra.png": """
<circle cx="256" cy="256" r="116" fill="none" stroke="url(#blue)" stroke-width="30"/>
<circle cx="256" cy="256" r="34" fill="#0B1C2B" stroke="#DDF7FF" stroke-width="10"/>
<path d="M126 332c36-42 70-58 104-48 32 9 46 43 80 46 26 2 49-10 76-39" fill="none" stroke="#65D9FF" stroke-width="22" stroke-linecap="round"/>
<path d="M126 376c36-42 70-58 104-48 32 9 46 43 80 46 26 2 49-10 76-39" fill="none" stroke="#65E6B4" stroke-width="12" stroke-linecap="round" opacity=".9"/>
""",
    "ic_zeus.png": """
<circle cx="256" cy="256" r="116" fill="none" stroke="url(#blue)" stroke-width="30"/>
<circle cx="256" cy="256" r="34" fill="#0B1C2B" stroke="#DDF7FF" stroke-width="10"/>
<path d="M304 92 196 260h66l-34 160 112-198h-69z" fill="#FFC857" stroke="#FFE6A6" stroke-width="8" stroke-linejoin="round"/>
""",
    "ic_fast.png": """
<path d="M124 178h264l-28 74H152z" fill="#FF6B9A" stroke="#FFD1DF" stroke-width="10" stroke-linejoin="round"/>
<path d="M142 254h228v106H142z" fill="#173C59" stroke="#65D9FF" stroke-width="10"/>
<path d="M166 178v74M205 178v74M244 178v74M283 178v74M322 178v74" stroke="#0B1C2B" stroke-width="12"/>
<path d="m320 286 34 40h-35l-25 48-5-43h-31l36-57 8 34z" fill="#FFC857" stroke="#FFE6A6" stroke-width="6" stroke-linejoin="round"/>
""",
    "ic_pegasus.png": """
<circle cx="256" cy="266" r="102" fill="none" stroke="url(#blue)" stroke-width="28"/>
<circle cx="256" cy="266" r="30" fill="#0B1C2B" stroke="#DDF7FF" stroke-width="9"/>
<path d="M144 164c-34-38-22-70 20-76 18 34 44 58 80 74" fill="none" stroke="#DDF7FF" stroke-width="18" stroke-linecap="round"/>
<path d="M368 164c34-38 22-70-20-76-18 34-44 58-80 74" fill="none" stroke="#65D9FF" stroke-width="18" stroke-linecap="round"/>
<path d="m390 326 12 26 28 3-21 19 6 28-25-14-25 14 6-28-21-19 28-3z" fill="#FFC857"/>
""",
    "ic_turbo.png": """
<circle cx="256" cy="256" r="112" fill="none" stroke="url(#blue)" stroke-width="28"/>
<circle cx="256" cy="256" r="32" fill="#0B1C2B" stroke="#DDF7FF" stroke-width="9"/>
<path d="M112 176h78M94 224h75M336 288h82M318 336h78" stroke="#65E6B4" stroke-width="15" stroke-linecap="round"/>
<path d="M256 92v44M256 376v44" stroke="#FFC857" stroke-width="15" stroke-linecap="round"/>
""",
    "ic_ares.png": """
<path d="M126 174h260l-28 72H154z" fill="#FF6B9A" stroke="#FFD1DF" stroke-width="10"/>
<path d="M150 248h212v108H150z" fill="#173C59" stroke="#65D9FF" stroke-width="10"/>
<path d="M204 276h108v54H204z" fill="#65D9FF"/>
<path d="m172 112 28 34 40-4-30 27 10 39-36-22-36 22 10-39-30-27 40 4z" fill="#FFC857"/>
""",
    "ic_poseidon.png": """
<circle cx="256" cy="214" r="96" fill="none" stroke="url(#blue)" stroke-width="26"/>
<circle cx="256" cy="214" r="28" fill="#0B1C2B" stroke="#DDF7FF" stroke-width="9"/>
<path d="M108 334c48-42 96 42 148 0 52-42 100 42 148 0" fill="none" stroke="#65D9FF" stroke-width="20" stroke-linecap="round"/>
<path d="M128 382c48-42 96 42 148 0 52-42 100 42 148 0" fill="none" stroke="#65E6B4" stroke-width="13" stroke-linecap="round"/>
""",
    "ic_vip.png": """
<path d="m132 180 38-34 44 30 42-38 42 38 44-30 38 34-30 162H162z" fill="#FFC857" stroke="#FFE6A6" stroke-width="10" stroke-linejoin="round"/>
<path d="M160 236h192M174 278h164" stroke="#0B1C2B" stroke-width="12" stroke-linecap="round"/>
<circle cx="256" cy="340" r="24" fill="#FF6B9A" stroke="#FFD1DF" stroke-width="8"/>
""",
    "ic_odin.png": """
<circle cx="256" cy="256" r="112" fill="none" stroke="url(#blue)" stroke-width="28"/>
<circle cx="256" cy="256" r="32" fill="#0B1C2B" stroke="#DDF7FF" stroke-width="9"/>
<path d="m256 100 20 42 46 5-35 30 10 45-41-24-41 24 10-45-35-30 46-5z" fill="#FFC857"/>
<path d="M156 366h200" stroke="#65E6B4" stroke-width="16" stroke-linecap="round"/>
""",
    "ic_kraken.png": """
<circle cx="256" cy="222" r="82" fill="none" stroke="url(#blue)" stroke-width="24"/>
<circle cx="256" cy="222" r="25" fill="#0B1C2B" stroke="#DDF7FF" stroke-width="8"/>
<path d="M174 304c-8 68-44 56-50 96M212 308c4 74-26 82-32 106M256 310v112M300 308c-4 74 26 82 32 106M338 304c8 68 44 56 50 96" fill="none" stroke="#A78BFA" stroke-width="18" stroke-linecap="round"/>
""",
    "ic_hidra.png": """
<circle cx="186" cy="260" r="68" fill="none" stroke="#65D9FF" stroke-width="22"/>
<circle cx="326" cy="260" r="68" fill="none" stroke="#65E6B4" stroke-width="22"/>
<circle cx="256" cy="172" r="68" fill="none" stroke="#FFC857" stroke-width="22"/>
<circle cx="256" cy="260" r="20" fill="#0B1C2B" stroke="#DDF7FF" stroke-width="8"/>
""",
    "ic_cerberus.png": """
<path d="M256 110 378 158v94c0 80-54 126-122 150-68-24-122-70-122-150v-94z" fill="#173C59" stroke="#65D9FF" stroke-width="12"/>
<circle cx="208" cy="238" r="44" fill="none" stroke="#DDF7FF" stroke-width="15"/>
<circle cx="304" cy="238" r="44" fill="none" stroke="#DDF7FF" stroke-width="15"/>
<circle cx="256" cy="308" r="44" fill="none" stroke="#FFC857" stroke-width="15"/>
<path d="M256 150v58" stroke="#65D9FF" stroke-width="15" stroke-linecap="round"/>
""",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()
    args.output_directory.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="cinenova-server-icons-") as temporary:
        temporary = Path(temporary)
        for filename, body in ICONS.items():
            svg = temporary / filename.replace(".png", ".svg")
            svg.write_text(svg_icon(body))
            subprocess.run(
                [
                    "magick",
                    str(svg),
                    "-background",
                    "none",
                    "-resize",
                    "512x512",
                    f"PNG32:{args.output_directory / filename}",
                ],
                check=True,
            )


if __name__ == "__main__":
    main()