#!/usr/bin/env python3
"""v31: Distinct background shades for homepage sections (AR & EN)."""
import re

FILES = ['index.html', 'en/index.html']

REPLACEMENTS = [
    # What I Do section -> very light mint tint
    ('<section class="about-section">', '<section class="about-section tint-mint">'),
    # Programs section -> remove generic bg-soft so it stays white (contrast with neighbors)
    ('<section id="programs" class="programs-section bg-soft">', '<section id="programs" class="programs-section">'),
]

for f in FILES:
    s = open(f).read()
    for a, b in REPLACEMENTS:
        assert a in s, f"missing: {a} in {f}"
        s = s.replace(a, b)
    open(f, 'w').write(s)
    print(f, 'updated')
