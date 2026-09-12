"""Freeport Shore Excursion — page bodies (Phase 19B growth rebuild)."""
from __future__ import annotations

from freeport_config import (
    ACCENT,
    BEACH_ALT,
    BEACH_IMG,
    BEST_ALT,
    BEST_IMG,
    CAVES_ALT,
    CAVES_IMG,
    HERO,
    HERO_ALT,
    INTRO_ALT,
    INTRO_IMG,
    NATURE_ALT,
    NATURE_IMG,
    RELATED_CORE,
    SNORKEL_ALT,
    SNORKEL_IMG,
)
from freeport_shell import (
    cruise_snapshot,
    editorial_cta,
    faq_section,
    hero_band,
    page_shell,
    related_links,
)

EMAIL = "hello@freeportshoreexcursion.com"


def _snap_common(**overrides: str) -> str:
    base = {
        "Geography": "Freeport call on Grand Bahama",
        "Pier note": "Standard calls dock at Lucayan Harbour — not Port Lucaya",
        "Near-port": "Taxi to Port Lucaya / Lucaya-area beaches",
        "East island": "Lucayan National Park / Gold Rock needs more port-day time",
        "Water days": "Snorkel &amp; boat plans are weather-dependent",
        "Planning rule": "One primary plan; leave a return buffer",
    }
    base.update(overrides)
    return cruise_snapshot(list(base.items()))


# ── Home ──────────────────────────────────────────────────────────────

HOME_FAQS = [
    (
        "Is Freeport a dock port?",
        "Most standard Freeport cruise calls dock alongside at Lucayan Harbour "
        "(also called the Freeport cruise terminal). That is different from "
        "Port Lucaya, the tourist marketplace. Some Carnival Corporation sailings "
        "use Celebration Key — a separate private pier with different logistics.",
    ),
    (
        "What should first-time visitors do in Freeport?",
        "Choose one primary plan that fits your usable hours: a Garden of the "
        "Groves / city-style outing, a Lucaya-area beach day, or — on a fuller "
        "window — Lucayan National Park or a dedicated snorkel excursion. "
        "Avoid stacking east-island nature, beach, and city shopping on a short call.",
    ),
    (
        "Is Port Lucaya the cruise pier?",
        "No. Port Lucaya is a tourist marketplace and marina area. You typically "
        "need a taxi or organised transfer from the cruise terminal. Do not "
        "assume a walkable tourist strip at the pier.",
    ),
    (
        "What is Lucayan National Park versus Garden of the Groves?",
        "Garden of the Groves is a botanical garden outing often paired with "
        "Freeport / Port Lucaya sightseeing. Lucayan National Park sits farther "
        "east and includes cave areas and Gold Rock Beach access — treat it as "
        "a dedicated half-day-style commitment, not a quick add-on.",
    ),
]


