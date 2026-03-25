#!/usr/bin/env python3
"""Fix SNOWL website i18n: broken lang-switcher buttons + add data-i18n attributes."""

import re

WD = "/Users/carson/ai-workspace/snowl-w/"

# ============================================================
# FIX 1: Broken lang-switcher in about/contact/news/videos.html
# ============================================================
BROKEN_PATTERN = (
    r'<div class="lang-switcher">'
    r'<button class="lang-btn active">EN</button>'
    r'<button class="lang-btn" onclick="setLang\(\'zh\'\)"> data-lang="zh">中</button>'
    r'<button class="lang-btn">DE</button>'
    r'<button class="lang-btn">FR</button>'
    r'<button class="lang-btn">RU</button>'
    r'<button class="lang-btn">PT</button>'
    r'<button class="lang-btn">ES</button>'
    r'</div>'
)
CORRECT_LANGSWITCHER = (
    '<div class="lang-switcher">'
    '<button class="lang-btn active" data-lang="en" onclick="setLang(\'en\')">EN</button>'
    '<button class="lang-btn" data-lang="zh" onclick="setLang(\'zh\')">中</button>'
    '<button class="lang-btn" data-lang="de" onclick="setLang(\'de\')">DE</button>'
    '<button class="lang-btn" data-lang="fr" onclick="setLang(\'fr\')">FR</button>'
    '<button class="lang-btn" data-lang="ru" onclick="setLang(\'ru\')">RU</button>'
    '<button class="lang-btn" data-lang="pt" onclick="setLang(\'pt\')">PT</button>'
    '<button class="lang-btn" data-lang="es" onclick="setLang(\'es\')">ES</button>'
    '</div>'
)

BROKEN_FILES = ["about.html", "contact.html", "news.html", "videos.html"]
for fname in BROKEN_FILES:
    fpath = WD + fname
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = re.sub(BROKEN_PATTERN, CORRECT_LANGSWITCHER, content)
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[FIXED] {fname}: lang-switcher")
    else:
        print(f"[SKIP]  {fname}: lang-switcher (already OK or not found)")

# ============================================================
# FIX 2: Fix misplaced data-i18n in footer h4/p tags
# Pattern: <h4> data-i18n="key">Text</h4>  →  <h4 data-i18n="key">Text</h4>
# ============================================================
MISPLACED_PATTERNS = [
    (r'<h4> data-i18n="(f_\w+)">(.*?)</h4>', r'<h4 data-i18n="\1">\2</h4>'),
    (r'<p> data-i18n="(f_\w+)">(.*?)</p>', r'<p data-i18n="\1">\2</p>'),
]
for fname in ["about.html", "contact.html", "news.html", "videos.html", "products.html"]:
    fpath = WD + fname
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = content
    for pat, repl in MISPLACED_PATTERNS:
        new_content = re.sub(pat, repl, new_content)
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[FIXED] {fname}: misplaced data-i18n in h4/p")
    else:
        print(f"[SKIP]  {fname}: misplaced data-i18n (none found)")

print("\nAll lang-switcher fixes done.")
