# 8.33. Ncurses-6.6

تحتوي حزمة Ncurses على مكتبات للتعامل مع شاشات الأحرف بشكل مستقل عن نوع الطرفية (Terminal).

**وقت البناء التقريبي:**
0.2 SBU
**المساحة المطلوبة من القرص:**
47 ميجابايت

## 8.33.1. تثبيت Ncurses

تجهيز Ncurses للتجميع:

**./configure --prefix=/usr           \**
**--mandir=/usr/share/man \**
**--with-shared           \**
**--without-debug         \**
**--without-normal        \**
**--with-cxx-shared       \**
**--enable-pc-files       \**
**--with-pkg-config-libdir=/usr/lib/pkgconfig**

**معاني خيارات التهيئة الجديدة:**

`--with-shared`

يجعل Ncurses يقوم ببناء وتثبيت مكتبات C المشتركة.

`--without-normal`

يمنع Ncurses من بناء وتثبيت مكتبات C الاستاتيكية.

`--without-debug`

يمنع Ncurses من بناء وتثبيت مكتبات التصحيح (Debug libraries).

`--with-cxx-shared`

يجعل Ncurses يقوم ببناء وتثبيت روابط C++ المشتركة، كما يمنعه من بناء وتثبيت روابط C++ الاستاتيكية.

`--enable-pc-files`

يقوم هذا المفتاح بتوليد وتثبيت ملفات `.pc` الخاصة بـ `pkg-config`.

تجميع الحزمة:

**make**

تحتوي هذه الحزمة على مجموعة اختبارات، ولكن لا يمكن تشغيلها إلا بعد تثبيت الحزمة. توجد الاختبارات في دليل `test/`. راجع ملف `README` في ذلك الدليل لمزيد من التفاصيل.

عملية تثبيت هذه الحزمة ستؤدي إلى استبدال الملف `libncursesw.so.6.6` في مكانه. قد يتسبب ذلك في تعطل عملية الغلاف (Shell process) التي تستخدم الكود والبيانات من ملف المكتبة. قم بتثبيت الحزمة باستخدام `DESTDIR` واستبدل ملف المكتبة بشكل صحيح باستخدام خيار `--remove-destination` الخاص بالأمر `cp` (يتم أيضاً تعديل الترويسة `curses.h` لضمان استخدام واجهة التطبيق الثنائية (ABI) للأحرف العريضة كما فعلنا في القسم 6.3، "Ncurses-6.6"):