def home_page() -> str:
    hero = hero_band(
        eyebrow="Freeport · Grand Bahama",
        title_html=(
            f'Freeport Shore<br/><span class="{ACCENT}">Excursions</span>'
            "<br/>from the Cruise Port"
        ),
        lead=(
            "A practical guide to Freeport tours and cruise excursions on Grand Bahama — "
            "beach days, snorkelling, Garden of the Groves, Lucayan nature, and how to "
            "shape one realistic day from the pier."
        ),
        image=HERO,
        aria_label=HERO_ALT,
        actions=(
            '<a href="/best-freeport-shore-excursions" class="btn-primary inline-flex '
            'items-center justify-center gap-2 text-white font-semibold px-7 py-3 '
            'rounded-full text-sm shadow-xl">Compare options</a>'
            '<a href="/one-day-in-freeport-from-a-cruise-ship" class="btn-outline inline-flex '
            'items-center justify-center gap-2 text-white font-semibold px-7 py-3 '
            'rounded-full text-sm">One day in Freeport</a>'
        ),
        tags=["Beach", "Snorkelling", "See Grand Bahama", "Lucayan nature", "Cruise planning"],
    )
    main = f"""
<section class="pt-10 pb-6 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    {_snap_common()}
  </div>
</section>

<section class="py-14 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-10">
      <div class="section-label mx-auto">Decision spine</div>
      <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-4">How do you want to spend Freeport?</h2>
      <p class="text-gray-600 text-sm max-w-2xl mx-auto">Pick one primary shape for your usable hours ashore. Private or small-group arrangements may suit some travellers later — we do not list live private inventory here.</p>
    </div>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <a href="/freeport-beach-excursions" class="card-hover block bg-white rounded-3xl p-6 border border-ocean-100 shadow-sm">
        <h3 class="font-display font-bold text-lg text-gray-900 mb-2">Beach</h3>
        <p class="text-sm text-gray-600 leading-relaxed">Taino Beach and Lucaya-area beach days — relaxed swimming and shade when you want a low-complexity port day.</p>
      </a>
      <a href="/freeport-snorkelling-excursions" class="card-hover block bg-white rounded-3xl p-6 border border-ocean-100 shadow-sm">
        <h3 class="font-display font-bold text-lg text-gray-900 mb-2">Snorkelling / water</h3>
        <p class="text-sm text-gray-600 leading-relaxed">Ocean snorkel excursions (including Blue Hole–style boat days). Weather and sea state can cancel or change plans.</p>
      </a>
      <a href="/freeport-nature-garden-tours" class="card-hover block bg-white rounded-3xl p-6 border border-ocean-100 shadow-sm">
        <h3 class="font-display font-bold text-lg text-gray-900 mb-2">See Grand Bahama</h3>
        <p class="text-sm text-gray-600 leading-relaxed">Garden of the Groves and Freeport / Port Lucaya sightseeing — a land-based way to see more of the island without a boat.</p>
      </a>
      <a href="/one-day-in-freeport-from-a-cruise-ship" class="card-hover block bg-white rounded-3xl p-6 border border-ocean-100 shadow-sm">
        <h3 class="font-display font-bold text-lg text-gray-900 mb-2">One day in Freeport</h3>
        <p class="text-sm text-gray-600 leading-relaxed">Short-call, half-day, and fuller-day scenarios — what is realistic, and what to skip.</p>
      </a>
      <a href="/freeport-nature-garden-tours" class="card-hover block bg-white rounded-3xl p-6 border border-ocean-100 shadow-sm">
        <h3 class="font-display font-bold text-lg text-gray-900 mb-2">Nature / Lucayan National Park</h3>
        <p class="text-sm text-gray-600 leading-relaxed">East-island caves, park trails, and Gold Rock Beach context — treat as a dedicated outing, not a quick hop.</p>
      </a>
      <a href="/freeport-cruise-port-guide" class="card-hover block bg-white rounded-3xl p-6 border border-ocean-100 shadow-sm">
        <h3 class="font-display font-bold text-lg text-gray-900 mb-2">Port logistics</h3>
        <p class="text-sm text-gray-600 leading-relaxed">Lucayan Harbour vs Port Lucaya vs Celebration Key — get the names straight before you book anything.</p>
      </a>
    </div>
  </div>
</section>

<section class="py-16 bg-sand-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid lg:grid-cols-2 gap-12 items-center">
      <div>
        <div class="section-label">Grand Bahama orientation</div>
        <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Freeport is the call name — Grand Bahama is the island</h2>
        <p class="text-gray-600 leading-relaxed mb-4">Cruise passengers usually arrive at <strong>Lucayan Harbour</strong> (the Freeport cruise terminal). <strong>Port Lucaya</strong> is a separate tourist marketplace and marina area. <strong>Lucayan National Park</strong> and <strong>Gold Rock Beach</strong> sit farther east. Confusing those names is the fastest way to build an unrealistic day.</p>
        <p class="text-gray-600 leading-relaxed mb-5">Read the <a href="/freeport-cruise-port-guide" class="text-ocean-600 font-semibold">port guide</a> before comparing tours.</p>
        <a href="/best-freeport-shore-excursions" class="text-ocean-600 font-semibold text-sm">Compare Freeport shore excursion styles →</a>
      </div>
      <div class="info-image rounded-3xl aspect-[4/3] shadow-xl overflow-hidden">
        <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
      </div>
    </div>
  </div>
</section>

<section class="py-16 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-10">
      <h2 class="text-3xl font-display font-bold text-gray-900">Popular Freeport planning themes</h2>
      <p class="text-gray-600 text-sm mt-3 max-w-xl mx-auto">Themes cruise guests research most — not a ranked catalogue or popularity score.</p>
    </div>
    <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="rounded-3xl overflow-hidden border border-ocean-100 bg-white shadow-sm">
        <div class="card-media h-40"><img src="{BEACH_IMG}" alt="{BEACH_ALT}" width="400" height="240" loading="lazy" decoding="async" /></div>
        <div class="p-5"><h3 class="font-display font-semibold mb-2">Beach day</h3><p class="text-sm text-gray-600">Calm-water swimming near the Lucaya side of the island.</p></div>
      </div>
      <div class="rounded-3xl overflow-hidden border border-ocean-100 bg-white shadow-sm">
        <div class="card-media h-40"><img src="{SNORKEL_IMG}" alt="{SNORKEL_ALT}" width="400" height="240" loading="lazy" decoding="async" /></div>
        <div class="p-5"><h3 class="font-display font-semibold mb-2">Snorkel day</h3><p class="text-sm text-gray-600">Boat-based reef / Blue Hole–style water time with weather risk.</p></div>
      </div>
      <div class="rounded-3xl overflow-hidden border border-ocean-100 bg-white shadow-sm">
        <div class="card-media h-40"><img src="{NATURE_IMG}" alt="{NATURE_ALT}" width="400" height="240" loading="lazy" decoding="async" /></div>
        <div class="p-5"><h3 class="font-display font-semibold mb-2">Gardens &amp; city</h3><p class="text-sm text-gray-600">Garden of the Groves plus Freeport / Port Lucaya context.</p></div>
      </div>
      <div class="rounded-3xl overflow-hidden border border-ocean-100 bg-white shadow-sm">
        <div class="card-media h-40"><img src="{CAVES_IMG}" alt="{CAVES_ALT}" width="400" height="240" loading="lazy" decoding="async" /></div>
        <div class="p-5"><h3 class="font-display font-semibold mb-2">Lucayan nature</h3><p class="text-sm text-gray-600">Park caves and Gold Rock area — east-island commitment.</p></div>
      </div>
    </div>
  </div>
</section>

{faq_section(HOME_FAQS, heading="Freeport shore excursions FAQ")}

{editorial_cta(
    "See Grand Bahama without overpacking the day",
    "Garden and city-style outings are often the simplest land-based way to get island context. Explore that tour type on our nature and comparison pages — booking is not live on this site yet.",
    "/freeport-nature-garden-tours",
    "Explore this type of tour",
)}

<section class="py-16 cta-gradient">
  <div class="max-w-3xl mx-auto px-4 text-center">
    <h2 class="text-3xl font-display font-bold text-white mb-4">Plan your Freeport port day</h2>
    <p class="text-white/85 text-sm mb-6">Compare excursion styles, build a realistic one-day plan, and confirm pier versus Port Lucaya before you go ashore.</p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <a href="/best-freeport-shore-excursions" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Compare excursions</a>
      <a href="/one-day-in-freeport-from-a-cruise-ship" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">One-day scenarios</a>
    </div>
  </div>
</section>
"""
    return page_shell(
        title="Freeport Shore Excursion | Grand Bahama Cruise Tours & Port Planning",
        description=(
            "Plan Freeport shore excursions on Grand Bahama — beach, snorkelling, "
            "Garden of the Groves, Lucayan National Park, and realistic one-day cruise planning."
        ),
        canonical_path="/",
        page_id="home",
        hero_html=hero,
        main_html=main,
        og_image=HERO,
        faq_entities=HOME_FAQS,
    )


# ── Best excursions ───────────────────────────────────────────────────

