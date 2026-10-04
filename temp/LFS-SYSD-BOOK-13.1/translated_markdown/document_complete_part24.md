# 6.4. Bash-5.3

تحتوي حزمة Bash على غلاف Bourne-Again Shell.

**وقت البناء التقريبي:**
0.2 SBU
**مساحة القرص المطلوبة:**
73 ميجابايت

## 6.4.1. تثبيت Bash

تجهيز Bash للتجميع:

**./configure --prefix=/usr                      \**
**--build=$(sh support/config.guess) \**
**--host=$LFS_TGT                    \**
**--without-bash-malloc              \**
**--docdir=/usr/share/doc/bash-5.3**

**معنى خيارات التهيئة (configure):**

--without-bash-malloc

يقوم هذا الخيار بإيقاف استخدام دالة تخصيص الذاكرة (malloc) الخاصة بـ Bash، والمعروفة بتسببها في أخطاء تقسيم الذاكرة (segmentation faults). ومن خلال إيقاف هذا الخيار، سيستخدم Bash دوال malloc من مكتبة Glibc والتي تعد أكثر استقراراً.

تجميع الحزمة:

**make**

تثبيت الحزمة:

**make DESTDIR=$LFS install**

**إنشاء رابط للبرامج التي تستخدم sh كغلاف (shell):**

**ln -sv bash $LFS/bin/sh**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.39.2، "محتويات Bash".

---

Linux From Scratch - Version 13.1-systemd

# 6.5. Coreutils-9.11

تحتوي حزمة Coreutils على برامج الأدوات الأساسية التي يحتاجها كل نظام تشغيل.

**وقت البناء التقريبي:**
0.3 SBU
**مساحة القرص المطلوبة:**
193 ميجابايت

## 6.5.1. تثبيت Coreutils

تجهيز Coreutils للتجميع:

**./configure --prefix=/usr                     \**
**--host=$LFS_TGT                   \**
**--build=$(build-aux/config.guess) \**
**--enable-install-program=hostname**

**معنى خيارات التهيئة (configure):**

--enable-install-program=hostname

**يسمح هذا الخيار ببناء وتثبيت الملف الثنائي لـ hostname؛ وهو معطل افتراضياً ولكن تتطلبه مجموعة اختبارات Perl.**

تجميع الحزمة:

**make**

تثبيت الحزمة:

**make DESTDIR=$LFS install**

نقل البرامج إلى مواقعها النهائية المتوقعة. على الرغم من أن هذا ليس ضرورياً في هذه البيئة المؤقتة، إلا أنه يجب علينا القيام بذلك لأن بعض البرامج تستخدم مسارات ثابتة (hardcode) للملفات التنفيذية:

**mv -v $LFS/usr/bin/chroot              $LFS/usr/sbin**
**mkdir -pv $LFS/usr/share/man/man8**
**mv -v $LFS/usr/share/man/man1/chroot.1 $LFS/usr/share/man/man8/chroot.8**
**sed -i 's/"1"/"8"/'                    $LFS/usr/share/man/man8/chroot.8**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.61.2، "محتويات Coreutils".

---

Linux From Scratch - Version 13.1-systemd

# 6.6. Diffutils-3.12

تحتوي حزمة Diffutils على برامج تعرض الفروقات بين الملفات أو الأدلة.

**وقت البناء التقريبي:**
0.1 SBU
**مساحة القرص المطلوبة:**
35 ميجابايت

## 6.6.1. تثبيت Diffutils

تجهيز Diffutils للتجميع:

**./configure --prefix=/usr   \**
**--host=$LFS_TGT \**
**gl_cv_func_strcasecmp_works=yes \**
**--build=$(./build-aux/config.guess)**

**معنى خيارات التهيئة (configure):**

gl_cv_func_strcasecmp_works=yes

يحدد هذا الخيار نتيجة فحص دالة strcasecmp. يتطلب الفحص تشغيل برنامج C مجمّع، وهذا مستحيل أثناء التجميع المتقاطع لأن البرنامج المجمّع متقاطعاً لا يمكنه بشكل عام التشغيل على توزيعة النظام المضيف. عادةً ما يستخدم نص التهيئة قيمة احتياطية (fall-back) في حالة التجميع المتقاطع، ولكن القيمة الاحتياطية لهذا الفحص مفقودة، مما سيؤدي إلى توقف نص التهيئة عن العمل لعدم وجود قيمة يستخدمها. لقد قام المطورون الأصليون (Upstream) بإصلاح هذه المشكلة بالفعل، ولكن لتطبيق الإصلاح سنحتاج إلى تشغيل autoconf الذي قد يفتقر إليه النظام المضيف. لذا، نقوم ببساطة بتحديد نتيجة الفحص (yes لأننا نعلم أن دالة strcasecmp في Glibc-2.44 تعمل بشكل جيد)، وعندها سيستخدم نص التهيئة القيمة المحددة ويتجاوز عملية الفحص.

تجميع الحزمة:

**make**

تثبيت الحزمة:

**make DESTDIR=$LFS install**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.62.2، "محتويات Diffutils".

---

