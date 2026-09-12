/**
 * Freeport destination booking core.
 * Product catalogue: shared/destinations/freeport-products.ts
 * Public editorial: scripts/build-freeport-site.py
 * Internal supply mapping: product.supplierReferenceNotes (never public HTML)
 */
import type { DestinationBookingCore } from "../world-booking/types";

export const freeportBookingCore = {
  id: "freeport",
  siteName: "Freeport Shore Excursions",
  siteHostname: "freeportshoreexcursion.com",
  siteUrl: "https://freeportshoreexcursion.com",
  bookingEmail: "hello@freeportshoreexcursion.com",
  originatingSite: "freeportshoreexcursion.com",
  originatingPort: "Freeport, Grand Bahama",
  bookingRefPrefix: "W2FPO",
  sessionKeyPrefix: "w2-fpo-booking",
  sessionKeyVersion: 1,
  currencyCode: "USD",
  bookableWindow: {
    start: "2026-09-01",
    end: "2028-12-31",
  },
  /** No Freeport schedule import — cruise date/ship are customer-entered. */
  schedulePortSlug: "freeport",
  customShipSlug: "not-listed",
  contactPath: "/contact",
  termsPath: "/terms",
  privacyPath: "/privacy",
} as const satisfies DestinationBookingCore;
