"""Build the Arabic (RTL) site from the English pages plus a translation dictionary.

Usage:  python3 _i18n/build_ar.py            build /ar/ and update hreflang + switcher
        python3 _i18n/build_ar.py --missing  list untranslated strings and exit

The English pages are the single source of structure. Every visible string is
looked up in STR (English -> Arabic). Anything not found is reported, so an
Arabic page can never silently fall back to English.
"""
import glob, os, re, sys, importlib
from bs4 import BeautifulSoup, NavigableString, Comment

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "_i18n"))

DOMAIN = "https://ztactique.com"
PAGES = ["index.html", "about.html", "contact.html"] + sorted(glob.glob("services/*.html")) + sorted(glob.glob("insights/*.html"))

STR = {}
for mod in ["ar_common", "ar_home", "ar_pages", "ar_services", "ar_insights"]:
    try:
        STR.update(importlib.import_module(mod).STR)
    except ModuleNotFoundError:
        pass

SKIP_TAGS = {"script", "style", "svg", "canvas", "noscript"}
ALLOW_LATIN = {"ZTactique", "AWS", "Microsoft Azure", "Python", "React", "Z", "Tactique", "/", "·", "→", "←"}
ATTRS = ["aria-label", "placeholder", "alt", "title"]

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

def has_latin(s):
    return re.search(r"[A-Za-z]{2,}", re.sub(r"<[^>]+>", "", s)) is not None

missing = {}
def miss(page, key):
    missing.setdefault(key, set()).add(page)

def en_to_ar_path(p):
    """'/services/x.html' -> '/ar/services/x.html', '/' -> '/ar/'"""
    if p == "/":
        return "/ar/"
    return "/ar" + p

def page_url(path):
    """english file path -> absolute url path"""
    url = "/" + path
    if url.endswith("index.html"):
        url = url[: -len("index.html")]
    return url

def translate_node(el, page):
    if not getattr(el, "name", None) or el.name in SKIP_TAGS:
        return
    for a in ATTRS:
        if el.has_attr(a):
            v = norm(el[a])
            if v in STR:
                el[a] = STR[v]
            elif has_latin(v):
                miss(page, "[attr %s] %s" % (a, v))
    if el.name == "input" and el.get("type") == "hidden" and el.get("name") == "subject":
        v = el.get("value", "")
        el["value"] = STR.get(v, v)
    if el.name == "meta" and el.get("name") == "description":
        v = norm(el["content"])
        if v in STR: el["content"] = STR[v]
        else: miss(page, "[meta] " + v)
        return
    if el.name == "input" and el.get("type") == "email":
        el["dir"] = "ltr"
    child_tags = [c for c in el.children if getattr(c, "name", None)]
    inner = norm(el.decode_contents())
    # whole-element match first (handles inline <strong>/<a> inside paragraphs and list items)
    if child_tags and inner in STR:
        el.clear()
        el.append(BeautifulSoup(STR[inner], "html.parser"))
        return
    INLINE = {"strong", "em", "b", "i", "a", "code", "br"}
    has_direct_text = any(isinstance(c, NavigableString) and not isinstance(c, Comment) and norm(str(c)) for c in el.children)
    if child_tags and has_direct_text and all(c.name in INLINE for c in child_tags):
        # text mixed with inline tags: must be translated as one sentence (word order differs in Arabic)
        if has_latin(inner):
            miss(page, inner)
        return
    for c in list(el.children):
        if isinstance(c, Comment):
            continue
        if isinstance(c, NavigableString):
            t = norm(str(c))
            if not t:
                continue
            if t in STR:
                lead = " " if str(c)[:1].isspace() else ""
                trail = " " if str(c)[-1:].isspace() else ""
                c.replace_with(lead + STR[t] + trail)
            elif has_latin(t) and t not in ALLOW_LATIN:
                miss(page, t)
        else:
            translate_node(c, page)
    if child_tags and inner not in STR and not el.name in ("html", "body", "head"):
        pass

def rewrite_links(soup):
    for a in soup.find_all(["a", "link"]):
        h = a.get("href")
        if not h or not h.startswith("/") or h.startswith("//"):
            continue
        base = h.split("?")[0]
        if re.match(r"^/(assets|animations|style\.css|script\.js|logo|favicon)", base):
            continue
        if a.name == "link":
            continue
        a["href"] = en_to_ar_path(h)

def head_alternates(soup, url_path):
    head = soup.head
    for old in head.find_all("link", rel="alternate"):
        old.decompose()
    ar_url = DOMAIN + en_to_ar_path(url_path)
    en_url = DOMAIN + url_path
    for lang, u in (("en", en_url), ("ar", ar_url), ("x-default", en_url)):
        t = soup.new_tag("link", rel="alternate", hreflang=lang, href=u)
        head.append(t); head.append(NavigableString("\n  "))

def set_canonical(soup, url):
    for old in soup.head.find_all("link", rel="canonical"):
        old.decompose()
    t = soup.new_tag("link", rel="canonical", href=url)
    soup.head.append(t); soup.head.append(NavigableString("\n  "))

