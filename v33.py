#!/usr/bin/env python3
"""v33: featured research as a single horizontal line strip."""
import re

for f in ['index.html', 'en/index.html']:
    s = open(f).read()
    # wrap the research-feature block with a horizontal strip container
    old = '    <div class="research-feature reveal">\n'
    new = '    <div class="research-line reveal"><div class="accent-rail"></div><div class="research-feature">\n'
    assert old in s, f'{f}: feature open not found'
    s = s.replace(old, new, 1)
    tail_old = '    </div>\n  </div>\n</section>\n\n<!-- ================= PROGRAMS'
    tail_new = '    </div></div>\n  </div>\n</section>\n\n<!-- ================= PROGRAMS'
    assert tail_old in s, f'{f}: close not found'
    s = s.replace(tail_old, tail_new, 1)
    open(f, 'w').write(s)
    print(f, 'html ok')

css = open('style.css').read()
assert 'v33' not in css
strip = """
/* ================= v33: Featured research as a single horizontal line ================= */
.research-line{
  border-radius:20px;
  border:1px solid rgba(15,118,110,.14);
  box-shadow:0 2px 8px rgba(26,139,101,.06), 0 14px 30px rgba(26,139,101,.08);
  background:#fff;
  display:flex;
  align-items:stretch;
  overflow:hidden;
}
.research-line .accent-rail{
  flex:0 0 auto;
  width:8px;
  background:linear-gradient(to bottom, rgba(16,108,78,.9), rgba(184,227,209,.7));
}
.research-line .research-feature{
  flex:1 1 auto;
  padding:30px 34px;
  border-radius:0;
  box-shadow:none;
  border-right:none;
}
.research-line .research-header{margin-bottom:12px}
.research-line .research-feature h3{font-size:1.25rem;margin-bottom:8px}
.research-line .research-feature h4{margin-bottom:12px}
.research-line .research-feature p{margin-bottom:14px}
.research-line .research-meta{display:none}
.research-line .research-actions{gap:10px}
@media (max-width:900px){
  .research-line{flex-direction:column}
  .research-line .accent-rail{width:100%;height:8px}
  .research-line .research-feature{padding:24px 26px}
}
"""
css += strip
open('style.css', 'w').write(css)
print('css ok')
