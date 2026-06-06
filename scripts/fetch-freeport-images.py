#!/usr/bin/env python3
"""Download images from Wikimedia Commons for Freeport site."""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

DOWNLOADS: list[tuple[str, str, str]] = [
    ("hero-freeport.png",
     "https://upload.wikimedia.org/wikipedia/commons/a/a6/Northwest_Providence_Channel_View_From_Gold_Rock_Beach_The_Lucayan_National_Park_of_the_Bahamas_in_East_Grand_Bahama.jpg",
     "Wikimedia: Gold Rock Beach Lucayan National Park Grand Bahama"),
    ("freeport-cruise-port.png",
     "https://upload.wikimedia.org/wikipedia/commons/c/cf/Radisson_Our_Lucaya_Beach_%5E_Golf_Resort_Grand_Bahama_Island_-_panoramio.jpg",
     "Wikimedia: Port Lucaya beach resort Grand Bahama"),
    ("freeport-intro.png",
     "https://upload.wikimedia.org/wikipedia/commons/9/9d/Branches_Gold_Rock_Beach_The_Lucayan_National_Park_of_the_Bahamas_in_Grand_Bahama.jpg",
     "Wikimedia: Grand Bahama Lucayan beach coastline"),
    ("best-freeport-excursions.png",
     "https://upload.wikimedia.org/wikipedia/commons/a/a6/Northwest_Providence_Channel_View_From_Gold_Rock_Beach_The_Lucayan_National_Park_of_the_Bahamas_in_East_Grand_Bahama.jpg",
     "Wikimedia: Turquoise Lucayan beach Grand Bahama"),
    ("one-day-freeport.png",
     "https://upload.wikimedia.org/wikipedia/commons/c/cf/Radisson_Our_Lucaya_Beach_%5E_Golf_Resort_Grand_Bahama_Island_-_panoramio.jpg",
     "Wikimedia: Port Lucaya harbour resort area"),
    ("freeport-beach.png",
     "https://upload.wikimedia.org/wikipedia/commons/d/d1/Taino_Beach%2C_Grand_Bahama_Island%2C_Bahamas.jpg",
     "Wikimedia: Taino Beach Grand Bahama"),
    ("freeport-snorkelling.png",
     "https://upload.wikimedia.org/wikipedia/commons/6/61/Peterson_Cay_National_Park_with_Fringing_Coral_Reefs_view_from_Peterson_Beach_of_Grand_Bahama.jpg",
     "Wikimedia: Peterson Cay reef snorkelling Grand Bahama"),
    ("freeport-nature.png",
     "https://upload.wikimedia.org/wikipedia/commons/e/e1/Understory_Canopy_at_Garden_of_the_Groves_Botanical_Garden_in_Grand_Bahama.jpg",
     "Wikimedia: Garden of the Groves Grand Bahama"),
    ("freeport-dolphin.png",
     "https://upload.wikimedia.org/wikipedia/commons/1/10/Tursiops_truncatus_01.jpg",
     "Wikimedia: Bottlenose dolphin encounter"),
    ("freeport-caves.png",
     "https://upload.wikimedia.org/wikipedia/commons/d/d4/Lucayan_Caverns_The_Bahamian_Dry_Forests_Rocky_Coppice_Lucayan_National_Park_of_the_Bahamas_in_Grand_Bahama.jpg",
     "Wikimedia: Lucayan National Park caves Grand Bahama"),
    ("freeport-blue-hole.png",
     "https://upload.wikimedia.org/wikipedia/commons/3/3c/Ben%E2%80%99s_Cave_Inland_blue_Hole_Lucayan_National_Park_of_the_Bahamas_in_Grand_Bahama.jpg",
     "Wikimedia: Ben's Cave blue hole Lucayan National Park"),
    ("freeport-faq.png",
     "https://upload.wikimedia.org/wikipedia/commons/c/cf/Radisson_Our_Lucaya_Beach_%5E_Golf_Resort_Grand_Bahama_Island_-_panoramio.jpg",
     "Wikimedia: Freeport harbour resort area"),
]


def download(filename: str, url: str, note: str) -> bool:
    dest = IMAGES / filename
    print(f"  {filename}")
    print(f"    {note}")
    result = subprocess.run(
        ["curl", "-fsSL", "-o", str(dest), url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"    FAILED: {result.stderr.strip()}", file=sys.stderr)
        return False
    size = dest.stat().st_size
    print(f"    OK ({size // 1024} KB)")
    return True


def main() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    print("Downloading Freeport images…")
    failed = 0
    for i, (filename, url, note) in enumerate(DOWNLOADS):
        if i:
            time.sleep(1.0)
        if not download(filename, url, note):
            failed += 1
    if failed:
        print(f"Warning: {failed} download(s) failed — placeholders remain for those files.")
    else:
        print("Done.")


if __name__ == "__main__":
    main()