def write_sitemap():
    rows = []
    for path in PAGES:
        en = DOMAIN + page_url(path)
        ar = DOMAIN + en_to_ar_path(page_url(path))
        for loc in (en, ar):
            rows.append(
                "  <url>\n    <loc>%s</loc>\n"
                "    <xhtml:link rel=\"alternate\" hreflang=\"en\" href=\"%s\"/>\n"
                "    <xhtml:link rel=\"alternate\" hreflang=\"ar\" href=\"%s\"/>\n"
                "    <xhtml:link rel=\"alternate\" hreflang=\"x-default\" href=\"%s\"/>\n  </url>" % (loc, en, ar, en))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    open("sitemap.xml", "w", encoding="utf-8").write(xml)
    open("robots.txt", "w", encoding="utf-8").write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % DOMAIN)

def build_ar(missing_only=False):
    for path in PAGES:
        src = clean_src(open(path, encoding="utf-8").read())
        soup = BeautifulSoup(src, "html.parser")
        url_path = page_url(path)
        # language + direction
        soup.html["lang"] = "ar"; soup.html["dir"] = "rtl"
        # title
        if soup.title:
            t = norm(soup.title.string or "")
            if t in STR: soup.title.string = STR[t]
            else: miss(path, "[title] " + t)
        translate_node(soup.body, path)
        for m in soup.find_all("meta", attrs={"name": "description"}):
            translate_node(m, path)
        if missing_only:
            continue
        # fonts: add an Arabic face
        for l in soup.find_all("link", href=re.compile("fonts.googleapis.com/css2")):
            l["href"] = "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=Roboto:wght@400;500;700&display=swap"
        rewrite_links(soup)
        # language switcher: link to the English twin
        nav = soup.find("ul", class_="nav-links")
        if nav:
            for old_li in nav.find_all(class_="lang-switch"):
                old_li.decompose()   # the English source carries an Arabic switch; replace it
        if nav:
            li = soup.new_tag("li"); li["class"] = "lang-switch"
            a = soup.new_tag("a", href=url_path); a["lang"] = "en"; a["hreflang"] = "en"; a.string = "English"
            li.append(a)
            nav.insert(len(nav.find_all("li", recursive=False)) - 1, li)  # before the Contact button
        head_alternates(soup, url_path)
        set_canonical(soup, DOMAIN + en_to_ar_path(url_path))
        out = os.path.join("ar", path)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(serialize(soup))

def clean_src(s):
    """Remove what a previous run added, so the same input always gives the same output."""
    s = re.sub(r'\n[ \t]*<li class="lang-switch">.*?</li>', "", s, flags=re.S)
    return re.sub(r'\n[ \t]*<link rel="(?:alternate|canonical)"[^>]*>', "", s)

def add_switch_to_english():
    """Give every English page an Arabic switcher, canonical and hreflang tags.

    Done with small string edits (not a parser round-trip) so the hand-written
    English files change only where intended. Idempotent.
    """
    for path in PAGES:
        s = open(path, encoding="utf-8").read()
        url_path = page_url(path)
        # remove anything a previous run added
        s = re.sub(r'\n[ \t]*<li class="lang-switch">.*?</li>', "", s, flags=re.S)
        s = re.sub(r'\n[ \t]*<link rel="(?:alternate|canonical)"[^>]*>', "", s)
        # language switcher, placed just before the Contact button
        m = re.search(r'\n([ \t]*)<li><a href="/contact\.html" class="btn btn-outline">', s)
        if m:
            ind = m.group(1)
            li = '\n%s<li class="lang-switch"><a href="%s" lang="ar" hreflang="ar">العربية</a></li>' % (ind, en_to_ar_path(url_path))
            s = s[:m.start()] + li + s[m.start():]
        # canonical + hreflang, before </head>
        en_url, ar_url = DOMAIN + url_path, DOMAIN + en_to_ar_path(url_path)
        tags = ('  <link rel="canonical" href="%s" />\n'
                '  <link rel="alternate" hreflang="en" href="%s" />\n'
                '  <link rel="alternate" hreflang="ar" href="%s" />\n'
                '  <link rel="alternate" hreflang="x-default" href="%s" />\n') % (en_url, en_url, ar_url, en_url)
        s = s.replace("</head>", tags + "</head>", 1)
        open(path, "w", encoding="utf-8").write(s)

def serialize(soup):
    """bs4 writes boolean attributes as x="" ; restore the canonical short form."""
    html = str(soup)
    html = re.sub(r'(\s(?:crossorigin|required|disabled|async|defer))=""', r"\1", html)
    html = html.replace("<!DOCTYPE html>\n\n", "<!DOCTYPE html>\n", 1)
    return html.replace("<html ", "<!-- Generated by _i18n/build_ar.py from the English page. Edit the English page or the translations, then rebuild. -->\n<html ", 1)

if __name__ == "__main__":
    only = "--missing" in sys.argv
    build_ar(missing_only=only)
    if missing:
        print("UNTRANSLATED: %d strings" % len(missing))
        for k in sorted(missing, key=lambda x: (-len(missing[x]), x)):
            print("%2d | %s" % (len(missing[k]), k))
        if not only:
            print("\nBuild wrote Arabic pages with these strings still in English.")
    else:
        print("All strings translated.")
    if not only:
        add_switch_to_english()
        write_sitemap()
        print("Built %d Arabic pages." % len(PAGES))
