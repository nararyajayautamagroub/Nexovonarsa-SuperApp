# Nexovonarsa SuperApp

A responsive web MVP for learning, entertainment discovery, games, security education, productivity, and a digital service store.

## Current status

- **Home portal:** `index.html` is a standalone responsive interface with feature search and categories.\n- **Store prototype:** `store.html` adds a redesigned responsive storefront, searchable service catalog, functional cart, checkout form, generated demo transaction ID, 10-minute browser countdown, WhatsApp deep-link demo, and AI assistant placeholder.
- **Catalog:** Search and category filters work in the browser.
- **Developer & Security Lab:** `developer-tools.html` includes a structured bug-report builder with TXT download, WhatsApp compatibility checklist, phone privacy/anti-spy checklist, JSON validator, text inspector, and demo ID generator. Checklists are manual guidance, not device scans.
- **Live status page:** `status.html` polls the public GitHub Actions API every 60 seconds and shows recent workflow runs. It reports CI status, not complete production-service health.
- **Interactive demos:** Local notes, basic phone-number format validation, demo study prompt, and sample bug-report generation.
- **Not production-ready:** QRIS is a visual placeholder only; no payment is collected or verified. AI replies are demo text. WhatsApp uses a browser deep link, not an automated confirmation system. No backend, authentication, persistent database, payment gateway, webhook, live service APIs, APK packaging, or production monitoring is connected.

## Feature catalog

### Learning
- Qur'an reading module (planned; connect a verified, properly licensed source)
- Shalawat audio player (planned; use authorized audio)
- Study hub and learning checklist (demo)

### Entertainment
- Comic discovery and official provider links (planned)
- Anime and film discovery through licensed services (planned)
- Music and podcast discovery (planned)
- Mini-game / HTML5 game area (planned)

### Communication
- Global sender concept with opt-in recipients, rate limits, unsubscribe controls, and abuse prevention (planned)
- Phone-number format validation only; does not identify a number's owner or confirm WhatsApp registration (demo)

### Security
- Device privacy checklist
- Wi-Fi security guidance for networks you own or are authorized to assess
- Website security checklist for authorized domains
- WhatsApp account-security guide
- No DDoS, Wi-Fi disruption, device intrusion, account takeover, spam, or crash/freeze payloads

### Productivity and developer tools
- Browser-local notes (demo; stored only in the current browser)
- AI assistant integration (planned; a secured backend and provider API key are required; never expose API keys in browser code). No live AI is connected yet.
- API playground for authorized endpoints (planned)
- Bug report builder with TXT export (local only; no server submission yet)
- Developer utilities: JSON validation, text inspector, demo IDs
- WhatsApp compatibility and anti-spyware checklists (manual, defensive guidance)
- Service status page (planned)
- Feedback and help center (planned)

## Run locally

Open `index.html` in a modern browser. The home page links to `store.html` and `developer-tools.html`. No build step is required for this static prototype.

## Deploy as a GitHub Pages site

1. Open repository **Settings → Pages**.
2. Select **Deploy from a branch**.
3. Choose `main` and `/(root)`, then save.
4. Wait for the Pages deployment workflow to finish and open the published URL shown in Settings → Pages.

## Next engineering milestones

1. Add automated HTML/JavaScript checks and accessibility tests.
2. Split the prototype into maintainable modules and add unit tests.
3. Add a backend, database, authentication, rate limiting, logging, and privacy controls before storing user data.
4. Integrate third-party APIs only after checking licensing, terms, and API security.
5. Create an Android app shell only after the web features and backend contracts are stable.
6. Add CI checks and a staging deployment before production.

## Safety and content policy

This project is for lawful, consent-based use. It does not implement DDoS tools, Wi-Fi killers, unauthorized phone access, WhatsApp crash/freeze exploits, spam payloads, or group takeovers. Adult content is not included. Security modules should remain defensive and limited to systems the operator owns or has explicit permission to test.

## Version

Web MVP: **0.4.0**. CI runs on pushes and pull requests; a Pages deployment workflow and live GitHub Actions status page have been added. Feature labels describe prototypes or plans, not fully integrated live services.
