"""Page content for Freeport Shore Excursion site."""
from freeport_config import (
    BEACH_ALT,
    BEACH_IMG,
    BLUE_HOLE_ALT,
    BLUE_HOLE_IMG,
    BOOKING_URL,
    CAVE_ALT,
    CAVE_IMG,
    DOLPHIN_ALT,
    DOLPHIN_IMG,
    INTRO_ALT,
    INTRO_IMG,
    NATURE_ALT,
    NATURE_IMG,
    ONE_DAY_ALT,
    ONE_DAY_IMG,
    PORT_ALT,
    PORT_IMG,
    SNORKEL_ALT,
    SNORKEL_IMG,
)
from freeport_helpers import (
    book_cta,
    card_grid,
    comparison_rows,
    comparison_section,
    content_category_page,
    internal_links,
    snapshot_default,
)


def home_faq_data() -> list[tuple[str, str]]:
    return [
        ("Is Freeport Bahamas a dock port for cruise ships?", "Yes — most ships dock at the Freeport cruise terminal and passengers walk off directly without tender boats."),
        ("How long do cruise ships stay in Freeport?", "Most Freeport port calls are 6 to 10 hours — enough for a half-day tour or relaxed beach day."),
        ("What is the best Freeport excursion for first-time visitors?", "Blue Hole snorkel and beach, Garden of the Groves city tour, or Taino Beach resort day pass."),
        ("How far is Lucayan National Park from the Freeport cruise port?", "Approximately 25–30 minutes by road east of the Freeport harbour area."),
        ("What currency is used in the Bahamas?", "Bahamian dollars (BSD) are official; US dollars are widely accepted at excursions and shops."),
        ("Are Freeport shore excursions return-to-ship friendly?", "Reputable operators plan returns with a 60–90 minute buffer before published all-aboard times."),
        ("Can you see dolphins in Freeport on a port day?", "Yes — Sanctuary Bay offers close encounters and swim-with-dolphin programmes timed for cruise schedules."),
    ]


def home_faq_section() -> str:
    return """<section class="py-16 bg-white"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-3xl font-display font-bold text-gray-900 text-center mb-8">Freeport Shore Excursions FAQ</h2>
  <div class="space-y-4">
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is Freeport a dock or tender port?</summary>
      <p class="mt-4 text-sm text-gray-500">Freeport is a <strong>dock port</strong> for most cruise lines — ships tie up at the Freeport cruise terminal and you walk off directly.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What are the most popular Freeport shore excursions?</summary>
      <p class="mt-4 text-sm text-gray-500">Blue Hole snorkel and beach, Taino Beach resort day, Garden of the Groves, Lucayan National Park caves and dolphin encounters at Sanctuary Bay.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do cruise ships stay in Freeport?</summary>
      <p class="mt-4 text-sm text-gray-500">Most port calls run <strong>6 to 10 hours</strong>. Half-day tours (4–5 hours) fit comfortably; dolphin encounters are short enough to pair with shopping.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What currency is used in the Bahamas?</summary>
      <p class="mt-4 text-sm text-gray-500">Bahamian dollars (BSD) are official. <strong>US dollars</strong> are widely accepted near the cruise port — carry small bills for tips and souvenirs.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is Port Lucaya worth visiting on a port day?</summary>
      <p class="mt-4 text-sm text-gray-500">Yes — Port Lucaya Marketplace offers Bahamian crafts, restaurants and harbour views. Many city and garden tours include a stop there.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Are Freeport excursions safe for cruise passengers?</summary>
      <p class="mt-4 text-sm text-gray-500">Organised shore excursions with licensed operators are the standard approach. See our <a href="freeport-cruise-port-guide.html" class="text-ocean-600">port guide</a> and <a href="freeport-faq.html" class="text-ocean-600">FAQ</a> for planning tips.</p></details>
  </div>
  <p class="text-center mt-8"><a href="freeport-faq.html" class="text-ocean-600 font-semibold text-sm">Full FAQ →</a></p>
</div></section>"""


