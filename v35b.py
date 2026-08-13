#!/usr/bin/env python3
"""v35b: shrink research-interests chips so all 6 fit one line without scrolling."""
css = open('style.css').read()

old = """.research-interest{display:inline-flex;align-items:center;gap:.45rem;background:#fff;border:1px solid rgba(15,118,110,.18);border-radius:999px;padding:.5rem 1rem;font-size:.88rem;font-weight:600;color:var(--emerald-dark);box-shadow:0 4px 10px rgba(17,94,89,.05)}"""
new = """.research-interest{
  display:inline-flex;
  align-items:center;
  gap:.4rem;
  background:#fff;
  border:1px solid rgba(15,118,110,.18);
  border-radius:999px;
  padding:.4rem .85rem;
  font-size:.8rem;
  font-weight:600;
  color:var(--emerald-dark);
  box-shadow:0 4px 10px rgba(17,94,89,.05);
  white-space:nowrap;
  flex:0 0 auto;
}"""
assert old in css, 'research-interest base not found'
css = css.replace(old, new, 1)

# In the research line: make chips row wrap-friendly but stay on one line
old2 = """.research-section .research-interests{justify-content:center}"""
new2 = """.research-section .research-interests{justify-content:center}
@media (max-width:1100px){
  .research-interests{flex-wrap:wrap}
}"""
assert old2 in css
css = css.replace(old2, new2, 1)

open('style.css','w').write(css)
print('v35b applied')
