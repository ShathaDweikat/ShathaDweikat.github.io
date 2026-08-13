#!/usr/bin/env python3
"""v46g: fix en/projects.html structure — restore missing </div> (grid close) and content-block div."""
content = open('en/projects.html').read()
content = content.replace('</div>\n<h3>Community Initiatives</h3>',
                          '</div>\n</div>\n<div class="content-block reveal" style="margin-top:40px">\n<h3>Community Initiatives</h3>', 1)
open('en/projects.html','w').write(content)
# validate structure
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.stack=[]; s.err=0
    def handle_starttag(s,t,a):
        if t in ('div','section','main','header','footer'): s.stack.append(t)
    def handle_endtag(s,t):
        if t in ('div','section','main','header','footer'):
            if s.stack and s.stack[-1]==t: s.stack.pop()
            else: s.err+=1
p=P(); p.feed(content)
print('errors:', p.err, 'endstack:', p.stack, 'cards:', content.count('program-card'))
