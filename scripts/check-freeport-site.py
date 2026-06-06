#!/usr/bin/env python3
"""QA checks for Freeport Shore Excursion site."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "freeportshoreexcursion.com"

FORBIDDEN = [
    "barbados", "antigua", "cozumel", "aruba", "st maarten", "st. maarten",
    "bonaire", "dominica", "flam", "flåm", "belize", "altun ha", "caye caulker",
    "amber cove", "grand cayman", "san juan", "tortola", "gibraltar", "norway",
    "costa maya", "bimini", "curacao", "st lucia", "st. lucia", "falmouth",
    "jamaica", "dunn's river", "dunns river", "martha brae", "george town",
    "stingray city", "seven mile beach",
]

SCAN_EXTENSIONS = {".html", ".py", ".json", ".jsonc", ".txt", ".xml", ".md", ".js", ".css", ".sh"}
SKIP_DIRS = {"node_modules", ".git", "scripts/__pycache__"}

REQUIRED_PAGES = [
    "index.html",
    "best-freeport-shore-excursions.html",
    "freeport-beach-excursions.html",
    "freeport-snorkelling-excursions.html",
    "freeport-nature-garden-tours.html",
    "freeport-dolphin-encounters.html",
    "one-day-in-freeport-from-a-cruise-ship.html",
    "freeport-cruise-port-guide.html",
    "freeport-faq.html",
]


def iter_files() -> list[Path]:
    files = []
    for p in ROOT.rglob("*"):
        if p.is_dir():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.suffix.lower() in SCAN_EXTENSIONS:
            files.append(p)
    return files


def check_forbidden_references() -> list[str]:
    errors = []
    for path in iter_files():
        if path.name == "check-freeport-site.py":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        for term in FORBIDDEN:
            if term in text:
                errors.append(f"Forbidden reference '{term}' in {path.relative_to(ROOT)}")
    return errors


def check_domain_config() -> list[str]:
    errors = []
    robots = (ROOT / "robots.txt").read_text(encoding="utf-8") if (ROOT / "robots.txt").exists() else ""
    if DOMAIN not in robots:
        errors.append("robots.txt missing freeportshoreexcursion.com sitemap")

    wrangler = (ROOT / "wrangler.jsonc").read_text(encoding="utf-8") if (ROOT / "wrangler.jsonc").exists() else ""
    if DOMAIN not in wrangler:
        errors.append("wrangler.jsonc missing freeportshoreexcursion.com domain")

    sitemap = ROOT / "sitemap.xml"
    if not sitemap.exists():
        errors.append("sitemap.xml missing")
    else:
        tree = ET.parse(sitemap)
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = [el.text for el in tree.findall(".//sm:loc", ns)]
        if not locs:
            locs = [el.text for el in tree.findall(".//loc")]
        bad = [u for u in locs if u and DOMAIN not in u]
        if bad:
            errors.append(f"sitemap.xml has non-Freeport URLs: {bad[:3]}")
        if len(locs) != 9:
            errors.append(f"sitemap.xml has {len(locs)} URLs (expected 9)")

    index = (ROOT / "index.html").read_text(encoding="utf-8") if (ROOT / "index.html").exists() else ""
    if "Freeport Shore Excursion" not in index:
        errors.append("index.html missing Freeport site title")
    if 'geo.region" content="BS"' not in index:
        errors.append("index.html missing Bahamas geo.region metadata")
    if "Cruise Passenger Snapshot" not in index:
        errors.append("index.html missing Cruise Passenger Snapshot block")

    return errors


def check_required_content() -> list[str]:
    errors = []
    for page in REQUIRED_PAGES:
        if not (ROOT / page).exists():
            errors.append(f"Missing page: {page}")
    for page in REQUIRED_PAGES[1:]:
        html = (ROOT / page).read_text(encoding="utf-8") if (ROOT / page).exists() else ""
        if page != "freeport-faq.html" and "Cruise Passenger Snapshot" not in html:
            errors.append(f"{page} missing Cruise Passenger Snapshot")
        if "Return To Ship" not in html and page not in (
            "freeport-cruise-port-guide.html",
            "one-day-in-freeport-from-a-cruise-ship.html",
            "freeport-faq.html",
        ):
            errors.append(f"{page} missing return-to-ship reassurance")
    return errors


def check_images() -> list[str]:
    errors = []
    for path in iter_files():
        if path.suffix != ".html":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for fragment in text.split('src="/images/')[1:]:
            fname = fragment.split('"')[0]
            if not (ROOT / "images" / fname).exists():
                errors.append(f"{path.name} references missing image: {fname}")
    return errors


def main() -> None:
    print("Running Freeport site QA checks…")
    errors = []
    errors.extend(check_forbidden_references())
    errors.extend(check_domain_config())
    errors.extend(check_required_content())
    errors.extend(check_images())

    if errors:
        print("FAILED:")
        for e in errors:
            print(f"  ✗ {e}")
        raise SystemExit(1)

    print("All checks passed.")
    print(f"  Domain: {DOMAIN}")
    print("  Ready for GitHub and Cloudflare deploy.")


if __name__ == "__main__":
    main()
