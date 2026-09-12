import { freeportBookingCore } from "./freeport";
import type { AgeBand, BookableProductConfig, ProductCapacity, ProductPricing } from "../world-booking/types";

/**
 * Operational routing: Wow A Tour ops mailbox for Graham’s manual fulfilment.
 * Public customers never see SEG. Graham places corresponding bookings via his
 * established SEG affiliate / white-label account using INTERNAL supply refs only.
 */
const OPERATIONS = {
  id: "wow-a-tour-operations",
  displayName: "Wow A Tour",
  notificationEmail: "info@wowatour.com",
  routingStatus: "production_ready" as const,
};

const REQUEST_SETTLEMENT = "charge_refund" as const;

/** Graham online max — never describe as supplier / vehicle capacity. */
const FPO_CAPACITY: ProductCapacity = {
  minGuests: 1,
  maxGuestsPerBooking: 10,
  maxGuestsPerBookingSource: "approved",
  supplierGroupSize: null,
  maxGuestsPerGuide: null,
};

/**
 * Launch model (Phase 19D Graham-approved):
 * Ages 0–2 free (recorded).
 * Ages 3+ paying participant USD 69 (no invented child discount).
 * Technical adult band = paying participants ages 3+; child band not sold.
 *
 * FREEZE after live launch: deeper commercial review only after first genuine
 * booking OR meaningful Google traffic (net/margin/SEG/direct/van/price/etc.).
 */
const PAYING_INFANT_BANDS: readonly AgeBand[] = [
  { id: "adult", label: "Participants age 3+", minAge: 3, maxAge: null, pricingStatus: "priced" },
  { id: "child", label: "Children", minAge: 3, maxAge: 11, pricingStatus: "not_sold" },
  { id: "infant", label: "Children age 0–2 (free)", minAge: 0, maxAge: 2, pricingStatus: "priced" },
];

function payingGuestInfantUsd(payingAmount: number): ProductPricing {
  return {
    model: "adult_child",
    currency: "USD",
    adultAmount: payingAmount,
    childAmount: null,
    childPricingStatus: "not_sold",
    infantAmount: 0,
    infantPricingStatus: "priced",
    pricingNeedsConfirmation: false,
  };
}

const SHARED_PENDING = [
  "Customer cancellation APPROVED: free outside 14 days before excursion; from the 14th day non-refundable.",
  "Unable to confirm after payment: full refund to original payment method.",
  "Meeting: approximately 5–10 minute walk from cruise ship pier; exact instructions after confirmation / on e-ticket.",
  "Stay-behind: if guest remains at Port Lucaya Marketplace or Lucaya Beach after the tour group departs, return transport to the cruise pier is NOT included — guest arranges/pays own return.",
  "Default: guest remains with tour → return transport included with tour.",
  "Fulfilment: Graham places corresponding booking via established SEG affiliate / white-label route (INTERNAL).",
  "Payment received ≠ excursion confirmed.",
  "Online max 10 guests per booking including free 0–2 (Graham online limit — not supplier capacity).",
  "At least one paying participant (ages 3+) required.",
  "Activity: Easy. Surfaces may include paved, gravel, wooden plank, packed dirt, a few steps. Wheelchair accessibility UNKNOWN — do not claim.",
  "commercial_status=SEG_FULFILMENT_READY · fulfilment_mode=SEG_MANUAL · supplier=UNKNOWN · direct_supplier_status=NOT_CONTACTED · net_cost=UNKNOWN · margin=UNKNOWN",
] as const;

export const FREEPORT_CANCELLATION_COPY = {
  customerCancellation:
    "Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable. If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  freeWindow: "Free cancellation outside 14 days before your excursion.",
  insideWindow: "From the 14th day before your excursion, bookings are non-refundable.",
  unableToConfirm:
    "If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  paymentNotConfirmation:
    "Secure your booking request with payment today. We'll confirm your excursion separately, and if we're unable to confirm it, you'll receive a full refund.",
  meetingInstructions:
    "Meeting point is approximately a 5–10 minute walk from the cruise ship pier. Exact meeting instructions will be provided after confirmation / on your e-ticket.",
  overTenGuidance: "For groups larger than 10, email hello@freeportshoreexcursion.com before requesting.",
  stayBehind:
    "I understand that if I choose to stay behind at Port Lucaya Marketplace or Lucaya Beach after the tour group departs, my return transport to the cruise pier is not included and I must arrange it myself.",
} as const;

const GARDEN: BookableProductConfig = {
  id: "garden-of-the-groves-city-tour",
  destinationId: freeportBookingCore.id,
  slug: "garden-of-the-groves-city-tour",
  name: "Garden of the Groves & Freeport City Tour",
  durationLabel: "4 hours",
  bookingMode: "request",
  availability: "live",
  bookingPath: "/book/garden-of-the-groves-city-tour",
  receivedPath: "/book/garden-of-the-groves-city-tour/received",
  confirmedPath: "/book/garden-of-the-groves-city-tour/received",
  productPath: "/freeport-nature-garden-tours",
  pricing: payingGuestInfantUsd(69),
  ageBands: PAYING_INFANT_BANDS,
  capacity: FPO_CAPACITY,
  requiredCustomerFields: ["name", "email", "phone"],
  supplier: OPERATIONS,
  paymentSettlement: REQUEST_SETTLEMENT,
  schedulePortSlug: "freeport",
  pendingCommercialRules: [
    ...SHARED_PENDING,
    "Paying participant USD 69 (ages 3+) · Children 0–2 FREE (must record) · require ≥1 paying participant",
    "Narrated vehicle tour · Freeport / recovery-area context · Garden of the Groves · Port Lucaya Marketplace OR approximately 45-minute Lucaya Beach option · Royal Palm Way / Cooper's Castle narrative context",
    "Do not invent interior admission charges, fixed stop sequence beyond source, wheelchair accessibility, taxi availability/pricing, or return-to-ship guarantees",
  ],
  supplierReferenceNotes: [
    "INTERNAL SUPPLY: SEG_MANUAL · CAFPGARDEN",
    "INTERNAL CODE: CAFPGARDEN",
    "Fulfilment mode: SEG_MANUAL",
    "Supplier contact: UNKNOWN · NOT_CONTACTED · net/margin UNKNOWN",
    "Fulfilment: place via established SEG affiliate / white-label route (manual — do not automate).",
    "Selling: Paying participant USD 69 (ages 3+) · Children 0–2 FREE (recorded).",
    "Customer cancellation: Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable.",
    "Unable to confirm after payment: full refund to original payment method.",
  ],
};

export const FREEPORT_BOOKABLE_PRODUCTS: readonly BookableProductConfig[] = [GARDEN];

export function findFreeportBookingProduct(productId: string): BookableProductConfig | null {
  return FREEPORT_BOOKABLE_PRODUCTS.find((p) => p.id === productId) ?? null;
}

export function listFreeportBookingProducts(): readonly BookableProductConfig[] {
  return FREEPORT_BOOKABLE_PRODUCTS;
}
