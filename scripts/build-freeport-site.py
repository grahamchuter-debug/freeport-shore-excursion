#!/usr/bin/env python3
"""Generate Freeport Shore Excursion static site files."""
from pathlib import Path

from freeport_config import (
    ACCENT,
    ALL_IMAGES,
    BEST_ALT,
    BEST_IMG,
    BEACH_ALT,
    BEACH_IMG,
    BLUE_HOLE_ALT,
    BLUE_HOLE_IMG,
    BOOKING_URL,
    DATE,
    DOMAIN,
    DOLPHIN_ALT,
    DOLPHIN_IMG,
    FAQ_ALT,
    FAQ_IMG,
    HERO_GRADIENT,
    HOME_HERO,
    HOME_HERO_ALT,
    INTRO_ALT,
    INTRO_IMG,
    NATURE_ALT,
    NATURE_IMG,
    ONE_DAY_ALT,
    ONE_DAY_IMG,
    PLACEHOLDER_PNG,
    PORT_ALT,
    PORT_IMG,
    ROOT,
    SITE,
    SITEMAP_PAGES,
    SNORKEL_ALT,
    SNORKEL_IMG,
)
from freeport_content import all_content, home_faq_data
from freeport_helpers import hero_inner, hero_wave, home_schema, static_page_shell


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  wrote {path}")


def hero_home() -> str:
    return f"""  <section class="site-hero">
    <div class="absolute inset-0 hero-bg" style="background-image: {HERO_GRADIENT}, url('{HOME_HERO}');" role="img" aria-label="{HOME_HERO_ALT}"></div>
    <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
          <span class="w-2 h-2 rounded-full bg-pr-400 animate-pulse"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">Freeport · Grand Bahama</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          Freeport Shore<br/><span class="{ACCENT}">Excursions</span><br/>from the Cruise Port
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Beaches, Blue Hole snorkelling, Garden of the Groves, Lucayan caves and dolphin encounters — the shore excursions cruise passengers book most from Freeport, Bahamas.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="best-freeport-shore-excursions.html" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Compare Excursions</a>
          <a href="freeport-snorkelling-excursions.html" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Blue Hole Snorkel</a>
        </div>
        <div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Taino Beach</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Blue Hole Snorkel</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Garden of the Groves</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Cruise Passengers</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">BSD &amp; USD</span>
        </div>
      </div>
    </div>
    {hero_wave()}
  </section>"""


def nav_html() -> str:
    return f"""<nav class="fixed top-0 left-0 right-0 z-50 bg-white/90 border-b border-pr-100 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-12">
      <a href="index.html" class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-full btn-ocean flex items-center justify-center">
          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>
          </svg>
        </div>
        <span class="font-display font-semibold text-ocean-800 text-base leading-tight">Freeport Shore<br/><span class="text-[10px] font-body font-normal text-pr-600 tracking-widest uppercase">Excursion</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-5 text-sm font-medium">
        <a href="index.html" data-nav="home" class="text-gray-600 hover:text-ocean-600 transition-colors">Home</a>
        <a href="best-freeport-shore-excursions.html" data-nav="excursions" class="text-gray-600 hover:text-ocean-600 transition-colors">Excursions</a>
        <a href="freeport-beach-excursions.html" data-nav="beach" class="text-gray-600 hover:text-ocean-600 transition-colors">Beaches</a>
        <a href="freeport-snorkelling-excursions.html" data-nav="snorkel" class="text-gray-600 hover:text-ocean-600 transition-colors">Snorkelling</a>
        <a href="freeport-nature-garden-tours.html" data-nav="nature" class="text-gray-600 hover:text-ocean-600 transition-colors">Nature</a>
        <a href="freeport-dolphin-encounters.html" data-nav="dolphin" class="text-gray-600 hover:text-ocean-600 transition-colors">Dolphins</a>
        <a href="freeport-cruise-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
      </div>
      <a href="best-freeport-shore-excursions.html" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        Compare Tours
      </a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sand-50" aria-label="Open menu">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>
</nav>
"""


