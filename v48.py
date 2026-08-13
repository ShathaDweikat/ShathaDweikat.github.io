#!/usr/bin/env python3
"""v48: convert research, programs, library sections in index.html (AR & EN) into compact teaser cards
that link to the new standalone pages, keeping the 'What I Do' emerald section untouched."""

def make_card(icon, label_en, label_ar, desc, btn_label, href):
    return f'''<div class="whatido-card">
        <i data-lucide="{icon}"></i>
        <h3>{label_ar}<br><span>{label_en}</span></h3>
        <p>{desc}</p>
        <a href="{href}" class="resource-link">{btn_label}<i data-lucide="arrow-left"></i></a>
      </div>'''

# ---------- Arabic ----------
ar = open('index.html').read()

# Research teaser (replace whole research section, lines ~191-237)
ar_research_new = '''<section id="research" class="research-section cream-bg">
  <div class="container">
    <div class="section-heading reveal">
      <span class="section-label"><i data-lucide="file-text"></i>Featured Research</span>
      <h2>أبرز الأبحاث</h2>
      <p>أبحاث تستكشف الإنسان والمؤسسات والظروف التي تصنع التنمية المستدامة.</p>
    </div>
    <div class="whatido-grid reveal">
      ''' + make_card('landmark', 'Higher Education Governance', 'إعادة تشكيل الحوكمة الجامعية',
      'دراسة تحليلية حول حوكمة التعليم العالي الفلسطيني والمرونة المؤسسية في مواجهة الأزمات المركبة.',
      'قراءة الملخص', 'research.html') + '''
      ''' + make_card('file-search', 'Explore All Research', 'استكشف جميع الأبحاث',
      'مجالاتي البحثية: التمكين الاجتماعي، التنمية المجتمعية، المسؤولية المجتمعية والاستدامة، المرونة المؤسسية، والحوكمة.',
      'عرض الأبحاث', 'research.html') + '''
    </div>
  </div>
</section>'''

s = ar.find('<section id="research"')
e = ar.find('<!-- ================= PROGRAMS ================= -->')
assert s != -1 and e != -1
ar = ar[:s] + ar_research_new + '\n' + ar[e:]

# Programs teaser (replace programs section, lines ~238-274)
ar_programs_new = '''<section id="programs" class="programs-section">
  <div class="container">
    <div class="section-heading reveal">
      <span class="section-label"><i data-lucide="graduation-cap"></i>Learning &amp; Programs</span>
      <h2>مساحات للتعلم والنمو</h2>
      <p>خلق مساحات للتعلم والتأمل وبناء القدرات.</p>
    </div>
    <div class="whatido-grid reveal">
      ''' + make_card('route', 'Journey of Change', 'رحلة التغيير',
      'برنامج تعليمي مجاني يركز على الوعي الذاتي وفهم التغيير والنمو الشخصي.',
      'استكشف البرنامج', 'projects.html') + '''
      ''' + make_card('compass', 'Strategic Thinking', 'التفكير الاستراتيجي',
      'برنامج قيد التطوير يركز على بناء أساسيات التفكير الاستراتيجي وتحويل الأهداف إلى خطوات عملية — قريبًا.',
      'قريبًا', 'projects.html') + '''
    </div>
  </div>
</section>'''
s = ar.find('<section id="programs"')
e = ar.find('<!-- ================= KNOWLEDGE & ANALYSIS ================= -->')
assert s != -1 and e != -1
ar = ar[:s] + ar_programs_new + '\n' + ar[e:]

# Library teaser (replace library section, lines ~275-305)
ar_library_new = '''<section id="library" class="library-section bg-soft">
  <div class="container">
    <div class="section-heading reveal">
      <span class="section-label"><i data-lucide="pen-line"></i>المعرفة والتحليل</span>
      <h2>المعرفة والتحليل</h2>
      <p>قراءات مختارة، تحليلات، وموارد معرفية حول التنمية الاجتماعية والاستدامة والأثر الاجتماعي.</p>
    </div>
    <div class="whatido-grid reveal">
      ''' + make_card('pen-line', 'Latest Article', 'أحدث المقالات',
      'تحليلاتي وقراءاتي حول المسؤولية المجتمعية والتنمية المستدامة على LinkedIn.',
      'اقرأ على LinkedIn', 'https://www.linkedin.com/in/shatha-dweikat/') + '''
      ''' + make_card('library', 'Knowledge Hub', 'مكتبة المعرفة',
      'كتب وأدلة بحثية وموارد تعليمية في المسؤولية المجتمعية والتنمية المستدامة والحوكمة.',
      'افتح المكتبة', 'knowledge-hub.html') + '''
    </div>
  </div>
</section>'''
s = ar.find('<section id="library"')
e = ar.find('<!-- ================= FROM KNOWLEDGE TO IMPACT ================= -->')
assert s != -1 and e != -1
ar = ar[:s] + ar_library_new + '\n' + ar[e:]

