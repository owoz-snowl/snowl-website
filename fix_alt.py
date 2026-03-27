#!/usr/bin/env python3
"""Fix generic alt text in HTML files with descriptive alternatives."""

import re, os

base = "/Users/carson/ai-workspace/snowl-w"

# Multi-thumbnail files need line-by-line replacement
# Key: (filename, src_substring) → new_alt
SRC_BASED_REPLACEMENTS = {
    # 4000B5T - tool with 2 thumbs
    ("4000b5t.html", "4000B5T1"): 'alt="SNOWL 4000B5T snap fastener installation tool thumbnail 1"',
    ("4000b5t.html", "4000B5T2"): 'alt="SNOWL 4000B5T snap fastener installation tool thumbnail 2"',
    # 4000B6T - tool with 2 thumbs
    ("4000b6t.html", "4000B6T1"): 'alt="SNOWL 4000B6T snap fastener installation tool thumbnail 1"',
    ("4000b6t.html", "4000B6T2"): 'alt="SNOWL 4000B6T snap fastener installation tool thumbnail 2"',
}

# Simple global replacements: file + exact old alt → new alt
SIMPLE_REPLACEMENTS = [
    ("4000a1t1.html", 'alt="Thumb"',
     'alt="SNOWL 4000A1T1 snap fastener installation tool thumbnail"'),
    ("4000b1.html", 'alt="Thumbnail 1"',
     'alt="SNOWL 4000B1 turn button product photo"'),
    ("4000b1t1.html", 'alt="Thumb"',
     'alt="SNOWL 4000B1T1 turn button installation tool thumbnail"'),
    ("4000b3.html", 'alt="Thumbnail 1"',
     'alt="SNOWL 4000B3 turn button product photo"'),
    ("4000b5.html", 'alt="Thumbnail 1"',
     'alt="SNOWL 4000B5 turn button product photo"'),
    ("4000b5.html", 'alt="Thumbnail 2"',
     'alt="SNOWL 4000B5 turn button detail view"'),
    ("4000b6.html", 'alt="Thumbnail 1"',
     'alt="SNOWL 4000B6 turn button product photo"'),
    ("4000b7.html", 'alt="Thumbnail 1"',
     'alt="SNOWL 4000B7 turn button product photo"'),
    ("4000b8.html", 'alt="Thumbnail 1"',
     'alt="SNOWL 4000B8A turn button product photo"'),
    ("4000b8.html", 'alt="Thumbnail 2"',
     'alt="SNOWL 4000B8B turn button detail view"'),
    ("4000bs316.html", 'alt="Thumbnail 1"',
     'alt="SNOWL 4000BS316 316 stainless steel turn button product photo"'),
    ("4000d8t1.html", 'alt="Thumb"',
     'alt="SNOWL 4000D8T1 snap fastener installation tool thumbnail"'),
    ("hibur.html", 'alt="Thumb"',
     'alt="SNOWL HIBUR snap fastener installation tool thumbnail"'),
]

changed_files = set()

# Simple replacements
for fname, old_alt, new_alt in SIMPLE_REPLACEMENTS:
    fpath = os.path.join(base, fname)
    if not os.path.exists(fpath):
        print(f"SKIP (not found): {fname}")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    if old_alt not in content:
        print(f"NOT FOUND: {fname} — {old_alt}")
        continue
    new_content = content.replace(old_alt, new_alt, 1)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"FIXED: {fname} — {old_alt}")
    changed_files.add(fname)

# Multi-thumbnail files: replace based on src path context
for (fname, src_key), new_alt in SRC_BASED_REPLACEMENTS.items():
    fpath = os.path.join(base, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        if f'src="{src_key}' in line and 'alt="Thumb"' in line:
            # Replace the alt="Thumb" in this specific line
            new_line = re.sub(r'alt="Thumb"', new_alt, line)
            new_lines.append(new_line)
            alt_val = new_alt.split('"')[1]
            print(f"FIXED: {fname} line — {src_key} → {alt_val}")
            changed_files.add(fname)
        else:
            new_lines.append(line)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

print(f"\nTotal files changed: {len(changed_files)}")
for f in sorted(changed_files):
    print(f"  - {f}")
