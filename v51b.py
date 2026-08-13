#!/usr/bin/env python3
"""v51b: fix broken program-grid in projects.html AR/EN.
The placeholder-removal regex left a stray '</div>' and floating button.
Rebuild the grid content cleanly."""

journey_ar = ('<div class="program-card reveal">\n'
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

strategic_ar = ('<div class="program-card reveal">\n'
    '<div class="program-icon"><i data-lucide="compass"></i></div>\n'
    '<span class="program-status tag-soon">قيد التطوير • In Development</span>\n'
    '<h3>أساسيات التفكير الاستراتيجي<br>Fundamentals of Strategic Thinking</h3>\n'
    '<p class="program-tags">Strategic Thinking · Vision · Goal Setting · Action</p>\n'
    '<p>برنامج قيد التطوير يركز على بناء أساسيات التفكير الاستراتيجي وتحويل الأهداف إلى خطوات عملية.</p>\n'
    '<div class="program-meta">\n'
    '<span><i data-lucide="book-open"></i>Free Program</span>\n'
    '<span><i data-lucide="languages"></i>Arabic</span>\n'
    '</div>\n'
    '<span class="btn btn-outline" style="pointer-events:none;">قريبًا</span>\n'
    '</div>\n')

journey_en = ('<div class="program-card reveal">\n'
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

strategic_en = ('<div class="program-card reveal">\n'
    '<div class="program-icon"><i data-lucide="compass"></i></div>\n'
    '<span class="program-status tag-soon">In Development • قيد التطوير</span>\n'
    '<h3>Fundamentals of Strategic Thinking<br>أساسيات التفكير الاستراتيجي</h3>\n'
    '<p class="program-tags">Strategic Thinking · Vision · Goal Setting · Action</p>\n'
    '<p>A development program focused on building fundamentals of strategic thinking and turning goals into actionable steps.</p>\n'
    '<div class="program-meta">\n'
    '<span><i data-lucide="book-open"></i>Free Program</span>\n'
    '<span><i data-lucide="languages"></i>Arabic</span>\n'
    '</div>\n'
    '<span class="btn btn-outline" style="pointer-events:none;">Coming Soon</span>\n'
    '</div>\n')

for path, pair in [('projects.html', (journey_ar, strategic_ar)),
                   ('en/projects.html', (journey_en, strategic_en))]:
    c = open(path).read()
    start = c.find('<div class="program-grid">')
    assert start != -1
    start += len('<div class="program-grid">')
    end = c.find('</div>', start)  # grid closing div
    assert end != -1
    c = c[:start] + '\n' + pair[0] + pair[1] + c[end:]
    print(f'{path}: grid rebuilt, {c.count("program-card")} cards')
    open(path, 'w').write(c)
