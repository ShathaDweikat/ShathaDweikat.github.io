#!/usr/bin/env python3
"""v46b: replace en/projects.html card lines 78..105 with modern v31 cards."""
lines = open('en/projects.html').read().split('\n')
assert lines[77].strip() == '<div class="program-grid">', lines[77]

# find end: '</div>' at depth 0 after the two cards — search for line '</div>' right after 'Course Template' card
start = 78
end = None
depth = 0
for i in range(start-1, len(lines)):
    l = lines[i]
    if '<div class="program-card' in l:
        depth += 1
    elif l.strip() == '</div>' and depth > 0:
        depth -= 1
        if depth == 0:
            end = i
            break
assert end is not None, 'card block end not found'
print('replace lines', start+1, 'to', end+1)

new_cards = '''<div class="program-card reveal">
<div class="program-icon"><i data-lucide="route"></i></div>
<span class="program-status tag-ready">Available Now • متاح الآن</span>
<h3>Journey of Change<br>رحلة التغيير</h3>
<p class="program-tags">Self-Awareness · Change · Personal Growth</p>
<p>An educational journey supporting self-awareness, understanding the stages of change, and building practical steps toward personal growth and development.</p>
<div class="program-meta">
<span><i data-lucide="book-open"></i>Free Program</span>
<span><i data-lucide="languages"></i>Arabic</span>
</div>
<a href="journey-of-change.html" class="btn btn-primary">Explore the Program</a>
</div>
<div class="program-card reveal">
<div class="program-icon"><i data-lucide="compass"></i></div>
<span class="program-status tag-soon">In Development • قيد التطوير</span>
<h3>Fundamentals of Strategic Thinking<br>أساسيات التفكير الاستراتيجي</h3>
<p class="program-tags">Strategic Thinking · Vision · Goal Setting · Action</p>
<p>A program in development focused on building the fundamentals of strategic thinking and turning goals into actionable steps.</p>
<div class="program-meta">
<span><i data-lucide="book-open"></i>Free Program</span>
<span><i data-lucide="languages"></i>Arabic</span>
</div>
<a href="course-template.html" class="btn btn-outline">Coming Soon</a>
</div>'''
lines = lines[:78] + new_cards.split('\n') + lines[end+1:]
open('en/projects.html','w').write('\n'.join(lines))
print('en/projects.html updated. cards:', '\n'.join(lines).count('program-card'))
