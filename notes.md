# تشخيص ترتيب أزرار التواصل (v55)

المستخدم: "آخر الصفحة الرئيسيه عند المربعات الصغار يلي تحت بالابيض يلي عند البريد الالكتروني ولنكدان خليهم جنب بعش في واحند تحتهم منظره مو لطيف"

الفحص البصري (screenshot من localhost:8000/index.html):
- قسم contact (.contact-section): شارات contact-areas (4 شارات) موزعة على صفين (3+1) بسبب grid auto-fit minmax(190px,1fr) — "التعاون البحثي/تطوير البرامج/المشاريع المعرفية" سطر أول و"مبادرات الأثر الاجتماعي" سطر ثاني. منظره مو لطيف.
- contact-buttons: زر البريد و LinkedIn هما جنب بعض فعلاً (display:flex, gap:18px) — ليسوا المشكلة.
- إذن المشكلة: شارات contact-areas الأربعة تنكسر لصفين — يجب أن تكون في سطر واحد.

الحل:
1. contact-areas: grid-template-columns: repeat(4, 1fr) desktop (بدلاً من auto-fit) و repeat(2,1fr) على الموبايل
2. التأكد أن الشارات لا تنكسر (white-space:nowrap إذا لزم)
3. تنطبق AR (index.html) و EN (en/index.html) — نفس البنية

ملفات:
- /home/ubuntu/site/style.css: قاعدة 3288 .contact-areas
- index.html / en/index.html: contact-areas div (سطر 293)