def content_home() -> str:
    cards = card_grid([
        (BEACH_IMG, BEACH_ALT, "Beach Excursions", "Taino Beach resort day passes and calm Caribbean swim days with cruise-friendly returns.", "freeport-beach-excursions.html", "Beach Guide"),
        (SNORKEL_IMG, SNORKEL_ALT, "Snorkelling", "Blue Hole drift snorkel, reef exploration and turtle sightings in clear Grand Bahama water.", "freeport-snorkelling-excursions.html", "Snorkel Tours"),
        (NATURE_IMG, NATURE_ALT, "Nature &amp; Gardens", "Garden of the Groves, Lucayan National Park caves and easy island sightseeing.", "freeport-nature-garden-tours.html", "Nature Tours"),
        (DOLPHIN_IMG, DOLPHIN_ALT, "Dolphin Encounters", "Close encounters and swim programmes at Sanctuary Bay — all ages welcome.", "freeport-dolphin-encounters.html", "Dolphin Tours"),
    ])
    snap = snapshot_default()
    return f"""<section class="pt-8 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-10">
    <div class="section-label mx-auto">Best Excursions</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-4">Best Freeport Shore Excursions</h2>
    <p class="text-gray-600 text-sm max-w-2xl mx-auto">Ranked for cruise schedules — beaches, snorkelling, nature tours and dolphin encounters from Freeport, Grand Bahama.</p>
  </div>
  {cards}
  <p class="text-center mt-8"><a href="best-freeport-shore-excursions.html" class="text-ocean-600 font-semibold text-sm">See full comparison →</a></p>
</div></section>
<section class="pt-4 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <div class="inline-flex items-center gap-2 text-ocean-600 text-xs font-semibold tracking-widest uppercase mb-3"><div class="w-8 h-px bg-ocean-400"></div>Freeport · Grand Bahama</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-5">Why Cruise Passengers<br/><span class="text-ocean-600">Choose Freeport</span></h2>
    <p class="text-gray-600 leading-relaxed mb-5">Freeport delivers <strong>turquoise beaches</strong>, <strong>Blue Hole snorkelling</strong>, the tropical <strong>Garden of the Groves</strong>, <strong>Lucayan cave adventures</strong> and <strong>dolphin encounters</strong> on a typical <strong>6–10 hour</strong> dock port call. US dollars are widely accepted near the cruise terminal.</p>
    <a href="freeport-cruise-port-guide.html" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Port Guide</a>
  </div>
  <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
    <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-16 bg-amber-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-12"><h2 class="text-3xl font-display font-bold text-gray-900">Top Things To Do In Freeport</h2>
  <p class="text-gray-600 text-sm mt-3 max-w-xl mx-auto">Easy port days and signature Grand Bahama experiences cruise passengers book most.</p></div>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Blue Hole Snorkel</h3><p class="text-gray-600">Drift snorkelling, turtle sightings, beach time and Bahamian lunch on Grand Bahama's signature water adventure.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Taino Beach</h3><p class="text-gray-600">Resort pool, beach chairs and calm Caribbean swim — a relaxed port day without a packed itinerary.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Garden of the Groves</h3><p class="text-gray-600">Tropical botanical gardens, wildlife and a guided city tour with Port Lucaya shopping time.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Lucayan Caves</h3><p class="text-gray-600">Arawak Indian caves and national park trails — history and nature on an easy half-day tour.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Dolphin Encounters</h3><p class="text-gray-600">Kiss, hug and swim with dolphins at Sanctuary Bay — short enough to pair with other port plans.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Port Lucaya</h3><p class="text-gray-600">Marketplace shopping, harbour dining and Bahamian crafts near the cruise port area.</p></div>
  </div>
</div></section>
<section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BLUE_HOLE_IMG}" alt="{BLUE_HOLE_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Blue Hole Snorkel &amp; Beach</h2>
    <p class="text-gray-600 leading-relaxed mb-4">The <strong>Freeport Blue Hole Snorkel and Beach with Lunch</strong> tour combines drift snorkelling in crystal-clear water, turtle sightseeing and beachside relaxation — the water adventure cruise passengers rate highest from Freeport.</p>
    <p class="text-gray-600 leading-relaxed mb-5">Small-group departures and included lunch make it an easy full port-day pick. See our <a href="freeport-snorkelling-excursions.html" class="text-ocean-600 font-medium">snorkelling guide</a> for what to expect.</p>
    <a href="freeport-snorkelling-excursions.html" class="text-ocean-600 font-semibold text-sm">Snorkelling excursions →</a>
  </div>
</div></div></section>
<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Garden of the Groves &amp; City Tour</h2>
    <p class="text-gray-600 leading-relaxed mb-4"><strong>Garden of the Groves</strong> is Grand Bahama's famous botanical garden — palm-lined paths, tropical flowers, birds and quiet trails. The half-day city tour adds Freeport highlights and <strong>Port Lucaya Marketplace</strong> shopping.</p>
    <p class="text-gray-600 leading-relaxed mb-5">Easy activity level suits mixed-age groups and passengers who prefer land-based sightseeing. Read our <a href="freeport-nature-garden-tours.html" class="text-ocean-600 font-medium">nature &amp; garden guide</a>.</p>
    <a href="freeport-nature-garden-tours.html" class="text-ocean-600 font-semibold text-sm">Nature tours →</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{NATURE_IMG}" alt="{NATURE_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BEACH_IMG}" alt="{BEACH_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Taino Beach Resort Day</h2>
    <p class="text-gray-600 leading-relaxed mb-4"><strong>Taino Beach</strong> offers a resort day pass with pool, beach access and calm turquoise swim — ideal when you want a low-effort Caribbean port day without a long coach tour.</p>
    <p class="text-gray-600 leading-relaxed mb-5">Five-hour excursions include transport and return-to-ship timing. Compare options in our <a href="freeport-beach-excursions.html" class="text-ocean-600 font-medium">beach excursions guide</a>.</p>
    <a href="freeport-beach-excursions.html" class="text-ocean-600 font-semibold text-sm">Beach excursions →</a>
  </div>
</div></div></section>
{comparison_section(comparison_rows())}
{home_faq_section()}
<section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-white mb-4">Plan Your Freeport Port Day</h2>
  <p class="text-white/85 text-sm mb-6">Compare excursions, read the Freeport port guide and build your Grand Bahama itinerary before you dock.</p>
  <div class="flex flex-col sm:flex-row gap-4 justify-center">
    <a href="best-freeport-shore-excursions.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Compare Excursions</a>
    <a href="{BOOKING_URL}" rel="noopener noreferrer" target="_blank" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">View &amp; Book Tours</a>
  </div>
</div></section>"""


