#!/usr/bin/env python3
"""v51: restore Journey of Change card in projects.html (AR/EN), linked to the template page.
Remove the generic 'Coming Soon' placeholder card inserted in v50."""

card_ar = ('<div class="program-card reveal">\n'
    '<div class="program-icon"><i data-lucide="route"></i></div>\n'
    '<span class="program-status tag-ready">متاح الآن • Available</span>\n'
    '<h3>رحلة التغيير<br>Journey of Change</h3>\n'
    '<p class="program-tags">Self-Awareness · Change · Personal Growth</p>\n'
    '<p>برنامج تعليمي مجاني يركز على الوعي الذاتي وفهم التغيير والنمو الشخصي.</p>\n'
    '<div class="program-meta">\n'
    '<span><i data-lucide="book-open"></i>Free Program</span>\n'
    '<span><i data-lucide="languages"></i>Arabic</span>\n'
    '</div>\n'
    '<a href="journey-of-change.html" class="btn btn-primary">استكشف البرنامج</a>\n'
    '</div>\n')

card_en = ('<div class="program-card reveal">\n'
    '<div class="program-icon"><i data-lucide="route"></i></div>\n'
    '<span class="program-status tag-ready">Available • متاح الآن</span>\n'
    '<h3>Journey of Change<br>رحلة التغيير</h3>\n'
    '<p class="program-tags">Self-Awareness · Change · Personal Growth</p>\n'
    '<p>A free learning program focused on self-awareness, understanding change, and personal growth.</p>\n'
    '<div class="program-meta">\n'
    '<span><i data-lucide="book-open"></i>Free Program</span>\n'
    '<span><i data-lucide="languages"></i>Arabic</span>\n'
    '</div>\n'
    '<a href="../journey-of-change.html" class="btn btn-primary">Explore the Program</a>\n'
    '</div>\n')

import re

for path, card in [('projects.html', card_ar), ('en/projects.html', card_en)]:
    c = open(path).read()
    # remove the generic Coming Soon placeholder card
    m = re.search(r'<div class="program-card reveal">\n<div class="program-icon"><i data-lucide="route"></i></div>\n<span class="program-status tag-soon">.*?\n</div>\n', c, re.S)
    if m:
        c = c[:m.start()] + c[m.end():]
        print(f'{path}: removed placeholder card')
    else:
        # fallback: remove by anchor text
        m2 = re.search(r'<div class="program-card reveal">.*?قيد التحضير • Coming Soon.*?\n</div>\n', c, re.S)
        if m2:
            c = c[:m2.start()] + c[m2.end():]
            print(f'{path}: removed placeholder card (fallback)')
        else:
            print(f'{path}: placeholder card not found')
    # insert Journey card at the beginning of the grid (before strategic thinking card)
    anchor = c.find('<div class="program-card reveal">')
    assert anchor != -1, f'no program-card in {path}'
    c = c[:anchor] + card + c[anchor:]
    print(f'{path}: Journey card restored; now {c.count("program-card")} cards')
    open(path, 'w').write(c)