def best_page() -> str:
    hero = hero_band(
        eyebrow="Comparison guide",
        title_html=f'Best Freeport<br/><span class="{ACCENT}">Shore Excursions</span>',
        lead=(
            "A decision guide for cruise passengers — compare garden/city, beach, "
            "Lucayan National Park, and snorkel days by port-day fit, not fake rankings."
        ),
        image=BEST_IMG,
        aria_label=BEST_ALT,
        breadcrumb="Best Freeport shore excursions",
        actions=(
            '<a href="/one-day-in-freeport-from-a-cruise-ship" class="btn-primary inline-flex '
            'items-center justify-center gap-2 text-white font-semibold px-7 py-3 '
            'rounded-full text-sm shadow-xl">One-day scenarios</a>'
            '<a href="/freeport-cruise-port-guide" class="btn-outline inline-flex '
            'items-center justify-center gap-2 text-white font-semibold px-7 py-3 '
            'rounded-full text-sm">Port guide</a>'
        ),
    )
    main = f"""
<section class="pt-10 pb-4 bg-white">
  <div class="max-w-3xl mx-auto px-4 text-center">
    <p class="text-gray-600 text-sm leading-relaxed">This page compares <strong>styles of Freeport shore excursion</strong>, not a scored product catalogue. Operators, meeting points, and inclusions vary — confirm live details before you travel. We do not publish live prices or booking forms here.</p>
  </div>
</section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{_snap_common(**{"Best for": "Matching one plan to your usable hours"})}</div></section>

<section class="py-14 bg-sand-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-display font-bold text-gray-900 text-center mb-4">Which Freeport excursion style fits?</h2>
    <p class="text-center text-gray-600 text-sm max-w-2xl mx-auto mb-10">Use activity type, complexity, and how much of Grand Bahama you want to cover — then protect your return window.</p>
    <div class="overflow-x-auto rounded-3xl border border-ocean-100 shadow-sm bg-white">
      <table class="w-full text-sm text-left min-w-[720px]">
        <thead class="bg-ocean-800 text-white">
          <tr>
            <th class="py-4 px-4 font-semibold rounded-tl-3xl">Style</th>
            <th class="py-4 px-3 font-semibold">Best when</th>
            <th class="py-4 px-3 font-semibold">Complexity</th>
            <th class="py-4 px-4 font-semibold rounded-tr-3xl">Guide</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-ocean-50">
            <td class="py-4 px-4 font-semibold text-gray-900">Garden / city (See Grand Bahama)</td>
            <td class="py-4 px-3 text-gray-600">You want land sightseeing and Port Lucaya context without a boat</td>
            <td class="py-4 px-3 text-gray-600">Usually simpler pier-meet patterns</td>
            <td class="py-4 px-4"><a href="/freeport-nature-garden-tours" class="text-ocean-600 font-medium">Nature &amp; gardens →</a></td>
          </tr>
          <tr class="border-b border-ocean-50">
            <td class="py-4 px-4 font-semibold text-gray-900">Beach day</td>
            <td class="py-4 px-3 text-gray-600">You want swimming and shade more than sightseeing</td>
            <td class="py-4 px-3 text-gray-600">Often taxi or organised transfer from the pier</td>
            <td class="py-4 px-4"><a href="/freeport-beach-excursions" class="text-ocean-600 font-medium">Beaches →</a></td>
          </tr>
          <tr class="border-b border-ocean-50">
            <td class="py-4 px-4 font-semibold text-gray-900">Lucayan National Park / caves</td>
            <td class="py-4 px-3 text-gray-600">You want east-island nature as the main plan</td>
            <td class="py-4 px-3 text-gray-600">More port-day time; not a quick add-on</td>
            <td class="py-4 px-4"><a href="/freeport-nature-garden-tours" class="text-ocean-600 font-medium">Lucayan context →</a></td>
          </tr>
          <tr class="border-b border-ocean-50">
            <td class="py-4 px-4 font-semibold text-gray-900">Snorkel / Blue Hole–style water day</td>
            <td class="py-4 px-3 text-gray-600">You want a boat-and-mask day and accept weather risk</td>
            <td class="py-4 px-3 text-gray-600">Higher logistics; sea state can change everything</td>
            <td class="py-4 px-4"><a href="/freeport-snorkelling-excursions" class="text-ocean-600 font-medium">Snorkelling →</a></td>
          </tr>
          <tr>
            <td class="py-4 px-4 font-semibold text-gray-900">One-day combination logic</td>
            <td class="py-4 px-3 text-gray-600">You are choosing between short, half, and fuller calls</td>
            <td class="py-4 px-3 text-gray-600">Scenario planning — no fake hourly clocks</td>
            <td class="py-4 px-4"><a href="/one-day-in-freeport-from-a-cruise-ship" class="text-ocean-600 font-medium">One day →</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="py-14 bg-white">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">What “best” means here</h2>
    <ul class="space-y-3 text-sm text-gray-600">
      <li><strong class="text-gray-900">Fit to usable hours</strong> — short calls favour one near-port or garden/city plan; east-island nature needs more time.</li>
      <li><strong class="text-gray-900">Meeting clarity</strong> — pier-walk meets are simpler than self-taxi beach passes; confirm your ticket.</li>
      <li><strong class="text-gray-900">Weather honesty</strong> — water days can be cancelled or altered; have a land backup idea.</li>
      <li><strong class="text-gray-900">No fake scores</strong> — we do not invent ratings, popularity ranks, or availability counts.</li>
    </ul>
    <div class="mt-10">
      {related_links(RELATED_CORE)}
    </div>
  </div>
</section>

{editorial_cta(
    "Garden and city-style Freeport days",
    "If you want a straightforward land-based introduction to Freeport and Port Lucaya, explore Garden of the Groves / city tour styles on the nature page. Editorial guidance only — no live booking on this site.",
    "/freeport-nature-garden-tours",
    "Explore this type of tour",
)}
"""
    return page_shell(
        title="Best Freeport Shore Excursions | Compare Grand Bahama Cruise Options",
        description=(
            "Compare Freeport shore excursion styles for cruise passengers — garden/city, "
            "beach, Lucayan National Park, and snorkel days by port-day fit."
        ),
        canonical_path="/best-freeport-shore-excursions",
        page_id="excursions",
        hero_html=hero,
        main_html=main,
        og_image=BEST_IMG,
    )


# ── One day (flagship) ────────────────────────────────────────────────

