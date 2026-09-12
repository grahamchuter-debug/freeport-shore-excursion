#!/usr/bin/env python3
"""Generate /book/{slug}/ and /book/{slug}/received/ for Freeport Garden RTB."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from freeport_shell import footer_html, nav_html  # noqa: E402

PRODUCTS = [
    {
        "id": "garden-of-the-groves-city-tour",
        "name": "Garden of the Groves & Freeport City Tour",
        "product_path": "/freeport-nature-garden-tours",
        "price_list": (
            "<li>Participants age 3+ — $69</li>"
            "<li>Children age 0–2 — free (still recorded)</li>"
        ),
        "duration": "4 hours",
        "meeting": (
            "Meeting point is approximately a 5–10 minute walk from the cruise ship pier. "
            "Exact meeting instructions are provided after confirmation / on your e-ticket."
        ),
        "truth": (
            "Narrated vehicle tour with Freeport / recovery-area context, Garden of the Groves, "
            "and Port Lucaya Marketplace or an approximately 45-minute Lucaya Beach option, "
            "plus Royal Palm Way / Cooper's Castle narrative context. Easy activity level; "
            "surfaces may include paved, gravel, wooden plank, packed dirt, and a few steps. "
            "Wheelchair accessibility is not stated. Stay with the group for included return "
            "transport; staying behind means arranging your own return to the pier."
        ),
    },
]


def guest_fieldset(name: str) -> str:
    return f"""
        <fieldset class="booking-fieldset">
          <legend>How many people are travelling?</legend>
          <label for="adults">Participants age 3+ <span class="muted">— $69 each</span>
            <input type="number" name="adults" id="adults" min="1" max="10" value="2" required />
          </label>
          <label for="infants">Children age 0–2 <span class="muted">— free</span>
            <input type="number" name="infants" id="infants" min="0" max="10" value="0" />
          </label>
          <p class="help">At least one paying participant (age 3+) is required. Children age 0–2 are free but must be included in the guest count. Maximum 10 guests online including free children. For larger groups email <a href="mailto:hello@freeportshoreexcursion.com">hello@freeportshoreexcursion.com</a>.</p>
        </fieldset>
        <div class="booking-review" id="booking-review" aria-live="polite">
          <h3>Review</h3>
          <dl>
            <div><dt>Tour</dt><dd>{name}</dd></div>
            <div><dt>Date</dt><dd id="rev-date">—</dd></div>
            <div><dt>Cruise ship</dt><dd id="rev-ship">—</dd></div>
            <div><dt>Participants age 3+</dt><dd id="rev-adults">—</dd></div>
            <div id="rev-infants-row"><dt>Children age 0–2</dt><dd id="rev-infants">—</dd></div>
            <div class="booking-total"><dt>Total</dt><dd id="rev-total">USD $0</dd></div>
          </dl>
          <p class="help">Displayed total is for review. The charge amount is always calculated server-side. This is a request — payment does not confirm the excursion.</p>
        </div>"""


def book_page(p: dict) -> str:
    pid = p["id"]
    name = p["name"]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Book {name} | Freeport Shore Excursions</title>
  <meta name="description" content="Request {name} online. Pay securely to request — confirmation is emailed separately." />
  <link rel="canonical" href="https://freeportshoreexcursion.com/book/{pid}" />
  <meta name="robots" content="noindex,follow" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700&amp;family=Source+Sans+3:wght@400;500;600;700&amp;display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/css/site.css" />
</head>
<body data-page="book" data-product-id="{pid}">
{nav_html()}
<main id="main" class="page-main">

<section class="section booking-flow">
  <div class="wrap booking-shell px-4 sm:px-6">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">Home</a> · <a href="{p["product_path"]}">Nature &amp; gardens</a> · Booking
    </nav>
    <p class="eyebrow">Booking request</p>
    <h1 class="text-3xl font-display font-bold text-gray-900 mb-3">Book your excursion</h1>
    <p class="text-gray-600 mb-4">Choose your cruise date and complete payment to send your booking request. Confirmation is emailed separately after we arrange your excursion.</p>
    <ol class="booking-steps" aria-label="Booking steps">
      <li class="is-current">Tour</li>
      <li>Date / cruise</li>
      <li>Guests</li>
      <li>Details</li>
      <li>Review</li>
      <li>Payment</li>
      <li>Received</li>
    </ol>
    <div class="booking-panel">
      <h2 class="text-xl font-display font-bold text-gray-900">{name}</h2>
      <ul class="price-list">{p["price_list"]}</ul>
      <p class="help">{p["duration"]}. {p["meeting"]}</p>
      <p class="help">{p["truth"]}</p>
      <div class="booking-status-banner" id="booking-status-banner" role="status">
        <strong id="booking-status-title">Book with confidence</strong>
        <p id="booking-status-body">Secure your booking request with payment today. We'll confirm your excursion separately, and if we're unable to confirm it, you'll receive a full refund.</p>
      </div>
      <form class="booking-form" id="fpo-booking-form" method="post" action="#" data-product-id="{pid}" data-live="0" novalidate>
        <fieldset class="booking-fieldset">
          <legend>Date / cruise</legend>
          <label for="cruise_date">Excursion date
            <input type="date" name="cruise_date" id="cruise_date" required min="2026-09-01" max="2028-12-31" />
          </label>
          <label for="ship_name">Cruise ship
            <input type="text" name="ship_name" id="ship_name" required maxlength="80" autocomplete="organization" placeholder="e.g. Carnival Elation" />
          </label>
          <p class="help">Enter your ship and date. We do not invent a published Freeport ship-call schedule — availability is confirmed after your request.</p>
        </fieldset>
{guest_fieldset(name)}
        <fieldset class="booking-fieldset">
          <legend>Lead passenger details</legend>
          <label for="lead_name">Full name
            <input type="text" name="name" id="lead_name" required minlength="2" autocomplete="name" />
          </label>
          <label for="lead_email">Email
            <input type="email" name="email" id="lead_email" required autocomplete="email" />
          </label>
          <label for="lead_phone">Mobile / WhatsApp
            <input type="tel" name="phone" id="lead_phone" required autocomplete="tel" />
          </label>
          <label for="mobility">Mobility information
            <textarea name="mobility" id="mobility" rows="2" maxlength="500" placeholder="Any walking limits or mobility needs we should know about"></textarea>
          </label>
          <label for="special_requirements">Special requirements <span class="muted">(optional)</span>
            <textarea name="special_requirements" id="special_requirements" rows="2" maxlength="800"></textarea>
          </label>
        </fieldset>
        <div class="booking-honesty" id="booking-honesty">
          <h3>Book with confidence</h3>
          <p>Secure your booking request with payment today. We'll confirm your excursion separately, and if we're unable to confirm it, you'll receive a full refund.</p>
          <p>Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable.</p>
          <p>If you stay with the tour group, return transport to the cruise pier is included. If you choose to stay behind at Port Lucaya Marketplace or Lucaya Beach after the group departs, return transport is not included.</p>
        </div>
        <label class="consent">
          <input type="checkbox" name="staybehind_ack" id="staybehind_ack" required />
          <span>I understand that if I choose to stay behind at Port Lucaya Marketplace or Lucaya Beach after the tour group departs, my return transport to the cruise pier is not included and I must arrange it myself.</span>
        </label>
        <label class="consent">
          <input type="checkbox" name="ack" id="booking_ack" required />
          <span>I understand this is a booking request. Payment is taken when I submit my request and does not confirm the excursion. Confirmation will be emailed separately when my places are confirmed. If the excursion cannot be confirmed, the amount paid will be refunded in full to my original payment method.</span>
        </label>
        <p id="booking-error" class="booking-error" hidden role="alert"></p>
        <div class="booking-actions">
          <a class="btn btn--outline" href="{p["product_path"]}">Back</a>
          <button type="submit" class="btn btn--solid" id="booking-submit" hidden>Pay &amp; request</button>
          <button type="button" class="btn btn--solid" id="booking-submit-locked" disabled title="Live checkout is locked">Checkout locked — opening soon</button>
        </div>
        <p class="help" id="booking-footer-note">Prefer to ask first? <a href="mailto:hello@freeportshoreexcursion.com">hello@freeportshoreexcursion.com</a></p>
      </form>
    </div>
  </div>
</section>

</main>
{footer_html()}
  <script src="/js/commercial-config.js" defer></script>
  <script src="/js/booking.js" defer></script>
  <script src="/js/nav.js" defer></script>
</body>
</html>
"""


