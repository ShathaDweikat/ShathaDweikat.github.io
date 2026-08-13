#!/usr/bin/env python3
"""v35d: shrink interest chips further so 6 fit one line in ~750px."""
css = open('style.css').read()

old = """padding:.32rem .62rem;
  font-size:.74rem;"""
new = """padding:.28rem .52rem;
  font-size:.68rem;
  gap:.32rem;"""
assert old in css, 'chip base not found'
css = css.replace(old, new, 1)

old2 = """.research-interest i{width:16px;height:16px;color:var(--emerald)}"""
new2 = """.research-interest i{width:14px;height:14px;color:var(--emerald);flex:none}"""
assert old2 in css, 'chip icon not found'
css = css.replace(old2, new2, 1)

open('style.css','w').write(css)
print('v35d applied')
