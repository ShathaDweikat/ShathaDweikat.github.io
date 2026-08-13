#!/usr/bin/env python3
"""v43f: rebuild the missing Journey of Change card. Current grid has only a stray button + strategic card."""
content = open('projects.html').read()

bad = '''<div class="program-grid">
<a href="journey-of-change.html" class="btn btn-primary">استكشف البرنامج</a>
</div>'''
good = '''<div class="program-grid">
<div class="program-card reveal">
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
</div>
</div>'''
assert bad in content, 'bad grid not found'
content = content.replace(bad, good, 1)
# remove the now-duplicated strategic card that comes after
dup = '''<div class="program-card reveal">
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
</div>
</div>'''
# after replacement there is one extra closing </div> and duplicate card
idx1 = content.find(good)
rest = content[idx1+len(good):]
# rest starts with duplicated card + extra </div>
assert rest.startswith(dup), 'dup not found'
content = content[:idx1+len(good)] + rest[len(dup):]
open('projects.html','w').write(content)
print('fixed. cards:', content.count('<div class="program-card reveal">'))
