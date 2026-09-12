"""Freeport Shore Excursion site configuration."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://freeportshoreexcursion.com"
SITE = "Freeport Shore Excursion"
DATE = "2026-06-06"
BOOKING_URL = "https://www.shoreexcursionsgroup.com/port/freeport-cruise-port-tours"
FONTS = (
    "https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700"
    "&family=Source+Sans+3:wght@400;500;600;700&display=swap"
)
HERO_GRADIENT = (
    "linear-gradient(135deg, rgba(37, 99, 235, 0.75) 0%, "
    "rgba(249, 115, 22, 0.65) 50%, rgba(30, 58, 138, 0.55) 100%)"
)
ACCENT = "text-pr-300"

HOME_HERO = "images/hero-freeport.png"
HOME_HERO_ALT = (
    "Turquoise water and white sand beach on Grand Bahama Island near Freeport "
    "cruise port — calm Caribbean shoreline for cruise passenger shore excursions"
)
PORT_IMG = "images/freeport-cruise-port.png"
PORT_ALT = (
    "Freeport Grand Bahama harbour with cruise ship at dock and turquoise water "
    "for cruise passenger arrival at Freeport Bahamas cruise port"
)
BEST_IMG = "images/best-freeport-excursions.png"
BEST_ALT = (
    "Grand Bahama coastline and turquoise Caribbean water representing the best "
    "Freeport shore excursions for cruise passengers from Freeport Bahamas port"
)
ONE_DAY_IMG = "images/one-day-freeport.png"
ONE_DAY_ALT = (
    "Port Lucaya marketplace and harbour area on Grand Bahama for planning a "
    "one-day cruise ship shore excursion itinerary from Freeport Bahamas"
)
INTRO_IMG = "images/freeport-intro.png"
INTRO_ALT = (
    "Aerial view of Grand Bahama Island coastline with turquoise reef water and "
    "white sand beaches near Freeport cruise port for shore excursions"
)
BEACH_IMG = "images/freeport-beach.png"
BEACH_ALT = (
    "Calm turquoise water and white sand at Taino Beach resort area on Grand "
    "Bahama for cruise passenger beach shore excursions from Freeport port"
)
SNORKEL_IMG = "images/freeport-snorkelling.png"
SNORKEL_ALT = (
    "Snorkeller in clear turquoise Caribbean water over visible reef on a "
    "Freeport Bahamas snorkelling shore excursion for cruise passengers"
)
NATURE_IMG = "images/freeport-nature.png"
NATURE_ALT = (
    "Lush tropical gardens and palm trees at Garden of the Groves botanical "
    "garden on Grand Bahama for Freeport nature shore excursions"
)
DOLPHIN_IMG = "images/freeport-dolphin.png"
DOLPHIN_ALT = (
    "Dolphin close encounter experience at Sanctuary Bay on Grand Bahama for "
    "cruise passenger dolphin shore excursions from Freeport Bahamas port"
)
CAVE_IMG = "images/freeport-caves.png"
CAVE_ALT = (
    "Underground limestone cave formation at Lucayan National Park Grand Bahama "
    "on a guided shore excursion for cruise passengers from Freeport port"
)
BLUE_HOLE_IMG = "images/freeport-blue-hole.png"
BLUE_HOLE_ALT = (
    "Crystal-clear turquoise Blue Hole lagoon and beach on Grand Bahama for "
    "drift snorkelling on a Freeport Bahamas cruise shore excursion"
)
FAQ_IMG = "images/freeport-faq.png"
FAQ_ALT = (
    "Freeport Grand Bahama waterfront and cruise port area for cruise passenger "
    "shore excursion planning and FAQ guidance"
)

ALL_IMAGES = [
    HOME_HERO, PORT_IMG, BEST_IMG, ONE_DAY_IMG, INTRO_IMG,
    BEACH_IMG, SNORKEL_IMG, NATURE_IMG, DOLPHIN_IMG, CAVE_IMG,
    BLUE_HOLE_IMG, FAQ_IMG,
]

SHIP_ICON = (
    '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">'
    '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" '
    'd="M3 17h18M5 17l2-8h10l2 8M9 9l1-4h4l1 4"/></svg>'
)

PLACEHOLDER_PNG = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
    b"\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
    b"\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n"
    b"\xdb\x00\x00\x00\x00IEND\xaeB`\x82"
)

SITEMAP_PAGES = [
    ("", "1.0", "weekly"),
    ("best-freeport-shore-excursions.html", "0.9", "weekly"),
    ("freeport-beach-excursions.html", "0.9", "weekly"),
    ("freeport-snorkelling-excursions.html", "0.9", "weekly"),
    ("freeport-nature-garden-tours.html", "0.9", "weekly"),
    ("freeport-dolphin-encounters.html", "0.9", "weekly"),
    ("one-day-in-freeport-from-a-cruise-ship.html", "0.8", "monthly"),
    ("freeport-cruise-port-guide.html", "0.8", "monthly"),
    ("freeport-faq.html", "0.8", "monthly"),
]

FEATURED_TOURS = [
    {
        "title": "Freeport Blue Hole Snorkel and Beach with Lunch",
        "slug": "blue-hole-snorkel",
        "duration": "5 hours",
        "activity": "Moderate",
        "size": "Small group",
        "desc": "Drift snorkelling at the Blue Hole, turtle sightings, beach time and Bahamian lunch — the signature water adventure from Freeport.",
        "category": "snorkel",
    },
    {
        "title": "Garden of the Groves and Freeport City Day Tour",
        "slug": "garden-groves",
        "duration": "4 hours",
        "activity": "Easy",
        "size": "Standard",
        "desc": "Guided city tour, tropical botanical gardens and shopping at Port Lucaya Marketplace — an easy half-day from the cruise port.",
        "category": "nature",
    },
    {
        "title": "Lucayan National Park and Caves",
        "slug": "lucayan-caves",
        "duration": "4 hours",
        "activity": "Easy",
        "size": "Small group",
        "desc": "Explore Arawak Indian caves and walk through Lucayan National Park — history, nature and one of the world's longest underwater cave systems.",
        "category": "nature",
    },
    {
        "title": "Taino Beach Resort Day Pass",
        "slug": "taino-beach",
        "duration": "5 hours",
        "activity": "Easy",
        "size": "Small group",
        "desc": "Resort pool, beach chairs and calm Caribbean swim at Taino Beach — a relaxed port day without a packed tour schedule.",
        "category": "beach",
    },
    {
        "title": "Dolphin Close Encounter at Sanctuary Bay",
        "slug": "dolphin-encounter",
        "duration": "1 hour",
        "activity": "Moderate",
        "size": "Standard",
        "desc": "Kiss, hug and interact with dolphins in a controlled encounter — all ages welcome at Sanctuary Bay on Grand Bahama.",
        "category": "dolphin",
    },
    {
        "title": "Swim with the Dolphins",
        "slug": "swim-dolphins",
        "duration": "1 hour",
        "activity": "Moderate",
        "size": "Small group",
        "desc": "Swim alongside dolphins in the water at Sanctuary Bay — a premium marine encounter for active cruise passengers.",
        "category": "dolphin",
    },
]
