#!/usr/bin/env python3
"""v46: upgrade en/projects.html cards to the polished v31 structure using line replacement."""
content = open('en/projects.html').read()

bad = '''<div class="program-card reveal">
<span class="program-status">Free Program</span>
<div class="program-icon"><i data-lucide="compass"></i></div>
<h3>Journey of Change</h3>
<p>
An educational journey supporting self-awareness, understanding the stages of change, and building practical steps toward personal growth and development.
</p>
<div class="program-meta">
<span><i data-lucide="globe"></i>Arabic</span>
<span><i data-lucide="badge-check"></i>Currently Available</span>
</div>
<a class="btn btn-primary" href="journey-of-change.html">Explore the Program</a>
</div>
<div class="program-card reveal">
<span class="program-status">In Development</span>
<div class="program-icon"><i data-lucide="brain-circuit"></i></div>
<h3>Fundamentals of Strategic Thinking for Youth</h3>
<p>
A training program developing strategic thinking among youth through self-analysis, vision building, goal setting, and turning ideas into actionable steps.
</p>
<div class="program-meta">
<span><i data-lucide="globe"></i>Arabic</span>
<span><i data-lucide="clock"></i>Coming Soon</span>
</div>
<a class="btn btn-outline" href="course-template.html">Course Template</a>
</div>'''
good = '''<div class="program-card reveal">
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
assert bad in content, 'bad cards not found'
content = content.replace(bad, good, 1)
open('en/projects.html','w').write(content)
print('en/projects.html updated. cards:', content.count('program-card'))
