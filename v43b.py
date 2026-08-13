#!/usr/bin/env python3
"""v43b: replace the two program cards in projects.html via line ranges."""
lines = open('projects.html').read().split('\n')
# find card start lines
start = None; end = None
for i, l in enumerate(lines):
    if l.strip() == '<div class="program-grid">':
        start = i
    if start is not None and l.strip() == '</div>' and i > start and start < i - 2:
        # the grid close div — check previous content
        pass
# simpler: replace lines 78..115 (0-indexed 77..114) assuming grid contains both cards
# verify first
assert lines[77].strip() == '<div class="program-card reveal">', lines[77]
# find end of second card: look for '</div>' at indentation 0 after 77
depth = 0
end = None
for i in range(77, len(lines)):
    l = lines[i]
    if l.strip().startswith('<div class="program-card'):
        depth += 1
    elif l.strip() == '</div>' and depth > 0:
        depth -= 1
        if depth == 0:
            end = i
            break
print('cards span lines', 78, 'to', end+1)

new_cards = '''<div class="program-card reveal">
<div class="program-icon"><i data-lucide="route"></i></div>
<span class="program-status tag-ready">متاح الآن • Available</span>
<h3>رحلة التغيير<br>Journey of Change</h3>
<p class="program-tags">Self-Awareness · Change · Personal Growth</p>
<p>برنامج تعليمي مجاني يركز على الوعي الذاتي وفهم التغيير والنمو الشخصي.</p>
<div class="program-meta">
<span><i data-lucide="book-open"></i>Free Program</span>
<span><i data-lucide="languages"></i>Arabic</span>
</div>
<a href="journey-of-change.html" class="btn btn-primary">استكشف البرنامج</a>
</div>
<div class="program-card reveal">
<div class="program-icon"><i data-lucide="compass"></i></div>
<span class="program-status tag-soon">قيد التطوير • In Development</span>
<h3>أساسيات التفكير الاستراتيجي<br>Fundamentals of Strategic Thinking</h3>
<p class="program-tags">Strategic Thinking · Vision · Goal Setting · Action</p>
<p>برنامج قيد التطوير يركز على بناء أساسيات التفكير الاستراتيجي وتحويل الأهداف إلى خطوات عملية.</p>
<div class="program-meta">
<span><i data-lucide="book-open"></i>Free Program</span>
<span><i data-lucide="languages"></i>Arabic</span>
</div>
<a href="course-template.html" class="btn btn-outline">قريبًا</a>
</div>'''
lines = lines[:77] + new_cards.split('\n') + lines[end+1:]

# remove stale template hint button
lines = [l for l in lines if 'قالب صفحة دورة جاهز' not in l]

open('projects.html','w').write('\n'.join(lines))
print('projects.html updated')
