#!/usr/bin/env python3
"""v44b: insert library section from index into knowledge-hub.html before resource-grid."""
sect = open('/tmp/sect_library.html').read().strip().split('\n')
# build section with 0-indent (matching page style)
out = ['<section id="knowledge-highlights" class="library-section bg-soft">']
for l in sect[1:]:
    out.append(l)
out.append('</section>')
section_html = '\n'.join(out)

page = open('knowledge-hub.html').read()
marker = '<div class="resource-grid">'
assert marker in page
page = page.replace(marker, section_html + '\n' + marker, 1)
open('knowledge-hub.html','w').write(page)
print('knowledge-hub.html updated')
