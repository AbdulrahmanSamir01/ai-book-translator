# 8.16. Flex-2.6.4

تحتوي حزمة Flex على أداة برمجية لتوليد برامج قادرة على التعرف على الأنماط (Patterns) في النصوص.

**وقت البناء التقريبي:**
0.1 SBU
**مساحة القرص المطلوبة:**
33 ميجابايت

## 8.16.1. تثبيت Flex

تجهيز Flex للتجميع:

**./configure --prefix=/usr    \**
**--disable-static \**
**--docdir=/usr/share/doc/flex-2.6.4**

تجميع الحزمة:

**make**

لاختبار النتائج، قم بتنفيذ:

**make check**

تثبيت الحزمة:

**make install**

**هناك بعض البرامج التي لا تتعرف على flex بعد وتحاول تشغيل سلفه lex. لدعم هذه البرامج، قم بإنشاء رابط رمزي باسم lex يقوم بتشغيل flex في وضع محاكاة lex، وأيضاً قم بإنشاء صفحة الدليل (man page) الخاصة بـ lex كرابط رمزي:**

**ln -sv flex   /usr/bin/lex**
**ln -sv flex.1 /usr/share/man/man1/lex.1**

## 8.16.2. محتويات Flex

**البرامج المثبتة:**
flex، و flex++ (رابط إلى flex)، و lex (رابط إلى flex)
**المكتبات المثبتة:**
libfl.so
**الدليل المثبت:**
/usr/share/doc/flex-2.6.4

**وصف موجز**

**flex**
أداة لتوليد برامج تتعرف على الأنماط في النصوص؛ وهي تتيح مرونة عالية في تحديد قواعد البحث عن الأنماط، مما يلغي الحاجة إلى تطوير برنامج متخصص لكل حالة.

**flex++**
**امتداد لـ flex، يُستخدم لتوليد أكواد وفئات (Classes) بلغة ++C. وهو عبارة عن رابط رمزي إلى flex.**

**lex**
**رابط رمزي يقوم بتشغيل flex في وضع محاكاة lex.**

libfl
مكتبة flex

---

Linux From Scratch - Version 13.1-systemd

# 8.17. Tcl-8.6.18

تحتوي حزمة Tcl على لغة Tool Command Language، وهي لغة برمجة نصية (Scripting Language) قوية وعامة الغرض. وقد كُتبت حزمة Expect باستخدام لغة Tcl (تُنطق "tickle").

**وقت البناء التقريبي:**
2.9 SBU
**مساحة القرص المطلوبة:**
92 ميجابايت

## 8.17.1. تثبيت Tcl

يتم تثبيت هذه الحزمة والحزمتين التاليتين (Expect و DejaGNU) لدعم تشغيل مجموعات الاختبارات (Test Suites) لـ Binutils و GCC وحزم أخرى. قد يبدو تثبيت ثلاث حزم لأغراض الاختبار أمراً مبالغاً فيه، ولكن من المطمئن جداً، بل ومن الضروري، التأكد من أن أهم الأدوات تعمل بشكل صحيح.

تجهيز Tcl للتجميع:

**SRCDIR=$(pwd)**
**cd unix**
**./configure --prefix=/usr           \**
**--mandir=/usr/share/man \**
**--disable-rpath**

**معنى معاملات التهيئة الجديدة:**

--disable-rpath

يمنع هذا المعامل كتابة مسارات البحث عن المكتبات (rpath) بشكل ثابت (Hard coding) داخل الملفات التنفيذية الثنائية والمكتبات المشتركة. لا تحتاج هذه الحزمة إلى rpath عند التثبيت في الموقع القياسي، كما أن rpath قد يتسبب أحياناً في تأثيرات غير مرغوب فيها أو حتى مشكلات أمنية.

بناء الحزمة:

**make**

**sed -e "s|$SRCDIR/unix|/usr/lib|" \**
**-e "s|$SRCDIR|/usr/include|"  \**
**-i tclConfig.sh**

