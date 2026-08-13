#!/usr/bin/env python3
"""v35g: final 10px trim to eliminate last overflow."""
css = open('style.css').read()

old = """padding:.26rem .44rem;
  font-size:.66rem;
  gap:.28rem;"""
new = """padding:.24rem .42rem;
  font-size:.66rem;
  gap:.26rem;"""
assert old in css, 'chip base not found'
css = css.replace(old, new, 1)

open('style.css','w').write(css)
print('v35g applied')
