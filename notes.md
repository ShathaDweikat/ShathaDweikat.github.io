# حالة v42-v49 — صفحات الأقسام المستقلة

## منجز بالكامل
- research.html + en/research.html: صفحات أبحاث كاملة مع Featured Research ✓
- projects.html + en/projects.html: بطاقات v31 للبرامج (رحلة التغيير/التفكير الاستراتيجي) + مبادرات مجتمعية ✓
- knowledge-hub.html + en/knowledge-hub.html: مكتبة مع قسم highlights ✓
- knowledge-hub: حُذفت بطاقة "رؤية بحثية/استكشف البحث" وبطاقة "رحلة التغيير — الدورة التدريبية" من AR و EN (v49, v49b) ✓
- index.html + en/index.html: أقسام research/programs/library → بطاقات whatido-grid مختصرة بروابط للصفحات ✓
- روابط nav: programs→projects.html, research→research.html, library→knowledge-hub.html, contact→index.html#contact ✓

## معاينة بعد v49
- knowledge-hub AR: تعمل — 3 بطاقات knowledge-highlights (بقيت LinkedIn/Research Insight... في الواقع حُذف Research Insight، بقي ملخص معرفي فقط في grid: 1+2 = 3) — OK.
- ملاحظة: knowledge-highlights grid فيه الآن بطاقة واحدة فقط (ملخص معرفي) + resource-grid فيه بطاقتان (CSR book + أدلة بحثية). يبدو جيدًا.

## المتبقي الوحيد
- رفع: git add -A && git commit -m "v49: standalone pages + library cleanup" && git push origin main
- تسليم النتيجة للمستخدم

## تقنية
- server: python3 -m http.server 8000 في /home/ubuntu/site
- CSS: style.css?v=41
