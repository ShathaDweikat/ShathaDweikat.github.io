#!/usr/bin/env python3
"""v33b: compress research line — hide tags & English title, tighten spacing."""
css = open('style.css').read()

old = """.research-line .research-header{margin-bottom:12px}
.research-line .research-feature h3{font-size:1.25rem;margin-bottom:8px}
.research-line .research-feature h4{margin-bottom:12px}
.research-line .research-feature p{margin-bottom:14px}
.research-line .research-meta{display:none}
.research-line .research-actions{gap:10px}"""

new = """.research-line .research-header{display:none}
.research-line .research-feature{
  display:flex;
  align-items:center;
  flex-wrap:wrap;
  gap:22px;
}
.research-line .research-feature h3{
  flex:1 1 420px;
  font-size:1.2rem;
  line-height:1.75;
  margin-bottom:0;
  min-width:0;
}
.research-line .research-feature h4{display:none}
.research-line .research-feature p{display:none}
.research-line .research-meta{display:none}
.research-line .research-actions{
  display:flex;
  flex:0 0 auto;
  gap:10px;
  align-items:center;
}
.research-line .research-actions .btn{padding:.7rem 1.3rem;font-size:.88rem;white-space:nowrap}"""

assert old in css
css = css.replace(old, new, 1)

# tighten main feature padding too
css = css.replace('padding:30px 34px !important;', 'padding:22px 26px !important;')

open('style.css','w').write(css)
print('compressed')
