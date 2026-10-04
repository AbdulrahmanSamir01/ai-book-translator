# 8.43. Expat-2.8.3

تحتوي حزمة Expat على مكتبة لغة C موجهة للتدفق (stream oriented) لتحليل ملفات XML.

**وقت البناء التقريبي:**
0.1 SBU
**مساحة القرص المطلوبة:**
12 ميجابايت

## 8.43.1. تثبيت Expat

تجهيز Expat للتجميع:

**./configure --prefix=/usr    \**
**--disable-static \**
**--docdir=/usr/share/doc/expat-2.8.3**

تجميع الحزمة:

**make**

لاختبار النتائج، قم بتنفيذ:

**make check**

تثبيت الحزمة:

**make install**

إذا كنت ترغب في ذلك، قم بتثبيت التوثيق:

**install -v -m644 doc/*.{html,css} /usr/share/doc/expat-2.8.3**

## 8.43.2. محتويات Expat

**البرامج المثبتة:**
xmlwf
**المكتبات المثبتة:**
libexpat.so
**الدليل المثبت:**
/usr/share/doc/expat-2.8.3

**وصف موجز**

**xmlwf**
أداة غير تحققية (non-validating) للتأكد مما إذا كانت مستندات XML جيدة التكوين (well formed) أم لا.

**libexpat**
تحتوي على ترويسات API لتحليل ملفات XML.

---

Linux From Scratch - Version 13.1-systemd

# 8.44. Inetutils-2.8

تحتوي حزمة Inetutils على برامج للشبكات الأساسية.

**وقت البناء التقريبي:**
0.3 SBU
**مساحة القرص المطلوبة:**
38 ميجابايت

## 8.44.1. تثبيت Inetutils

أولاً، اجعل الحزمة قابلة للبناء باستخدام gcc-14.1 أو إصدار أحدث:

**sed -i 's/def HAVE_TERMCAP_TGETENT/ 1/' telnet/telnet.c**

تجهيز Inetutils للتجميع:

**./configure --prefix=/usr        \**
**--bindir=/usr/bin    \**
**--localstatedir=/var \**
**--disable-logger     \**
**--disable-whois      \**
**--disable-rcp        \**
**--disable-rexec      \**
**--disable-rlogin     \**
**--disable-rsh        \**
**--disable-servers**

**معاني خيارات التهيئة (configure options):**

`--disable-logger`

**يمنع هذا الخيار Inetutils من تثبيت برنامج logger، الذي تستخدمه النصوص البرمجية لتمرير الرسائل إلى**
System Log Daemon. لا تقم بتثبيته لأن حزمة Util-linux تثبت إصداراً أحدث.

`--disable-whois`

**يعطل هذا الخيار بناء عميل whois الخاص بـ Inetutils، لأنه قديم. تتوفر تعليمات لعميل whois**
أفضل في كتاب BLFS.

`--disable-r*`

تعطل هذه المعاملات بناء البرامج المهجورة التي لا ينبغي استخدامها بسبب مشكلات أمنية. يمكن توفير الوظائف
التي تقدمها هذه البرامج عبر حزمة openssh الموجودة في كتاب BLFS.

`--disable-servers`

يعطل هذا الخيار تثبيت خوادم الشبكة المختلفة المضمنة كجزء من حزمة Inetutils. هذه الخوادم
تعتبر غير مناسبة في نظام LFS أساسي؛ فبعضها غير آمن بطبيعته ولا يعتبر آمناً إلا في
الشبكات الموثوقة. لاحظ أن هناك بدائل أفضل متاحة للعديد من هذه الخوادم.

تجميع الحزمة:

**make**

لاختبار النتائج، قم بتنفيذ:

**make check**

تثبيت الحزمة:

**make install**

نقل البرنامج إلى الموقع الصحيح:

**mv -v /usr/{,s}bin/ifconfig**

---

Linux From Scratch - Version 13.1-systemd

## 8.44.2. محتويات Inetutils

**البرامج المثبتة:**
dnsdomainname, ftp, ifconfig, hostname, ping, ping6, talk, telnet, tftp, and traceroute

**وصف موجز**

**dnsdomainname**
عرض اسم نطاق DNS الخاص بالنظام.

**ftp**
برنامج بروتوكول نقل الملفات.

**hostname**
عرض أو تعيين اسم المضيف.

**ifconfig**
إدارة واجهات الشبكة.

**ping**
إرسال حزم طلب الصدى (echo-request) وتقرير الوقت الذي تستغرقه الردود.

**ping6**
**إصدار من ping مخصص لشبكات IPv6.**

**talk**
يستخدم للدردشة مع مستخدم آخر.

**telnet**
واجهة لبروتوكول TELNET.

**tftp**
برنامج بسيط لنقل الملفات.

**traceroute**
تتبع المسار الذي تسلكه حزمك من المضيف الذي تعمل عليه إلى مضيف آخر على الشبكة،
مع إظهار جميع القفزات الوسيطة (البوابات) على طول الطريق.

---

Linux From Scratch - Version 13.1-systemd

# 8.45. Less-704

تحتوي حزمة Less على مستعرض للملفات النصية.

**وقت البناء التقريبي:**
0.1 SBU
**مساحة القرص المطلوبة:**
17 ميجابايت

## 8.45.1. تثبيت Less

تجهيز Less للتجميع:

**./configure --prefix=/usr --sysconfdir=/etc**

**معاني خيارات التهيئة (configure options):**

`--sysconfdir=/etc`

يوجه هذا الخيار البرامج التي تنشئها الحزمة للبحث في /etc عن ملفات التهيئة.

تجميع الحزمة:

**make**

لاختبار النتائج، قم بتنفيذ:

**make check**

تثبيت الحزمة:

**make install**

## 8.45.2. محتويات Less

**البرامج المثبتة:**
less, lessecho, and lesskey

**وصف موجز**

**less**
مستعرض ملفات أو pager؛ يقوم بعرض محتويات الملف المحدد، مما يسمح للمستخدم بالتمرير، والبحث عن النصوص، والقفز إلى علامات محددة.

**lessecho**
مطلوب لتوسيع الأحرف الميتا (meta-characters)، مثل * و ?، في أسماء الملفات على أنظمة Unix.

**lesskey**
**يستخدم لتحديد ارتباطات المفاتيح لبرنامج less.**

---

Linux From Scratch - Version 13.1-systemd

# 8.46. Perl-5.44.0

تحتوي حزمة Perl على لغة الاستخراج والتقارير العملية (Practical Extraction and Report Language).

**وقت البناء التقريبي:**
1.3 SBU
**مساحة القرص المطلوبة:**
261 ميجابايت

## 8.46.1. تثبيت Perl

يقوم هذا الإصدار من Perl ببناء وحدات Compress::Raw::Zlib و Compress::Raw::BZip2. افتراضياً، سيستخدم Perl نسخة داخلية من المصادر للبناء. قم بتنفيذ الأمر التالي لضمان استخدام Perl للمكتبات المثبتة على النظام:

**export BUILD_ZLIB=False**
**export BUILD_BZIP2=0**

للحصول على تحكم كامل في طريقة إعداد Perl، يمكنك إزالة خيارات "-des" من الأمر التالي واختيار طريقة بناء هذه الحزمة يدوياً. بدلاً من ذلك، استخدم الأمر تماماً كما هو موضح أدناه لاستخدام الإعدادات الافتراضية التي يكتشفها Perl تلقائياً:

**sh Configure -des                                          \**
**-D prefix=/usr                                \**
**-D vendorprefix=/usr                          \**
**-D privlib=/usr/lib/perl5/5.44/core_perl      \**
**-D archlib=/usr/lib/perl5/5.44/core_perl      \**
**-D sitelib=/usr/lib/perl5/5.44/site_perl      \**
**-D sitearch=/usr/lib/perl5/5.44/site_perl     \**
**-D vendorlib=/usr/lib/perl5/5.44/vendor_perl  \**
**-D vendorarch=/usr/lib/perl5/5.44/vendor_perl \**
**-D man1dir=/usr/share/man/man1                \**
**-D man3dir=/usr/share/man/man3                \**
**-D pager="/usr/bin/less -isR"                 \**
**-D useshrplib                                 \**
**-D usethreads**

**معاني خيارات Configure الجديدة:**

`-D pager="/usr/bin/less -isR"`

**يضمن هذا استخدام less بدلاً من more.**

`-D man1dir=/usr/share/man/man1 -D man3dir=/usr/share/man/man3`

**بما أن Groff لم يتم تثبيته بعد، فإن Configure لن ينشئ صفحات الدليل (man pages) لـ Perl. هذه المعاملات تتجاوز هذا السلوك.**

`-D usethreads`

بناء Perl مع دعم الخيوط (threads).

تجميع الحزمة:

**make**

لاختبار النتائج، قم بتنفيذ:

**TEST_JOBS=$(nproc) make test_harness**

تثبيت الحزمة والتنظيف:

**make install**
**unset BUILD_ZLIB BUILD_BZIP2**

---

Linux From Scratch - Version 13.1-systemd

## 8.46.2. محتويات Perl

**البرامج المثبتة:**
corelist, cpan, enc2xs, encguess, h2ph, h2xs, instmodsh, json_pp, libnetcfg, perl,
perl5.44.0 (رابط صلب إلى perl), perlbug, perldoc, perlivp, perlthanks (رابط صلب إلى perlbug),
piconv, pl2pm, pod2html, pod2man, pod2text, pod2usage, podchecker, podselect, prove,
ptar, ptardiff, ptargrep, shasum, splain, xsubpp, and zipdetails
**المكتبات المثبتة:**
كثير جداً بحيث لا يمكن سردها جميعاً هنا
**الدليل المثبت:**
/usr/lib/perl5

**وصف موجز**

**corelist**
واجهة سطر أوامر لـ Module::CoreList.

**cpan**
التفاعل مع شبكة أرشيف Perl الشاملة (CPAN) من سطر الأوامر.

**enc2xs**
بناء امتداد Perl لوحدة Encode إما من خرائط أحرف Unicode أو ملفات ترميز Tcl.

**encguess**
تخمين نوع الترميز لملف واحد أو عدة ملفات.

**h2ph**
تحويل ملفات ترويسات C ذات الامتداد .h إلى ملفات ترويسات Perl ذات الامتداد .ph.

**h2xs**
تحويل ملفات ترويسات C ذات الامتداد .h إلى امتدادات Perl.

**instmodsh**
نص برمجي غلافي (Shell script) لفحص وحدات Perl المثبتة؛ يمكنه إنشاء ملف tarball من وحدة مثبتة.

**json_pp**
تحويل البيانات بين تنسيقات إدخال وإخراج معينة.

**libnetcfg**
يمكن استخدامه لتهيئة وحدة libnet في Perl.

**perl**
**يجمع بين أفضل ميزات C و sed و awk و sh في لغة واحدة تشبه "السكين السويسري".**

**perl5.44.0**
**رابط صلب إلى perl.**

**perlbug**
يستخدم لإنشاء تقارير عن الأخطاء في Perl، أو الوحدات المرفقة معه، وإرسالها عبر البريد.

**perldoc**
يعرض جزءاً من التوثيق بتنسيق pod المضمن في شجرة تثبيت Perl أو في نص برمجي لـ Perl.

**perlivp**
إجراء التحقق من تثبيت Perl؛ يمكن استخدامه للتأكد من تثبيت Perl ومكتباته بشكل صحيح.

**perlthanks**
يستخدم لإنشاء رسائل شكر لإرسالها إلى مطوري Perl.

**piconv**
**إصدار Perl من محول ترميز الأحرف iconv.**

**pl2pm**
أداة تقريبية لتحويل ملفات Perl4 ذات الامتداد .pl إلى وحدات Perl5 ذات الامتداد .pm.

**pod2html**
تحويل الملفات من تنسيق pod إلى تنسيق HTML.

**pod2man**
تحويل بيانات pod إلى مدخلات *roff منسقة.

**pod2text**
تحويل بيانات pod إلى نص ASCII منسق.

**pod2usage**
طباعة رسائل الاستخدام من وثائق pod المضمنة في الملفات.

**podchecker**
فحص بناء جملة (syntax) ملفات التوثيق بتنسيق pod.

**podselect**
عرض أقسام مختارة من توثيق pod.

**prove**
أداة سطر أوامر لتشغيل الاختبارات مقابل وحدة Test::Harness.

**ptar**
**برنامج يشبه tar مكتوب بلغة Perl.**

**ptardiff**
برنامج Perl يقارن بين أرشيف مستخرج وآخر غير مستخرج.

---

Linux From Scratch - Version 13.1-systemd

**ptargrep**
برنامج Perl يطبق مطابقة الأنماط (pattern matching) على محتويات الملفات في أرشيف tar.

**shasum**
طباعة أو فحص مجموعات SHA (checksums).

**splain**
يستخدم لفرض تشخيصات تحذيرية مفصلة في Perl.

**xsubpp**
تحويل كود Perl XS إلى كود C.

**zipdetails**
عرض تفاصيل حول البنية الداخلية لملف Zip.

---

Linux From Scratch - Version 13.1-systemd