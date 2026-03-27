#!/usr/bin/env python3
"""SEO product content supplement script for SNOWL website.
Adds: Marine Applications section, CE/ISO certifications, fixes broken content.
"""
import re
import os

SNOWL_W = "/Users/carson/ai-workspace/snowl-w"
CERT_BANNER = """
        <!-- Marine Applications -->
        <div style="background:linear-gradient(135deg,#f0f7ff,#e8f4fd);border:2px solid #0057b7;border-radius:12px;padding:20px;margin:20px 0">
          <div style="font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:#0057b7;margin-bottom:12px">⚓ Marine Applications</div>
          <div style="display:flex;gap:16px;flex-wrap:wrap">
            <div style="text-align:center;min-width:80px">
              <div style="font-size:1.8rem;margin-bottom:4px">🚤</div>
              <div style="font-size:0.78rem;color:#555;font-weight:600">Yacht</div>
            </div>
            <div style="text-align:center;min-width:80px">
              <div style="font-size:1.8rem;margin-bottom:4px">⛵</div>
              <div style="font-size:0.78rem;color:#555;font-weight:600">Sailboat</div>
            </div>
            <div style="text-align:center;min-width:80px">
              <div style="font-size:1.8rem;margin-bottom:4px">🛥️</div>
              <div style="font-size:0.78rem;color:#555;font-weight:600">Dinghy</div>
            </div>
            <div style="text-align:center;min-width:80px">
              <div style="font-size:1.8rem;margin-bottom:4px">🚢</div>
              <div style="font-size:0.78rem;color:#555;font-weight:600">Commercial Vessel</div>
            </div>
            <div style="text-align:center;min-width:80px">
              <div style="font-size:1.8rem;margin-bottom:4px">🏕️</div>
              <div style="font-size:0.78rem;color:#555;font-weight:600">Bimini Top</div>
            </div>
            <div style="text-align:center;min-width:80px">
              <div style="font-size:1.8rem;margin-bottom:4px">⛺</div>
              <div style="font-size:0.78rem;color:#555;font-weight:600">Sail Cover</div>
            </div>
          </div>
        </div>
        <!-- Certifications -->
        <div style="display:flex;gap:10px;margin:16px 0;flex-wrap:wrap">
          <div style="background:#e8f5e9;border:2px solid #2e7d32;border-radius:8px;padding:6px 14px;display:flex;align-items:center;gap:6px">
            <div style="width:22px;height:22px;background:#2e7d32;color:#fff;border-radius:4px;font-size:0.65rem;font-weight:900;display:flex;align-items:center;justify-content:center">CE</div>
            <span style="font-size:0.78rem;font-weight:700;color:#2e7d32">CE Certified</span>
          </div>
          <div style="background:#fff3e0;border:2px solid #e65100;border-radius:8px;padding:6px 14px;display:flex;align-items:center;gap:6px">
            <div style="width:22px;height:22px;background:#e65100;color:#fff;border-radius:4px;font-size:0.55rem;font-weight:900;display:flex;align-items:center;justify-content:center;line-height:1">ISO<br>9001</div>
            <span style="font-size:0.78rem;font-weight:700;color:#e65100">ISO 9001</span>
          </div>
          <div style="background:#f3e5f5;border:2px solid #7b1fa2;border-radius:8px;padding:6px 14px;display:flex;align-items:center;gap:6px">
            <div style="font-size:0.9rem">🌊</div>
            <span style="font-size:0.78rem;font-weight:700;color:#7b1fa2">Marine Grade</span>
          </div>
        </div>
"""

CERT_ROW = "<tr><td>Certifications</td><td>CE, ISO 9001</td></tr>"
APP_ROW   = "<tr><td>Marine Applications</td><td>Yacht, Sailboat, Dinghy, Commercial Vessel, Bimini Top, Sail Cover</td></tr>"

