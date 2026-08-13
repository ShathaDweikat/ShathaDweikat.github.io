#!/usr/bin/env python3
"""v46c: replace en/projects.html card lines 78..105 (0-indexed 77..104) with modern cards."""
lines = open('en/projects.html').read().split('\n')
# program-grid at index 76, first card at 77
assert lines[77].startswith('<div class="program-card'), lines[77]
start = 77
end = None
depth = 0
for i in range(start, len(lines)):
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
lines = lines[:start] + new_cards.split('\n') + lines[end+1:]
open('en/projects.html','w').write('\n'.join(lines))
print('en/projects.html updated. cards:', '\n'.join(lines).count('program-card'))