def one_day_page() -> str:
    hero = hero_band(
        eyebrow="Port-day scenarios",
        title_html=f'One Day in Freeport<br/><span class="{ACCENT}">from a Cruise Ship</span>',
        lead=(
            "Choose a short-call, half-day, or fuller-day plan for Freeport on Grand Bahama — "
            "without invented hour-by-hour clocks."
        ),
        image=None,
        aria_label="Cruise day planning atmosphere for Freeport Grand Bahama",
        css_only=True,
        breadcrumb="One day in Freeport",
        actions=(
            '<a href="/best-freeport-shore-excursions" class="btn-primary inline-flex '
            'items-center justify-center gap-2 text-white font-semibold px-7 py-3 '
            'rounded-full text-sm shadow-xl">Compare styles</a>'
            '<a href="/freeport-cruise-port-guide" class="btn-outline inline-flex '
            'items-center justify-center gap-2 text-white font-semibold px-7 py-3 '
            'rounded-full text-sm">Port guide</a>'
        ),
        tags=["Short call", "Half day", "Fuller day", "No fake schedules"],
    )
    main = f"""
<section class="py-14 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <p class="text-gray-600 text-sm max-w-3xl mb-10">Use your ship’s published arrival, all-aboard, and tender/dock notes — not a generic timetable. Times below are <strong>scenario labels only</strong>. We do not invent fixed departure clocks.</p>
    {_snap_common(**{"Best for": "Choosing one realistic Freeport plan"})}

    <div class="grid lg:grid-cols-3 gap-6 mb-14">
      <article class="bg-sky-50 rounded-3xl p-7 border border-sky-100">
        <h2 class="font-display font-bold text-lg mb-3">Short call</h2>
        <p class="text-sm text-gray-600 leading-relaxed mb-3">Choose <strong>one</strong> main plan:</p>
        <ul class="text-sm text-gray-600 space-y-2 mb-3 list-disc pl-5">
          <li>Garden / city-style sightseeing (Garden of the Groves + Freeport / Port Lucaya context), <strong>or</strong></li>
          <li>A nearer beach / Port Lucaya–area day</li>
        </ul>
        <p class="text-sm text-gray-600"><strong>Do not stack</strong> east-island Lucayan nature + beach + city shopping.</p>
      </article>
      <article class="bg-teal-50 rounded-3xl p-7 border border-teal-100">
        <h2 class="font-display font-bold text-lg mb-3">Half day</h2>
        <p class="text-sm text-gray-600 leading-relaxed mb-3">Possible primary plans:</p>
        <ul class="text-sm text-gray-600 space-y-2 mb-3 list-disc pl-5">
          <li>Garden of the Groves + city / Port Lucaya</li>
          <li>Beach day (Taino / Lucaya-area)</li>
          <li>Lucayan National Park / caves as the <strong>sole</strong> outing</li>
        </ul>
        <p class="text-sm text-gray-600"><strong>Rule:</strong> one primary plan beats three “quick” stops.</p>
      </article>
      <article class="bg-amber-50 rounded-3xl p-7 border border-amber-100">
        <h2 class="font-display font-bold text-lg mb-3">Fuller port day</h2>
        <p class="text-sm text-gray-600 leading-relaxed mb-3">When your usable window is clearly longer, choose one signature day:</p>
        <ul class="text-sm text-gray-600 space-y-2 mb-3 list-disc pl-5">
          <li>Lucayan National Park / Gold Rock area, <strong>or</strong></li>
          <li>Blue Hole–style ocean snorkel day, <strong>or</strong></li>
          <li>Beach + light Port Lucaya browsing</li>
        </ul>
        <p class="text-sm text-gray-600">Still leave margin for transfer queues and weather changes.</p>
      </article>
    </div>

    <div class="max-w-3xl">
      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">What is realistic</h2>
      <p class="text-gray-600 leading-relaxed mb-6">The cruise pier is not Port Lucaya. Many beaches and attractions need transport. East-island nature uses more of your day than a marketplace stop. Water activities can be delayed or cancelled in poor sea state.</p>

      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">What is not realistic</h2>
      <p class="text-gray-600 leading-relaxed mb-6">Treating Lucayan National Park, a full beach resort day, and extensive Freeport shopping as three equal “short” stops on a tight call. Also: assuming Celebration Key logistics apply to a normal Freeport Lucayan Harbour call (or the reverse).</p>

      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Return planning</h2>
      <p class="text-gray-600 leading-relaxed mb-6">Build your own buffer from all-aboard. We do not claim operators “return you on time,” publish guaranteed buffers, or promise the ship will wait for independent bookings. Confirm operator policies in writing if that matters to you.</p>

      {related_links([
        ("/best-freeport-shore-excursions", "Best excursions"),
        ("/freeport-cruise-port-guide", "Port guide"),
        ("/freeport-beach-excursions", "Beaches"),
        ("/freeport-nature-garden-tours", "Nature &amp; gardens"),
        ("/freeport-snorkelling-excursions", "Snorkelling"),
      ])}
    </div>
  </div>
</section>

{editorial_cta(
    "Garden / city as a short or half-day plan",
    "If your usable hours favour land sightseeing over boats, explore Garden of the Groves and Freeport city-style tour themes. Editorial only — booking is not live here.",
    "/freeport-nature-garden-tours",
    "Explore this type of tour",
)}
"""
    return page_shell(
        title="One Day in Freeport from a Cruise Ship | Port Day Scenarios",
        description=(
            "How to spend one day in Freeport from a cruise ship — short-call, half-day, "
            "and fuller-day scenarios for Grand Bahama without invented hourly itineraries."
        ),
        canonical_path="/one-day-in-freeport-from-a-cruise-ship",
        page_id="oneday",
        hero_html=hero,
        main_html=main,
        og_image=None,
    )


# ── Port guide ────────────────────────────────────────────────────────