def content_best_excursions() -> str:
    cards = card_grid([
        (SNORKEL_IMG, SNORKEL_ALT, "Blue Hole Snorkel", "Drift snorkel, turtles, beach and lunch on Grand Bahama's signature water tour.", "freeport-snorkelling-excursions.html", "Snorkel Guide"),
        (BEACH_IMG, BEACH_ALT, "Taino Beach", "Resort day pass with pool, beach and calm Caribbean swim.", "freeport-beach-excursions.html", "Beach Guide"),
        (NATURE_IMG, NATURE_ALT, "Garden of the Groves", "Botanical gardens, city tour and Port Lucaya shopping.", "freeport-nature-garden-tours.html", "Nature Guide"),
        (DOLPHIN_IMG, DOLPHIN_ALT, "Dolphin Encounters", "Close encounter and swim programmes at Sanctuary Bay.", "freeport-dolphin-encounters.html", "Dolphin Guide"),
    ])
    snap = snapshot_default(best_for="Comparing all excursion types", popular="See comparison table below")
    rankings = """<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Excursions by Traveler Type</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Families</h3><p class="text-gray-600 mb-3">Taino Beach, Garden of the Groves and dolphin close encounters suit mixed ages.</p><a href="freeport-beach-excursions.html" class="text-ocean-600 font-semibold">Beach Day →</a></div>
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Active Swimmers</h3><p class="text-gray-600 mb-3">Blue Hole drift snorkel with lunch — turtles and clear Caribbean water.</p><a href="freeport-snorkelling-excursions.html" class="text-ocean-600 font-semibold">Snorkelling →</a></div>
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">First Timers</h3><p class="text-gray-600 mb-3">Garden of the Groves city tour showcases Freeport highlights in half a day.</p><a href="freeport-nature-garden-tours.html" class="text-ocean-600 font-semibold">City Tour →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Nature Lovers</h3><p class="text-gray-600 mb-3">Lucayan National Park caves and national park trails.</p><a href="freeport-nature-garden-tours.html" class="text-ocean-600 font-semibold">Lucayan Park →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Marine Encounters</h3><p class="text-gray-600 mb-3">Dolphin kiss-and-hug encounters or full swim programmes.</p><a href="freeport-dolphin-encounters.html" class="text-ocean-600 font-semibold">Dolphins →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Relaxed Days</h3><p class="text-gray-600 mb-3">Taino Beach resort pass — pool, sand and no rushed schedule.</p><a href="freeport-beach-excursions.html" class="text-ocean-600 font-semibold">Taino Beach →</a></div>
  </div>
</div></section>"""
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best Freeport Shore Excursions</h2>
  <p class="text-gray-600 leading-relaxed text-sm">Operators meet at the <strong>Freeport cruise terminal</strong> and plan returns with buffer before all aboard. Compare beaches, snorkelling, nature tours and dolphin encounters for your ship schedule.</p>
  <div class="mt-6">{book_cta()}</div>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
{comparison_section(comparison_rows())}
{rankings}
<section class="py-16 bg-amber-50"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Excursion Guides</h2>
  {cards}
  <div class="mt-12 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>"""


