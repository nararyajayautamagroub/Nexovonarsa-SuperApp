# Nexovonarsa SuperApp

A responsive web MVP for a multi-purpose portal covering learning, entertainment discovery, games, communication utilities, security education, and productivity.

## Current status

- **Web MVP:** `index.html` is a standalone responsive interface.
- **Catalog:** Search and category filters work in the browser.
- **Interactive demos:** Local notes, basic phone-number format validation, demo study prompt, and sample bug-report generation.
- **Not production-ready:** External services, authentication, persistent database, APK packaging, AI, streaming, and live monitoring are not connected yet.

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
- AI assistant integration (planned; backend required; keep API keys server-side)
- API playground for authorized endpoints (planned)
- Bug reports with generated demo IDs (not uploaded to a server yet)
- Service status page (planned)
- Feedback and help center (planned)

## Run locally

Open `index.html` in a modern browser. No build step is required for this prototype.

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

Web MVP: **0.1.0**. Feature labels describe prototypes or plans, not fully integrated live services.
