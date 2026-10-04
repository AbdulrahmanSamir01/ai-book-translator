# الفصل 3. الحزم والرقع البرمجية

# 3.1. مقدمة

يتضمن هذا الفصل قائمة بالحزم التي يجب تحميلها لبناء نظام لينكس أساسي. تتوافق أرقام الإصدارات المذكورة مع إصدارات البرمجيات التي ثبت عملها، وبناءً عليها تم تأليف هذا الكتاب. ونحن ننصح بشدة بعدم استخدام إصدارات مختلفة، لأن أوامر البناء الخاصة بإصدار معين قد لا تعمل مع إصدار آخر، ما لم يتم تحديد إصدار مختلف عبر "تصويبات" (erratum) LFS أو تنبيه أمني. كما قد تحتوي أحدث إصدارات الحزم على مشكلات تتطلب حلولاً بديلة، وهذه الحلول يتم تطويرها واستقرارها في نسخة التطوير من الكتاب.

بالنسبة لبعض الحزم، قد يتم نشر ملف الـ tarball الخاص بالإصدار الرسمي وملف الـ tarball الخاص بلقطة المستودع (Git أو SVN) لهذا الإصدار بأسماء ملفات متشابهة أو حتى متطابقة. ولكن ملف الإصدار الرسمي قد يحتوي على بعض الملفات الضرورية التي **لا يتم تخزينها في المستودع (على سبيل المثال، نص التهيئة configure script الذي يتم إنشاؤه بواسطة autoconf)، بالإضافة إلى محتويات** لقطة المستودع المقابلة. يستخدم الكتاب ملفات الإصدارات الرسمية كلما أمكن ذلك، حيث إن استخدام لقطة المستودع بدلاً من الإصدار الرسمي المحدد في الكتاب سيؤدي إلى حدوث مشكلات.

