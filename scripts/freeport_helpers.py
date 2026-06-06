"""HTML helpers for Freeport Shore Excursion site build."""
import json

from freeport_config import (
    ACCENT,
    BOOKING_URL,
    DOMAIN,
    FONTS,
    HERO_GRADIENT,
    HOME_HERO,
    SHIP_ICON,
    SITE,
)


def abs_images(html: str) -> str:
    return (
        html.replace('src="images/', 'src="/images/')
        .replace("url('images/", "url('/images/")
        .replace('url("images/', 'url("/images/')
    )


def static_page_shell(
    *,
    title: str,
    description: str,
    keywords: str,
    canonical_path: str,
    data_page: str,
    nav: str,
    hero: str,
    content: str,
    footer: str,
    preload: str = HOME_HERO,
    schema: dict | None = None,
    trust: str = "",
) -> str:
    canon = f"{DOMAIN}/" if not canonical_path else f"{DOMAIN}/{canonical_path}"
    preload_path = preload if preload.startswith("/") else f"/{preload}"
    schema_block = ""
    if schema:
        schema_block = (
            f'  <script type="application/ld+json">\n'
            f"{json.dumps(schema, indent=2)}\n"
            f"  </script>\n"
        )
    trust_html = abs_images(trust) if trust else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="{keywords}" />
  <link rel="canonical" href="{canon}" />
  <link rel="preload" as="image" href="{preload_path}" fetchpriority="high" />

  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{DOMAIN}{preload_path}" />
  <meta property="og:site_name" content="{SITE}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="geo.region" content="BS" />
  <meta name="geo.placename" content="Freeport, Grand Bahama, Bahamas" />

{schema_block}
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="/js/tailwind-config.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{FONTS}" rel="stylesheet" />
  <link rel="stylesheet" href="/css/site.css" />
</head>
<body class="bg-white text-gray-800 antialiased" data-page="{data_page}">

{abs_images(nav)}
{abs_images(hero)}
{trust_html}
<main id="page-content">{abs_images(content)}</main>
{abs_images(footer)}

  <script src="/js/site.js"></script>
</body>
</html>
"""


def cruise_snapshot(
    *,
    time_in_port: str,
    best_for: str,
    activity_level: str,
    family: str,
    return_ship: str,
    popular: str,
) -> str:
    return f"""<aside class="cruise-snapshot mb-10 px-4 sm:px-0" aria-label="Cruise passenger snapshot">
  <h3 class="font-display font-bold text-lg text-gray-900 mb-4">Cruise Passenger Snapshot</h3>
  <dl class="cruise-snapshot__grid">
    <div class="cruise-snapshot__item"><dt>Typical Time In Port</dt><dd>{time_in_port}</dd></div>
    <div class="cruise-snapshot__item"><dt>Best For</dt><dd>{best_for}</dd></div>
    <div class="cruise-snapshot__item"><dt>Activity Level</dt><dd>{activity_level}</dd></div>
    <div class="cruise-snapshot__item"><dt>Family Friendly</dt><dd>{family}</dd></div>
    <div class="cruise-snapshot__item"><dt>Return To Ship Friendly</dt><dd>{return_ship}</dd></div>
    <div class="cruise-snapshot__item"><dt>Popular Excursion Types</dt><dd>{popular}</dd></div>
  </dl>
</aside>"""


def snapshot_default(**overrides: str) -> str:
    defaults = dict(
        time_in_port="6–10 hours (typical dock port)",
        best_for="Beaches, snorkelling, Garden of the Groves, dolphins",
        activity_level="Varies — see comparison",
        family="Excellent with age-appropriate picks",
        return_ship="Operators build 60–90 min buffer before all aboard",
        popular="Blue Hole snorkel, Taino Beach, Lucayan caves, dolphins",
    )
    defaults.update(overrides)
    return cruise_snapshot(**defaults)


def return_to_ship_badge() -> str:
    return (
        f'<span class="return-to-ship-badge" role="status">'
        f"{SHIP_ICON}Return To Ship On Time</span>"
    )


def small_group_badge() -> str:
    return '<span class="best-for-badge" role="status">Small Group Available</span>'


def best_for_badge(label: str) -> str:
    return f'<span class="best-for-badge" role="status">{label}</span>'


def why_choose_section(points: list[str], heading: str | None = None) -> str:
    title = heading or "Why Cruise Passengers Choose This Freeport Excursion"
    items = "".join(
        f'<li class="flex gap-2 text-sm text-gray-600">'
        f'<span class="text-ocean-500 shrink-0">✓</span>{p}</li>'
        for p in points
    )
    return f"""<section class="py-10 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">{title}</h2>
  <ul class="grid sm:grid-cols-2 gap-3">{items}</ul>
