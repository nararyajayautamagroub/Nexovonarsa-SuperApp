# Real-time data and 10-scraper integration plan

## Truthful status

The current app is a static GitHub Pages MVP. It cannot safely host private API keys, run reliable scheduled scraping, verify payment webhooks, or provide a live server-side AI session. This document defines the integration contract; it does **not** claim that ten live scrapers or a backend are already deployed.

Never label cached, missing, demo, or stale data as real-time or 100% accurate. Every displayed record should include its source, fetched time, status, and freshness limit.

## Ten independent scraper adapters

Use ten independently deployable adapters behind a server-side ingestion service. Each adapter must return the same normalized envelope:

```json
{
  "source_id": "source-01",
  "status": "ok",
  "fetched_at": "2026-01-01T00:00:00Z",
  "observed_at": "2026-01-01T00:00:00Z",
  "ttl_seconds": 300,
  "records": [],
  "warnings": []
}
```

Recommended adapter slots (choose actual sources according to the product feature and each provider's terms; do not scrape these blindly):

1. Official provider API / public data feed (preferred primary source).
2. Official provider status or changelog feed.
3. Official RSS/Atom feed.
4. Public structured-data endpoint permitted by the provider.
5. Licensed catalog or discovery API.
6. Official event/news feed.
7. Official learning/content source with licensing checks.
8. Official service availability/status endpoint.
9. Secondary authorized source for cross-checking.
10. Independent fallback source for resilience.

These are adapter roles, not ten sources that are already connected. Configure each adapter with an allowlisted hostname, documented terms, rate limit, timeout, parser tests, and source owner before enabling it.

## Reliability and freshness rules

- Fetch concurrently with per-source timeout, retry with exponential backoff and jitter, and a circuit breaker.
- Respect robots.txt where applicable, provider terms, rate limits, licensing, and authentication. Prefer official APIs over HTML scraping.
- Validate schemas and sanitize untrusted HTML/text. Do not bypass login, CAPTCHAs, paywalls, or access controls.
- Preserve provenance and timestamps for every record. Keep raw payloads only when lawful and necessary.
- Use a configurable TTL per source. Mark results `stale` after TTL and `unavailable` after failure; never silently present stale data as current.
- Deduplicate by stable provider ID or canonical URL. Cross-check conflicts and surface disagreement instead of inventing a single “100% accurate” answer.
- Store snapshots and audit logs server-side. Public frontend endpoints must not expose API keys or scraper credentials.
- Add monitoring for success rate, latency, last successful fetch, parse failures, and provider rate limits.

## AI and API security

Live AI must be called through a server-side endpoint. Keep provider keys in deployment secrets, enforce request limits and input/output size limits, avoid logging sensitive prompts, and show a clear unavailable state when no key/backend is configured. A browser-only placeholder is not live AI.

## Payments and WhatsApp

QRIS needs a supported payment provider, server-created order IDs, server-side expiry, signature-verified payment webhooks, idempotency, and reconciliation. A client-side countdown or screenshot is not proof of payment. WhatsApp automation should use the official Business Platform or an authorized provider, consent, opt-out handling, and rate limits. A wa.me link is only a handoff to the user.

## Deployment and feature updates

GitHub Actions can run checks and deploy code after a reviewed commit. It must not blindly generate and commit arbitrary features in production. Use a pull request, automated tests, security checks, and human review for generated changes. Configure repository Pages permissions and required secrets in GitHub Settings; workflows cannot safely invent those credentials.

## Release checklist

- [ ] Ten real adapter implementations are configured with authorized source URLs.
- [ ] Contract tests pass for each adapter and malformed/stale responses.
- [ ] Backend and database are deployed; secrets remain server-side.
- [ ] AI endpoint is live and rate-limited.
- [ ] Payment webhooks are signature-verified and tested in provider sandbox.
- [ ] Frontend displays source, last-updated time, and stale/unavailable state.
- [ ] CI, browser tests, accessibility checks, and deployment all pass.
- [ ] Production URL and critical flows are manually smoke-tested.
