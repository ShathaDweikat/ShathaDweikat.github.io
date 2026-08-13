#!/usr/bin/env python3
"""v35f: shrink ~42px more so chips fit fully (768 scroll -> <750)."""
css = open('style.css').read()

old = """padding:.28rem .5rem;
  font-size:.68rem;
  gap:.3rem;"""
new = """padding:.26rem .44rem;
  font-size:.66rem;
  gap:.28rem;"""
assert old in css, 'chip base not found'
css = css.replace(old, new, 1)

old2 = """.research-interest i{width:14px;height:14px;color:var(--emerald);flex:none}"""
new2 = """.research-interest i{width:13px;height:13px;color:var(--emerald);flex:none}"""
assert old2 in css, 'chip icon not found'
css = css.replace(old2, new2, 1)

open('style.css','w').write(css)
print('v35f applied')
