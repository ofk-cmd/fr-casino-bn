#!/usr/bin/env python3
"""Apply fairpari v2 template, bump assets, SEO dates."""
from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://fairpari-casino-bonus.com"
ASSET_V = "20260618v2"
TODAY = "2026-06-18"


def css_prefix(path: Path) -> str:
    rel = path.relative_to(ROOT)
    depth = len(rel.parts) - 1
    return "../" * depth if depth else ""


def patch_html(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    orig = text
    changes: list[str] = []
    prefix = css_prefix(path)

    if 'data-template="v2"' not in text:
        text = text.replace("<html ", '<html data-template="v2" ', 1)
        changes.append("data-template")

    if "fairpari-v2.css" not in text:
        text = re.sub(
            rf'(<link rel="stylesheet" href="{re.escape(prefix)}css/fairpari-light-theme\.css\?v=[^"]+" />\n)',
            rf'\1    <link rel="stylesheet" href="{prefix}css/fairpari-v2.css?v={ASSET_V}" />\n',
            text,
            count=1,
        )
        changes.append("v2-css")

    text = re.sub(r"\?v=202606\d{2}[a-z0-9]*", f"?v={ASSET_V}", text)

    text = re.sub(r'"dateModified": "2026-06-\d{2}"', f'"dateModified": "{TODAY}"', text)
    text = re.sub(r"Yangilangan: 2026-06-\d{2}", f"Yangilangan: {TODAY}", text)
    text = re.sub(r"Оxirgi yangilanish: 2026-06-\d{2}", f"Oxirgi yangilanish: {TODAY}", text)
    text = re.sub(r"Oxirgi yangilanish: 2026-06-\d{2}", f"Oxirgi yangilanish: {TODAY}", text)
    text = re.sub(r"Последнее обновление: 2026-06-\d{2}", f"Последнее обновление: {TODAY}", text)
    text = re.sub(r"Обновлено: 2026-06-\d{2}", f"Обновлено: {TODAY}", text)
    text = re.sub(r"Yangilangan: 2026-06-\d{2} ·", f"Yangilangan: {TODAY} ·", text)

    # SEO fix: empty footer link
    if '<a href="">Главная</a>' in text:
        text = text.replace('<a href="">Главная</a>', '<a href="/">Главная</a>')
        changes.append("footer-link-fix")

    if text != orig:
        path.write_text(text, encoding="utf-8")
    return changes


def update_sitemap():
    sm = ROOT / "sitemap.xml"
    if not sm.exists():
        return
    urls = re.findall(r"<loc>([^<]+)</loc>", sm.read_text(encoding="utf-8"))
    entries = []
    for loc in urls:
        rel = loc.replace(DOMAIN, "").rstrip("/")
        if not rel or rel == "/":
            fp = ROOT / "index.html"
        elif rel == "/ru":
            fp = ROOT / "ru" / "index.html"
        elif rel.startswith("/ru/"):
            fp = ROOT / rel.lstrip("/")
            if not fp.suffix:
                fp = Path(str(fp) + ".html")
        else:
            fp = ROOT / (rel.lstrip("/") + ".html")
        lm = TODAY
        if fp.exists():
            lm = datetime.fromtimestamp(fp.stat().st_mtime).strftime("%Y-%m-%d")
        pri = "1.0" if rel in ("", "/", "/ru") else "0.3" if any(
            x in rel for x in ("politika", "cookie", "usloviya", "maxfiylik", "foydalanish", "masuliyat", "otvetstvennaya")
        ) else "0.8"
        entries.append((loc, pri, lm))
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc, pri, lm in entries:
        lines.append(f"  <url><loc>{loc}</loc><lastmod>{lm}</lastmod><priority>{pri}</priority></url>")
    lines.append("</urlset>")
    sm.write_text("\n".join(lines) + "\n", encoding="utf-8")


def word_count(path: Path) -> int:
    html = path.read_text(encoding="utf-8", errors="ignore")
    html = re.sub(r"<script.*?</script>", "", html, flags=re.S | re.I)
    html = re.sub(r"<[^>]+>", " ", html)
    return len(html.split())


def main():
    updated = 0
    for html in sorted(ROOT.rglob("*.html")):
        ch = patch_html(html)
        if ch:
            updated += 1
    update_sitemap()
    uz = word_count(ROOT / "index.html")
    ru = word_count(ROOT / "ru" / "index.html")
    print(f"Patched {updated} HTML files, asset v={ASSET_V}")
    print(f"Brand review UZ: {uz} words, RU: {ru} words")
    for label, w in [("UZ", uz), ("RU", ru)]:
        print(f"  {label}: {'OK' if w >= 2500 else 'UNDER 2500'}")


if __name__ == "__main__":
    main()
