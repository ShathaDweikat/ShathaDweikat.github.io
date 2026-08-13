#!/usr/bin/env python3
"""v46f: directly remove stale card block in en/projects.html by scanning after '</div>' of second new card."""
lines = open('en/projects.html').read().split('\n')
# find position of 'Coming Soon' link of second new card
pos = None
for i, l in enumerate(lines):
    if l.strip() == '<a href="course-template.html" class="btn btn-outline">Coming Soon</a>':
        pos = i
        break
assert pos is not None
# after pos: </div> (card close), </div> (grid close) — then stale lines until the next '</div>' (container/section close)
# print what comes after
print(''.join(lines[pos:pos+22]), '\n---')

# Structure now: pos=101, 102: '</div>' card close, 103: '</div>' grid close, 104: '', 105-118: stale card, then '</div>' container.
# We want exactly: after new card close </div>, grid close </div>.
# Remove everything from index pos+2 (grid '</div>') that is stale, i.e., remove lines pos+1..up to but keeping one grid '</div>'.
# Simpler: find grid '</div>' at pos+1; then remove lines from pos+2 until the line before the 'Community Initiatives' section.
markers = ['Community Initiatives', '<h3>Community Initiatives</h3>']
end = None
for i in range(pos+2, len(lines)):
    if lines[i].strip() in markers or 'Community Initiatives' in lines[i]:
        end = i
        break
assert end is not None
print('removing', pos+2, 'to', end-1)
lines = lines[:pos+2] + lines[end:]
content = '\n'.join(lines)
# ensure single stray btn removed
content = content.replace('<a class="btn btn-primary" href="journey-of-change.html">Explore the Program</a>\n', '', 1)
open('en/projects.html','w').write(content)
print('cards:', content.count('program-card'))
