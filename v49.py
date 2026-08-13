#!/usr/bin/env python3
"""v49: remove 'Research Insight' card (research.html link) and 'Journey of Change — الدورة التدريبية' card from knowledge-hub.html AR."""
content = open('knowledge-hub.html').read()

# 1) remove the whatido-card that links to research.html (Research Insight)
block1 = content.find('<section id="knowledge-highlights"')
end1 = content.find('</section>', block1)
section = content[block1:end1]
import re
card1 = re.search(r'<div class="whatido-card">.*?استكشف البحث<i data-lucide="arrow-left"></i></a>\s*</div>', section, re.S)
if card1:
    print('removing Research Insight card (pos in section:', card1.start(), ')')
    section = section[:card1.start()] + section[card1.end():]
content = content[:block1] + section + content[end1:]

# 2) remove the resource-card for Journey of Change course
card2 = re.search(r'<div class="resource-card reveal">\s*<div class="resource-icon"><i data-lucide="compass"></i></div>\s*<h3>رحلة التغيير — الدورة التدريبية</h3>.*?</div>\s*', content, re.S)
if card2:
    print('removing Journey of Change card:', repr(content[card2.start():card2.start()+80]))
    content = content[:card2.start()] + content[card2.end():]
else:
    print('journey card not matched verbatim; searching...')
    i = content.find('رحلة التغيير — الدورة التدريبية')
    print('found at', i)

open('knowledge-hub.html','w').write(content)
cards = len(re.findall(r'class="whatido-card"', content)) + len(re.findall(r'class="resource-card reveal"', content))
print('knowledge-hub.html updated. resource cards:', cards)
