#!/usr/bin/env python3
"""v52b: find 3rd and 4th program-card occurrences and remove them entirely."""

import re

for path in ['projects.html', 'en/projects.html']:
    c = open(path).read()
    starts = [m.start() for m in re.finditer(r'<div class="program-card reveal">', c)]
    assert len(starts) >= 4, f'{path}: only {len(starts)} cards'
    dup_start = starts[2]
    dup_end = starts[3]
    # end of 4th card: find the matching </div> after its btn
    seg = c[dup_end:]
    # locate btn line then the following closing </div>
    btn = seg.find('btn')
    close = seg.find('</div>', btn) + len('</div>')
    full = c[:dup_start] + c[dup_end + close:]
    n = full.count('program-card')
    assert n == 2, f'{path}: expected 2 cards, got {n}'
    assert full.count('<div') == full.count('</div>'), f'{path}: unbalanced'
    print(f'{path}: {n} cards, balanced')
    open(path, 'w').write(full)