PRODUCT_FILES = [
    # 4000 series tool pages
    "4000a1t1.html","4000ax.html","4000b1t1.html","4000b5t.html",
    "4000b6t.html","4000d8t1.html","hibur.html",
    # 4000 series turn button
    "4000b1.html","4000b3.html","4000b5.html","4000b6.html",
    "4000b7.html","4000b8.html","4000bn.html","4000bs316.html",
    # 4000 series snap
    "4000c1.html","4000c4.html","4000c5.html","4000c7.html",
    "4000dx.html","4000rx.html",
    # OWOZ series
    "owoz-800000x.html","owoz-800001x.html","owoz-800002x.html",
    "owoz-800003x.html","owoz-800004x.html","owoz-800005x.html",
    "owoz-800006x.html","owoz-800007x.html",
    # Other products
    "833333x.html","msnap.html","ysnap.html","nylon-button.html",
    "turn-button.html","snap-fastener.html","owoz-fastener.html","tool.html",
]

def patch_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    basename = os.path.basename(filepath)

    # 1. Add cert row to spec-table if not present
    if "Certifications" not in content:
        # Find last <tr> inside spec-table and add after it
        # Match spec-table body
        spec_match = re.search(r'(<table class="spec-table">.*?</table>)', content, re.DOTALL)
        if spec_match:
            table = spec_match.group(1)
            # Find last <tr>
            last_tr = list(re.finditer(r'<tr>.*?</tr>', table, re.DOTALL))
            if last_tr:
                last_pos = last_tr[-1].end()
                table_new = table[:last_pos] + CERT_ROW + table[last_pos:]
                content = content.replace(table, table_new, 1)

    # 2. Add Marine Applications row to spec-table if not present
    if "Marine Applications" not in content:
        spec_match = re.search(r'(<table class="spec-table">.*?</table>)', content, re.DOTALL)
        if spec_match:
            table = spec_match.group(1)
            last_tr = list(re.finditer(r'<tr>.*?</tr>', table, re.DOTALL))
            if last_tr:
                last_pos = last_tr[-1].end()
                table_new = table[:last_pos] + APP_ROW + table[last_pos:]
                content = content.replace(table, table_new, 1)

    # 3. Add marine apps + cert banner before Inquiry button if not present
    if "Marine Applications</div>" not in content:
        # Find the inquiry button anchor
        btn_match = re.search(r'(<a href="contact\.html" class="btn btn-primary"[^>]*>.*?)(</a>)', content, re.DOTALL)
        if btn_match:
            # Insert banner just before the button
            content = content.replace(
                btn_match.group(1) + btn_match.group(2),
                CERT_BANNER + "\n        " + btn_match.group(1) + btn_match.group(2)
            )

    # 4. Fix hibur.html broken feat-list
    if "hibur.html" in basename and "镁合金" in content:
        # Replace the mega-single feat-list item with proper ones
        broken_feat = '<li>🪶 超轻量化设计'
        fixed_feats = """<li>🪶 Ultra-Lightweight — magnesium alloy, only 428g, reduces operator fatigue</li>
          <li>💪 High-Strength Structure — magnesium alloy, shock-resistant, built for longevity</li>
          <li>🎯 Precision Engineered — designed for SNAP product installation, accurate positioning</li>
          <li>✨ Professional Silver Finish — sleek metallic appearance for professional settings</li>
          <li>🔧 Easy Operation — 28.5 × 13.5 cm, comfortable grip, flexible operation</li>
          <li>🏭 Industrial Grade — suitable for high-frequency commercial installation work</li>"""
        content = content.replace(broken_feat, fixed_feats)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Patched: {basename}")
        return True
    else:
        print(f"  - No changes: {basename}")
        return False

def main():
    changed = []
    for fname in PRODUCT_FILES:
        fpath = os.path.join(SNOWL_W, fname)
        if os.path.exists(fpath):
            if patch_file(fpath):
                changed.append(fname)
        else:
            print(f"  ! Not found: {fname}")
    print(f"\nDone. {len(changed)} files changed: {changed}")

if __name__ == "__main__":
    main()