def port_page() -> str:
    hero = hero_band(
        eyebrow="Logistics",
        title_html=f'Freeport Cruise<br/><span class="{ACCENT}">Port Guide</span>',
        lead=(
            "Lucayan Harbour, Port Lucaya, Lucayan National Park, and Celebration Key — "
            "the names that matter for a Freeport cruise call on Grand Bahama."
        ),
        image=None,
        aria_label="Freeport cruise port planning on Grand Bahama",
        css_only=True,
        breadcrumb="Freeport cruise port guide",
        actions=(
            '<a href="/one-day-in-freeport-from-a-cruise-ship" class="btn-primary inline-flex '
            'items-center justify-center gap-2 text-white font-semibold px-7 py-3 '
            'rounded-full text-sm shadow-xl">One-day scenarios</a>'
            '<a href="/best-freeport-shore-excursions" class="btn-outline inline-flex '
            'items-center justify-center gap-2 text-white font-semibold px-7 py-3 '
            'rounded-full text-sm">Compare options</a>'
        ),
    )
    main = f"""
<section class="py-14 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    {_snap_common(**{"Best for": "Getting pier vs tourist areas straight"})}
    <div class="max-w-3xl prose-like">
      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Where ships dock</h2>
      <p class="text-gray-600 leading-relaxed mb-6">Most <strong>standard Freeport</strong> cruise calls dock at <strong>Lucayan Harbour</strong> (also described as the Freeport cruise terminal) on Grand Bahama. Passengers typically walk off a pier — this is a dock call pattern for those sailings, not a tender operation. Always confirm your sailing’s berth notes.</p>

      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Names that get confused</h2>
      <dl class="space-y-4 text-sm mb-10">
        <div class="bg-sand-50 rounded-2xl p-5 border border-ocean-50"><dt class="font-semibold text-gray-900">Grand Bahama</dt><dd class="text-gray-600 mt-1">The island.</dd></div>
        <div class="bg-sand-50 rounded-2xl p-5 border border-ocean-50"><dt class="font-semibold text-gray-900">Freeport</dt><dd class="text-gray-600 mt-1">Main city / common cruise call name.</dd></div>
        <div class="bg-sand-50 rounded-2xl p-5 border border-ocean-50"><dt class="font-semibold text-gray-900">Lucayan Harbour / Freeport cruise terminal</dt><dd class="text-gray-600 mt-1">Main docking area for many non–Celebration Key Freeport calls. Not the same place as Port Lucaya.</dd></div>
        <div class="bg-sand-50 rounded-2xl p-5 border border-ocean-50"><dt class="font-semibold text-gray-900">Port Lucaya</dt><dd class="text-gray-600 mt-1">Tourist marketplace / marina district. Usually requires a taxi or organised transfer from the cruise pier.</dd></div>
        <div class="bg-sand-50 rounded-2xl p-5 border border-ocean-50"><dt class="font-semibold text-gray-900">Lucayan National Park</dt><dd class="text-gray-600 mt-1">East-island park with cave areas and access toward Gold Rock Beach — a dedicated outing.</dd></div>
        <div class="bg-sand-50 rounded-2xl p-5 border border-ocean-50"><dt class="font-semibold text-gray-900">Gold Rock Beach</dt><dd class="text-gray-600 mt-1">Beach associated with the Lucayan National Park area — not Port Lucaya beach.</dd></div>
        <div class="bg-amber-50 rounded-2xl p-5 border border-amber-100"><dt class="font-semibold text-gray-900">Celebration Key</dt><dd class="text-gray-600 mt-1">A separate Carnival private destination / pier context on Grand Bahama. Do not assume Freeport Lucayan Harbour logistics, tours, or walking patterns apply there (or the reverse).</dd></div>
      </dl>

      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Getting around</h2>
      <p class="text-gray-600 leading-relaxed mb-6">Licensed taxis and organised excursions are the usual tools from the pier. We do not publish taxi fares or exact drive times here — sources disagree, and traffic varies. Ask at the terminal or confirm with your operator for live estimates.</p>

      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Cruise usefulness</h2>
      <ul class="space-y-2 text-sm text-gray-600 mb-8 list-disc pl-5">
        <li>The port area is not the same as Port Lucaya.</li>
        <li>Many beaches and attractions require transport.</li>
        <li>East-island attractions use more of your port day.</li>
        <li>Weather can affect snorkel and boat plans.</li>
        <li>Short calls need simpler plans.</li>
        <li>Leave a personal return buffer — we do not guarantee ship waits for independent tours.</li>
      </ul>

      {related_links(RELATED_CORE)}
    </div>
  </div>
</section>
"""
    return page_shell(
        title="Freeport Cruise Port Guide | Lucayan Harbour, Port Lucaya & Grand Bahama",
        description=(
            "Freeport cruise port guide for Grand Bahama — Lucayan Harbour vs Port Lucaya, "
            "Lucayan National Park, Gold Rock, and Celebration Key logistics for cruise passengers."
        ),
        canonical_path="/freeport-cruise-port-guide",
        page_id="port",
        hero_html=hero,
        main_html=main,
        og_image=None,
    )


# ── Beach ─────────────────────────────────────────────────────────────

def beach_page() -> str:
    hero = hero_band(
        eyebrow="Beach days",
        title_html=f'Freeport<br/><span class="{ACCENT}">Beach Excursions</span>',
        lead=(
            "Taino Beach and Lucaya-area beach options for cruise passengers — "
            "organised day passes versus DIY taxi days, without invented fares."
        ),
        image=BEACH_IMG,
        aria_label=BEACH_ALT,
        breadcrumb="Freeport beach excursions",
        actions=(
            '<a href="/one-day-in-freeport-from-a-cruise-ship" class="btn-primary inline-flex '
            'items-center justify-center gap-2 text-white font-semibold px-7 py-3 '
            'rounded-full text-sm shadow-xl">One-day scenarios</a>'
            '<a href="/best-freeport-shore-excursions" class="btn-outline inline-flex '
            'items-center justify-center gap-2 text-white font-semibold px-7 py-3 '
            'rounded-full text-sm">Compare options</a>'
        ),
    )
    main = f"""
<section class="py-14 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    {_snap_common(**{"Best for": "Relaxed swimming and shade"})}
    <div class="grid lg:grid-cols-2 gap-12 items-start">
      <div>
        <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Taino Beach and Lucaya-area options</h2>
        <p class="text-gray-600 leading-relaxed mb-4">Many cruise guests look at <strong>Taino Beach</strong> resort-style day access and other Lucaya-area beaches for calm swimming. These areas are <strong>not</strong> at the Lucayan Harbour pier — expect a transfer.</p>
        <p class="text-gray-600 leading-relaxed mb-4">Organised beach day products sometimes include transport; others are day-pass only with <strong>self-arranged taxi</strong>. Do not assume transport is included. Read the ticket carefully.</p>
        <ul class="space-y-2 text-sm text-gray-600 mb-6 list-disc pl-5">
          <li>DIY taxi days can work on longer calls if you keep a strict return clock.</li>
          <li>Organised returns can reduce stress — still verify meeting points and all-aboard against your ship.</li>
          <li>Short calls: beach-only is often cleaner than beach + east-island nature.</li>
        </ul>
        <p class="text-sm text-gray-500">We do not invent taxi rates or transfer minutes.</p>
      </div>
      <div class="info-image rounded-3xl aspect-[4/3] shadow-xl overflow-hidden">
        <img src="{BEACH_IMG}" alt="{BEACH_ALT}" width="800" height="600" loading="lazy" decoding="async" />
      </div>
    </div>
    <div class="max-w-3xl mt-12">
      {related_links(RELATED_CORE)}
    </div>
  </div>
</section>
"""
    return page_shell(
        title="Freeport Beach Excursions | Taino Beach & Lucaya-Area Cruise Days",
        description=(
            "Freeport beach excursions for cruise passengers — Taino Beach and Lucaya-area "
            "options, DIY vs organised days, and short-call practicality on Grand Bahama."
        ),
        canonical_path="/freeport-beach-excursions",
        page_id="beach",
        hero_html=hero,
        main_html=main,
        og_image=BEACH_IMG,
    )


