#!/usr/bin/env python3
"""v35: research-interests as a single horizontal row inside the research line."""
css = open('style.css').read()

old = """.research-interests{display:flex;flex-wrap:wrap;gap:.7rem;margin-top:1.4rem}"""
new = """.research-interests{
  display:flex;
  flex-wrap:nowrap;
  gap:.6rem;
  margin-top:1rem;
  justify-content:flex-start;
  align-items:center;
  overflow-x:auto;
}
.research-interest{white-space:nowrap;flex:0 0 auto}
.research-section .research-interests{justify-content:center}
@media (max-width:768px){
  .research-interests{flex-wrap:wrap;justify-content:center}
}"""
assert old in css, 'research-interests not found'
css = css.replace(old, new, 1)

open('style.css','w').write(css)

# bump css version to 35 in all HTML
import glob
for f in glob.glob('/home/ubuntu/site/**/*.html', recursive=True):
    s = open(f).read()
    if 'style.css?v=' in s:
        s2 = s.replace('style.css?v=34', 'style.css?v=35')
        open(f,'w').write(s2)

print('v35 applied')