**sed -e "s|$SRCDIR/unix/pkgs/tdbc1.1.13|/usr/lib/tdbc1.1.13|" \**
**-e "s|$SRCDIR/pkgs/tdbc1.1.13/generic|/usr/include|"     \**
**-e "s|$SRCDIR/pkgs/tdbc1.1.13/library|/usr/lib/tcl8.6|"  \**
**-e "s|$SRCDIR/pkgs/tdbc1.1.13|/usr/include|"             \**
**-i pkgs/tdbc1.1.13/tdbcConfig.sh**

**sed -e "s|$SRCDIR/unix/pkgs/itcl4.3.7|/usr/lib/itcl4.3.7|" \**
**-e "s|$SRCDIR/pkgs/itcl4.3.7/generic|/usr/include|"    \**
**-e "s|$SRCDIR/pkgs/itcl4.3.7|/usr/include|"            \**
**-i pkgs/itcl4.3.7/itclConfig.sh**

**unset SRCDIR**

تعمل تعليمات "sed" المختلفة بعد أمر "make" على إزالة الإشارات إلى دليل البناء من ملفات التهيئة واستبدالها بدليل التثبيت. هذا الإجراء ليس إلزامياً لبقية مراحل LFS، ولكنه قد يكون مطلوباً إذا استخدمت حزمة يتم بناؤها لاحقاً لغة Tcl.

لاختبار النتائج، قم بتنفيذ:

**LC_ALL=C.UTF-8 make test**

---

Linux From Scratch - Version 13.1-systemd

تثبيت الحزمة:

**make install**
**chmod 644 /usr/lib/libtclstub8.6.a**

اجعل المكتبة المثبتة قابلة للكتابة حتى يمكن إزالة رموز التصحيح (Debugging Symbols) لاحقاً:

**chmod -v u+w /usr/lib/libtcl8.6.so**

تثبيت ترويسات Tcl، حيث تتطلبها الحزمة التالية Expect.

**make install-private-headers**

الآن قم بإنشاء الرابط الرمزي الضروري:

**ln -sfv tclsh8.6 /usr/bin/tclsh**

إعادة تسمية صفحة دليل تتعارض مع صفحة دليل خاصة بـ Perl:

**mv -v /usr/share/man/man3/{Thread,Tcl_Thread}.3**

اختيارياً، يمكنك تثبيت التوثيقات عبر تنفيذ الأوامر التالية:

