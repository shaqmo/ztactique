# Arabic site build

The Arabic pages under `/ar/` are **generated** from the English pages.
Do not edit files in `/ar/` by hand.

## Change English copy
1. Edit the English page (e.g. `about.html`).
2. Add or update the matching Arabic string in `_i18n/ar_*.py`
   (the key is the exact English text, the value is the Arabic).
3. Run `python3 _i18n/build_ar.py`.

The build lists any English string that has no Arabic translation yet, and
refuses to leave it silent. `python3 _i18n/build_ar.py --missing` only reports.

## What the build does
- copies each English page to `/ar/` with `lang="ar" dir="rtl"`
- swaps in the translations, rewrites internal links to `/ar/...`
- adds the Arabic web font, a language switcher, canonical and hreflang tags
- writes `sitemap.xml` (with language alternates) and `robots.txt`

Needs: `python3 -m pip install --user beautifulsoup4`.
After changing `style.css` or `script.js`, bump the `?v=` on the asset links.

## Analytics
`python3 _i18n/add_analytics.py <token>` adds the Cloudflare Web Analytics beacon
to every page (English pages, then the Arabic pages are rebuilt from them).
`--remove` takes it off. Run it again with a new token to replace the old one.
