# 5.4. ترويسات API الخاصة بـ Linux-7.1.8

تقوم ترويسات API الخاصة بلينكس (الموجودة في الملف `linux-7.1.8.tar.xz`) بكشف واجهة برمجة تطبيقات النواة (Kernel API) لاستخدامها بواسطة مكتبة Glibc.

**وقت البناء التقريبي:**
أقل من 0.1 SBU
**المساحة المطلوبة من القرص:**
1.8 جيجابايت

## 5.4.1. تثبيت ترويسات API الخاصة بلينكس

تحتاج نواة لينكس إلى كشف واجهة برمجة تطبيقات (API) لتستخدمها مكتبة لغة C الخاصة بالنظام (وهي Glibc في LFS). يتم ذلك عن طريق تنقية ملفات ترويسات C المختلفة التي يتم شحنها في ملف tarball الخاص بالكود المصدري لنواة لينكس.

تأكد من عدم وجود ملفات قديمة مدمجة في الحزمة:

**make mrproper**

الآن قم باستخراج ترويسات النواة المرئية للمستخدم من المصدر. لا يمكن استخدام هدف make الموصى به "headers_install" لأنه يتطلب `rsync` الذي قد لا يكون متاحاً. يتم وضع الترويسات أولاً في `./usr` ثم نسخها إلى الموقع المطلوب.

**make headers**
**find usr/include -type f ! -name '*.h' -delete**
**cp -rv usr/include $LFS/usr**

## 5.4.2. محتويات ترويسات API الخاصة بلينكس

**الترويسات المثبتة:**
`/usr/include/asm/*.h`, `/usr/include/asm-generic/*.h`, `/usr/include/drm/*.h`, `/usr/include/linux/*.h`, `/usr/include/misc/*.h`, `/usr/include/mtd/*.h`, `/usr/include/rdma/*.h`, `/usr/include/scsi/*.h`, `/usr/include/sound/*.h`, `/usr/include/video/*.h`, و `/usr/include/xen/*.h`

**الأدلة المثبتة:**
`/usr/include/asm`, `/usr/include/asm-generic`, `/usr/include/drm`, `/usr/include/linux`, `/usr/include/misc`, `/usr/include/mtd`, `/usr/include/rdma`, `/usr/include/scsi`, `/usr/include/sound`, `/usr/include/video`, و `/usr/include/xen`

**وصف موجز**

`/usr/include/asm/*.h`
ترويسات ASM الخاصة بـ Linux API

`/usr/include/asm-generic/*.h`
ترويسات ASM العامة الخاصة بـ Linux API

`/usr/include/drm/*.h`
ترويسات DRM الخاصة بـ Linux API

`/usr/include/linux/*.h`
ترويسات Linux الخاصة بـ Linux API

`/usr/include/misc/*.h`
ترويسات متنوعة خاصة بـ Linux API

`/usr/include/mtd/*.h`
ترويسات MTD الخاصة بـ Linux API

`/usr/include/rdma/*.h`
ترويسات RDMA الخاصة بـ Linux API

`/usr/include/scsi/*.h`
ترويسات SCSI الخاصة بـ Linux API

`/usr/include/sound/*.h`
ترويسات الصوت الخاصة بـ Linux API

`/usr/include/video/*.h`
ترويسات الفيديو الخاصة بـ Linux API

`/usr/include/xen/*.h`
ترويسات Xen الخاصة بـ Linux API

---

Linux From Scratch - الإصدار 13.1-systemd

# 5.5. Glibc-2.44

تحتوي حزمة Glibc على مكتبة C الرئيسية. توفر هذه المكتبة الروتينات الأساسية لتخصيص الذاكرة، والبحث في الأدلة، وفتح وإغلاق الملفات، وقراءة وكتابة الملفات، ومعالجة النصوص، ومطابقة الأنماط، والعمليات الحسابية، وما إلى ذلك.

**وقت البناء التقريبي:**
1.3 SBU
**المساحة المطلوبة من القرص:**
900 ميجابايت

## 5.5.1. تثبيت Glibc

أولاً، قم بإنشاء رابط رمزي للامتثال لمعيار LSB. بالإضافة إلى ذلك، بالنسبة لمعمارية x86_64، قم بإنشاء رابط رمزي للتوافق مطلوب للتشغيل السليم للمحمل الديناميكي للمكتبات:

**case $(uname -m) in**
**i?86)   ln -sfv ld-linux.so.2 $LFS/lib/ld-lsb.so.3**
**;;**
**x86_64) ln -sfv ../lib/ld-linux-x86-64.so.2 $LFS/lib64**
**ln -sfv ../lib/ld-linux-x86-64.so.2 $LFS/lib64/ld-lsb-x86-64.so.3**
**;;**
**esac**

### ملاحظة

**الأمر أعلاه صحيح. يحتوي الأمر `ln` على عدة إصدارات نحوية، لذا تأكد من مراجعة `info coreutils ln` و `ln(1)` قبل الإبلاغ عما قد يبدو خطأً.**

