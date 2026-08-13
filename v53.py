#!/usr/bin/env python3
"""v53: Journey of Change card lost its primary button (v52b cut the last element).
Re-insert the button before each card's closing '</div>' after the meta block."""

for path, label, href, lang in [
    ('projects.html', 'استكشف البرنامج', 'journey-of-change.html', 'AR'),
    ('en/projects.html', 'Explore the Program', '../journey-of-change.html', 'EN')]:
    c = open(path).read()
    marker = '</div>\n<div class="program-meta">\n<span><i data-lucide="book-open"></i>Free Program</span>\n<span><i data-lucide="languages"></i>Arabic</span>\n</div>'
    i = c.find(marker)
    assert i != -1, f'{path}: marker not found'
    i += len(marker)
    # the card ends at the next '</div>' after marker
    end = c.find('</div>', i)
    insert = f'\n<a href="{href}" class="btn btn-primary">{label}</a>'
    c = c[:end] + insert + c[end:]
    assert c.count('<div') == c.count('</div>'), f'{path}: unbalanced'
    assert c.count('program-card') == 2, f'{path}: cards={c.count("program-card")}'
    print(f'{path} ({lang}): button restored, balanced, 2 cards')
    open(path, 'w').write(c)