def footer_html() -> str:
    return f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="index.html" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Planning guide for cruise visitors to Freeport, Grand Bahama. Not affiliated with any cruise line.</p>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Excursions</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="best-freeport-shore-excursions.html" class="hover:text-white transition-colors">All Excursions</a></li>
            <li><a href="freeport-beach-excursions.html" class="hover:text-white transition-colors">Beach Excursions</a></li>
            <li><a href="freeport-snorkelling-excursions.html" class="hover:text-white transition-colors">Snorkelling</a></li>
            <li><a href="freeport-nature-garden-tours.html" class="hover:text-white transition-colors">Nature &amp; Gardens</a></li>
            <li><a href="freeport-dolphin-encounters.html" class="hover:text-white transition-colors">Dolphin Encounters</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Guides</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="freeport-cruise-port-guide.html" class="hover:text-white transition-colors">Cruise Port Guide</a></li>
            <li><a href="one-day-in-freeport-from-a-cruise-ship.html" class="hover:text-white transition-colors">One Day in Freeport</a></li>
            <li><a href="freeport-faq.html" class="hover:text-white transition-colors">FAQ</a></li>
            <li><a href="{BOOKING_URL}" rel="noopener noreferrer" target="_blank" class="hover:text-white transition-colors">View &amp; Book Tours</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Verify times and prices with operators before booking.</p>
      </div>
    </div>
  </footer>
"""


def trust_strip_html() -> str:
    return """<section class="trust-strip" aria-label="Freeport shore excursion highlights">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="trust-strip__list">
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Taino Beach Days</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Blue Hole Snorkel</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Garden of the Groves</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Return To Ship On Time</li>
    </ul>
  </div>