Linux From Scratch - Version 13.1-systemd

# 6.7. File-5.48

تحتوي حزمة File على أداة لتحديد نوع ملف أو مجموعة ملفات معينة.

**وقت البناء التقريبي:**
0.1 SBU
**مساحة القرص المطلوبة:**
46 ميجابايت

## 6.7.1. تثبيت File

**يجب أن يكون أمر file على النظام المضيف بنفس إصدار الإصدار الذي نقوم ببنائه من أجل إنشاء ملف التوقيع (signature file). قم بتشغيل الأوامر التالية لعمل نسخة مؤقتة من أمر file:**

**mkdir build**
**pushd build**
**../configure --disable-bzlib      \**
**--disable-libseccomp \**
**--disable-xzlib      \**
**--disable-zlib**
**make**
**popd**

**معنى خيار التهيئة الجديد:**

--disable-*

يحاول نص التهيئة استخدام بعض الحزم من توزيعة النظام المضيف إذا كانت ملفات المكتبات المقابلة موجودة. قد يتسبب ذلك في فشل التجميع إذا كان ملف المكتبة موجوداً ولكن ملفات الترويسات المقابلة غير موجودة. تمنع هذه الخيارات استخدام هذه القدرات غير الضرورية من النظام المضيف.

تجهيز File للتجميع:

**./configure --prefix=/usr --host=$LFS_TGT --build=$(./config.guess)**

تجميع الحزمة:

**make FILE_COMPILE=$(pwd)/build/src/file**

تثبيت الحزمة:

**make DESTDIR=$LFS install**

حذف ملف أرشيف libtool لأنه ضار بعملية التجميع المتقاطع:

**rm -v $LFS/usr/lib/libmagic.la**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.11.2، "محتويات File".

---

Linux From Scratch - Version 13.1-systemd

# 6.8. Findutils-4.11.0

تحتوي حزمة Findutils على برامج للبحث عن الملفات. توفر الحزمة برامج للبحث في جميع الملفات ضمن شجرة الأدلة، وإنشاء قاعدة بيانات وصيانتها والبحث فيها (غالباً ما تكون أسرع من البحث المتكرر، ولكنها غير موثوقة ما لم يتم تحديث قاعدة البيانات مؤخراً). كما توفر Findutils برنامج xargs، الذي يمكن استخدامه لتشغيل أمر محدد على كل ملف يتم اختياره بواسطة البحث.

**وقت البناء التقريبي:**
0.2 SBU
**مساحة القرص المطلوبة:**
51 ميجابايت

## 6.8.1. تثبيت Findutils

تجهيز Findutils للتجميع:

**./configure --prefix=/usr                   \**
**--localstatedir=/var/lib/locate \**
**--host=$LFS_TGT                 \**
**--build=$(build-aux/config.guess)**

تجميع الحزمة:

**make**

تثبيت الحزمة:

**make DESTDIR=$LFS install**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.63.2، "محتويات Findutils".

---

Linux From Scratch - Version 13.1-systemd

# 6.9. Gawk-5.4.1

تحتوي حزمة Gawk على برامج لمعالجة الملفات النصية.

**وقت البناء التقريبي:**
0.1 SBU
**مساحة القرص المطلوبة:**
52 ميجابايت

## 6.9.1. تثبيت Gawk

أولاً، تأكد من عدم تثبيت بعض الملفات غير الضرورية:

**sed -i 's/extras//' Makefile.in**

تجهيز Gawk للتجميع:

**./configure --prefix=/usr   \**
**--host=$LFS_TGT \**
**--build=$(build-aux/config.guess)**

تجميع الحزمة:

**make**

تثبيت الحزمة:

**make DESTDIR=$LFS install**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.31.2، "محتويات Gawk".

---

Linux From Scratch - Version 13.1-systemd

# 6.10. Grep-3.12

تحتوي حزمة Grep على برامج للبحث في محتويات الملفات.

**وقت البناء التقريبي:**
0.1 SBU
**مساحة القرص المطلوبة:**
32 ميجابايت

## 6.10.1. تثبيت Grep

تجهيز Grep للتجميع:

**./configure --prefix=/usr   \**
**--host=$LFS_TGT \**
**--build=$(./build-aux/config.guess)**

تجميع الحزمة:

**make**

تثبيت الحزمة:

**make DESTDIR=$LFS install**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.38.2، "محتويات Grep".

---

Linux From Scratch - Version 13.1-systemd

# 6.11. Gzip-1.14

تحتوي حزمة Gzip على برامج لضغط وفك ضغط الملفات.

**وقت البناء التقريبي:**
0.1 SBU
**مساحة القرص المطلوبة:**
12 ميجابايت

## 6.11.1. تثبيت Gzip

تجهيز Gzip للتجميع:

**./configure --prefix=/usr --host=$LFS_TGT**

تجميع الحزمة:

**make**

تثبيت الحزمة:

**make DESTDIR=$LFS install**

يمكن العثور على تفاصيل هذه الحزمة في القسم 8.66.2، "محتويات Gzip".

---

Linux From Scratch - Version 13.1-systemd