def content_beach() -> str:
    return content_category_page(
        "Freeport beach excursions centre on <strong>Taino Beach</strong> — a resort day pass with pool, beach chairs and calm turquoise Caribbean water. Unlike packed coach tours, a beach day lets you swim, relax and still return to the ship with a comfortable buffer.",
        [
            "Taino Beach Resort Day Pass runs approximately five hours with transport included.",
            "Easy activity level suits seniors, families and anyone wanting a low-effort port day.",
            "Small-group excursion size keeps pickup and drop-off efficient.",
            "Pair with a short Port Lucaya stop only if your ship stays late.",
        ],
        [
            "Calm water and resort facilities — no long drives across the island.",
            "Return-to-ship timing built into organised beach day passes.",
            "Pool and ocean access in one location — ideal for mixed preferences.",
            "More affordable than multi-stop adventure tours for a simple port day.",
            "Small-group departures from the Freeport cruise terminal.",
            "USD widely accepted — no currency hassle near the port.",
        ],
        [
            (BEACH_IMG, BEACH_ALT, "Taino Beach Resort", "Resort pool, beach access and Caribbean swim on a five-hour day pass from the cruise port."),
            (INTRO_IMG, INTRO_ALT, "Calm Caribbean Water", "Grand Bahama's leeward coast delivers gentle waves and clear turquoise shallows."),
            (PORT_IMG, PORT_ALT, "Easy Port Timing", "Beach days fit 6–10 hour port calls with afternoon return buffer."),
        ],
        dict(
            best_for="Relaxed beach and pool days",
            activity_level="Easy — swimming and lounging",
            popular="Taino Beach resort day pass",
        ),
        BEACH_IMG,
        BEACH_ALT,
        badge="Best Beach Day",
        show_small_group=True,
        highlights_title="Freeport Beach Tour Highlights",
        highlights_subtitle="What to expect on Taino Beach and Grand Bahama beach shore excursions.",
        why_heading="Why Cruise Passengers Choose Freeport Beach Excursions",
    )


def content_snorkelling() -> str:
    return content_category_page(
        "Freeport snorkelling excursions highlight the <strong>Blue Hole Snorkel and Beach with Lunch</strong> — drift snorkelling in crystal-clear water, turtle sightings, beach time and a Bahamian lunch. Small-group tours run about five hours with moderate activity level.",
        [
            "Drift snorkelling at the Blue Hole — minimal fin effort in clear current.",
            "Turtle and reef fish sightings common in Grand Bahama waters.",
            "Lunch included on the signature Blue Hole excursion.",
            "Snorkel gear provided — bring reef-safe sunscreen and a rash guard.",
        ],
        [
            "Blue Hole is Freeport's highest-rated water adventure for cruise passengers.",
            "Small-group size keeps the snorkel experience personal.",
            "Lunch included — one less thing to plan on a port day.",
            "Combines underwater exploration with beach relaxation.",
            "Operators coordinate return times with 60–90 minute ship buffer.",
            "Moderate activity suits confident swimmers; flotation aids often available.",
        ],
        [
            (BLUE_HOLE_IMG, BLUE_HOLE_ALT, "Blue Hole Snorkel", "Drift snorkel in turquoise lagoon water with turtle sightseeing."),
            (SNORKEL_IMG, SNORKEL_ALT, "Clear Caribbean Reef", "Visibility over reef and sandy bottom in Grand Bahama's calm waters."),
            (BEACH_IMG, BEACH_ALT, "Beach &amp; Lunch Stop", "Beachside relaxation and Bahamian lunch included on full-day snorkel tours."),
        ],
        dict(
            best_for="Snorkellers and active water lovers",
            activity_level="Moderate — drift snorkel &amp; swim",
            popular="Blue Hole snorkel with lunch",
        ),
        SNORKEL_IMG,
        SNORKEL_ALT,
        badge="Best Snorkel Tour",
        show_small_group=True,
        highlights_title="Freeport Snorkelling Highlights",
        highlights_subtitle="Signature underwater experiences on Grand Bahama shore excursions.",
        why_heading="Why Cruise Passengers Choose Freeport Snorkelling",
    )


