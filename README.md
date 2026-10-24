# Nexovonarsa SuperApp

Responsive web MVP for learning, entertainment discovery, games, security education, productivity, and a digital service store.

## Current implementation

- **Home portal** (`index.html`): responsive portal with feature search and categories.
- **Store prototype** (`store.html`): searchable catalog, browser-side cart, checkout demo, demo transaction ID, 10-minute browser countdown, WhatsApp deep link, and AI assistant placeholder.
- **Developer & Security Lab** (`developer-tools.html`): bug-report builder with TXT export, JSON validator, text inspector, demo ID generator, and manual WhatsApp compatibility and device-privacy checklists.
- **Status page** (`status.html`): polls the public GitHub Actions API every 60 seconds to show recent workflow runs. This reflects workflow state, not full production uptime.
- **Automated checks**: GitHub Actions runs the static-site checker and Playwright browser tests on pushes to `main` and pull requests targeting `main`; screenshot artifacts are uploaded by CI.

## Important limitations

This is a static web prototype, not a production-ready service.

- **AI:** no live AI provider is connected. The assistant content is demo text. Real AI needs a secured server-side integration and a provider API key stored as a secret. Never put private API keys in browser JavaScript.
- **Payments:** QRIS is a visual placeholder. No money is collected or verified. Real payments require a payment provider, server-side order records, signature-verified webhooks, and server-side expiry checks.
- **WhatsApp:** the checkout creates a browser deep link only. It does not send automated messages or independently confirm payment.
- **Data:** there is no backend, account system, persistent database, or connected live domain-specific data API. Browser-local notes remain in the current browser.
- **Phone checks:** phone-number validation checks format only; it does not identify an owner or verify WhatsApp registration. Privacy checklists are manual guidance, not device scans.

Do not describe demo data as real-time or verified production data.

## Feature catalog

### Learning
- Qur'an reading module: planned; requires a verified and properly licensed source.
- Shalawat audio player: planned; use authorized audio.
- Study hub and learning checklist: demo.

### Entertainment
- Comic discovery and official provider links: planned.
- Anime, film, music, and podcast discovery through licensed services: planned.
- Mini-game / HTML5 game area: planned.

### Communication
- Opt-in messaging concept with rate limits, unsubscribe controls, and abuse prevention: planned.
- Phone-number format validation: demo only.

### Security
- Device privacy checklist.
- Wi-Fi security guidance for networks owned by the operator or explicitly authorized for assessment.
- Website security checklist for authorized domains.
- WhatsApp account-security guide.
- No DDoS, Wi-Fi disruption, device intrusion, account takeover, spam, or crash/freeze payloads.

### Productivity and developer tools
- Browser-local notes: demo.
- Live AI assistant: planned; secured backend and provider credentials required.
- Authorized API playground: planned.
- Bug-report builder with TXT export: local only; no server submission.
- JSON validation, text inspection, and demo ID generation.
- Feedback and help center: planned.

## Run locally

Open `index.html` in a modern browser. The prototype has no local build step. Automated checks run in GitHub Actions and use Python, Node.js, and Playwright.

## Enable GitHub Pages deployment

The deployment workflow is configured to run on pushes to `main`, but the repository's latest deployment attempt failed while configuring Pages. A repository owner must verify the hosting configuration and permissions:

1. Open repository **Settings → Pages**.
2. Set the build and deployment source to **GitHub Actions**.
3. Confirm GitHub Actions is permitted to deploy Pages for this repository.
4. Open the **Actions** tab and rerun the deployment workflow after fixing the configuration.
5. Verify the published URL in **Settings → Pages** and test the deployed pages.

A successful CI test does not mean the Pages deployment succeeded. Check each workflow result separately.

## Automation and verification

- A push to `main` triggers static checks and the Pages deployment workflow.
- Pull requests targeting `main` trigger static checks.
- CI uploads browser screenshots as an artifact for 14 days.
- The status page refreshes workflow information every 60 seconds.
- New functionality is not generated automatically by a commit. Code changes must still be implemented, reviewed, tested, and committed. Deployment only happens when the configured workflow succeeds.

## Next engineering milestones

1. Keep expanding automated tests, accessibility checks, and mobile browser coverage.
2. Add unit tests and split larger scripts into maintainable modules.
3. Build a secure backend with authentication, authorization, rate limiting, logging, and privacy controls before storing user data.
4. Integrate live data APIs only after verifying their sources, freshness, licensing, and terms.
5. Add AI through a secured backend and test provider errors, rate limits, and cost controls.
6. Integrate payments only through a supported payment provider with server-side webhook verification.
7. Add staging and production monitoring before presenting the app as production-ready.

## Safety and content policy

This project is for lawful, consent-based use. Security modules should remain defensive and limited to systems the operator owns or has explicit permission to test. No DDoS tools, Wi-Fi killers, unauthorized phone access, WhatsApp crash/freeze exploits, spam payloads, or group takeovers are included.

## Version

Web MVP: **0.4.1**. Features explicitly marked as demos or planned are not fully integrated live services.
