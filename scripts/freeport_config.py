"""Freeport Shore Excursion — World 2.0 Phase 19B site configuration."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DOMAIN = "freeportshoreexcursion.com"
APEX = f"https://{DOMAIN}"
SITE = "Freeport Shore Excursion"
EMAIL = "hello@freeportshoreexcursion.com"
DATE = "2026-09-12"
ACCENT = "text-pr-400"

FONTS = (
    "https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700"
    "&family=Source+Sans+3:wght@400;500;600;700&display=swap"
)

HERO_GRADIENT = (
    "linear-gradient(140deg, rgba(15, 23, 42, 0.78) 0%, "
    "rgba(30, 64, 175, 0.62) 42%, rgba(249, 115, 22, 0.38) 72%, "
    "rgba(0, 0, 0, 0.22) 100%)"
)

# Active images only — see images/ATTRIBUTION.md. Quarantine must not be referenced.
HERO = "/images/hero-freeport.png"
HERO_ALT = (
    "Gold Rock Beach and turquoise water at Lucayan National Park on Grand Bahama"
)

BEST_IMG = "/images/best-freeport-excursions.png"
BEST_ALT = HERO_ALT

BEACH_IMG = "/images/freeport-beach.png"
BEACH_ALT = "Taino Beach white sand and calm turquoise water on Grand Bahama"

SNORKEL_IMG = "/images/freeport-snorkelling.png"
SNORKEL_ALT = (
    "Fringing coral reef and clear water at Peterson Cay National Park, Grand Bahama"
)

NATURE_IMG = "/images/freeport-nature.png"
NATURE_ALT = "Tropical understory canopy at Garden of the Groves, Grand Bahama"

CAVES_IMG = "/images/freeport-caves.png"
CAVES_ALT = (
    "Limestone rocky coppice and cave landscape at Lucayan National Park, Grand Bahama"
)

INTRO_IMG = "/images/freeport-intro.png"
INTRO_ALT = (
    "Coastal branches and shoreline at Lucayan National Park on Grand Bahama"
)

# Extensionless, NO trailing slash — matches live GSC preferred form.
PROTECTED_ROUTES: list[dict] = [
    {"path": "/", "file": "index.html", "kind": "home"},
    {
        "path": "/best-freeport-shore-excursions",
        "file": "best-freeport-shore-excursions/index.html",
        "kind": "hub",
    },
    {
        "path": "/one-day-in-freeport-from-a-cruise-ship",
        "file": "one-day-in-freeport-from-a-cruise-ship/index.html",
        "kind": "guide",
    },
    {
        "path": "/freeport-cruise-port-guide",
        "file": "freeport-cruise-port-guide/index.html",
        "kind": "guide",
    },
    {
        "path": "/freeport-beach-excursions",
        "file": "freeport-beach-excursions/index.html",
        "kind": "attraction",
    },
    {
        "path": "/freeport-snorkelling-excursions",
        "file": "freeport-snorkelling-excursions/index.html",
        "kind": "attraction",
    },
    {
        "path": "/freeport-nature-garden-tours",
        "file": "freeport-nature-garden-tours/index.html",
        "kind": "attraction",
    },
    {
        "path": "/freeport-dolphin-encounters",
        "file": "freeport-dolphin-encounters/index.html",
        "kind": "attraction",
    },
    {
        "path": "/freeport-faq",
        "file": "freeport-faq/index.html",
        "kind": "guide",
    },
    {"path": "/contact", "file": "contact/index.html", "kind": "trust"},
    {"path": "/about", "file": "about/index.html", "kind": "trust"},
    {"path": "/privacy", "file": "privacy/index.html", "kind": "trust"},
    {"path": "/terms", "file": "terms/index.html", "kind": "trust"},
    {"path": "/methodology", "file": "methodology/index.html", "kind": "trust"},
]

RELATED_CORE = [
    ("/best-freeport-shore-excursions", "Best excursions"),
    ("/one-day-in-freeport-from-a-cruise-ship", "One day in Freeport"),
    ("/freeport-cruise-port-guide", "Port guide"),
    ("/freeport-beach-excursions", "Beaches"),
    ("/freeport-snorkelling-excursions", "Snorkelling"),
    ("/freeport-nature-garden-tours", "Nature &amp; gardens"),
]