def received_page(p: dict) -> str:
    pid = p["id"]
    name = p["name"]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Booking request received | Freeport Shore Excursions</title>
  <meta name="description" content="Your Freeport excursion payment was received. This is a booking request, not a confirmation." />
  <link rel="canonical" href="https://freeportshoreexcursion.com/book/{pid}/received" />
  <meta name="robots" content="noindex,follow" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700&amp;family=Source+Sans+3:wght@400;500;600;700&amp;display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/css/site.css" />
</head>
<body data-page="book" data-product-id="{pid}">
{nav_html()}
<main id="main" class="page-main">

<section class="section booking-flow">
  <div class="wrap booking-shell px-4 sm:px-6">
    <p class="eyebrow">Booking request</p>
    <h1 class="text-3xl font-display font-bold text-gray-900 mb-3">Booking request received</h1>
    <p class="text-gray-600 mb-4">We've received your payment and your excursion request. This is not a booking confirmation. We're arranging your {name} and will email you again once it is confirmed.</p>
    <div id="booking-ref-wrap" class="booking-ref" hidden>
      <p class="eyebrow">Booking reference</p>
      <p id="booking-ref" class="booking-ref__code"></p>
    </div>
    <ul class="text-gray-600 space-y-2 mb-8 list-disc pl-5">
      <li>Payment successful — request awaiting confirmation</li>
      <li>Confirmation is emailed separately when places are arranged</li>
      <li>If we are unable to confirm, you will receive a full refund to your original payment method</li>
      <li>Meeting instructions will be provided after confirmation / on your e-ticket</li>
    </ul>
    <div class="booking-actions">
      <a class="btn btn--solid" href="{p["product_path"]}">Back to nature guide</a>
      <a class="btn btn--outline" href="mailto:hello@freeportshoreexcursion.com">Contact us</a>
    </div>
  </div>
</section>

</main>
{footer_html()}
  <script src="/js/booking-received.js" defer></script>
  <script src="/js/nav.js" defer></script>
</body>
</html>
"""


def main() -> None:
    for p in PRODUCTS:
        book_dir = ROOT / "book" / p["id"]
        recv_dir = book_dir / "received"
        book_dir.mkdir(parents=True, exist_ok=True)
        recv_dir.mkdir(parents=True, exist_ok=True)
        (book_dir / "index.html").write_text(book_page(p), encoding="utf-8")
        (recv_dir / "index.html").write_text(received_page(p), encoding="utf-8")
        print(f"  wrote book/{p['id']}/")


if __name__ == "__main__":
    main()
