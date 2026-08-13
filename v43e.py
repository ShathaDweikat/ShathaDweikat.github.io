#!/usr/bin/env python3
"""v43e: verify card structure; should be exactly 2 cards."""
content = open('projects.html').read()
import re
cards = re.findall(r'<div class="program-card reveal">(.*?)</div>\n<div class="program-card reveal">|<div class="program-card reveal">(.*?)</div>', content, re.S)
print('cards found:', len(cards))
print('journey btn:', 'استكشف البرنامج' in content)
print('strategic btn:', 'قريبًا' in content)
print('grid:', content.count('<div class="program-grid">'))
