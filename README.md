# Tap Out · Founder Associate application

Job Sinke's application page for the Founder Associate role at Tap Out.

- `public/` – what gets hosted: the built page (`index.html`) and its screenshots (`shots/`)
- `src.html` – page source with placeholders for inline assets
- `build.py` – rebuilds `public/index.html` from `src.html`: `python3 build.py`
- `fonts/`, `img/` – fonts and portrait embedded at build time

Keep this repository private: `fonts/` contains Denton Condensed, a licensed typeface.

## Hosting

Deployed on Cloudflare Workers (static assets) from `main` through Workers Builds; `wrangler.jsonc` points the site at `public/`. Every push to `main` redeploys.
