#!/usr/bin/env python3
"""v44: merge index.html library section (3 whatido-cards) into knowledge-hub.html AR above the resource grid."""
sect = open('/tmp/sect_library.html').read().strip()
# adjust: on this standalone page, links should stay; change self-link 'افتح المكتبة' remains fine.
page = open('knowledge-hub.html').read()
marker = '<section>\n<div class="container">\n<div class="resource-grid">'
assert marker in page, 'resource grid marker not found'
section_html = sect.replace('    ', '\n').replace('  ', '\n')
# simpler: indent sect content by one level (2 spaces) since page uses 0 indent
lines = sect.split('\n')
out_lines = ['<section id="knowledge-highlights" class="library-section bg-soft">']
for l in lines[1:]:
    out_lines.append('  ' + l if l.strip() else '')
out_lines.append('</section>')
section_html = '\n'.join(out_lines)
page = page.replace(marker, section_html + '\n' + marker, 1)
open('knowledge-hub.html','w').write(page)
print('knowledge-hub.html updated')
