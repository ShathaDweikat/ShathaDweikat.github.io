#!/usr/bin/env python3
"""v43c: remove leftover old card and stray lines in projects.html."""
lines = open('projects.html').read().split('\n')

# Remove the stale card lines (after 'قريبًا' card) and stray button
to_remove_markers = ['قالب الدورة', 'أساسيات التفكير الاستراتيجي للشباب', 'by-lucide="brain-circuit"']
out = []
i = 0
while i < len(lines):
    l = lines[i]
    if 'قالب الدورة' in l or 'أساسيات التفكير الاستراتيجي للشباب' in l:
        # remove from '<a class="btn btn-outline"...' (line before 'قالب الدورة')
        if i > 0 and 'قالب الدورة' in l:
            out.pop()  # drop preceding line if not a card div
        i += 1
        continue
    if l.strip() == '<div class="program-icon"><i data-lucide="brain-circuit"></i></div>':
        i += 1
        continue
    if l.strip() == '<span class="program-status">قيد التطوير</span>' and i+1 < len(lines) and 'أساسيات' in lines[i+1]:
        i += 1
        continue
    out.append(l)
    i += 1
# drop stray standalone btn (not inside card) — the one after ً tag
out = [l for l in out if not (l.strip().startswith('<a class="btn btn-primary" href="journey-of-change.html">استكشف البرنامج</a>') and ('program-card' not in ''.join(out[-15:])))]

open('projects.html','w').write('\n'.join(out))
print('cleaned, lines:', len(out))