def content_nature() -> str:
    return content_category_page(
        "Freeport nature and garden tours cover <strong>Garden of the Groves</strong> — tropical botanical gardens with palm paths and wildlife — plus the <strong>Lucayan National Park &amp; Cave Tour</strong> exploring Arawak Indian caves and one of the world's longest underwater cave systems. Half-day tours run about four hours at easy activity level.",
        [
            "Garden of the Groves and City Tour includes Port Lucaya Marketplace shopping.",
            "Lucayan National Park tour explores limestone caves and park trails.",
            "Easy walking — suitable for passengers avoiding strenuous water activities.",
            "Guided commentary covers Grand Bahama history and ecology.",
        ],
        [
            "Garden of the Groves is Grand Bahama's premier botanical attraction.",
            "City tour adds Freeport highlights without a full-island drive.",
            "Lucayan caves offer a unique underground experience rare in the Caribbean.",
            "Port Lucaya shopping time built into garden and city tours.",
            "Easy activity level fits seniors and mixed-mobility groups.",
            "Half-day duration leaves room for harbour shopping on longer port calls.",
        ],
        [
            (NATURE_IMG, NATURE_ALT, "Garden of the Groves", "Tropical palms, flowers and quiet garden paths on a guided tour."),
            (CAVE_IMG, CAVE_ALT, "Lucayan Caves", "Arawak Indian cave formations and national park trails east of Freeport."),
            (ONE_DAY_IMG, ONE_DAY_ALT, "Port Lucaya Stop", "Marketplace crafts, dining and harbour views on city tour itineraries."),
        ],
        dict(
            best_for="Nature, gardens and easy sightseeing",
            activity_level="Easy — garden walks &amp; cave touring",
            popular="Garden of the Groves, Lucayan caves",
        ),
        NATURE_IMG,
        NATURE_ALT,
        badge="Best Nature Tour",
        show_small_group=True,
        highlights_title="Freeport Nature Tour Highlights",
        highlights_subtitle="Gardens, caves and island sightseeing from the cruise port.",
        why_heading="Why Cruise Passengers Choose Freeport Nature Tours",
    )


def content_dolphin() -> str:
    return content_category_page(
        "Freeport dolphin encounters at <strong>Sanctuary Bay</strong> include the <strong>Dolphin Close Encounter</strong> — kiss, hug and interact from a platform (all ages welcome) — and <strong>Swim with the Dolphins</strong> for guests who want in-water time. Programmes run about one hour, leaving room to pair with beach or shopping plans.",
        [
            "Dolphin Close Encounter suits families and guests who prefer dry-platform interaction.",
            "Swim with the Dolphins is a premium in-water programme — check age and health requirements.",
            "Short duration (approx. 1 hour) fits easily into most port schedules.",
            "Transport from the Freeport cruise terminal typically included.",
        ],
        [
            "Sanctuary Bay is Grand Bahama's established dolphin facility.",
            "Close Encounter welcomes all ages — popular with multi-generational groups.",
            "One-hour format leaves afternoon free for Port Lucaya or beach time.",
            "Professional trainers guide every interaction for safety.",
            "Return-to-ship coordination handled by excursion operators.",
            "Pair with Taino Beach or garden tour on a 8+ hour port call.",
        ],
        [
            (DOLPHIN_IMG, DOLPHIN_ALT, "Close Encounter", "Platform interaction — kiss, hug and meet dolphins at Sanctuary Bay."),
            (SNORKEL_IMG, SNORKEL_ALT, "Swim Programme", "In-water dolphin swim for confident swimmers seeking a premium encounter."),
            (BEACH_IMG, BEACH_ALT, "Easy Port Timing", "One-hour programmes pair well with beach or shopping on the same day."),
        ],
        dict(
            best_for="Marine life enthusiasts and families",
            activity_level="Moderate — platform or swim interaction",
            popular="Dolphin close encounter, swim programme",
            family="Excellent — age rules apply for swim programme",
        ),
        DOLPHIN_IMG,
        DOLPHIN_ALT,
        badge="Best Dolphin Encounter",
        highlights_title="Freeport Dolphin Tour Highlights",
        highlights_subtitle="Marine encounters at Sanctuary Bay for cruise passengers.",
        why_heading="Why Cruise Passengers Choose Freeport Dolphin Tours",
    )


