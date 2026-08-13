#!/usr/bin/env python3
"""v35e: final tweak so 6 chips fit within 750px (total 792 -> ~740)."""
css = open('style.css').read()

old = """padding:.28rem .52rem;
  font-size:.68rem;
  gap:.32rem;"""
new = """padding:.28rem .5rem;
  font-size:.68rem;
  gap:.3rem;"""
assert old in css, 'chip base not found'
css = css.replace(old, new, 1)

# hide scrollbar track on the interests row while keeping scroll capability
old2 = """.research-interests{
  display:flex;
  flex-wrap:nowrap;
  gap:.6rem;"""
new2 = """.research-interests{
  display:flex;
  flex-wrap:nowrap;
  gap:.6rem;
  scrollbar-width:none;
  padding-bottom:2px;
}
.research-interests::-webkit-scrollbar{display:none}"""
assert old2 in css, 'row base not found'
css = css.replace(old2, new2, 1)

open('style.css','w').write(css)
print('v35e applied')
