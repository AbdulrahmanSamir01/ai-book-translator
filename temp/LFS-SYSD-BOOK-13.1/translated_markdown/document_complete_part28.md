# 7.7. Gettext-1.0

تحتوي حزمة Gettext على أدوات مخصصة لعمليات التدويل (Internationalization) والتوطين (Localization). تتيح هذه الأدوات تجميع البرامج مع دعم اللغات الأصلية (NLS)، مما يمكنها من إخراج الرسائل بلغة المستخدم الأصلية.

**وقت البناء التقريبي:**
1.5 SBU
**مساحة القرص المطلوبة:**
531 ميجابايت

## 7.7.1. تثبيت Gettext

بالنسبة لمجموعة أدواتنا المؤقتة، نحتاج فقط إلى تثبيت ثلاثة برامج من Gettext.

قم بتهيئة Gettext للتجميع:

**./configure --disable-shared**

**معنى خيار التهيئة:**

--disable-shared

لا نحتاج إلى تثبيت أي من مكتبات Gettext المشتركة في الوقت الحالي، لذا لا داعي لبنائها.

قم بتجميع الحزمة:

**make**

**تثبيت برامج msgfmt و msgmerge و xgettext:**

**cp -v gettext-tools/src/{msgfmt,msgmerge,xgettext} /usr/bin**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.36.2، "محتويات Gettext".

---

Linux From Scratch - Version 13.1-systemd

# 7.8. Bison-3.8.2

تحتوي حزمة Bison على مولد محلل لغوي (Parser Generator).

**وقت البناء التقريبي:**
0.2 SBU
**مساحة القرص المطلوبة:**
58 ميجابايت

## 7.8.1. تثبيت Bison

قم بتهيئة Bison للتجميع:

**./configure --prefix=/usr \**
**--docdir=/usr/share/doc/bison-3.8.2**

**معنى خيار التهيئة الجديد:**

--docdir=/usr/share/doc/bison-3.8.2

يوجه هذا الخيار نظام البناء لتثبيت وثائق Bison في دليل يحمل رقم الإصدار.

قم بتجميع الحزمة:

**make**

تثبيت الحزمة:

**make install**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.37.2، "محتويات Bison".

---

Linux From Scratch - Version 13.1-systemd

# 7.9. Perl-5.44.0

تحتوي حزمة Perl على لغة الاستخراج والتقارير العملية (Practical Extraction and Report Language).

**وقت البناء التقريبي:**
0.6 SBU
**مساحة القرص المطلوبة:**
301 ميجابايت

## 7.9.1. تثبيت Perl

قم بتهيئة Perl للتجميع:

**sh Configure -des                                         \**
**-D prefix=/usr                               \**
**-D vendorprefix=/usr                         \**
**-D useshrplib                                \**
**-D privlib=/usr/lib/perl5/5.44/core_perl     \**
**-D archlib=/usr/lib/perl5/5.44/core_perl     \**
**-D sitelib=/usr/lib/perl5/5.44/site_perl     \**
**-D sitearch=/usr/lib/perl5/5.44/site_perl    \**
**-D vendorlib=/usr/lib/perl5/5.44/vendor_perl \**
**-D vendorarch=/usr/lib/perl5/5.44/vendor_perl**

**معنى خيارات التهيئة (Configure):**

-des

هذا مزيج من ثلاثة خيارات: `-d` يستخدم القيم الافتراضية لجميع العناصر؛ `-e` يضمن إتمام جميع المهام؛ `-s` يكتم المخرجات غير الأساسية.

-D vendorprefix=/usr

**يضمن هذا الخيار معرفة Perl بكيفية إخبار الحزم بمكان تثبيت وحدات Perl الخاصة بها.**

-D useshrplib

بناء `libperl` المطلوبة لبعض وحدات Perl كمكتبة مشتركة بدلاً من مكتبة استاتيكية.

-D privlib,-D archlib,-D sitelib,...

تحدد هذه الإعدادات الأماكن التي يبحث فيها Perl عن الوحدات المثبتة. اختار محررو LFS وضعها في هيكل أدلة يعتمد على الإصدار الرئيسي والفرعي لـ Perl (5.44)، مما يسمح بترقية Perl إلى مستويات تصحيحية أحدث (مستوى التصحيح هو الجزء الأخير المفصول بنقطة في سلسلة الإصدار الكاملة مثل 5.44.0) دون الحاجة إلى إعادة تثبيت جميع الوحدات.

قم بتجميع الحزمة:

**make**

تثبيت الحزمة:

**make install**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.46.2، "محتويات Perl".

---

Linux From Scratch - Version 13.1-systemd

# 7.10. Zlib-1.3.2

تحتوي حزمة Zlib على روتينات الضغط وفك الضغط التي تستخدمها بعض البرامج.

**وقت البناء التقريبي:**
أقل من 0.1 SBU
**مساحة القرص المطلوبة:**
5.7 ميجابايت

## 7.10.1. تثبيت Zlib

قم بتهيئة Zlib للتجميع:

**./configure --prefix=/usr**

قم بتجميع الحزمة:

**make**

تثبيت الحزمة:

**make install**

حذف مكتبة استاتيكية غير ضرورية:

**rm -fv /usr/lib/libz.a**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.6.2، "محتويات Zlib".

---

Linux From Scratch - Version 13.1-systemd

# 7.11. mpdecimal-4.0.1

تحتوي حزمة mpdecimal على مكتبات C/C++ سريعة للحسابات العشرية ذات الفاصلة العائمة وبدقة عشوائية مقربة بشكل صحيح.

