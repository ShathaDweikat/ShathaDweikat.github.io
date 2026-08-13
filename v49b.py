#!/usr/bin/env python3
"""v49b: remove 'Research Insight' card and 'Journey of Change — Training Course' card from en/knowledge-hub.html."""
import re
content = open('en/knowledge-hub.html').read()

# 1) remove whatido-card Research Insight (links to research.html / ../research.html)
block1 = content.find('<section id="knowledge-highlights"')
end1 = content.find('</section>', block1)
section = content[block1:end1]
card1 = re.search(r'<div class="whatido-card">.*?Explore the Research', section, re.S)
if card1:
    # extend to the closing </div> of the card
    card_html = card1.group(0)
    depth = card_html.count('<div') - card_html.count('</div>')
    rest = section[card1.end():]
    i = 0
    while depth > 0:
        if rest[i:i+4] == '<div':
            depth += 1
        elif rest[i:i+6] == '</div>':
            depth -= 1
        i += 1
    section = section[:card1.start()] + rest[i:]
    print('removed Research Insight card EN')
content = content[:block1] + section + content[end1:]

# 2) remove resource-card Journey of Change — Training Course
card2 = re.search(r'<div class="resource-card reveal">\s*<div class="resource-icon"><i data-lucide="compass"></i></div>\s*<h3>Journey of Change — Training Course</h3>.*?</div>\s*', content, re.S)
if card2:
    content = content[:card2.start()] + content[card2.end():]
    print('removed Journey of Change card EN')
else:
    print('EN journey card not matched verbatim')

open('en/knowledge-hub.html','w').write(content)
cards = len(re.findall(r'class="resource-card reveal"', content))
print('en/knowledge-hub.html updated. resource cards:', cards)