</div></section>"""


def tour_highlights(title: str, subtitle: str, cards: list[tuple]) -> str:
    items = []
    for img, alt, h3, p in cards:
        items.append(
            f"""<div class="bg-white rounded-3xl overflow-hidden shadow-md border border-pr-100 flex flex-col">
      <div class="card-media h-40">
        <img src="{img}" alt="{alt}" width="400" height="240" loading="lazy" decoding="async" />
      </div>
      <div class="p-5">
        <h3 class="font-display font-semibold text-gray-900 mb-2">{h3}</h3>
        <p class="text-sm text-gray-600 leading-relaxed">{p}</p>
      </div>
    </div>"""
        )
    return f"""<section class="py-14 bg-amber-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-10">
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">{title}</h2>
    <p class="text-gray-600 text-sm max-w-2xl mx-auto">{subtitle}</p>
  </div>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">{"".join(items)}</div>
</div></section>"""


def hero_wave() -> str:
    return (
        '<div class="absolute bottom-0 left-0 right-0">'
        '<svg viewBox="0 0 1440 48" xmlns="http://www.w3.org/2000/svg" '
        'preserveAspectRatio="none" class="site-hero__wave" aria-hidden="true">'
        '<path d="M0 24 C360 48 1080 0 1440 24 L1440 48 L0 48 Z" fill="white"/>'
        "</svg></div>"
    )


def hero_inner(
    eyebrow: str,
    title: str,
    lead: str,
    image: str,
    aria: str,
    breadcrumb: str = "",
    cta: tuple[str, str] | None = None,
    tags: list[str] | None = None,
) -> str:
    bc = ""
    if breadcrumb:
        bc = f"""<nav class="site-hero__breadcrumb flex items-center gap-2 mb-4 text-xs text-white/60" aria-label="Breadcrumb">
        <a href="index.html" class="hover:text-white transition-colors">Home</a>
        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
        <span class="text-white/80">{breadcrumb}</span>
      </nav>"""
    cta_html = ""
    if cta:
        cta_html = (
            f'<a href="{cta[0]}" class="btn-ocean inline-flex items-center justify-center gap-2 '
            f'text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">{cta[1]}</a>'
        )
    tags_html = ""
    if tags:
        tags_html = (
            '<div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">'
            + "".join(
                f'<span class="inline-flex items-center bg-white/10 border border-white/25 '
                f'rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">{t}</span>'
                for t in tags
            )
            + "</div>"
        )
    return f"""<section class="site-hero">
  <div class="absolute inset-0 hero-bg-custom" style="background-image: {HERO_GRADIENT}, url('{image}');" role="img" aria-label="{aria}"></div>
  <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl">
      {bc}
      <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
        <span class="w-2 h-2 rounded-full bg-pr-400 animate-pulse"></span>
        <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">{eyebrow}</span>
      </div>
      <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">{title}</h1>
      <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">{lead}</p>
      <div class="site-hero__actions flex flex-col sm:flex-row gap-3">{cta_html}</div>
      {tags_html}
    </div>
  </div>
  {hero_wave()}
</section>"""


def internal_links() -> str:
    links = [
        ("freeport-cruise-port-guide.html", "Port Guide"),
        ("best-freeport-shore-excursions.html", "Best Excursions"),
        ("one-day-in-freeport-from-a-cruise-ship.html", "One Day in Freeport"),
        ("freeport-beach-excursions.html", "Beach Excursions"),
        ("freeport-snorkelling-excursions.html", "Snorkelling"),
        ("freeport-nature-garden-tours.html", "Nature &amp; Gardens"),
        ("freeport-dolphin-encounters.html", "Dolphin Encounters"),
        ("freeport-faq.html", "FAQ"),
    ]
    parts = []
    for i, (href, label) in enumerate(links):
        if i:
            parts.append('<span class="text-gray-300">·</span>')
        parts.append(
            f'<a href="{href}" class="text-ocean-600 hover:text-ocean-800 font-medium">{label}</a>'
        )
    return f"""<nav class="mt-10 pt-8 border-t border-gray-100" aria-label="Related Freeport guides">
  <p class="text-sm font-semibold text-gray-900 mb-3">Plan your port day</p>
  <div class="flex flex-wrap gap-3 text-sm">{"".join(parts)}</div>