</section>
"""


PAGE_META = [
    dict(
        file="index.html",
        title=f"{SITE} | Beaches, Snorkelling &amp; Nature Tours from Freeport Bahamas",
        description="Plan Freeport Bahamas shore excursions for cruise passengers — Taino Beach, Blue Hole snorkel, Garden of the Groves, Lucayan caves and dolphin encounters from Freeport cruise port.",
        keywords="Freeport shore excursions, Freeport Bahamas cruise excursions, Taino Beach Freeport, Blue Hole snorkel Bahamas, Garden of the Groves tour",
        path="",
        data_page="home",
        hero_key="hero-home.html",
        content_key="home.html",
        preload=HOME_HERO,
        schema=home_schema(home_faq_data()),
    ),
    dict(
        file="best-freeport-shore-excursions.html",
        title="Best Freeport Shore Excursions | Compare Grand Bahama Cruise Tours",
        description="Compare the best Freeport shore excursions — Blue Hole snorkel, Taino Beach, Garden of the Groves, Lucayan caves and dolphin encounters with cruise timing from Freeport Bahamas.",
        keywords="Freeport shore excursions, Freeport Bahamas cruise port tours, compare Freeport excursions, Grand Bahama cruise trips",
        path="best-freeport-shore-excursions.html",
        data_page="excursions",
        hero_key="hero-excursions.html",
        content_key="best-freeport-shore-excursions.html",
        preload=BEST_IMG,
        schema={"@context": "https://schema.org", "@type": "Article", "headline": "Best Freeport Shore Excursions", "url": f"{DOMAIN}/best-freeport-shore-excursions.html"},
    ),
    dict(
        file="freeport-beach-excursions.html",
        title="Freeport Beach Excursions | Taino Beach for Cruise Passengers",
        description="Freeport beach excursions for cruise passengers — Taino Beach resort day pass with pool, beach and calm Caribbean swim. Return-to-ship timing from Freeport Bahamas port.",
        keywords="Freeport beach excursions, Taino Beach cruise, Grand Bahama beach day, Freeport shore excursion beach",
        path="freeport-beach-excursions.html",
        data_page="beach",
        hero_key="hero-beach.html",
        content_key="freeport-beach-excursions.html",
        preload=BEACH_IMG,
        schema={"@context": "https://schema.org", "@type": "Article", "headline": "Freeport Beach Excursions", "url": f"{DOMAIN}/freeport-beach-excursions.html"},
    ),
    dict(
        file="freeport-snorkelling-excursions.html",
        title="Freeport Snorkelling Excursions | Blue Hole Snorkel Cruise Tours",
        description="Freeport snorkelling excursions for cruise passengers — Blue Hole drift snorkel, turtle sightings, beach and Bahamian lunch. Small-group tours from Freeport Bahamas cruise port.",
        keywords="Freeport snorkelling, Blue Hole snorkel Bahamas, Freeport cruise snorkel tour, Grand Bahama snorkelling excursion",
        path="freeport-snorkelling-excursions.html",
        data_page="snorkel",
        hero_key="hero-snorkel.html",
        content_key="freeport-snorkelling-excursions.html",
        preload=SNORKEL_IMG,
        schema={"@context": "https://schema.org", "@type": "Article", "headline": "Freeport Snorkelling Excursions", "url": f"{DOMAIN}/freeport-snorkelling-excursions.html"},
    ),
    dict(
        file="freeport-nature-garden-tours.html",
        title="Freeport Nature &amp; Garden Tours | Garden of the Groves &amp; Lucayan Caves",
        description="Freeport nature and garden tours for cruise passengers — Garden of the Groves botanical gardens, Lucayan National Park caves and city tour with Port Lucaya shopping.",
        keywords="Garden of the Groves Freeport, Lucayan National Park tour, Freeport nature excursion, Grand Bahama garden tour cruise",
        path="freeport-nature-garden-tours.html",
        data_page="nature",
        hero_key="hero-nature.html",
        content_key="freeport-nature-garden-tours.html",
        preload=NATURE_IMG,
        schema={"@context": "https://schema.org", "@type": "Article", "headline": "Freeport Nature and Garden Tours", "url": f"{DOMAIN}/freeport-nature-garden-tours.html"},
    ),
    dict(
        file="freeport-dolphin-encounters.html",
        title="Freeport Dolphin Encounters | Sanctuary Bay Cruise Excursions",
        description="Freeport dolphin encounters for cruise passengers — close encounter and swim programmes at Sanctuary Bay on Grand Bahama. All ages welcome on platform encounters.",
        keywords="Freeport dolphin encounter, Sanctuary Bay dolphins, swim with dolphins Bahamas cruise, Freeport dolphin tour",
        path="freeport-dolphin-encounters.html",
        data_page="dolphin",
        hero_key="hero-dolphin.html",
        content_key="freeport-dolphin-encounters.html",
        preload=DOLPHIN_IMG,
        schema={"@context": "https://schema.org", "@type": "Article", "headline": "Freeport Dolphin Encounters", "url": f"{DOMAIN}/freeport-dolphin-encounters.html"},
    ),
    dict(
        file="one-day-in-freeport-from-a-cruise-ship.html",
        title="One Day in Freeport from a Cruise Ship | Port Itinerary",
        description="How to spend one day in Freeport Bahamas on a cruise stop — Garden of the Groves, Port Lucaya, beach or snorkel with return-to-ship buffer.",
        keywords="one day in Freeport cruise, Freeport Bahamas port day itinerary, cruise stop Freeport planning",
        path="one-day-in-freeport-from-a-cruise-ship.html",
        data_page="port",
        hero_key="hero-one-day.html",
        content_key="one-day-in-freeport-from-a-cruise-ship.html",
        preload=ONE_DAY_IMG,
        schema={"@context": "https://schema.org", "@type": "Article", "headline": "One Day in Freeport from a Cruise Ship", "url": f"{DOMAIN}/one-day-in-freeport-from-a-cruise-ship.html"},
    ),
    dict(
        file="freeport-cruise-port-guide.html",
        title="Freeport Cruise Port Guide | Grand Bahama for Cruise Passengers",
        description="Freeport Bahamas cruise port guide — pier logistics, distances to Taino Beach and Lucayan National Park, taxis, currency and shore excursion planning.",
        keywords="Freeport cruise port guide, Freeport Bahamas port day, cruise passenger guide Freeport, Grand Bahama cruise terminal",
        path="freeport-cruise-port-guide.html",
        data_page="port",
        hero_key="hero-port-guide.html",
        content_key="freeport-cruise-port-guide.html",
        preload=PORT_IMG,
        schema={"@context": "https://schema.org", "@type": "Article", "headline": "Freeport Cruise Port Guide", "url": f"{DOMAIN}/freeport-cruise-port-guide.html"},
    ),
    dict(
        file="freeport-faq.html",
        title="Freeport Shore Excursions FAQ | Cruise Passenger Planning",
        description="FAQ for Freeport Bahamas shore excursions — port hours, currency, best tours, Lucayan caves, dolphin encounters and booking independent vs ship excursions.",
        keywords="Freeport shore excursion FAQ, Freeport cruise port questions, Grand Bahama excursion planning",
        path="freeport-faq.html",
        data_page="faq",
        hero_key="hero-faq.html",
        content_key="freeport-faq.html",
        preload=FAQ_IMG,
        schema={"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in home_faq_data()
        ]},
    ),
]


def build_hero_defs() -> dict[str, str]:
    return {
        "hero-home.html": hero_home(),
        "hero-excursions.html": hero_inner(
            "Freeport · Grand Bahama",
            f"Best Freeport<br/><span class=\"{ACCENT}\">Shore Excursions</span>",
            "Compare beaches, Blue Hole snorkelling, Garden of the Groves, Lucayan caves and dolphin encounters for your Freeport cruise ship schedule.",
            BEST_IMG, BEST_ALT, breadcrumb="Shore Excursions",
            cta=("best-freeport-shore-excursions.html", "Compare All Tours →"),
        ),
        "hero-beach.html": hero_inner(
            "Grand Bahama · Caribbean",
            f"Freeport<br/><span class=\"{ACCENT}\">Beach Excursions</span>",
            "Taino Beach resort day passes — pool, beach chairs and calm turquoise swim with cruise-friendly returns.",
            BEACH_IMG, BEACH_ALT, breadcrumb="Beach Excursions",
            cta=(BOOKING_URL, "View Beach Tours →"),
            tags=["🏖️ Taino Beach", "Easy Port Day", "Small Group"],
        ),
        "hero-snorkel.html": hero_inner(
            "Blue Hole · Grand Bahama",
            f"Freeport<br/><span class=\"{ACCENT}\">Snorkelling</span> Excursions",
            "Drift snorkelling, turtle sightings, beach time and Bahamian lunch on Freeport's signature water adventure.",
            SNORKEL_IMG, SNORKEL_ALT, breadcrumb="Snorkelling Excursions",
            cta=(BOOKING_URL, "View Snorkel Tours →"),
            tags=["🤿 Blue Hole", "Turtles", "Lunch Included"],
        ),
        "hero-nature.html": hero_inner(
            "Botanical Gardens · Caves",
            f"Freeport<br/><span class=\"{ACCENT}\">Nature &amp; Garden</span> Tours",
            "Garden of the Groves, Lucayan National Park caves and city tour with Port Lucaya shopping.",
            NATURE_IMG, NATURE_ALT, breadcrumb="Nature &amp; Garden Tours",
            cta=(BOOKING_URL, "View Nature Tours →"),
            tags=["🌴 Garden of the Groves", "Lucayan Caves", "Port Lucaya"],
        ),
        "hero-dolphin.html": hero_inner(
            "Sanctuary Bay · Grand Bahama",
            f"Freeport<br/><span class=\"{ACCENT}\">Dolphin</span> Encounters",
            "Close encounter and swim programmes at Sanctuary Bay — all ages welcome on platform interactions.",
            DOLPHIN_IMG, DOLPHIN_ALT, breadcrumb="Dolphin Encounters",
            cta=(BOOKING_URL, "View Dolphin Tours →"),
            tags=["🐬 Close Encounter", "Swim Programme", "1 Hour"],
        ),
        "hero-port-guide.html": hero_inner(
            "Cruise Passenger Guide",
            f"Freeport<br/><span class=\"{ACCENT}\">Cruise Port Guide</span>",
            "Pier logistics, Port Lucaya, distances to beaches and nature sites, taxis and return-to-ship timing.",
            PORT_IMG, PORT_ALT, breadcrumb="Port Guide",
            cta=("best-freeport-shore-excursions.html", "View Shore Excursions →"),
            tags=["🚢 Dock Port", "🏖️ Taino Beach", "🌴 Garden of the Groves", "💵 BSD & USD"],
        ),
        "hero-one-day.html": hero_inner(
            "Port Day Timeline",
            f"One Day in<br/><span class=\"{ACCENT}\">Freeport</span>",
            "Hour-by-hour plan from gangway to departure — gardens, Port Lucaya, beach or snorkel with return-to-ship buffer.",
            ONE_DAY_IMG, ONE_DAY_ALT, breadcrumb="One Day in Freeport",
        ),
        "hero-faq.html": hero_inner(
            "Cruise Planning Answers",
            f"Freeport<br/><span class=\"{ACCENT}\">Excursions FAQ</span>",
            "Port timing, currency, best tours, dolphin encounters and booking independent vs ship excursions.",
            FAQ_IMG, FAQ_ALT, breadcrumb="FAQ",
        ),
    }


def main() -> None:
    print("Building Freeport Shore Excursion site…")

    write("partials/nav.html", nav_html())
    write("partials/footer.html", footer_html())
    write("partials/trust-strip.html", trust_strip_html())

    heroes = build_hero_defs()
    for name, html in heroes.items():
        write(f"partials/{name}", html)

    contents = all_content()
    for name, html in contents.items():
        write(f"content/{name}", html)

    nav = nav_html()
    footer = footer_html()
    trust = trust_strip_html()

    for p in PAGE_META:
        write(
            p["file"],
            static_page_shell(
                title=p["title"],
                description=p["description"],
                keywords=p["keywords"],
                canonical_path=p["path"],
                data_page=p["data_page"],
                nav=nav,
                hero=heroes[p["hero_key"]],
                content=contents[p["content_key"]],
                footer=footer,
                trust=trust,
                preload=p["preload"],
                schema=p.get("schema"),
            ),
        )

    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, priority, freq in SITEMAP_PAGES:
        url = f"{DOMAIN}/{loc}" if loc else f"{DOMAIN}/"
        lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{DATE}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines) + "\n")

    write("package.json", """{
  "name": "freeport-shore-excursion",
  "private": true,
  "scripts": {
    "build": "python3 scripts/build-freeport-site.py",
    "images": "python3 scripts/fetch-freeport-images.py",
    "check": "python3 scripts/check-freeport-site.py",
    "deploy": "wrangler deploy",
    "preview": "python3 -m http.server 8910"
  },
  "devDependencies": {
    "wrangler": "^4.94.0"
  }
}
""")

    write("wrangler.jsonc", """{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "freeport-shore-excursion",
  "compatibility_date": "2026-06-06",
  "observability": { "enabled": true },
  "assets": { "directory": "." },
  "routes": [
    {
      "pattern": "freeportshoreexcursion.com",
      "custom_domain": true
    }
  ]
}
""")

    write("deploy.sh", f"""#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

