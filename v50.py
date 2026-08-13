#!/usr/bin/env python3
"""v50: replace the Journey of Change card (linked to the user's private Canva template page)
with a 'Coming Soon' card in both AR and EN projects.html. The private template page
journey-of-change.html is removed from the site."""

import os, shutil

for path, lang in [('projects.html', 'AR'), ('en/projects.html', 'EN')]:
    c = open(path).read()

    # 1) remove the whole Journey of Change program-card block
    start = c.find('<div class="program-card reveal">\n<div class="program-icon"><i data-lucide="route">')
    assert start != -1, f'Journey card not found in {path}'
    end_marker = '</div>\n<div class="program-card reveal">\n<div class="program-icon"><i data-lucide="compass">'
    end = c.find(end_marker, start)
    assert end != -1, f'card boundary not found in {path}'
    removed = c[start:end]
    c = c[:start] + c[end:]
    print(f'{path} ({lang}): removed old Journey card ({len(removed)} chars)')

    # 2) insert a generic "Coming Soon" card before the Strategic Thinking card
    card_ar = ('<div class="program-card reveal">\n'
        '<div class="program-icon"><i data-lucide="route"></i></div>\n'
        '<span class="program-status tag-soon">قيد التحضير • Coming Soon</span>\n'
        '<h3>برنامج تدريبي جديد<br>New Training Program</h3>\n'
        '<p class="program-tags">Self-Awareness · Change · Personal Growth</p>\n'
        '<p>برنامج تدريبي جديد تحت التحضير — سيُعلن عنه قريبًا.</p>\n'
        '<div class="program-meta">\n'
        '<span><i data-lucide="book-open"></i>Free Program</span>\n'
        '<span><i data-lucide="languages"></i>Arabic</span>\n'
        '</div>\n'
        '<span class="btn btn-outline" style="pointer-events:none;">قريبًا</span>\n'
        '</div>\n')
    card_en = ('<div class="program-card reveal">\n'
        '<div class="program-icon"><i data-lucide="route"></i></div>\n'
        '<span class="program-status tag-soon">Coming Soon • قيد التحضير</span>\n'
        '<h3>New Training Program<br>برنامج تدريبي جديد</h3>\n'
        '<p class="program-tags">Self-Awareness · Change · Personal Growth</p>\n'
        '<p>A new training program is under preparation — announcement coming soon.</p>\n'
        '<div class="program-meta">\n'
        '<span><i data-lucide="book-open"></i>Free Program</span>\n'
        '<span><i data-lucide="languages"></i>Arabic</span>\n'
        '</div>\n'
        '<span class="btn btn-outline" style="pointer-events:none;">Coming Soon</span>\n'
        '</div>\n')
    anchor = c.find('<div class="program-card reveal">\n<div class="program-icon"><i data-lucide="compass">')
    assert anchor != -1, f'Strategic Thinking anchor not found in {path}'
    card = card_ar if lang == 'AR' else card_en
    c = c[:anchor] + card + c[anchor:]
    print(f'{path} ({lang}): inserted Coming Soon card')

    open(path, 'w').write(c)

# 3) remove the private template pages from the repo entirely
for f in ['journey-of-change.html', 'course-template.html', 'en/journey-of-change.html', 'en/course-template.html']:
    if os.path.exists(f):
        os.remove(f)
        print(f'removed file: {f}')
    else:
        print(f'file not found (already gone): {f}')
