# Hey Y'all

Austin happy hour finder. Pick neighborhoods, a time, a max drink price and a vibe; it ranks real happy hours and maps them.

- **Data:** `src/data.js` — 33 venues across East Austin, South Lamar, South Congress and Zilker, gathered with Nimble on Oct 13-14, 2026.
- **App:** `src/template.html` — single-page app (no framework). `build.py` wraps it into `site/index.html`.
- **Map:** Leaflet 1.9.4 (bundled in `site/vendor/leaflet`, BSD-2 license) with CARTO Voyager tiles over OpenStreetMap data. Address search falls back to OpenStreetMap Nominatim.
- **Deploy:** Netlify builds on every push (`netlify.toml`: runs `python3 build.py`, publishes `site/`).

Next phases (see spec): database, monthly Nimble refresh, live re-check of top picks older than 30 days.