open('index.html','w').write(ar)
print('index.html updated')

# ---------- English ----------
en = open('en/index.html').read()

en_research_new = '''<section id="research" class="research-section cream-bg">
  <div class="container">
    <div class="section-heading reveal">
      <span class="section-label"><i data-lucide="file-text"></i>Featured Research</span>
      <h2>Featured Research</h2>
      <p>Research that explores people, institutions, and the conditions that shape sustainable development.</p>
    </div>
    <div class="whatido-grid reveal">
      ''' + make_card('landmark', 'Higher Education Governance', 'Reshaping University Governance',
      'An analytical study of Palestinian higher education governance and institutional resilience in facing compound crises.',
      'Read the Abstract', 'research.html') + '''
      ''' + make_card('file-search', 'Explore All Research', 'Explore All Research',
      'My research interests: social empowerment, community development, CSR &amp; sustainability, institutional resilience, and governance.',
      'View Research', 'research.html') + '''
    </div>
  </div>
</section>'''
s = en.find('<section id="research"')
e = en.find('PROGRAMS', s)
# find the comment line
while e != -1 and not en[e-20:e+60].strip().startswith('<!--'):
    e = en.find('PROGRAMS', e+1)
assert s != -1 and e != -1
en = en[:s] + en_research_new + '\n' + en[e:]

en_programs_new = '''<section id="programs" class="programs-section">
  <div class="container">
    <div class="section-heading reveal">
      <span class="section-label"><i data-lucide="graduation-cap"></i>Learning &amp; Programs</span>
      <h2>Learning &amp; Growth Spaces</h2>
      <p>Creating spaces for learning, reflection, and capacity building.</p>
    </div>
    <div class="whatido-grid reveal">
      ''' + make_card('route', 'Journey of Change', 'Journey of Change',
      'A free educational program focused on self-awareness, understanding change, and personal growth.',
      'Explore the Program', 'projects.html') + '''
      ''' + make_card('compass', 'Strategic Thinking', 'Strategic Thinking',
      'A program in development focused on building the fundamentals of strategic thinking — coming soon.',
      'Coming Soon', 'projects.html') + '''
    </div>
  </div>
</section>'''
s = en.find('<section id="programs"')
e = en.find('KNOWLEDGE', s)
while e != -1 and not en[e-20:e+60].strip().startswith('<!--'):
    e = en.find('KNOWLEDGE', e+1)
assert s != -1 and e != -1
en = en[:s] + en_programs_new + '\n' + en[e:]

en_library_new = '''<section id="library" class="library-section bg-soft">
  <div class="container">
    <div class="section-heading reveal">
      <span class="section-label"><i data-lucide="pen-line"></i>Knowledge &amp; Analysis</span>
      <h2>Knowledge &amp; Analysis</h2>
      <p>Selected reflections, analyses, and knowledge resources on social development, sustainability, and social impact.</p>
    </div>
    <div class="whatido-grid reveal">
      ''' + make_card('pen-line', 'Latest Article', 'Latest Article',
      'My analyses and readings on CSR and sustainable development on LinkedIn.',
      'Read on LinkedIn', 'https://www.linkedin.com/in/shatha-dweikat/') + '''
      ''' + make_card('library', 'Knowledge Hub', 'Knowledge Hub',
      'Books, research guides, and educational resources on CSR, sustainable development, and governance.',
      'Open the Library', 'knowledge-hub.html') + '''
    </div>
  </div>
</section>'''
s = en.find('<section id="library"')
e = en.find('IMPACT', s)
while e != -1 and not en[e-20:e+60].strip().startswith('<!--'):
    e = en.find('IMPACT', e+1)
assert s != -1 and e != -1
en = en[:s] + en_library_new + '\n' + en[e:]

open('en/index.html','w').write(en)
print('en/index.html updated')
