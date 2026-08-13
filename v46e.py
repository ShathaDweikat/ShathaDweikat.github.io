#!/usr/bin/env python3
"""v46e: remove remaining stale card and stray button in en/projects.html."""
lines = open('en/projects.html').read().split('\n')
out = []
i = 0
n = len(lines)
removed = 0
while i < n:
    l = lines[i]
    # stale card: starts with <span class="program-status">In Development</span> without icon first
    if (l.strip() == '<span class="program-status">In Development</span>' and
            i > 0 and 'tag-soon' not in lines[i-1] and lines[i-2] == '<div class="program-card reveal">'):
        # find its closing </div> at matching depth
        depth = 1
        j = i - 2  # start from the card open
        k = j + 1
        while k < n and depth > 0:
            if '<div ' in lines[k] and '<div class="program-card' not in lines[k]:
                depth += 1
            elif lines[k].strip() == '</div>':
                depth -= 1
            k += 1
        print('removing stale card lines', i-1, 'to', k)
        i = k
        removed += 1
        continue
    out.append(l)
    i += 1
# remove stray standalone btn (right after second card, before grid close)
out = [l for l in out if not (l.strip() == '<a class="btn btn-primary" href="journey-of-change.html">Explore the Program</a>')]
open('en/projects.html','w').write('\n'.join(out))
print('done. cards now:', '\n'.join(out).count('program-card'), 'removed:', removed)
