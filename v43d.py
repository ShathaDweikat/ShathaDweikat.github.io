#!/usr/bin/env python3
"""v43d: remove the remaining broken card fragment in projects.html."""
lines = open('projects.html').read().split('\n')
out = []
skip = False
depth = 0
i = 0
n = len(lines)
while i < n:
    l = lines[i]
    if '<div class="program-card reveal">' in l and 'أساسيات التفكير الاستراتيجي<br>' not in ''.join(lines[i:i+8]):
        # second/broken card starts here (without <h3> containing <br> en name)
        # count its div depth
        j = i
        while j < n and not (lines[j].strip() == '</div>'):
            j += 1
        # skip from i to j inclusive (broken card)
        i = j + 1
        continue
    out.append(l)
    i += 1

open('projects.html','w').write('\n'.join(out))
# verify
content = open('projects.html').read()
print('broken card removed:', 'برنامج تدريبي يطور التفكير' not in content)
print('grid count:', content.count('<div class="program-grid">'))
print('card count:', content.count('program-card'))
