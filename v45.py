#!/usr/bin/env python3
"""v45: insert English Featured Research section into en/research.html before footer."""
sect = open('/tmp/en_sect_research.html').read().strip().split('\n')
out = ['<section id="featured" class="research-section cream-bg">']
for l in sect[1:]:
    out.append(l)
out.append('</section>')
section_html = '\n'.join(out)

page = open('en/research.html').read()
footer = '<footer>'
assert footer in page, 'footer not found in en/research.html'
page = page.replace(footer, section_html + '\n' + footer, 1)
open('en/research.html','w').write(page)
print('en/research.html updated')