**make DESTDIR=$PWD/dest install**
**sed -e 's/^#if.*XOPEN.*$/#if 1/' \**
**-i dest/usr/include/curses.h**
**cp --remove-destination -av dest/* /**

---

Linux From Scratch - Version 13.1-systemd

لا تزال العديد من التطبيقات تتوقع أن يكون الرابط (Linker) قادراً على إيجاد مكتبات Ncurses التي لا تدعم الأحرف العريضة. يمكنك خداع هذه التطبيقات لربطها بمكتبات الأحرف العريضة عن طريق الروابط الرمزية (لاحظ أن روابط `.so` تكون آمنة فقط بعد تعديل `curses.h` لاستخدام ABI الأحرف العريضة دائماً):

**for lib in ncurses form panel menu ; do**
**ln -sfv lib${lib}w.so /usr/lib/lib${lib}.so**
**ln -sfv ${lib}w.pc    /usr/lib/pkgconfig/${lib}.pc**
**done**

أخيراً، تأكد من أن التطبيقات القديمة التي تبحث عن `-lcurses` وقت البناء لا تزال قابلة للبناء:

**ln -sfv libncursesw.so /usr/lib/libcurses.so**

إذا كنت ترغب في ذلك، قم بتثبيت وثائق Ncurses:

**cp -v -R doc -T /usr/share/doc/ncurses-6.6**

### ملاحظة

التعليمات أعلاه لا تنشئ مكتبات Ncurses غير الداعمة للأحرف العريضة، حيث أن أي حزمة يتم تثبيتها عن طريق التجميع من الكود المصدري لن ترتبط بها في وقت التشغيل. ومع ذلك، فإن التطبيقات الوحيدة المعروفة التي تأتي كملفات ثنائية فقط وترتبط بمكتبات Ncurses غير الداعمة للأحرف العريضة تتطلب الإصدار 5. إذا كنت بحاجة إلى هذه المكتبات بسبب تطبيق ثنائي فقط أو للامتثال لمعيار LSB، فقم ببناء الحزمة مرة أخرى باستخدام الأوامر التالية:

**make distclean**
**./configure --prefix=/usr    \**
**--with-shared    \**
**--without-normal \**
**--without-debug  \**
**--without-cxx-binding \**
**--with-abi-version=5**
**make sources libs**
**cp -av lib/lib*.so.5* /usr/lib**

## 8.33.2. محتويات Ncurses

**البرامج المثبتة:**
`captoinfo` (رابط إلى tic)، `clear`، `infocmp`، `infotocap` (رابط إلى tic)، `ncursesw6-config`، `reset` (رابط إلى tset)، `tabs`، `tic`، `toe`، `tput` و `tset`.

**المكتبات المثبتة:**
`libcurses.so` (رابط رمزي)، `libform.so` (رابط رمزي)، `libformw.so`، `libmenu.so` (رابط رمزي)، `libmenuw.so`، `libncurses.so` (رابط رمزي)، `libncursesw.so`، `libncurses++w.so`، `libpanel.so` (رابط رمزي)، و `libpanelw.so`.

**الأدلة المثبتة:**
`/usr/share/tabset` و `/usr/share/terminfo` و `/usr/share/doc/ncurses-6.6`.

**وصف موجز**

**captoinfo**
يحول وصف termcap إلى وصف terminfo.

**clear**
يمسح الشاشة، إذا كان ذلك ممكناً.

**infocmp**
يقارن أو يطبع أوصاف terminfo.

**infotocap**
يحول وصف terminfo إلى وصف termcap.

**ncursesw6-config**
يوفر معلومات التهيئة لـ ncurses.

**reset**
يعيد تهيئة الطرفية إلى قيمها الافتراضية.

**tabs**
يمسح ويضبط توقفات الجدولة (Tab stops) في الطرفية.

---

Linux From Scratch - Version 13.1-systemd

**tic**
مجمّع أوصاف إدخالات terminfo الذي يترجم ملف terminfo من تنسيق المصدر إلى التنسيق الثنائي المطلوب لروتينات مكتبة ncurses. [يحتوي ملف terminfo على معلومات حول قدرات طرفية معينة].

**toe**
يسرد جميع أنواع الطرفيات المتاحة، مع تقديم الاسم الأساسي والوصف لكل منها.

**tput**
يجعل قيم القدرات المعتمدة على الطرفية متاحة للغلاف؛ ويمكن استخدامه أيضاً لإعادة ضبط أو تهيئة طرفية أو الإبلاغ عن اسمها الطويل.

**tset**
يمكن استخدامه لتهيئة الطرفيات.

`libncursesw`
تحتوي على دوال لعرض النصوص بطرق معقدة على شاشة الطرفية؛ ومثال جيد على استخدام هذه الدوال هو القائمة التي تظهر أثناء تنفيذ `make menuconfig` للنواة.

`libncurses++w`
تحتوي على روابط C++ للمكتبات الأخرى في هذه الحزمة.

`libformw`
تحتوي على دوال لتنفيذ النماذج (Forms).

`libmenuw`
تحتوي على دوال لتنفيذ القوائم (Menus).

`libpanelw`
تحتوي على دوال لتنفيذ اللوحات (Panels).

---

Linux From Scratch - Version 13.1-systemd

# 8.34. Sed-4.10

تحتوي حزمة Sed على محرر تدفق (Stream editor).

**وقت البناء التقريبي:**
0.4 SBU
**المساحة المطلوبة من القرص:**
42 ميجابايت

## 8.34.1. تثبيت Sed

تجهيز Sed للتجميع:

**./configure --prefix=/usr**

تجميع الحزمة وتوليد وثائق HTML:

**make**
**make html**

لاختبار النتائج، نفذ ما يلي:

**chown -R tester .**
**su tester -c "PATH=$PATH make check"**

تثبيت الحزمة ووثائقها:

**make install**
**install -vDm644 doc/sed.html -t /usr/share/doc/sed-4.10**

## 8.34.2. محتويات Sed

**البرنامج المثبت:**
`sed`
**الدليل المثبت:**
`/usr/share/doc/sed-4.10`

**وصف موجز**

**sed**
يقوم بتصفية وتحويل الملفات النصية في مرحلة واحدة.

---

Linux From Scratch - Version 13.1-systemd

# 8.35. Psmisc-23.7

تحتوي حزمة Psmisc على برامج لعرض معلومات حول العمليات الجارية.

**وقت البناء التقريبي:**
أقل من 0.1 SBU
**المساحة المطلوبة من القرص:**
6.8 ميجابايت

## 8.35.1. تثبيت Psmisc

تجهيز Psmisc للتجميع:

**./configure --prefix=/usr**

تجميع الحزمة:

**make**

لتشغيل مجموعة الاختبارات، نفذ:

**make check**

تثبيت الحزمة:

**make install**

## 8.35.2. محتويات Psmisc

**البرامج المثبتة:**
`fuser` و `killall` و `peekfd` و `prtstat` و `pslog` و `pstree` و `pstree.x11` (رابط إلى pstree).

**وصف موجز**

**fuser**
يبلغ عن معرفات العمليات (PIDs) للعمليات التي تستخدم ملفات أو أنظمة ملفات معينة.

**killall**
ينهي العمليات حسب الاسم؛ حيث يرسل إشارة إلى جميع العمليات التي تشغل أي من الأوامر المحددة.

**peekfd**
يستعرض واصفات الملفات (File descriptors) لعملية جارية، بناءً على معرف العملية (PID).

**prtstat**
يطبع معلومات حول عملية ما.

**pslog**
يبلغ عن مسار السجلات الحالي لعملية ما.

**pstree**
يعرض العمليات الجارية على شكل شجرة.

**pstree.x11**
نفس عمل `pstree` باستثناء أنه ينتظر التأكيد قبل الخروج.

---

Linux From Scratch - Version 13.1-systemd

# 8.36. Gettext-1.0

تحتوي حزمة Gettext على أدوات للتدويل (Internationalization) والتوطين (Localization). تسمح هذه الأدوات بتجميع البرامج مع دعم اللغات الأصلية (NLS)، مما يمكنها من إخراج الرسائل بلغة المستخدم الأصلية.

**وقت البناء التقريبي:**
2.1 SBU
**المساحة المطلوبة من القرص:**
448 ميجابايت

## 8.36.1. تثبيت Gettext

تجهيز Gettext للتجميع:

**./configure --prefix=/usr    \**
**--disable-static \**
**--docdir=/usr/share/doc/gettext-1.0**

تجميع الحزمة:

**make**

لاختبار النتائج، نفذ:

**make check**

تثبيت الحزمة:

**make install**
**chmod -v 0755 /usr/lib/preloadable_libintl.so**

## 8.36.2. محتويات Gettext

**البرامج المثبتة:**
`autopoint` و `envsubst` و `gettext` و `gettext.sh` و `gettextize` و `msgattrib` و `msgcat` و `msgcmp` و `msgcomm` و `msgconv` و `msgen` و `msgexec` و `msgfilter` و `msgfmt` و `msggrep` و `msginit` و `msgmerge` و `msgunfmt` و `msguniq` و `ngettext` و `recode-sr-latin` و `xgettext`.

**المكتبات المثبتة:**
`libasprintf.so` و `libgettextlib.so` و `libgettextpo.so` و `libgettextsrc.so` و `libtextstyle.so` و `preloadable_libintl.so`.

**الأدلة المثبتة:**
`/usr/lib/gettext` و `/usr/share/doc/gettext-1.0` و `/usr/share/gettext` و `/usr/share/gettext-1.0`.

**وصف موجز**

**autopoint**
ينسخ ملفات البنية التحتية القياسية لـ Gettext إلى حزمة مصدرية.

**envsubst**
يستبدل متغيرات البيئة في سلاسل تنسيق الغلاف (Shell format strings).

**gettext**
يترجم رسالة بلغة طبيعية إلى لغة المستخدم عن طريق البحث عن الترجمة في كتالوج الرسائل.

**gettext.sh**
يعمل بشكل أساسي كمكتبة دوال غلاف لـ gettext.

**gettextize**
ينسخ جميع ملفات Gettext القياسية إلى الدليل العلوي المحدد لحزمة ما لبدء تدويلها.

**msgattrib**
يصفي رسائل كتالوج الترجمة وفقاً لسماتها ويتحكم في تلك السمات.

**msgcat**
يربط ويدمج ملفات `.po` المحددة.

**msgcmp**
يقارن بين ملفي `.po` للتحقق من احتوائهما على نفس مجموعة سلاسل `msgid`.

---

Linux From Scratch - Version 13.1-systemd

**msgcomm**
يجد الرسائل المشتركة بين ملفات `.po` المحددة.

**msgconv**
يحول كتالوج الترجمة إلى ترميز أحرف مختلف.

**msgen**
ينشئ كتالوج ترجمة باللغة الإنجليزية.

**msgexec**
يطبق أمراً على جميع ترجمات كتالوج الترجمة.

**msgfilter**
يطبق مرشحاً (Filter) على جميع ترجمات كتالوج الترجمة.

**msgfmt**
يولد كتالوج رسائل ثنائي من كتالوج ترجمة.

**msggrep**
يستخرج جميع رسائل كتالوج الترجمة التي تطابق نمطاً معيناً أو تنتمي إلى ملفات مصدرية محددة.

**msginit**
ينشئ ملف `.po` جديداً، مع تهيئة المعلومات الوصفية بقيم من بيئة المستخدم.

**msgmerge**
يدمج ترجمتين خاميتين في ملف واحد.

**msgunfmt**
يفك تجميع كتالوج رسائل ثنائي إلى نص ترجمة خام.

**msguniq**
يوحد الترجمات المكررة في كتالوج الترجمة.

**ngettext**
يعرض ترجمات باللغة الأصلية لرسالة نصية يعتمد شكلها القواعدي على رقم ما.

**recode-sr-latin**
يعيد ترميز النص الصربي من الخط الكيريلي إلى الخط اللاتيني.

**xgettext**
يستخرج أسطر الرسائل القابلة للترجمة من الملفات المصدرية المحددة لإنشاء أول قالب ترجمة.

`libasprintf`
تعرف فئة `autosprintf` التي تجعل روتينات الإخراج المنسقة في C قابلة للاستخدام في برامج C++، لاستخدامها مع سلاسل `<string>` وتدفقات `<iostream>`.

`libgettextlib`
تحتوي على روتينات مشتركة تستخدمها برامج Gettext المختلفة؛ وهي غير مخصصة للاستخدام العام.

`libgettextpo`
تستخدم لكتابة برامج متخصصة تعالج ملفات `.po`؛ وتستخدم هذه المكتبة عندما لا تكون التطبيقات القياسية المرفقة مع Gettext (مثل `msgcomm` و `msgcmp` و `msgattrib` و `msgen`) كافية.

`libgettextsrc`
توفر روتينات مشتركة تستخدمها برامج Gettext المختلفة؛ وهي غير مخصصة للاستخدام العام.

`libtextstyle`
مكتبة لتنسيق النصوص.

`preloadable_libintl`
مكتبة مخصصة للاستخدام عبر `LD_PRELOAD` تساعد `libintl` في تسجيل الرسائل غير المترجمة.

---

Linux From Scratch - Version 13.1-systemd