تستخدم بعض برامج Glibc الدليل `/var/db` غير المتوافق مع معيار FHS لتخزين بيانات وقت التشغيل الخاصة بها. قم بتطبيق الرقعة البرمجية التالية لجعل هذه البرامج تخزن بيانات وقت التشغيل في المواقع المتوافقة مع FHS:

**patch -Np1 -i ../glibc-fhs-1.patch**

إصلاح مشكلة تتسبب في تعطل دالة `tanh(3)` على بعض معالجات x86_64 القديمة، ولإصلاح عملية التثبيت عند استخدام مهام `make` متعددة:

**patch -Np1 -i ../glibc-2.44-upstream_fixes-1.patch**

توصي وثائق Glibc ببناء Glibc في دليل بناء مخصص:

**mkdir -v build**
**cd       build**

**تأكد من تثبيت أدوات `ldconfig` و `sln` في `/usr/sbin`:**

**echo "rootsbindir=/usr/sbin" > configparms**

بعد ذلك، قم بتهيئة Glibc للتجميع:

**../configure                             \**
**--prefix=/usr                      \**
**--host=$LFS_TGT                    \**
**--build=$(../scripts/config.guess) \**
**--disable-nscd                     \**
**libc_cv_slibdir=/usr/lib           \**
**--enable-kernel=5.10**

**معاني خيارات التهيئة:**

`--host=$LFS_TGT`, `--build=$(../scripts/config.guess)`

التأثير المشترك لهذه المفاتيح هو أن نظام بناء Glibc يقوم بتهيئة نفسه ليتم تجميعه بشكل متقاطع، باستخدام الرابط المتقاطع والمجمّع المتقاطع الموجودين في `$LFS/tools`.

---

Linux From Scratch - الإصدار 13.1-systemd

`--enable-kernel=5.10`

يخبر هذا Glibc بتجميع المكتبة مع دعم لنواة لينكس 5.10 والإصدارات الأحدث. لا يتم تفعيل الحلول البديلة للنوى الأقدم.

`libc_cv_slibdir=/usr/lib`

يضمن ذلك تثبيت المكتبة في `/usr/lib` بدلاً من المسار الافتراضي `/lib64` في الأجهزة ذات 64 بت.

`--disable-nscd`

عدم بناء برنامج خدمة ذاكرة أسماء النطاقات (name service cache daemon) الذي لم يعد مستخدماً.

خلال هذه المرحلة، قد يظهر التحذير التالي:

`configure: WARNING:`
`*** These auxiliary programs are missing or`
`*** incompatible versions: msgfmt`
`*** some features will be disabled.`
`*** Check the INSTALL file for required versions.`

**برنامج `msgfmt` المفقود أو غير المتوافق غير ضار بشكل عام. هذا البرنامج هو جزء من حزمة Gettext، والتي يجب أن توفرها توزيعة النظام المضيف.**

### ملاحظة

وردت تقارير تفيد بأن هذه الحزمة قد تفشل عند البناء باستخدام "تجميع متوازٍ" (parallel make). إذا حدث ذلك، قم بتشغيل أمر `make` مرة أخرى مع خيار `-j1`.

تجميع الحزمة:

**make**

تثبيت الحزمة:

### تحذير

إذا لم يتم ضبط متغير LFS بشكل صحيح، وبالرغم من التوصيات، كنت تقوم بالبناء بصلاحيات الجذر (root)، فإن الأمر التالي سيقوم بتثبيت Glibc المبنية حديثاً على نظامك المضيف، وهو ما سيجعل النظام غير قابل للاستخدام على الأرجح. لذا تأكد مرتين من ضبط البيئة بشكل صحيح، وأنك لست مستخدماً جذراً، قبل تشغيل الأمر التالي.

**make DESTDIR=$LFS install**

**معنى خيار `make install`:**

`DESTDIR=$LFS`

يُستخدم متغير `DESTDIR` في `make` بواسطة جميع الحزم تقريباً لتحديد الموقع الذي يجب تثبيت الحزمة فيه. إذا لم يتم ضبطه، فإنه يذهب افتراضياً إلى دليل الجذر (`/`). هنا نحدد أن الحزمة تُثبت في `$LFS` والذي سيصبح دليل الجذر في القسم 7.4، "الدخول إلى بيئة chroot".

**إصلاح مسار مكتوب بشكل ثابت (hard coded) للمحمل التنفيذي في نص `ldd`:**

**sed '/RTLDLIST=/s@/usr@@g' -i $LFS/usr/bin/ldd**

الآن بعد أن أصبحت سلسلة الأدوات المتقاطعة جاهزة، من المهم التأكد من أن التجميع والربط سيعملان كما هو متوقع. نقوم بذلك عن طريق إجراء بعض الفحوصات الأولية:

**echo 'int main(){}' | $LFS_TGT-gcc -x c - -v -Wl,--verbose &> dummy.log**
**$LFS_TGT-readelf -l a.out | grep ': /lib'**