**cd ..**
**tar -xf ../tcl8.6.18-html.tar.gz --strip-components=1**
**mkdir -v -p /usr/share/doc/tcl-8.6.18**
**cp -v -r  ./html/* /usr/share/doc/tcl-8.6.18**

## 8.17.2. محتويات Tcl

**البرامج المثبتة:**
tclsh (رابط إلى tclsh8.6) و tclsh8.6
**المكتبات المثبتة:**
libtcl8.6.so و libtclstub8.6.a

**وصف موجز**

**tclsh8.6**
غلاف أوامر (Command Shell) لغة Tcl

**tclsh**
رابط إلى tclsh8.6

libtcl8.6.so
مكتبة Tcl

libtclstub8.6.a
مكتبة Tcl Stub

---

Linux From Scratch - Version 13.1-systemd

# 8.18. Expect-5.45.4

**تحتوي حزمة Expect على أدوات لأتمتة التطبيقات التفاعلية مثل telnet و ftp و passwd و fsck و rlogin و tip، وذلك عبر حوارات مبرمجة نصياً. كما تفيد Expect في اختبار هذه التطبيقات وتسهيل كافة المهام التي يصعب تنفيذها بأي وسيلة أخرى. وقد كُتب إطار عمل DejaGnu باستخدام Expect.**

**وقت البناء التقريبي:**
0.2 SBU
**مساحة القرص المطلوبة:**
3.9 ميجابايت

## 8.18.1. تثبيت Expect

تتطلب Expect وجود PTYs لتعمل. تحقق من أن PTYs تعمل بشكل صحيح داخل بيئة chroot عبر إجراء اختبار بسيط:

**python3 -c 'from pty import spawn; spawn(["echo", "ok"])'**

يجب أن يخرج هذا الأمر كلمة ok. أما إذا كانت المخرجات تتضمن OSError: out of pty devices، فهذا يعني أن البيئة غير مهيأة للعمل الصحيح لـ PTY. في هذه الحالة، يجب عليك الخروج من بيئة chroot، وإعادة قراءة القسم 7.3 "تجهيز أنظمة ملفات النواة الافتراضية"، والتأكد من ربط نظام ملفات devpts (وأنظمة ملفات النواة الافتراضية الأخرى) بشكل صحيح. ثم أعد الدخول إلى بيئة chroot باتباع القسم 7.4 "الدخول إلى بيئة Chroot". يجب حل هذه المشكلة قبل المتابعة، وإلا فإن مجموعات الاختبارات التي تتطلب Expect (مثل اختبارات Bash و Binutils و GCC و GDBM وبالطبع Expect نفسها) ستفشل فشلاً ذريعاً، وقد تحدث أعطال خفية أخرى.

الآن، قم بإجراء بعض التغييرات للسماح بتوافق الحزمة مع gcc-15.1 أو الإصدارات الأحدث:

**patch -Np1 -i ../expect-5.45.4-gcc15-1.patch**

تجهيز Expect للتجميع:

**./configure --prefix=/usr           \**
**--with-tcl=/usr/lib     \**
**--enable-shared         \**
**--disable-rpath         \**
**--mandir=/usr/share/man \**
**--with-tclinclude=/usr/include**

**معنى خيارات التهيئة:**

--with-tcl=/usr/lib

**هذا المعامل ضروري لإخبار configure بموقع نص tclConfig.sh.**

--with-tclinclude=/usr/include

يخبر هذا الخيار Expect صراحةً بمكان العثور على ترويسات Tcl الداخلية.

بناء الحزمة:

**make**

لاختبار النتائج، قم بتنفيذ:

**make test**

تثبيت الحزمة:

**make install**
**ln -svf expect5.45.4/libexpect5.45.4.so /usr/lib**

---

Linux From Scratch - Version 13.1-systemd

## 8.18.2. محتويات Expect

**البرنامج المثبت:**
expect
**المكتبة المثبتة:**
libexpect5.45.4.so

**وصف موجز**

**expect**
يتواصل مع البرامج التفاعلية الأخرى وفقاً لنص برمجي (Script)

libexpect-5.45.4.so
تحتوي على دوال تسمح باستخدام Expect كامتداد لـ Tcl أو استخدامها مباشرة من لغة C أو ++C (بدون Tcl)

---

Linux From Scratch - Version 13.1-systemd

# 8.19. DejaGNU-1.6.3

**تحتوي حزمة DejaGnu على إطار عمل لتشغيل مجموعات الاختبارات على أدوات GNU. وقد كُتبت باستخدام expect، والتي بدورها تستخدم Tcl (Tool Command Language).**

**وقت البناء التقريبي:**
أقل من 0.1 SBU
**مساحة القرص المطلوبة:**
7.4 ميجابايت

## 8.19.1. تثبيت DejaGNU

يوصي المطورون الأصليون (Upstream) ببناء DejaGNU في دليل بناء مخصص:

**mkdir -v build**
**cd       build**

تجهيز DejaGNU للتجميع:

**../configure --prefix=/usr**
**makeinfo --html --no-split -o doc/dejagnu.html ../doc/dejagnu.texi**
**makeinfo --plaintext       -o doc/dejagnu.txt  ../doc/dejagnu.texi**

لاختبار النتائج، قم بتنفيذ:

**make check**

تثبيت الحزمة:

**make install**
**install -v -dm755  /usr/share/doc/dejagnu-1.6.3**
**install -v -m644   doc/dejagnu.{html,txt} /usr/share/doc/dejagnu-1.6.3**

## 8.19.2. محتويات DejaGNU

**البرامج المثبتة:**
dejagnu و runtest

**وصف موجز**

**dejagnu**
مشغل أوامر مساعد لـ DejaGNU

**runtest**
**نص برمجي غلافي (Wrapper script) يحدد موقع غلاف expect المناسب ثم يقوم بتشغيل DejaGNU**

---

Linux From Scratch - Version 13.1-systemd