</nav>"""


def card_grid(cards: list[tuple]) -> str:
    items = []
    for img, alt, title, desc, link, label in cards:
        items.append(f"""<div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-pr-50 flex flex-col">
      <div class="card-media h-44 relative overflow-hidden">
        <img src="{img}" alt="{alt}" width="600" height="352" decoding="async" />
      </div>
      <div class="p-6 flex flex-col flex-1">
        <h3 class="text-lg font-display font-semibold text-gray-900 mb-2">{title}</h3>
        <p class="text-sm text-gray-500 leading-relaxed flex-1">{desc}</p>
        <a href="{link}" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">{label}</a>
      </div>
    </div>""")
    return '<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">' + "".join(items) + "</div>"


def book_cta(label: str = "View &amp; Book Tours") -> str:
    return (
        f'<a href="{BOOKING_URL}" rel="noopener noreferrer" target="_blank" '
        f'class="btn-ocean inline-flex items-center justify-center text-white font-semibold '
        f'px-7 py-3 rounded-full text-sm shadow-lg">{label}</a>'
    )


def content_category_page(
    intro: str,
    bullets: list[str],
    why_choose: list[str],
    highlights_cards: list[tuple],
    snapshot_kwargs: dict,
    img: str,
    alt: str,
    badge: str | None = None,
    show_small_group: bool = False,
    highlights_title: str = "Tour Highlights",
    highlights_subtitle: str = "What to expect on popular Freeport shore excursions.",
    why_heading: str | None = None,
) -> str:
    bl = "".join(
        f'<li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span>{b}</li>'
        for b in bullets
    )
    badges = [return_to_ship_badge()]
    if badge:
        badges.insert(0, best_for_badge(badge))
    if show_small_group:
        badges.append(small_group_badge())
    badge_html = f'<div class="mb-3 flex flex-wrap gap-2">{"".join(badges)}</div>'
    snap = snapshot_default(**snapshot_kwargs)
    highlights = tour_highlights(highlights_title, highlights_subtitle, highlights_cards)
    why = why_choose_section(why_choose, why_heading)
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
      <div>
        {badge_html}
        <p class="text-gray-600 leading-relaxed mb-6">{intro}</p>
        <ul class="space-y-3 mb-6">{bl}</ul>
        <div class="flex flex-wrap gap-3">{book_cta()}</div>
      </div>
      <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
        <img src="{img}" alt="{alt}" width="600" height="450" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    {why}
    {highlights}
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{internal_links()}</div></section>"""


def comparison_section(rows: list[tuple]) -> str:
    body = ""
    for name, dur, best, activity, link in rows:
        body += f"""<tr class="border-b border-pr-50 hover:bg-sand-50/80">
      <td class="py-4 pr-4 font-semibold text-gray-900"><a href="{link}" class="text-ocean-600 hover:text-ocean-800">{name}</a></td>
      <td class="py-4 px-3 text-gray-600">{dur}</td>
      <td class="py-4 px-3 text-gray-600">{best}</td>
      <td class="py-4 px-3 text-gray-600">{activity}</td>
      <td class="py-4 pl-3"><a href="{link}" class="text-pr-600 font-medium text-xs whitespace-nowrap">Guide →</a></td>
    </tr>"""
    return f"""<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 text-center mb-4">Which Freeport Excursion Is Right for Me?</h2>
  <p class="text-center text-gray-600 text-sm max-w-2xl mx-auto mb-10">Match your Freeport port day to beaches, snorkelling, nature tours and dolphin encounters — all timed for typical 6–10 hour dock port calls in Grand Bahama.</p>
  <div class="overflow-x-auto rounded-3xl border border-pr-100 shadow-sm">
    <table class="w-full text-sm text-left min-w-[720px]">
      <thead class="bg-ocean-800 text-white">
        <tr>
          <th class="py-4 px-4 font-semibold rounded-tl-3xl">Excursion</th>
          <th class="py-4 px-3 font-semibold">Duration</th>
          <th class="py-4 px-3 font-semibold">Best For</th>
          <th class="py-4 px-3 font-semibold">Activity Level</th>
          <th class="py-4 px-4 font-semibold rounded-tr-3xl">Details</th>
        </tr>
      </thead>
      <tbody class="bg-white">{body}</tbody>
    </table>
  </div>
  <p class="text-center mt-8">{book_cta("Browse All Freeport Tours")}</p>
</div></section>"""


def comparison_rows() -> list[tuple]:
    return [
        ("Blue Hole Snorkel &amp; Beach", "5 hrs", "Active water lovers", "Moderate — snorkel &amp; swim", "freeport-snorkelling-excursions.html"),
        ("Taino Beach Resort Day", "5 hrs", "Relaxed beach day", "Easy — pool &amp; swim", "freeport-beach-excursions.html"),
        ("Garden of the Groves &amp; City", "4 hrs", "Easy sightseeing", "Easy — gardens &amp; shopping", "freeport-nature-garden-tours.html"),
        ("Lucayan National Park &amp; Caves", "4 hrs", "Nature &amp; history", "Easy — cave walking", "freeport-nature-garden-tours.html"),
        ("Dolphin Close Encounter", "1 hr", "Marine encounters", "Moderate — platform interaction", "freeport-dolphin-encounters.html"),
        ("Swim with the Dolphins", "1 hr", "Premium dolphin swim", "Moderate — in-water swim", "freeport-dolphin-encounters.html"),
    ]


def faq_schema(questions: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in questions
        ],
    }


def home_schema(faq: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "name": SITE,
                "url": f"{DOMAIN}/",
                "description": "Planning guide for Freeport Grand Bahama cruise shore excursions",
            },
            {
                "@type": "LocalBusiness",
                "name": SITE,
                "url": f"{DOMAIN}/",
                "description": "Cruise passenger planning guide for Freeport Bahamas shore excursions",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Freeport",
                    "addressRegion": "Grand Bahama",
                    "addressCountry": "BS",
                },
                "areaServed": {
                    "@type": "City",
                    "name": "Freeport",
                    "containedInPlace": {"@type": "Country", "name": "Bahamas"},
                },
            },
            faq_schema(faq),
        ],
    }