---

Linux From Scratch - الإصدار 13.1-systemd

يجب ألا تكون هناك أخطاء، وسيكون مخرج الأمر الأخير (مع مراعاة الاختلافات حسب المنصة في اسم الرابط الديناميكي):

`[Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]`

لاحظ أن هذا المسار لا يجب أن يحتوي على `/mnt/lfs` (أو قيمة متغير LFS إذا كنت تستخدم قيمة مختلفة). يتم تحليل المسار عند تنفيذ البرنامج المجمّع، وهذا لا يجب أن يحدث إلا بعد دخولنا إلى بيئة chroot حيث ستعتبر النواة `$LFS` كدليل جذر (`/`).

الآن تأكد من أننا مهيؤون لاستخدام ملفات البدء الصحيحة:

**grep -E -o "$LFS/lib.*/S?crt[1in].*succeeded" dummy.log**

يجب أن يكون مخرج الأمر الأخير:

`/mnt/lfs/lib/../lib/Scrt1.o succeeded`
`/mnt/lfs/lib/../lib/crti.o succeeded`
`/mnt/lfs/lib/../lib/crtn.o succeeded`

تحقق من أن المجمّع يبحث عن ملفات الترويسات الصحيحة:

**grep -B3 "^ $LFS/usr/include" dummy.log**

يجب أن يعيد هذا الأمر المخرج التالي:

`#include <...> search starts here:`
`/mnt/lfs/tools/lib/gcc/x86_64-lfs-linux-gnu/16.2.0/include`
`/mnt/lfs/tools/lib/gcc/x86_64-lfs-linux-gnu/16.2.0/include-fixed`
`/mnt/lfs/usr/include`

مرة أخرى، قد يختلف الدليل المسمى حسب الثلاثية النظامية الخاصة بك عما سبق، اعتماداً على معمارية نظامك.

بعد ذلك، تحقق من أن الرابط الجديد يُستخدم مع مسارات البحث الصحيحة:

**grep 'SEARCH.*/usr/lib' dummy.log |sed 's|; \n|g'**

يجب تجاهل الإشارات إلى المسارات التي تحتوي على مكونات بها `-linux-gnu` ، ولكن بخلاف ذلك يجب أن يكون مخرج الأمر الأخير:

`SEARCH_DIR("=/mnt/lfs/tools/x86_64-lfs-linux-gnu/lib64")`
`SEARCH_DIR("=/usr/local/lib64")`
`SEARCH_DIR("=/lib64")`
`SEARCH_DIR("=/usr/lib64")`
`SEARCH_DIR("=/mnt/lfs/tools/x86_64-lfs-linux-gnu/lib")`
`SEARCH_DIR("=/usr/local/lib")`
`SEARCH_DIR("=/lib")`
`SEARCH_DIR("=/usr/lib");`

قد يستخدم نظام 32 بت بعض الأدلة الأخرى، ولكن في كل الأحوال الجانب المهم هنا هو أن جميع المسارات يجب أن تبدأ بعلامة يساوي (`=`) والتي سيتم استبدالها بدليل sysroot الذي قمنا بتهيئته للرابط.

بعد ذلك تأكد من أننا نستخدم libc الصحيحة:

**grep "/lib.*/libc.so.6 " dummy.log**

يجب أن يكون مخرج الأمر الأخير:

`attempt to open /mnt/lfs/usr/lib/libc.so.6 succeeded`

تأكد من أن GCC يستخدم الرابط الديناميكي الصحيح:

**grep found dummy.log**

---

Linux From Scratch - الإصدار 13.1-systemd

يجب أن يكون مخرج الأمر الأخير (مع مراعاة الاختلافات حسب المنصة في اسم الرابط الديناميكي):

`found ld-linux-x86-64.so.2 at /mnt/lfs/usr/lib/ld-linux-x86-64.so.2`

إذا لم يظهر المخرج كما هو موضح أعلاه أو لم يتم استلامه على الإطلاق، فهذا يعني أن هناك خطأً جسيماً. ابحث وتتبع الخطوات لمعرفة مكان المشكلة وقم بتصحيحها. يجب حل أي مشكلات قبل المتابعة في العملية.

بمجرد أن يعمل كل شيء بشكل صحيح، قم بتنظيف ملفات الاختبار:

**rm -v a.out dummy.log**

### ملاحظة

سيكون بناء الحزم في الفصل التالي بمثابة فحص إضافي للتأكد من بناء سلسلة الأدوات بشكل صحيح. إذا فشلت بعض الحزم في البناء، خاصة Binutils-pass2 أو GCC-pass2، فهذا مؤشر على حدوث خطأ ما في عمليات تثبيت Binutils أو GCC أو Glibc السابقة.

تفاصيل هذه الحزمة موجودة في القسم 8.5.3، "محتويات Glibc".

---

Linux From Scratch - الإصدار 13.1-systemd