echo "Deploying {SITE} to Cloudflare..."
npx wrangler deploy

echo "Done. Check {DOMAIN}/ shortly."
""")

    (ROOT / "deploy.sh").chmod(0o755)

    images_dir = ROOT / "images"
    images_dir.mkdir(exist_ok=True)
    backfill = {
        "freeport-intro.png": "hero-freeport.png",
        "best-freeport-excursions.png": "hero-freeport.png",
        "one-day-freeport.png": "freeport-cruise-port.png",
        "freeport-faq.png": "freeport-cruise-port.png",
        "freeport-caves.png": "freeport-nature.png",
        "freeport-blue-hole.png": "freeport-snorkelling.png",
    }
    for img in ALL_IMAGES:
        p = ROOT / img
        if p.exists() and p.stat().st_size > 5000:
            continue
        source = backfill.get(p.name)
        if source and (images_dir / source).exists() and (images_dir / source).stat().st_size > 5000:
            p.write_bytes((images_dir / source).read_bytes())
            continue
        p.write_bytes(PLACEHOLDER_PNG)

    write("images/ATTRIBUTION.md", """# Image attribution

Hero and content images are sourced from [Wikimedia Commons](https://commons.wikimedia.org) under Creative Commons licences where applicable.

Run `npm run images` to download location-accurate photos. Replace any image with your own assets — keep filenames consistent with `scripts/freeport_config.py`.
""")

    write("README.md", """# Freeport Shore Excursion

Cruise-passenger planning guide for Freeport, Grand Bahama shore excursions.

## Development

```bash
npm install
npm run build
npm run images
npm run check
npm run preview
```

Open http://localhost:8910

## Deploy to Cloudflare

```bash
npm run build && npm run images && npm run check && ./deploy.sh
```

Domain: https://freeportshoreexcursion.com
""")

    print("Done.")


if __name__ == "__main__":
    main()
