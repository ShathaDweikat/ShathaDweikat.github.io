#!/usr/bin/env python3
"""v42: add Featured Research section (from index.html) to research.html before footer, Arabic."""
sect = open('/tmp/sect_research.html').read().strip()
# strip id and section-level anchor links since this becomes a standalone page
sect = sect.replace('<section id="research" class="research-section cream-bg">',
                    '<section id="featured" class="research-section cream-bg">')

page = open('research.html').read()
footer = '<footer>'
assert footer in page
page = page.replace(footer, sect + '\n' + footer, 1)
open('research.html','w').write(page)
print('research.html updated')
