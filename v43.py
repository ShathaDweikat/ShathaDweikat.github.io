#!/usr/bin/env python3
"""v43: upgrade projects.html Arabic program cards to match the polished index.html version."""
page = open('projects.html').read()

old = """<div class="program-card reveal">
<span class="program-status">برنامج مجاني</span>
<div class="program-icon"><i data-lucide="compass"></i></div>
<h3>رحلة التغيير</h3>
<p>
رحلة تعليمية تدعم الوعي الذاتي، فهم مراحل التغيير، وبناء خطوات عملية نحو النمو الشخصي والتطور.
</p>
<div class="program-meta">
<span><i data-lucide="globe"></i>باللغة العربية</span>
<span><i data-lucide="badge-check"></i>متاح حالياً</span>
</div>
<a class="btn btn-primary" href="journey-of-change.html">استكشف البرنامج</a>
</div>
<div class="program-card reveal">
<span class="program-status">قيد التطوير</span>
<div class="program-icon"><i data-lucide="brain-circuit"></i></div>
<h3>أساسيات التفكير الاستراتيجي للشباب</h3>
<p>
برنامج تدريبي يطور التفكير الاستراتيجي لدى الشباب من خلال تحليل الذات، بناء الرؤية،
تحديد الأهداف، وتحويل الأفكار إلى خطوات قابلة للتنفيذ.
</p>
<div class="program-meta">
<span><i data-lucide="globe"></i>باللغة العربية</span>
<span><i data-lucide="clock"></i>قريباً</span>
</div>
<a class="btn btn-outline" href="course-template.html">قالب الدورة</a>
</div>"""
new = """<div class="program-card reveal">
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
</div>"""
assert old in page, 'old program cards not found'
page = page.replace(old, new, 1)

# remove the stale template hint button
old_btn = '<div class="container" style="text-align:center;margin:2rem 0 1rem"><a href="course-template.html" class="btn btn-outline" style="font-size:.85rem;padding:10px 24px"><i data-lucide="layout-template"></i>قالب صفحة دورة جاهز</a></div>'
if old_btn in page:
    page = page.replace(old_btn+'\n', '', 1)

open('projects.html','w').write(page)
print('projects.html updated')
