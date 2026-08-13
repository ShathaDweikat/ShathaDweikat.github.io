#!/usr/bin/env python3
"""v52: remove duplicated program cards. Each file has 4 cards (journey + strategic x2).
Keep only the first 2 (journey then strategic) and drop the duplicate pair."""

for path in ['projects.html', 'en/projects.html']:
    c = open(path).read()
    grid_start = c.find('<div class="program-grid">') + len('<div class="program-grid">')
    # find the 2nd card end: after 2nd '</div>' of program-card sequence = position after second card closes
    # cards are flat siblings; each card closes with '</div>\n'. Find the end of 2nd card.
    idx = grid_start
    card_ends = 0
    while card_ends < 2:
        d = c.find('</div>', idx)
        idx = d + len('</div>')
        card_ends += 1
    grid_end = c.find('</div>', idx)  # grid's own closing div
    assert grid_end != -1
    c = c[:idx] + '\n' + c[grid_end:]
    n = c.count('program-card')
    print(f'{path}: {n} cards')
    open(path, 'w').write(c)
    assert c.count('<div') == c.count('</div>'), f'{path}: unbalanced!'