قد لا تكون مواقع التحميل متاحة دائماً. إذا تغير موقع التحميل منذ نشر هذا الكتاب، فإن Google (https://www.google.com/) يوفر محرك بحث مفيد لمعظم الحزم. إذا لم ينجح هذا البحث، جرب إحدى الوسائل البديلة للتحميل عبر الرابط: https://www.linuxfromscratch.org/lfs/mirrors.html#files.

### هام

توجد في الصفحة التالية عدة حزم مهمة تقع في ftpmirror.gnu.org. الموقع الأصلي لهذه الحزم هو ftp.gnu.org، ولكن بسبب هجوم حجب الخدمة الموزع (DDOS) طويل الأمد، اقترح مدير الموقع على محرري LFS استخدام ftpmirror.gnu.org بدلاً من ذلك. راجع أخبار Slashdot لمزيد من التفاصيل.

في الواقع، يقوم رابط ftpmirror.gnu.org بإعادة التوجيه إلى أحد المرايا (mirrors) الخاصة بموقع ftp.gnu.org. يمكنك أيضاً اختيار مرآة يدوياً بدلاً من استخدام ftpmirror.gnu.org، وتوجد قائمة بالمرايا في https://www.gnu.org/prep/ftp.en.html. إذا اخترت استخدام قائمة wget الموضحة أدناه، فيمكن أيضاً تعديل ذلك الملف لاستخدام المرآة التي تفضلها.

ستحتاج الحزم والرقع البرمجية التي تم تحميلها إلى تخزينها في مكان متاح بسهولة طوال عملية البناء. كما يلزم وجود دليل عمل (working directory) لفك ضغط المصادر وبنائها. يمكن استخدام `$LFS/sources` كمكان لتخزين ملفات tarballs والرقع البرمجية وكدليل عمل في آن واحد. باستخدام هذا الدليل، ستكون العناصر المطلوبة موجودة على قسم LFS وستكون متاحة خلال جميع مراحل عملية البناء.

لإنشاء هذا الدليل، قم بتنفيذ الأمر التالي بصفتك المستخدم root، قبل بدء جلسة التحميل:

**mkdir -v $LFS/sources**

اجعل هذا الدليل قابلاً للكتابة و"لاصقاً" (sticky). تعني خاصية "sticky" أنه حتى لو كان لدى عدة مستخدمين إذن الكتابة في الدليل، فإن مالك الملف فقط هو من يمكنه حذف الملف داخل الدليل اللاصق. الأمر التالي سيفعل وضعي الكتابة واللاصق:

**chmod -v a+wt $LFS/sources**

هناك عدة طرق للحصول على جميع الحزم والرقع البرمجية اللازمة لبناء LFS:

- يمكن تحميل الملفات بشكل فردي كما هو موضح في القسمين التاليين.
- بالنسبة للإصدارات المستقرة من الكتاب، يمكن تحميل ملف tarball يحتوي على جميع الملفات المطلوبة من أحد مواقع المرايا المدرجة في https://www.linuxfromscratch.org/mirrors.html#files.

---

Linux From Scratch - Version 13.1-systemd

- يمكن تحميل الملفات باستخدام `wget` وقائمة `wget-list` كما هو موضح أدناه.

**لتحميل جميع الحزم والرقع البرمجية باستخدام `wget-list-systemd` كمدخل لأمر `wget` استخدم:**

**wget --input-file=wget-list-systemd --continue --directory-prefix=$LFS/sources**

بالإضافة إلى ذلك، وبدءاً من LFS-7.0، يوجد ملف منفصل باسم `md5sums` يمكن استخدامه للتحقق من توفر جميع الحزم الصحيحة قبل المتابعة. ضع هذا الملف في `$LFS/sources` وقم بتشغيل:

**pushd $LFS/sources**
**md5sum -c md5sums**
**popd**

يمكن إجراء هذا الفحص بعد استرداد الملفات المطلوبة بأي من الطرق المذكورة أعلاه.

إذا تم تحميل الحزم والرقع البرمجية كمستخدم غير root، فستكون هذه الملفات مملوكة لهذا المستخدم. يسجل نظام الملفات المالك عن طريق معرف المستخدم (UID)، ومعرف المستخدم العادي في توزيعة النظام المضيف غير معين في LFS. لذا ستظل الملفات مملوكة لمعرف UID غير مسمى في نظام LFS النهائي. إذا كنت لن تعين نفس الـ UID لمستخدمك في نظام LFS، فقم بتغيير ملاك هذه الملفات إلى root الآن لتجنب هذه المشكلة:

**chown root:root $LFS/sources/***

# 3.2. جميع الحزم

### ملاحظة

اقرأ التنبيهات الأمنية قبل تحميل الحزم لمعرفة ما إذا كان يجب استخدام إصدار أحدث من أي حزمة لتجنب الثغرات الأمنية.

قد يقوم المطورون الأصليون (upstream) بإزالة الإصدارات القديمة، خاصة عندما تحتوي تلك الإصدارات على ثغرة أمنية. إذا كان أحد الروابط أدناه غير متاح، يجب عليك قراءة التنبيهات الأمنية أولاً لمعرفة ما إذا كان يجب استخدام إصدار أحدث (تم فيه إصلاح الثغرة). إذا لم يكن الأمر كذلك، حاول تحميل الحزمة المحذوفة من إحدى المرايا. على الرغم من أنه من الممكن تحميل إصدار قديم من مرآة حتى لو تم حذفه بسبب ثغرة أمنية، إلا أنه ليس من الجيد استخدام إصدار معروف بأنه معرض للخطر عند بناء نظامك.

قم بتحميل أو الحصول على الحزم التالية:

**• Acl (2.4.0) - 376 KB:**
الصفحة الرئيسية: https://savannah.nongnu.org/projects/acl
التحميل: https://download.savannah.gnu.org/releases/acl/acl-2.4.0.tar.xz
MD5 sum: e289f370161698a96f50b2a3fdadf411

**• Attr (2.6.0) - 495 KB:**
الصفحة الرئيسية: https://savannah.nongnu.org/projects/attr
التحميل: https://download.savannah.gnu.org/releases/attr/attr-2.6.0.tar.gz
MD5 sum: 910a09c3ae0a211569d180586371cf7e

**• Autoconf (2.73) - 1,385 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/autoconf/
التحميل: https://ftpmirror.gnu.org/autoconf/autoconf-2.73.tar.xz
MD5 sum: 9cbad9a116ef845bafeed8e7bc771bf4

---

Linux From Scratch - Version 13.1-systemd

**• Automake (1.18.1) - 1,614 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/automake/
التحميل: https://ftpmirror.gnu.org/automake/automake-1.18.1.tar.xz
MD5 sum: cea31dbf1120f890cbf2a3032cfb9a68

**• Bash (5.3) - 11,089 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/bash/
التحميل: https://ftpmirror.gnu.org/bash/bash-5.3.tar.gz
MD5 sum: 977c8c0c5ae6309191e7768e28ebc951

**• Bc (7.0.3) - 464 KB:**
الصفحة الرئيسية: https://github.com/gavinhoward
التحميل: https://github.com/gavinhoward/bc/releases/download/7.0.3/bc-7.0.3.tar.xz
MD5 sum: ad4db5a0eb4fdbb3f6813be4b6b3da74

**• Binutils (2.47) - 28,355 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/binutils/
التحميل: https://sourceware.org/pub/binutils/releases/binutils-2.47.tar.xz
MD5 sum: d772acfbd55a81644e9fe7b8189cd2a5

**• Bison (3.8.2) - 2,752 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/bison/
التحميل: https://ftpmirror.gnu.org/bison/bison-3.8.2.tar.xz
MD5 sum: c28f119f405a2304ff0a7ccdcc629713

**• Bzip2 (1.0.8) - 792 KB:**
التحميل: https://www.sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz
MD5 sum: 67e051268d0c475ea773822f7500d0e5

**• Coreutils (9.11) - 6,409 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/coreutils/
التحميل: https://ftpmirror.gnu.org/coreutils/coreutils-9.11.tar.xz
MD5 sum: e52e9857e4aa9ae38ef32f8ed6a27604

**• D-Bus (1.16.2) - 1,090 KB:**
الصفحة الرئيسية: https://www.freedesktop.org/wiki/Software/dbus
التحميل: https://dbus.freedesktop.org/releases/dbus/dbus-1.16.2.tar.xz
MD5 sum: 97832e6f0a260936d28536e5349c22e5

**• DejaGNU (1.6.3) - 608 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/dejagnu/
التحميل: https://ftpmirror.gnu.org/dejagnu/dejagnu-1.6.3.tar.gz
MD5 sum: 68c5208c58236eba447d7d6d1326b821

**• Diffutils (3.12) - 1,894 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/diffutils/
التحميل: https://ftpmirror.gnu.org/diffutils/diffutils-3.12.tar.xz
MD5 sum: d1b18b20868fb561f77861cd90b05de4

**• E2fsprogs (1.47.4) - 9,870 KB:**
الصفحة الرئيسية: https://e2fsprogs.sourceforge.net/
التحميل: https://downloads.sourceforge.net/project/e2fsprogs/e2fsprogs/v1.47.4/e2fsprogs-1.47.4.tar.gz
MD5 sum: 733a93bc688314834ff2d10530ff4dc4

---

Linux From Scratch - Version 13.1-systemd

**• Elfutils (0.195) - 11,751 KB:**
الصفحة الرئيسية: https://sourceware.org/elfutils/
التحميل: https://sourceware.org/ftp/elfutils/0.195/elfutils-0.195.tar.bz2
MD5 sum: 3e8ef51c43beceddbbb74879549cf72c

**• Expat (2.8.3) - 506 KB:**
الصفحة الرئيسية: https://libexpat.github.io/
التحميل: https://github.com/libexpat/libexpat/releases/download/R_2_8_3/expat-2.8.3.tar.xz
MD5 sum: 1747f5a57b191f0373baeb5adc8078ca

**• Expect (5.45.4) - 618 KB:**
الصفحة الرئيسية: https://core.tcl.tk/expect/
التحميل: https://prdownloads.sourceforge.net/expect/expect5.45.4.tar.gz
MD5 sum: 00fce8de158422f5ccd2666512329bd2

**• File (5.48) - 2,631 KB:**
الصفحة الرئيسية: https://www.darwinsys.com/file/
التحميل: https://astron.com/pub/file/file-5.48.tar.gz
MD5 sum: 423686e97f731d8c24e9cd1a22b03dec

**• Findutils (4.11.0) - 2,394 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/findutils/
التحميل: https://ftpmirror.gnu.org/findutils/findutils-4.11.0.tar.xz
MD5 sum: 512c6875ed84034dca240c4bc9380b96

**• Flex (2.6.4) - 1,386 KB:**
الصفحة الرئيسية: https://github.com/westes/flex
التحميل: https://github.com/westes/flex/releases/download/v2.6.4/flex-2.6.4.tar.gz
MD5 sum: 2882e3179748cc9f9c23ec593d6adc8d

**• Flit-core (4.0.2) - 52 KB:**
الصفحة الرئيسية: https://pypi.org/project/flit-core/
التحميل: https://pypi.org/packages/source/f/flit-core/flit_core-4.0.2.tar.gz
MD5 sum: 89ebb783230fc8db6c1d2a39644b7085

**• Gawk (5.4.1) - 3,749 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/gawk/
التحميل: https://ftpmirror.gnu.org/gawk/gawk-5.4.1.tar.xz
MD5 sum: d379c2110e7a3e15347dd5559a41ad64

**• GCC (16.2.0) - 104,689 KB:**
الصفحة الرئيسية: https://gcc.gnu.org/
التحميل: https://ftpmirror.gnu.org/gcc/gcc-16.2.0/gcc-16.2.0.tar.xz
MD5 sum: 19b777fb19ea4982731392481306f0d3

**• GDBM (1.26) - 1,198 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/gdbm/
التحميل: https://ftpmirror.gnu.org/gdbm/gdbm-1.26.tar.gz
MD5 sum: aaa600665bc89e2febb3c7bd90679115

---

Linux From Scratch - Version 13.1-systemd

**• Gettext (1.0) - 10,471 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/gettext/
التحميل: https://ftpmirror.gnu.org/gettext/gettext-1.0.tar.xz
MD5 sum: dc8b2911535929cec1e263706b0a13a1

**• Glibc (2.44) - 20,138 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/libc/
التحميل: https://ftpmirror.gnu.org/glibc/glibc-2.44.tar.xz
MD5 sum: 7677da43ef759c68e005f5d4c37986a6