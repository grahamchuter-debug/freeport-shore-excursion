/**
 * Shared booking engine tests — Freeport Phase 19D (Garden of the Groves only).
 */
import assert from "node:assert/strict";
import { test } from "node:test";
import {
  FREEPORT_BOOKABLE_PRODUCTS,
  FREEPORT_CANCELLATION_COPY,
  findFreeportBookingProduct,
} from "../destinations/freeport-products";
import { freeportBookingCore } from "../destinations/freeport";
import {
  assertClientTotalMatches,
  calculateBookingQuote,
  createBookingReference,
  destinationBrandFromCore,
  requestedCustomerEmail,
  statusAfterPaymentSuccess,
  supplierRequestEmail,
  validateCruise,
  validateCustomer,
} from "./index";

const brand = destinationBrandFromCore(freeportBookingCore);
const garden = findFreeportBookingProduct("garden-of-the-groves-city-tour");
assert.ok(garden);

test("single Freeport product ID present", () => {
  assert.equal(FREEPORT_BOOKABLE_PRODUCTS.length, 1);
  assert.equal(FREEPORT_BOOKABLE_PRODUCTS[0]!.id, "garden-of-the-groves-city-tour");
});

test("garden tour paying 69 infant free; requires paying participant", () => {
  assert.equal(garden!.pricing.adultAmount, 69);
  assert.equal(garden!.pricing.childAmount, null);
  assert.equal(garden!.pricing.childPricingStatus, "not_sold");
  assert.equal(garden!.pricing.infantAmount, 0);
  assert.equal(garden!.pricing.infantPricingStatus, "priced");
  assert.equal(calculateBookingQuote(garden!, { adults: 1, children: 0, infants: 0 }).amountCents, 6900);
  assert.equal(calculateBookingQuote(garden!, { adults: 2, children: 0, infants: 0 }).amountCents, 13800);
  assert.equal(calculateBookingQuote(garden!, { adults: 1, children: 0, infants: 1 }).amountCents, 6900);
  assert.equal(calculateBookingQuote(garden!, { adults: 2, children: 0, infants: 2 }).amountCents, 13800);
  assert.equal(calculateBookingQuote(garden!, { adults: 1, children: 0, infants: 1 }).partySize, 2);
  assert.throws(() => calculateBookingQuote(garden!, { adults: 0, children: 0, infants: 1 }));
  assert.throws(() => calculateBookingQuote(garden!, { adults: 1, children: 1, infants: 0 }));
});

test("max 10 guests; 11 rejected; free children count toward max", () => {
  assert.equal(garden!.capacity.maxGuestsPerBooking, 10);
  assert.doesNotThrow(() => calculateBookingQuote(garden!, { adults: 10, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(garden!, { adults: 11, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(garden!, { adults: 0, children: 0, infants: 0 }));
  assert.doesNotThrow(() => calculateBookingQuote(garden!, { adults: 9, children: 0, infants: 1 }));
  assert.throws(() => calculateBookingQuote(garden!, { adults: 9, children: 0, infants: 2 }));
});

test("client total must match server quote", () => {
  const quote = calculateBookingQuote(garden!, { adults: 1, children: 0, infants: 1 });
  assert.doesNotThrow(() => assertClientTotalMatches(quote, 6900));
  assert.throws(() => assertClientTotalMatches(quote, 1));
});

test("payment success status is requested not confirmed", () => {
  assert.equal(statusAfterPaymentSuccess("request"), "requested");
});

test("booking references use Freeport W2FPO prefix", () => {
  assert.match(createBookingReference(freeportBookingCore), /^W2FPO-/);
  assert.equal(freeportBookingCore.bookingRefPrefix, "W2FPO");
});

test("customer and cruise validation", () => {
  assert.equal(
    validateCustomer({ name: "Alex Traveller", email: "alex@example.com", phone: "+447700900123" }),
    null,
  );
  assert.ok(validateCustomer({ name: "A", email: "x", phone: "1" }));
  assert.ok(
    validateCruise({
      date: "2020-01-01",
      shipName: "Carnival Elation",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    }),
  );
  assert.equal(
    validateCruise({
      date: "2026-12-15",
      shipName: "Carnival Elation",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    }),
    null,
  );
});

test("cancellation copy covers 14-day policy and full refund", () => {
  assert.match(FREEPORT_CANCELLATION_COPY.customerCancellation, /outside 14 days/i);
  assert.match(FREEPORT_CANCELLATION_COPY.customerCancellation, /14th day/i);
  assert.match(FREEPORT_CANCELLATION_COPY.unableToConfirm, /full refund/i);
  assert.match(FREEPORT_CANCELLATION_COPY.paymentNotConfirmation, /confirm.*separately|separately.*confirm/i);
  assert.match(FREEPORT_CANCELLATION_COPY.stayBehind, /stay behind/i);
});

test("customer email never exposes SEG or internal codes", () => {
  const mail = requestedCustomerEmail({
    brand,
    product: garden!,
    reference: "W2FPO-TEST0001",
    cruise: {
      date: "2026-12-15",
      shipName: "Carnival Elation",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    },
    guests: { adults: 1, children: 0, infants: 0 },
    amountLabel: "USD $69.00",
    customerName: "Alex Traveller",
  });
  const blob = JSON.stringify(mail);
  assert.doesNotMatch(blob, /\bSEG\b|CAFPGARDEN|Shore Excursions Group|info@wowatour/i);
  assert.match(blob, /request|confirm/i);
});

test("ops email includes internal supply notes for Graham", () => {
  const mail = supplierRequestEmail({
    product: garden!,
    reference: "W2FPO-TEST0001",
    cruise: {
      date: "2026-12-15",
      shipName: "Carnival Elation",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    },
    guests: { adults: 1, children: 0, infants: 1 },
    amountLabel: "USD $69.00",
    customer: {
      name: "Alex Traveller",
      email: "alex@example.com",
      phone: "+447700900123",
    },
    operationalNotes:
      "Stay-behind acknowledgement: YES — guest understands return transport is not included if they stay behind at Port Lucaya Marketplace or Lucaya Beach after the tour group departs.",
    destinationLabel: "Freeport Shore Excursions — new booking request",
  });
  const blob = JSON.stringify(mail);
  assert.match(blob, /CAFPGARDEN|SEG_MANUAL/i);
  assert.match(blob, /ACTION REQUIRED/i);
  assert.match(blob, /\+447700900123/);
  assert.match(blob, /Stay-behind acknowledgement/i);
  assert.match(blob, /Participants age 3\+/i);
  assert.doesNotMatch(blob, /info@wowatour\.com/);
});

test("reject foreign destination product lookup", () => {
  assert.equal(findFreeportBookingProduct("belize-cave-tubing"), null);
  assert.equal(findFreeportBookingProduct("highlights-and-beach-break"), null);
  assert.equal(findFreeportBookingProduct("soufriere-volcano-waterfalls-tour"), null);
  assert.equal(findFreeportBookingProduct("classic-beach-day"), null);
  assert.equal(findFreeportBookingProduct("unknown-product"), null);
});