# ── Snorkel ───────────────────────────────────────────────────────────

def snorkel_page() -> str:
    hero = hero_band(
        eyebrow="Water days",
        title_html=f'Freeport<br/><span class="{ACCENT}">Snorkelling Excursions</span>',
        lead=(
            "Ocean snorkel days from Freeport — including Blue Hole–style boat excursions — "
            "with clear separation from inland Ben’s Cave at Lucayan National Park."
        ),
        image=SNORKEL_IMG,
        aria_label=SNORKEL_ALT,
        breadcrumb="Freeport snorkelling excursions",
    )
    main = f"""
<section class="py-14 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    {_snap_common(**{"Best for": "Active water days with weather risk"})}
    <div class="grid lg:grid-cols-2 gap-12 items-start mb-12">
      <div>
        <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Blue Hole snorkelling ≠ Ben’s Cave</h2>
        <p class="text-gray-600 leading-relaxed mb-4"><strong>Blue Hole–style snorkel excursions</strong> from Freeport are typically <strong>ocean / boat</strong> experiences toward eastern Grand Bahama waters. They can involve a road transfer, a boat segment, gear, and time in the water.</p>
        <p class="text-gray-600 leading-relaxed mb-4"><strong>Ben’s Cave</strong> is an <strong>inland</strong> blue hole inside <strong>Lucayan National Park</strong> — a different place and a different kind of visit (park / cave context, not the marketed ocean snorkel product).</p>
        <p class="text-gray-600 leading-relaxed mb-4">Do not plan as if visiting Ben’s Cave equals booking a Blue Hole snorkel boat day.</p>
      </div>
      <div class="info-image rounded-3xl aspect-[4/3] shadow-xl overflow-hidden">
        <img src="{SNORKEL_IMG}" alt="{SNORKEL_ALT}" width="800" height="600" loading="lazy" decoding="async" />
      </div>
    </div>
    <div class="max-w-3xl">
      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Cruise-day suitability</h2>
      <ul class="space-y-2 text-sm text-gray-600 mb-6 list-disc pl-5">
        <li><strong>Weather dependence</strong> — operators may cancel or alter for unsafe seas or storms.</li>
        <li><strong>Participation</strong> — expect swimming ability and physical entry/exit from water; age and health rules vary by product.</li>
        <li><strong>Time commitment</strong> — treat as a primary plan for a fuller window, not a short-call add-on.</li>
        <li><strong>No wildlife guarantees</strong> — turtles and reef life are variable.</li>
      </ul>
      {related_links(RELATED_CORE + [("/freeport-nature-garden-tours", "Lucayan park / caves")])}
    </div>
  </div>
</section>
"""
    return page_shell(
        title="Freeport Snorkelling Excursions | Blue Hole Ocean Days vs Ben’s Cave",
        description=(
            "Freeport snorkelling excursions for cruise passengers — Blue Hole–style ocean "
            "boat days, weather risk, and how they differ from Ben’s Cave at Lucayan National Park."
        ),
        canonical_path="/freeport-snorkelling-excursions",
        page_id="snorkel",
        hero_html=hero,
        main_html=main,
        og_image=SNORKEL_IMG,
    )


# ── Nature ────────────────────────────────────────────────────────────

def nature_page() -> str:
    hero = hero_band(
        eyebrow="Land &amp; nature",
        title_html=f'Freeport Nature<br/><span class="{ACCENT}">&amp; Garden Tours</span>',
        lead=(
            "Garden of the Groves, Lucayan National Park caves, and Gold Rock area — "
            "two different kinds of Grand Bahama port day."
        ),
        image=NATURE_IMG,
        aria_label=NATURE_ALT,
        breadcrumb="Nature &amp; garden tours",
    )
    main = f"""
<section class="py-14 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    {_snap_common(**{"Best for": "Land sightseeing without a boat"})}
    <div class="grid lg:grid-cols-2 gap-8 mb-12">
      <article class="rounded-3xl border border-ocean-100 p-7 bg-sand-50">
        <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Garden of the Groves + city / Port Lucaya</h2>
        <p class="text-sm text-gray-600 leading-relaxed mb-3">A botanical garden outing often combined with Freeport highlights and time near <strong>Port Lucaya Marketplace</strong>. This is a <strong>see Grand Bahama</strong> land day — usually simpler than east-island nature when pier meeting and coach patterns are clear.</p>
        <p class="text-sm text-gray-500">Good short or half-day candidate when you want context without a boat.</p>
      </article>
      <article class="rounded-3xl border border-ocean-100 p-7 bg-white shadow-sm">
        <div class="card-media h-40 rounded-2xl overflow-hidden mb-4"><img src="{CAVES_IMG}" alt="{CAVES_ALT}" width="600" height="240" loading="lazy" decoding="async" /></div>
        <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Lucayan National Park / caves / Gold Rock</h2>
        <p class="text-sm text-gray-600 leading-relaxed mb-3">Farther <strong>east</strong> on Grand Bahama. Expect park trails, cave areas, and Gold Rock Beach context as a <strong>dedicated</strong> plan — not a quick add-on after a full beach day and shopping marathon.</p>
        <p class="text-sm text-gray-500">Inland Ben’s Cave belongs in this park context — not as a substitute for ocean Blue Hole snorkelling.</p>
      </article>
    </div>
    {editorial_cta(
        "Explore Garden / city tour styles",
        "Garden of the Groves and Freeport city-style days are often the cleanest land introduction for cruise guests. Editorial guidance only — no live booking or prices on this site.",
        "/best-freeport-shore-excursions",
        "Explore this type of tour",
    )}
    <div class="max-w-3xl mx-auto px-4">
      {related_links(RELATED_CORE)}
    </div>
  </div>
</section>
"""
    return page_shell(
        title="Freeport Nature & Garden Tours | Groves, Lucayan Park & Gold Rock",
        description=(
            "Freeport nature and garden tours — Garden of the Groves versus Lucayan National Park "
            "caves and Gold Rock for cruise passengers on Grand Bahama."
        ),
        canonical_path="/freeport-nature-garden-tours",
        page_id="nature",
        hero_html=hero,
        main_html=main,
        og_image=NATURE_IMG,
    )


