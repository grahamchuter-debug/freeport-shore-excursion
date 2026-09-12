/**
 * Public commercial status for Freeport Shore Excursions (Phase 19D).
 * Internal supply references must never appear on customer pages.
 *
 * Gate values:
 * - PRODUCTION_READY_LOCKED — journey visible; live Pay & request disabled
 * - BOOKING_ENABLED — live checkout allowed (requires Worker LIVE unlock too)
 */
window.FPO_COMMERCIAL = {
  bookingsApiUrl: "https://freeport-bookings-prod.dark-violet-8d91.workers.dev",
  email: "hello@freeportshoreexcursion.com",
  siteName: "Freeport Shore Excursions",
  defaultPublicBookingStatus: "BOOKING_ENABLED",
  cancellation:
    "Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable.",
  paymentNotConfirmation:
    "Secure your booking request with payment today. We'll confirm your excursion separately, and if we're unable to confirm it, you'll receive a full refund.",
  unableToConfirm:
    "If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  meetingInstructions:
    "Meeting point is approximately a 5–10 minute walk from the cruise ship pier. Exact meeting instructions will be provided after confirmation / on your e-ticket.",
  overTenGuidance:
    "For groups larger than 10, email hello@freeportshoreexcursion.com before requesting.",
  stayBehind:
    "I understand that if I choose to stay behind at Port Lucaya Marketplace or Lucaya Beach after the tour group departs, my return transport to the cruise pier is not included and I must arrange it myself.",
  products: {
    "garden-of-the-groves-city-tour": {
      productId: "garden-of-the-groves-city-tour",
      slug: "garden-of-the-groves-city-tour",
      name: "Garden of the Groves & Freeport City Tour",
      shortTitle: "Garden of the Groves & Freeport City Tour",
      productPath: "/freeport-nature-garden-tours",
      bookingPath: "/book/garden-of-the-groves-city-tour",
      receivedPath: "/book/garden-of-the-groves-city-tour/received",
      adultUsd: 69,
      childUsd: null,
      infantUsd: 0,
      guestModel: "ages3_plus_infant",
      durationLabel: "4 hours",
      maxGuests: 10,
      publicBookingStatus: "BOOKING_ENABLED",
      displayPrice: "Participants age 3+ $69 · Children age 0–2 free",
    },
  },
};