**وقت البناء التقريبي:**
أقل من 0.1 SBU
**مساحة القرص المطلوبة:**
3.3 ميجابايت

## 7.11.1. تثبيت mpdecimal

قم بتهيئة mpdecimal للتجميع:

**./configure --prefix=/usr    \**
**--disable-static \**
**--docdir=/usr/share/doc/mpdecimal-4.0.1**

قم بتجميع الحزمة:

**make**

تثبيت الحزمة:

**make install**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.53.2، "محتويات mpdecimal".

---

Linux From Scratch - Version 13.1-systemd

# 7.12. Python-3.14.7

تحتوي حزمة Python 3 على بيئة تطوير بايثون. وهي مفيدة للبرمجة كائنية التوجه، وكتابة السكربتات، وبناء النماذج الأولية للبرامج الكبيرة، وتطوير تطبيقات كاملة. بايثون هي لغة برمجة مفسرة.

**وقت البناء التقريبي:**
0.5 SBU
**مساحة القرص المطلوبة:**
603 ميجابايت

## 7.12.1. تثبيت Python

### ملاحظة

هناك ملفان لحزم يبدأ اسمهما ببادئة "python". الملف الذي يجب استخراجه هو `Python-3.14.7.tar.xz` (لاحظ الحرف الأول الكبير).

قم بتهيئة Python للتجميع:

**./configure --prefix=/usr       \**
**--enable-shared     \**
**--without-ensurepip \**
**--without-static-libpython**

**معنى خيارات التهيئة:**

--enable-shared

يمنع هذا المفتاح تثبيت المكتبات الاستاتيكية.

--without-ensurepip

يعطل هذا المفتاح مثبت حزم بايثون، وهو غير مطلوب في هذه المرحلة.

--without-static-libpython

يمنع هذا المفتاح بناء مكتبة استاتيكية ضخمة وغير ضرورية.

قم بتجميع الحزمة:

**make**

### ملاحظة

لا يمكن بناء بعض وحدات Python 3 الآن لأن التبعيات لم يتم تثبيتها بعد. بالنسبة لوحدة `ssl` ستظهر رسالة تفيد بأن Python يتطلب OpenSSL 1.1.1 أو إصداراً أحدث؛ يجب تجاهل هذه الرسالة. فقط **تأكد من أن أمر `make` الرئيسي لم يفشل**. الوحدات الاختيارية غير مطلوبة الآن وسيتم بناؤها في الفصل 8.

تثبيت الحزمة:

**make install**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.54.2، "محتويات Python 3".

---

Linux From Scratch - Version 13.1-systemd

# 7.13. Texinfo-7.3

تحتوي حزمة Texinfo على برامج لقراءة وكتابة وتحويل صفحات info.

**وقت البناء التقريبي:**
0.2 SBU
**مساحة القرص المطلوبة:**
147 ميجابايت

## 7.13.1. تثبيت Texinfo

قم بتهيئة Texinfo للتجميع:

**./configure --prefix=/usr**

قم بتجميع الحزمة:

**make**

تثبيت الحزمة:

**make install**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.73.2، "محتويات Texinfo".

---

Linux From Scratch - Version 13.1-systemd

# 7.14. Util-linux-2.42.2

تحتوي حزمة Util-linux على برامج أدوات مساعدة متنوعة.

**وقت البناء التقريبي:**
0.2 SBU
**مساحة القرص المطلوبة:**
211 ميجابايت

## 7.14.1. تثبيت Util-linux

يوصي معيار FHS باستخدام الدليل `/var/lib/hwclock` بدلاً من الدليل المعتاد `/etc` كموقع لملف `adjtime`. قم بإنشاء هذا الدليل باستخدام:

**mkdir -pv /var/lib/hwclock**

قم بتهيئة Util-linux للتجميع:

**./configure --libdir=/usr/lib     \**
**--runstatedir=/run    \**
**--disable-chfn-chsh   \**
**--disable-login       \**
**--disable-nologin     \**
**--disable-su          \**
**--disable-setpriv     \**
**--disable-runuser     \**
**--disable-pylibmount  \**
**--disable-static      \**
**--disable-liblastlog2 \**
**--without-python      \**
**ADJTIME_PATH=/var/lib/hwclock/adjtime \**
**--docdir=/usr/share/doc/util-linux-2.42.2**

**معنى خيارات التهيئة:**

ADJTIME_PATH=/var/lib/hwclock/adjtime

يحدد هذا موقع الملف الذي يسجل المعلومات حول ساعة العتاد وفقاً لمعيار FHS. هذا ليس ضرورياً بشكل صارم لهذه الأداة المؤقتة، ولكنه يمنع إنشاء ملف في موقع آخر لن يتم استبداله أو حذفه عند بناء حزمة util-linux النهائية.

--libdir=/usr/lib

يضمن هذا المفتاح أن الروابط الرمزية `.so` تستهدف ملف المكتبة المشتركة في نفس الدليل (`/usr/lib`) مباشرة.

--disable-*

تمنع هذه المفاتيح ظهور تحذيرات بشأن بناء مكونات تتطلب حزماً غير موجودة في LFS أو لم يتم تثبيتها بعد.

--without-python

يعطل هذا المفتاح استخدام Python، مما يتجنب محاولة بناء روابط (bindings) غير ضرورية.

runstatedir=/run

**يحدد هذا المفتاح موقع المقبس (socket) المستخدم بواسطة `uuidd` و `libuuid` بشكل صحيح.**

قم بتجميع الحزمة:

**make**

تثبيت الحزمة:

**make install**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.81.2، "محتويات Util-linux".

---

Linux From Scratch - Version 13.1-systemd