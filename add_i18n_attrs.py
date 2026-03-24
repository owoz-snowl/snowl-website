#!/usr/bin/env python3
"""
add_i18n_attrs.py — Add js/i18n.js script and fix lang switcher on all HTML pages.
"""
import re
from pathlib import Path

BASE = Path('/Users/carson/ai-workspace/snowl-w')
HTML_FILES = sorted(BASE.glob('*.html'))
I18N_SCRIPT = '<script src="js/i18n.js"></script>'


def make_replacements(html):
    result = html

    # ── 1. Script tag before </body> ──────────────────────────────────────
    if I18N_SCRIPT not in result:
        result = result.replace('</body>', I18N_SCRIPT + '\n</body>', 1)

    # ── 2. Lang switcher buttons — add data-lang ─────────────────────────
    def fix_btn(m):
        btn = m.group(0)
        if 'data-lang=' in btn:
            return btn
        lang_map = {'EN': 'en', '中': 'zh', 'DE': 'de', 'FR': 'fr', 'RU': 'ru', 'PT': 'pt', 'ES': 'es'}
        lang = next((v for k, v in lang_map.items() if k in btn), None)
        if not lang:
            return btn
        # Insert data-lang before the closing >
        return re.sub(r'(<button[^>]*>)', rf'\1 data-lang="{lang}">', btn, count=1)

    result = re.sub(
        r'<button class="lang-btn[^>]*>[EN中DEFRRUPTES]</button>',
        fix_btn, result
    )

    # ── 3. Specific targeted text replacements (low-risk patterns) ─────────

    # Hero badge: <div class="hero-badge">TEXT</div>
    def replace_hero_badge(m):
        inner = m.group(2)
        badge_map = {
            'Since 1995 · Marine Fastener Expert': 'hero_badge',
            'About SNOWL': 'hero_badge',
            'Get in Touch': 'hero_badge',
            'Latest Updates': 'hero_badge',
            'Marine Fastener Expert': 'hero_badge',
            'Watch & Learn': 'hero_badge',
        }
        key = badge_map.get(inner)
        if key:
            return f'<div class="hero-badge" data-i18n="{key}">{inner}</div>'
        return m.group(0)

    result = re.sub(
        r'(<div class="hero-badge">)([^<]+)(</div>)',
        replace_hero_badge, result
    )

    # Category hero badges (other pages)
    for tag_text, key in [
        ('Precision Turn Buttons for Canvas Fastening', 'turn_tag'),
        ('Lightweight Nylon Buttons for Sailboat Canvas', 'nylon_tag'),
        ('Heavy-Duty Stainless Steel Snap Fasteners', 'snap_tag'),
        ('All-Copper Marine Snap Button Bases', 'owoz_tag'),
        ('Professional Installation Tools for Marine Hardware', 'tool_tag'),
    ]:
        result = re.sub(
            rf'<div class="hero-badge">({re.escape(tag_text)})</div>',
            rf'<div class="hero-badge" data-i18n="{key}">\1</div>',
            result
        )

    # Section tags: <div class="section-tag">TEXT</div>
    section_map = {
        'Our Products': 'sec_prod_tag', 'Featured': 'sec_show_tag',
        'How to Order': 'proc_tag', 'Latest News': 'news_tag',
        'Videos': 'vid_tag', 'Video Library': 'vid_tag',
        'Contact Us': 'contact_tag', 'About Us': 'about_tag',
        'Why SNOWL': 'adv_tag', 'Our Story': 'about_tag',
        'Why Us': 'about_tag', 'Factory': 'about_tag',
        'Product Range': 'sec_prod_tag', 'Popular Series': 'sec_show_tag',
        'Product Series': 'series_tag', 'Specifications': 'spec_title',
        'Contact Info': 'info_title', 'Product Overview': 'prod_overview',
        "Let's Connect": 'gs_tag', "Let's Talk": 'contact_title',
        'How It Works': 'proc_tag',
    }
    for text, key in section_map.items():
        result = re.sub(
            rf'(<div class="section-tag">)({re.escape(text)})(</div>)',
            rf'\1 data-i18n="{key}">\2\3',
            result
        )

    # Footer copyright
    result = re.sub(
        r'(>)(© 2025 SNOWL HONG KONG\. All Rights Reserved\.</p>)',
        r'\1 data-i18n="f_copy">© 2025 SNOWL HONG KONG. All Rights Reserved.</p>',
        result
    )

    # Footer h4 columns
    footer_h4_map = {
        'Products': 'f_prod', 'Company': 'f_company',
        'Support': 'f_sup', 'Contact': 'f_contact',
    }
    for text, key in footer_h4_map.items():
        result = re.sub(
            rf'(<h4>)({re.escape(text)})(</h4>)',
            rf'\1 data-i18n="{key}">\2\3',
            result
        )

    return result


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────
stats = {'modified': 0, 'skipped': 0}
for filepath in HTML_FILES:
    html = filepath.read_text(encoding='utf-8')
    original = html
    new_html = make_replacements(html)
    if new_html != original:
        filepath.write_text(new_html, encoding='utf-8')
        stats['modified'] += 1
        print(f"  ✓ {filepath.name}")
    else:
        stats['skipped'] += 1
        print(f"  · {filepath.name}")

print(f"\nDone! Modified: {stats['modified']}, Skipped: {stats['skipped']}")
print("\nNOTE: Manual data-i18n additions still needed for:")
print("  - Nav links and dropdowns")
print("  - Footer links")
print("  - Buttons")
print("  - Form labels")
print("  - Product series cards")
print("  - Process steps")
print("  - Breadcrumbs")
