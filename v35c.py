#!/usr/bin/env python3
"""v35c: reduce interest chip font/padding so 6 fit in ~750px row."""
css = open('style.css').read()

old = """padding:.4rem .85rem;
  font-size:.8rem;"""
new = """padding:.32rem .62rem;
  font-size:.74rem;"""
assert old in css, 'chip padding not found'
css = css.replace(old, new, 1)

open('style.css','w').write(css)

import glob
for f in glob.glob('/home/ubuntu/site/**/*.html', recursive=True):
    s = open(f).read()
    if 'style.css?v=' in s:
        s2 = s.replace('style.css?v=36', 'style.css?v=37')
        open(f,'w').write(s2)
print('v35c applied')