# ── Dolphin (secondary) ───────────────────────────────────────────────

def dolphin_page() -> str:
    hero = hero_band(
        eyebrow="Secondary option",
        title_html=f'Freeport<br/><span class="{ACCENT}">Dolphin Encounters</span>',
        lead=(
            "Sanctuary Bay–area dolphin programmes are not at the cruise pier. "
            "Treat them as a specialised add-on with their own transfer rules."
        ),
        image=None,
        aria_label="Dolphin encounter planning context for Freeport Grand Bahama",
        css_only=True,
        breadcrumb="Dolphin encounters",
    )
    main = f"""
<section class="py-14 bg-white">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    {_snap_common(**{"Best for": "Specialised marine programmes — not a pier walk"})}
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Not at the cruise pier</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Dolphin encounter facilities associated with Freeport / Sanctuary Bay are reached by transfer — typically taxi or operator transport. Do not assume you can walk from Lucayan Harbour.</p>
    <p class="text-gray-600 leading-relaxed mb-4">We do not publish unverified taxi fares, guarantee animal interactions, or treat dolphin programmes as a primary Freeport decision spine. Confirm ages, waivers, pregnancy rules, and return timing with the operator.</p>
    <p class="text-sm text-gray-500 mb-8">This page is secondary. Start with <a href="/best-freeport-shore-excursions" class="text-ocean-600 font-semibold">excursion comparison</a> or <a href="/one-day-in-freeport-from-a-cruise-ship" class="text-ocean-600 font-semibold">one-day scenarios</a>.</p>
    {related_links(RELATED_CORE)}
  </div>
</section>
"""
    return page_shell(
        title="Freeport Dolphin Encounters | Sanctuary Bay Context for Cruise Guests",
        description=(
            "Freeport dolphin encounter context for cruise passengers — Sanctuary Bay is not "
            "the cruise pier; confirm transfers and programme rules with operators."
        ),
        canonical_path="/freeport-dolphin-encounters",
        page_id="dolphin",
        hero_html=hero,
        main_html=main,
        og_image=None,
        include_trust=False,
    )


# ── FAQ ───────────────────────────────────────────────────────────────

FAQ_ITEMS = [
    (
        "Dock or tender?",
        "Standard Freeport calls commonly dock at Lucayan Harbour. Confirm your sailing. "
        "Celebration Key is a separate pier context for some Carnival itineraries.",
    ),
    (
        "Is Port Lucaya walkable from the ship?",
        "Generally no — plan on a taxi or organised transfer from Lucayan Harbour to "
        "Port Lucaya marketplace and marina areas.",
    ),
    (
        "Currency tip?",
        "Bahamian dollars are official; US dollars are widely used in tourist areas. "
        "Carry small notes for tips and taxis. Confirm change policies as you go.",
    ),
    (
        "Independent vs ship tour?",
        "Ship tours may offer different delay protections. Independent operators have "
        "their own policies. We do not claim either returns you on time — read the fine print.",
    ),
]


def faq_page() -> str:
    hero = hero_band(
        eyebrow="Planning answers",
        title_html=f'Freeport<br/><span class="{ACCENT}">Excursions FAQ</span>',
        lead="Short answers for cruise passengers planning Freeport on Grand Bahama.",
        image=None,
        aria_label="Freeport cruise excursion FAQ",
        css_only=True,
        breadcrumb="FAQ",
    )
    main = f"""
<section class="py-10 bg-white"><div class="max-w-7xl mx-auto px-4">{_snap_common()}</div></section>
{faq_section(FAQ_ITEMS, heading="Frequently asked questions")}
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{related_links(RELATED_CORE)}</div></section>
"""
    return page_shell(
        title="Freeport Shore Excursions FAQ | Cruise Passenger Planning",
        description=(
            "FAQ for Freeport Bahamas shore excursions — pier vs Port Lucaya, dock calls, "
            "currency, and independent vs ship-tour planning notes."
        ),
        canonical_path="/freeport-faq",
        page_id="faq",
        hero_html=hero,
        main_html=main,
        og_image=None,
        faq_entities=FAQ_ITEMS,
        include_trust=False,
    )


# ── Trust pages ───────────────────────────────────────────────────────

def _trust_main(body: str) -> str:
    return f"""<section class="py-16 bg-white">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 prose prose-ocean">
    {body}
  </div>
</section>
"""


def contact_page() -> str:
    hero = hero_band(
        eyebrow="Contact",
        title_html="Contact",
        lead="Editorial questions about this Freeport cruise planning guide.",
        image=None,
        aria_label="Contact Freeport Shore Excursion",
        css_only=True,
        breadcrumb="Contact",
    )
    body = f"""
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Email</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Write to <a class="text-ocean-600 font-semibold" href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <p class="text-gray-600 leading-relaxed mb-4">Please include your ship date and the page you are asking about. Do not send payment card details by email.</p>
    <p class="text-sm text-gray-500">This site is an editorial planning guide. Online booking is not live in this phase.</p>
    """
    return page_shell(
        title="Contact | Freeport Shore Excursion",
        description="Contact Freeport Shore Excursion for editorial questions about this Freeport cruise planning guide.",
        canonical_path="/contact",
        page_id="contact",
        hero_html=hero,
        main_html=_trust_main(body),
        og_image=None,
        include_trust=False,
    )


