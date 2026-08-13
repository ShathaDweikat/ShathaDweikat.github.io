#!/usr/bin/env python3
"""v32: show the about cover fully (no top/bottom cropping). Line-based replace."""

lines = open('style.css').read().split('\n')
start = None
for i, l in enumerate(lines):
    if l.strip() == '.about-cover{':
        start = i
        break
assert start is not None
end = start
while '}' not in lines[end]:
    end += 1

new_lines = [
    '/* ================= v32: About Page Cover (full band, no cropping) ================= */',
    '.about-cover{',
    'position:relative;',
    'width:100%;',
    'overflow:hidden;',
    'animation:coverIn .9s cubic-bezier(.22,.61,.36,1) both;',
    '}',
]

# img rule right after the first closing brace
img_start = end + 1
img_end = img_start
while '}' not in lines[img_end]:
    img_end += 1

img_new = [
    '.about-cover img{',
    'width:100%;',
    'max-width:1600px;',
    'height:auto;',
    'display:block;',
    'margin:0 auto;',
    '}',
]

before = lines[:start]
middle = lines[end+1:img_start]
after = lines[img_end+1:]
lines = before + new_lines + middle + img_new + after
open('style.css', 'w').write('\n'.join(lines))
print('cover updated')
