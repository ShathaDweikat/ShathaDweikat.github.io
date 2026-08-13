#!/usr/bin/env python3
"""v34: What I Do cards -> rich emerald gradient with light text."""
css = open('style.css').read()

old = """.whatido-card{
background:linear-gradient(155deg,#e4f3ea 0%,rgba(184,227,209,.75) 100%);
border:1px solid rgba(15,118,110,.18);
border-radius:18px;
padding:1.6rem 1.3rem;
text-align:center;
box-shadow:0 10px 24px rgba(17,94,89,.08), inset 0 0 0 1px rgba(255,255,255,.6);
transition:transform .3s ease, box-shadow .3s ease, background .3s ease;
}
.whatido-card:hover{
transform:translateY(-6px);
background:linear-gradient(155deg,#d6eee1 0%,rgba(167,218,197,.9) 100%);
box-shadow:0 18px 36px rgba(17,94,89,.14);
}
.whatido-card i{
width:34px;
height:34px;
color:var(--emerald);
margin:0 auto 1rem;
}
.whatido-card h3{
font-family:var(--heading);
font-size:1.05rem;
font-weight:700;
color:var(--charcoal);
line-height:1.7;
}
.whatido-card h3 span{
font-size:.85rem;
font-weight:600;
color:var(--emerald);
letter-spacing:.3px;
}
.whatido-card p{
margin-top:.7rem;
font-size:.9rem;
color:#4a5568;
line-height:1.75;
}"""

new = """.whatido-card{
background:linear-gradient(155deg,#0f766e 0%,#10866c 55%,rgba(28,110,95,.92) 100%);
border:1px solid rgba(255,255,255,.16);
border-radius:18px;
padding:1.7rem 1.3rem;
text-align:center;
position:relative;
overflow:hidden;
box-shadow:0 10px 24px rgba(17,94,89,.22), inset 0 1px 0 rgba(255,255,255,.22);
transition:transform .35s ease, box-shadow .35s ease, background .35s ease;
}
.whatido-card::after{
content:"";
position:absolute;
inset:0;
background:radial-gradient(65% 55% at 75% 0%,rgba(255,255,255,.16) 0%,transparent 70%);
pointer-events:none;
}
.whatido-card:hover{
transform:translateY(-6px);
background:linear-gradient(155deg,#0d847a 0%,#119879 55%,rgba(30,120,103,.95) 100%);
box-shadow:0 20px 40px rgba(17,94,89,.30), inset 0 1px 0 rgba(255,255,255,.28);
}
.whatido-card i{
width:34px;
height:34px;
color:#e6f2ec;
margin:0 auto 1rem;
position:relative;
z-index:1;
}
.whatido-card h3{
font-family:var(--heading);
font-size:1.05rem;
font-weight:700;
color:#ffffff;
line-height:1.7;
position:relative;
z-index:1;
}
.whatido-card h3 span{
font-size:.85rem;
font-weight:600;
color:rgba(205,240,222,.92);
letter-spacing:.3px;
}
.whatido-card p{
margin-top:.7rem;
font-size:.9rem;
color:rgba(225,243,234,.88);
line-height:1.75;
position:relative;
z-index:1;
}"""

assert old in css, 'whatido-card base not found'
css = css.replace(old, new, 1)

# also update the dark-mode block references if they override background
css = css.replace(
    """.whatido-card,
.box-shadow-hover,
.cert-item,
.learn-item,""",
    """.whatido-card,
.box-shadow-hover,
.cert-item,
.learn-item,""", 1)  # no-op guard

open('style.css','w').write(css)

# bump css version to 34 in all HTML
import glob
for f in glob.glob('/home/ubuntu/site/**/*.html', recursive=True):
    s = open(f).read()
    if 'style.css?v=' in s:
        s2 = s.replace('style.css?v=33', 'style.css?v=34')
        open(f,'w').write(s2)

print('v34 applied')
