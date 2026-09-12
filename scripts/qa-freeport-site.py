#!/usr/bin/env python3
"""QA checks for Freeport Shore Excursion World 2.0 (Phase 19D)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "freeportshoreexcursion.com"
APEX = f"https://{DOMAIN}"
EMAIL = f"hello@{DOMAIN}"

FORBIDDEN_LEAKS = [
    "shoreexcursionsgroup.com",
    "wowatour.com",
    "CAFPGARDEN",
    "CAFPLUCNAT",
    "CAFPRESORT",
    "CAFPBLUE",
    "CAFPDOLPHIN",
    "stripe.com",
    "SEG_MANUAL",
    "Return To Ship On Time",
    "return to ship on time",
    "60–90 min",
    "60-90 min",
    "highest-rated",
    "rate highest",
    "AggregateRating",
    '"@type": "Product"',
    '"@type": "Offer"',
    '"@type": "LocalBusiness"',
]

FORBIDDEN_DEST = [
    "nassau",
    "paradise island",
    "atlantis",
    "curacao",
    "willemstad",
    "grenada",
    "st lucia",
    "montego",
    "belize",
]

REQUIRED_FILES = [
    "index.html",
    "404.html",
    "robots.txt",
    "sitemap.xml",
    "css/site.css",
    "js/nav.js",
    "js/commercial-config.js",
    "js/booking.js",
    "worker.js",
    "wrangler.jsonc",
    "book/garden-of-the-groves-city-tour/index.html",
    "book/garden-of-the-groves-city-tour/received/index.html",
    "best-freeport-shore-excursions/index.html",
    "one-day-in-freeport-from-a-cruise-ship/index.html",
    "freeport-cruise-port-guide/index.html",
    "freeport-beach-excursions/index.html",
    "freeport-snorkelling-excursions/index.html",
    "freeport-nature-garden-tours/index.html",
    "freeport-dolphin-encounters/index.html",
    "freeport-faq/index.html",
    "contact/index.html",
    "about/index.html",
    "privacy/index.html",
    "terms/index.html",
    "methodology/index.html",
]

PROTECTED_CANONICALS = {
    "index.html": f"{APEX}/",
    "best-freeport-shore-excursions/index.html": f"{APEX}/best-freeport-shore-excursions",
    "one-day-in-freeport-from-a-cruise-ship/index.html": (
        f"{APEX}/one-day-in-freeport-from-a-cruise-ship"
    ),
    "freeport-cruise-port-guide/index.html": f"{APEX}/freeport-cruise-port-guide",
    "book/garden-of-the-groves-city-tour/index.html": f"{APEX}/book/garden-of-the-groves-city-tour",
}


def errors() -> list[str]:
    errs: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errs.append(f"missing {rel}")

    quarantine = list((ROOT / "images" / "quarantine").glob("*")) if (ROOT / "images" / "quarantine").exists() else []
    qnames = {p.name for p in quarantine}
    for html in ROOT.rglob("*.html"):
        if any(part in html.parts for part in ("_legacy_phase19a", "node_modules", ".wrangler", "workers")):
            continue
        text = html.read_text(encoding="utf-8", errors="ignore")
        for name in qnames:
            if name in text:
                errs.append(f"quarantine image referenced in {html.relative_to(ROOT)}: {name}")

        for leak in FORBIDDEN_LEAKS:
            if leak in text:
                errs.append(f"leak '{leak}' in {html.relative_to(ROOT)}")

        lower = text.lower()
        for dest in FORBIDDEN_DEST:
            if dest in lower and html.name != "404.html":
                errs.append(f"cross-destination '{dest}' in {html.relative_to(ROOT)}")

        titles = re.findall(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
        if len(titles) != 1:
            errs.append(f"title count {len(titles)} in {html.relative_to(ROOT)}")
        h1s = re.findall(r"<h1\b", text, re.I)
        if len(h1s) != 1:
            errs.append(f"H1 count {len(h1s)} in {html.relative_to(ROOT)}")

        if "<nav" in text and 'id="menu-toggle"' not in text:
            errs.append(f"missing menu-toggle in {html.relative_to(ROOT)}")

        if "cdn.tailwindcss.com" in text:
            errs.append(f"Tailwind CDN in {html.relative_to(ROOT)}")

        if "<footer" in text and EMAIL not in text:
            errs.append(f"missing {EMAIL} in {html.relative_to(ROOT)}")

    for rel, canon in PROTECTED_CANONICALS.items():
        html = (ROOT / rel).read_text(encoding="utf-8", errors="ignore")
        m = re.search(r'rel="canonical"\s+href="([^"]+)"', html)
        if not m:
            errs.append(f"missing canonical in {rel}")
        elif m.group(1) != canon:
            errs.append(f"bad canonical in {rel}: {m.group(1)} != {canon}")

    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    if ".html" in sm:
        errs.append("sitemap contains .html URLs")
    if f"{APEX}/" not in sm:
        errs.append("sitemap missing home")
    for path in (
        "/best-freeport-shore-excursions",
        "/one-day-in-freeport-from-a-cruise-ship",
        "/freeport-cruise-port-guide",
    ):
        if f"{APEX}{path}" not in sm:
            errs.append(f"sitemap missing {path}")

    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    if f"{APEX}/sitemap.xml" not in robots:
        errs.append("robots missing sitemap")

    home = (ROOT / "index.html").read_text(encoding="utf-8")
    if "/one-day-in-freeport-from-a-cruise-ship" not in home:
        errs.append("one-day not linked from homepage")
    if 'data-nav="oneday"' not in home:
        errs.append("one-day not in primary nav")
    if "/book/garden-of-the-groves-city-tour" not in home:
        errs.append("homepage missing Garden RTB CTA")

    for rel in (
        "best-freeport-shore-excursions/index.html",
        "one-day-in-freeport-from-a-cruise-ship/index.html",
        "freeport-nature-garden-tours/index.html",
    ):
        text = (ROOT / rel).read_text(encoding="utf-8")
        if "/book/garden-of-the-groves-city-tour" not in text:
            errs.append(f"{rel} missing Garden RTB CTA")

    book = (ROOT / "book/garden-of-the-groves-city-tour/index.html").read_text(encoding="utf-8")
    if "staybehind_ack" not in book:
        errs.append("book page missing stay-behind acknowledgement")
    if "Participants age 3+" not in book:
        errs.append("book page missing preferred participant label")
    if "Children age 0–2" not in book and "Children age 0-2" not in book:
        errs.append("book page missing free-child label")

    sn = (ROOT / "freeport-snorkelling-excursions/index.html").read_text(encoding="utf-8")
    if "Ben" not in sn or "Blue Hole" not in sn:
        errs.append("snorkel page missing Blue Hole vs Ben's Cave clarification")

    port = (ROOT / "freeport-cruise-port-guide/index.html").read_text(encoding="utf-8")
    if "Not the same place as Port Lucaya" not in port and "not the same" not in port.lower():
        if "Port Lucaya" in port and "Lucayan Harbour" in port:
            pass
        else:
            errs.append("port guide missing Lucayan Harbour vs Port Lucaya distinction")

    od = (ROOT / "one-day-in-freeport-from-a-cruise-ship/index.html").read_text(encoding="utf-8")
    if re.search(r"\b0?8:00\b|\b10:00\b|\b16:00\b", od):
        errs.append("one-day page still has fake clock times")

    css = ROOT / "css" / "site.css"
    if css.exists() and css.stat().st_size < 1000:
        errs.append("css/site.css looks too small")

    commercial = (ROOT / "js/commercial-config.js").read_text(encoding="utf-8")
    for leak in ("CAFPGARDEN", "SEG_MANUAL", "info@wowatour"):
        if leak in commercial:
            errs.append(f"commercial-config leak {leak}")

    return errs


def main() -> int:
    errs = errors()
    if errs:
        print("QA FAILED:")
        for e in errs:
            print(f"  - {e}")
        return 1
    print("QA OK — Freeport Phase 19D checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
