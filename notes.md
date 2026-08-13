# حالة v50-v51 — استعادة بطاقة رحلة التغيير

## الحالة الحالية
- journey-of-change.html + en/journey-of-change.html: تم استعادتها من git (قالب الدورة الخاص بالمستخدمة)
- projects.html AR و EN: إعادة بناء grid — 4 بطاقات (2 رحلة التغيير "متاح الآن" برابط journey-of-change.html + 2 التفكير الاستراتيجي "قيد التطوير" بزر قريبًا)

## المشكلة المتبقية في AR فقط (projects.html)
البنية الفعلية عند الأسطر 96-131:
- بطاقة 1 (التفكير الاستراتيجي): meta div يغلق عند 98، زر قريبًا 99، </div> 100 — ثم سطر إضافي: 101 زر قريبًا + 102 </div> (مكرر/عائم = div زائدة 1)
- بطاقة 2 (رحلة التغيير): صحيحة عند 103-126 (زر قريبًا 125 + </div> 126)
- 129: </div> إضافي آخر؟ في الحقيقة 127-129 أسطر فارغة + </div> (ناتج فائض من v51b)
إذن AR يحتاج إزالة السطرين 101-102 فقط (زر قريبًا مكرر + إغلاقه) ليصبح متوازنًا: 23/23.
- EN متوازن 23/23 ✓

## أوامر التنفيذ المتبقية
1. حذف السطرين 101-102 من projects.html AR (sed -i '101,102d')
2. التحقق: grep -c 'program-card' (يجب 4) و div balance 23/23
3. رفع: git add -A && commit "v51: restore journey-of-change cards in programs" && git push
4. تنظيف v51.py v51b.py
5. معاينة browser: localhost:8000/projects.html ثم تسليم

## تقنية
- server: python3 -m http.server 8000 في /home/ubuntu/site
- knowledge-hub: نظيفة ✓ (لا Journey ولا Research Insight)
- CSS style.css?v=41