def content_port_guide() -> str:
    snap = snapshot_default(
        activity_level="Low at terminal; varies on tours",
        popular="Dock port, taxis, organised pickups",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <p class="text-gray-600 leading-relaxed text-sm">Ships dock at the <strong>Freeport cruise terminal</strong> on Grand Bahama. Calls usually run <strong>6–10 hours</strong> — enough for a half-day snorkel tour, garden visit or relaxed beach day.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-gray-50"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Where Ships Arrive</h2>
  <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
    <img src="{PORT_IMG}" alt="{PORT_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
  </div>
  <div class="grid lg:grid-cols-2 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Freeport Cruise Terminal</h3><p class="text-gray-600">Most cruise lines dock at the Freeport harbour terminal. Passengers walk off directly — no tender boats on standard dock calls.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Port Lucaya Marketplace</h3><p class="text-gray-600">Short taxi ride from the terminal — Bahamian crafts, restaurants and marina views. Many garden and city tours include a stop here.</p></div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Distances From Port</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Taino Beach</strong><p class="mt-2 text-gray-600">Approx. 15–20 minutes by road from the cruise terminal.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Garden of the Groves</strong><p class="mt-2 text-gray-600">Approx. 15 minutes — close to central Freeport.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Lucayan National Park</strong><p class="mt-2 text-gray-600">Approx. 25–30 minutes east of the harbour.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Sanctuary Bay</strong><p class="mt-2 text-gray-600">Approx. 20 minutes — dolphin encounter facility.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Blue Hole</strong><p class="mt-2 text-gray-600">East Grand Bahama — allow 30–40 minutes transfer on snorkel tours.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Port Lucaya</strong><p class="mt-2 text-gray-600">Approx. 10–15 minutes by taxi from the cruise terminal.</p></div>
  </div>
</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4">
  <div class="grid sm:grid-cols-3 gap-6 text-sm">
    <div class="bg-white rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">Bahamian dollars (BSD), pegged 1:1 with USD. <strong>US dollars</strong> widely accepted at excursions, taxis and Port Lucaya.</p></div>
    <div class="bg-white rounded-2xl p-6"><strong class="text-gray-900">Language</strong><p class="mt-2 text-gray-600">English — straightforward for North American and UK cruise guests.</p></div>
    <div class="bg-white rounded-2xl p-6"><strong class="text-gray-900">Getting Around</strong><p class="mt-2 text-gray-600">Licensed taxis at the terminal; organised excursions include port pickup and timed return.</p></div>
  </div>
  <p class="text-center mt-8"><a href="one-day-in-freeport-from-a-cruise-ship.html" class="text-ocean-600 font-semibold text-sm">One-day itinerary →</a></p>
  <div class="mt-10 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>"""


def content_one_day() -> str:
    snap = snapshot_default(best_for="Garden tour + beach or snorkel combo")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <p class="text-gray-600 text-sm">Sample timeline for a <strong>6–10 hour</strong> Freeport call. Adjust for your ship's actual gangway and all-aboard times.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Classic Freeport Port Day</h2>
  <ol class="space-y-4 text-sm">
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">08:00</span><div><strong>Depart pier</strong><p class="text-gray-600 mt-1">Meet your Garden of the Groves and city tour at the cruise terminal — early start maximises port time.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">08:30</span><div><strong>Garden of the Groves</strong><p class="text-gray-600 mt-1">Tropical botanical gardens, palm paths and wildlife on a guided walk.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">10:30</span><div><strong>Freeport city highlights</strong><p class="text-gray-600 mt-1">Coach tour through Freeport with commentary on Grand Bahama history.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">11:30</span><div><strong>Port Lucaya Marketplace</strong><p class="text-gray-600 mt-1">Shopping, crafts and harbour lunch options before afternoon plans.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">13:00</span><div><strong>Taino Beach or dolphin encounter</strong><p class="text-gray-600 mt-1">If your ship stays 8+ hours — afternoon beach pass or one-hour Sanctuary Bay programme.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">16:00</span><div><strong>Return to pier</strong><p class="text-gray-600 mt-1">Allow 60–90 minute buffer before published all-aboard.</p></div></li>
  </ol>
  <section class="mt-10 py-8 bg-white rounded-3xl p-6 border border-pr-100">
    <h3 class="font-display font-bold text-lg mb-3">Alternative: Adventure Port Day</h3>
    <p class="text-gray-600 text-sm mb-3">For active passengers, swap the garden tour for the <strong>Blue Hole Snorkel and Beach with Lunch</strong> — a full five-hour water adventure with drift snorkel, turtles and beach time.</p>
    <a href="freeport-snorkelling-excursions.html" class="text-ocean-600 font-semibold text-sm">Blue Hole snorkel guide →</a>
  </section>
  <div class="mt-10">{internal_links()}</div>
</div></section>"""


def content_faq() -> str:
    snap = snapshot_default(best_for="Quick planning answers", popular="See FAQ topics below")
    return f"""<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-8 bg-white"><div class="max-w-3xl mx-auto px-4 space-y-4">
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do cruise ships stay in Freeport?</summary>
    <p class="mt-4 text-sm text-gray-500">Most calls are <strong>6 to 10 hours</strong>. Half-day tours (4–5 hours) fit comfortably; dolphin encounters at one hour pair easily with other activities.</p></details>
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is Freeport a dock or tender port?</summary>
    <p class="mt-4 text-sm text-gray-500">Freeport is a <strong>dock port</strong> for most cruise lines — you walk off at the terminal without tender boats.</p></details>
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What is the best Freeport excursion for first-time visitors?</summary>
    <p class="mt-4 text-sm text-gray-500">Blue Hole snorkel for water lovers, Garden of the Groves for easy sightseeing, or Taino Beach for a relaxed pool-and-sand day.</p></details>
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Do I need Bahamian cash?</summary>
    <p class="mt-4 text-sm text-gray-500"><strong>US dollars</strong> are widely accepted. Bahamian dollars (BSD) are official and pegged 1:1 with USD. Carry small bills for tips and market vendors.</p></details>
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How far is Lucayan National Park from the port?</summary>
    <p class="mt-4 text-sm text-gray-500">Approximately <strong>25–30 minutes</strong> east of the Freeport cruise terminal by road on organised cave tours.</p></details>
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Can children do dolphin encounters?</summary>
    <p class="mt-4 text-sm text-gray-500">The <strong>Dolphin Close Encounter</strong> welcomes all ages on the platform. Swim programmes have age and height requirements — check with the operator when booking.</p></details>
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Ship excursion or book independently?</summary>
    <p class="mt-4 text-sm text-gray-500">Ship tours guarantee the vessel waits if the operator is late. Reputable Freeport operators plan returns with a 60–90 minute buffer — confirm policies and read reviews before booking.</p></details>
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What should I pack for a Freeport port day?</summary>
    <p class="mt-4 text-sm text-gray-500">Reef-safe sunscreen, hat, swimwear, towel, water shoes for cave tours, and your ship card. USD cash for tips and Port Lucaya souvenirs.</p></details>
  <div class="mt-8 text-center">{book_cta()}</div>
  {internal_links()}
</div></section>"""


def all_content() -> dict[str, str]:
    return {
        "home.html": content_home(),
        "best-freeport-shore-excursions.html": content_best_excursions(),
        "freeport-beach-excursions.html": content_beach(),
        "freeport-snorkelling-excursions.html": content_snorkelling(),
        "freeport-nature-garden-tours.html": content_nature(),
        "freeport-dolphin-encounters.html": content_dolphin(),
        "freeport-cruise-port-guide.html": content_port_guide(),
        "one-day-in-freeport-from-a-cruise-ship.html": content_one_day(),
        "freeport-faq.html": content_faq(),
    }
