"""Add (or update, or remove) the Cloudflare Web Analytics beacon on every English page,
then rebuild the Arabic pages so they inherit it.

  python3 _i18n/add_analytics.py <token>     add or replace the beacon
  python3 _i18n/add_analytics.py --remove    take it off every page

The token is the value in the JS snippet from Cloudflare:
Analytics & Logs > Web Analytics > your site > "Manage site".
Cloudflare Web Analytics is cookie-free.
"""
import glob, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
PAGES = ["index.html", "about.html", "contact.html"] + sorted(glob.glob("services/*.html")) + sorted(glob.glob("insights/*.html"))
BEACON_RE = re.compile(r"\n?[ \t]*<script [^>]*src=[\"']https://static\.cloudflareinsights\.com/beacon\.min\.js[\"'][^>]*></script>")

def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg not in ("--remove",) and not re.fullmatch(r"[0-9a-f]{32}", arg):
        sys.exit("Expected a 32-character hex token (or --remove). Got: %r" % arg)
    for path in PAGES:
        s = open(path, encoding="utf-8").read()
        s = BEACON_RE.sub("", s)
        if arg != "--remove":
            tag = "  <script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{\"token\": \"%s\"}'></script>\n" % arg
            s = s.replace("</body>", tag + "</body>", 1)
        open(path, "w", encoding="utf-8").write(s)
    subprocess.check_call([sys.executable, os.path.join(ROOT, "_i18n", "build_ar.py")])
    print("beacon %s %d English pages; Arabic pages rebuilt." % ("removed from" if arg == "--remove" else "set on", len(PAGES)))

if __name__ == "__main__":
    main()
