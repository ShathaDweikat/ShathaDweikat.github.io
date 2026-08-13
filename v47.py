#!/usr/bin/env python3
"""v47: insert English Knowledge & Analysis section into en/knowledge-hub.html before resource-grid."""
sect = open('/tmp/en_sect_library.html').read().strip().split('\n')
out = ['<section id="knowledge-highlights" class="library-section bg-soft">']
for l in sect[1:]:
    out.append(l)
out.append('</section>')
section_html = '\n'.join(out)

page = open('en/knowledge-hub.html').read()
marker = '<div class="resource-grid">'
assert marker in page
page = page.replace(marker, section_html + '\n' + marker, 1)
open('en/knowledge-hub.html','w').write(page)
print('en/knowledge-hub.html updated')