def about_page() -> str:
    hero = hero_band(
        eyebrow="About",
        title_html="About",
        lead="Independent Freeport / Grand Bahama cruise planning — not a cruise line.",
        image=None,
        aria_label="About Freeport Shore Excursion",
        css_only=True,
        breadcrumb="About",
    )
    body = f"""
    <p class="text-gray-600 leading-relaxed mb-4"><strong>Freeport Shore Excursion</strong> is an independent editorial guide for cruise passengers calling at Freeport on Grand Bahama. We explain pier logistics, day shapes, and excursion styles in plain language.</p>
    <p class="text-gray-600 leading-relaxed mb-4">We are not affiliated with any cruise line, harbour authority, or resort brand. Brand names appear for orientation only.</p>
    <p class="text-gray-600 leading-relaxed mb-4">See our <a href="/methodology" class="text-ocean-600 font-semibold">methodology</a> and contact <a href="mailto:{EMAIL}" class="text-ocean-600 font-semibold">{EMAIL}</a>.</p>
    """
    return page_shell(
        title="About | Freeport Shore Excursion",
        description="About Freeport Shore Excursion — independent cruise-passenger planning for Freeport on Grand Bahama.",
        canonical_path="/about",
        page_id="about",
        hero_html=hero,
        main_html=_trust_main(body),
        og_image=None,
        include_trust=False,
    )


def privacy_page() -> str:
    hero = hero_band(
        eyebrow="Legal",
        title_html="Privacy",
        lead="How this Freeport planning site handles contact email.",
        image=None,
        aria_label="Privacy policy",
        css_only=True,
        breadcrumb="Privacy",
    )
    body = f"""
    <p class="text-gray-600 leading-relaxed mb-4">If you email <a href="mailto:{EMAIL}" class="text-ocean-600 font-semibold">{EMAIL}</a>, we use your address to reply to your enquiry. We do not sell email lists.</p>
    <p class="text-gray-600 leading-relaxed mb-4">Hosting and CDN providers may process standard technical logs (IP, user agent, request path) to operate the site securely.</p>
    <p class="text-gray-600 leading-relaxed mb-4">This phase does not process card payments on-site. Do not email payment card details.</p>
    """
    return page_shell(
        title="Privacy | Freeport Shore Excursion",
        description="Privacy information for Freeport Shore Excursion.",
        canonical_path="/privacy",
        page_id="privacy",
        hero_html=hero,
        main_html=_trust_main(body),
        og_image=None,
        include_trust=False,
    )


def terms_page() -> str:
    hero = hero_band(
        eyebrow="Legal",
        title_html="Terms",
        lead="Editorial information only — not a booking contract.",
        image=None,
        aria_label="Terms of use",
        css_only=True,
        breadcrumb="Terms",
    )
    body = """
    <p class="text-gray-600 leading-relaxed mb-4">Content on this site is editorial planning information for cruise passengers. It is not a contract for travel services and not a substitute for your cruise line or operator terms.</p>
    <p class="text-gray-600 leading-relaxed mb-4">Confirm ship schedules, all-aboard times, meeting points, ages, and inclusions with operators before you travel. Conditions change.</p>
    <p class="text-gray-600 leading-relaxed mb-4">Place and brand names are used for geographic orientation only.</p>
    """
    return page_shell(
        title="Terms | Freeport Shore Excursion",
        description="Terms for Freeport Shore Excursion editorial planning content.",
        canonical_path="/terms",
        page_id="terms",
        hero_html=hero,
        main_html=_trust_main(body),
        og_image=None,
        include_trust=False,
    )


def methodology_page() -> str:
    hero = hero_band(
        eyebrow="Trust",
        title_html="Methodology",
        lead="How we write Freeport cruise guides.",
        image=None,
        aria_label="Methodology",
        css_only=True,
        breadcrumb="Methodology",
    )
    body = """
    <ul class="space-y-3 text-gray-600 text-sm leading-relaxed list-disc pl-5">
      <li>We write for cruise-port decisions: usable hours, pier vs tourist areas, and one primary plan.</li>
      <li>We preserve Search Console equity URLs when they already attract impressions.</li>
      <li>We do not invent hourly itineraries, taxi fares, ratings, popularity ranks, or return guarantees.</li>
      <li>We quarantine images that show the wrong place or context (for example, inland cave photos used as ocean snorkel).</li>
      <li>We avoid product/offer, review-aggregate, and local-business schema claims that imply a live shopfront we do not operate.</li>
      <li>Commercial booking, if added later, will be verified in a separate phase — not implied here.</li>
    </ul>
    """
    return page_shell(
        title="Methodology | Freeport Shore Excursion",
        description="How Freeport Shore Excursion writes cruise-passenger guides for Grand Bahama.",
        canonical_path="/methodology",
        page_id="methodology",
        hero_html=hero,
        main_html=_trust_main(body),
        og_image=None,
        include_trust=False,
    )


def not_found_page() -> str:
    hero = hero_band(
        eyebrow="404",
        title_html="Page not found",
        lead="That URL is not part of this Freeport guide.",
        image=None,
        aria_label="Page not found",
        css_only=True,
    )
    main = """
<section class="py-16 bg-white">
  <div class="max-w-3xl mx-auto px-4 text-center">
    <p class="text-gray-600 mb-6">Try the homepage, excursion comparison, or one-day scenarios.</p>
    <div class="flex flex-col sm:flex-row gap-3 justify-center">
      <a href="/" class="btn-ocean inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm">Home</a>
      <a href="/best-freeport-shore-excursions" class="btn-outline-ocean inline-flex items-center justify-center font-semibold px-7 py-3 rounded-full text-sm">Compare options</a>
      <a href="/one-day-in-freeport-from-a-cruise-ship" class="btn-outline-ocean inline-flex items-center justify-center font-semibold px-7 py-3 rounded-full text-sm">One day</a>
    </div>
  </div>
</section>
"""
    return page_shell(
        title="Page not found | Freeport Shore Excursion",
        description="The requested Freeport Shore Excursion page was not found.",
        canonical_path="/404.html",
        page_id="404",
        hero_html=hero,
        main_html=main,
        og_image=None,
        robots="noindex, follow",
        include_trust=False,
    )


def all_pages() -> dict[str, str]:
    return {
        "/": home_page(),
        "/best-freeport-shore-excursions": best_page(),
        "/one-day-in-freeport-from-a-cruise-ship": one_day_page(),
        "/freeport-cruise-port-guide": port_page(),
        "/freeport-beach-excursions": beach_page(),
        "/freeport-snorkelling-excursions": snorkel_page(),
        "/freeport-nature-garden-tours": nature_page(),
        "/freeport-dolphin-encounters": dolphin_page(),
        "/freeport-faq": faq_page(),
        "/contact": contact_page(),
        "/about": about_page(),
        "/privacy": privacy_page(),
        "/terms": terms_page(),
        "/methodology": methodology_page(),
        "/404.html": not_found_page(),
    }
