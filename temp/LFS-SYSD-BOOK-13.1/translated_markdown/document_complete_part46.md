# 8.55. Flit-Core-4.0.2

أداة Flit-core هي الجزء المسؤول عن بناء التوزيعات في Flit (وهي أداة تغليف لوحدات بايثون البسيطة).

**وقت البناء التقريبي:**
أقل من 0.1 SBU
**مساحة القرص المطلوبة:**
1.3 ميجابايت

## 8.55.1. تثبيت Flit-Core

بناء الحزمة:

**pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD**

تثبيت الحزمة:

**pip3 install --no-index --find-links dist flit_core**

**معاني خيارات تهيئة pip3 والأوامر المستخدمة:**

**wheel**

يقوم هذا الأمر ببناء أرشيف wheel لهذه الحزمة.

-w dist

يوجه pip لوضع ملف wheel الذي تم إنشاؤه في دليل dist.

--no-cache-dir

يمنع pip من نسخ ملف wheel المنشأ إلى دليل /root/.cache/pip.

**install**

يقوم هذا الأمر بتثبيت الحزمة.

--no-build-isolation, --no-deps, and --no-index

تمنع هذه الخيارات جلب الملفات من مستودع الحزم عبر الإنترنت (PyPI). إذا تم تثبيت الحزم بالترتيب الصحيح، فلن يحتاج pip إلى جلب أي ملفات في المقام الأول؛ وتضيف هذه الخيارات طبقة من الأمان في حالة حدوث خطأ من المستخدم.

--find-links dist

يوجه pip للبحث عن أرشيفات wheel في دليل dist.

## 8.55.2. محتويات Flit-Core

**الدليل المثبت:**
/usr/lib/python3.14/site-packages/flit_core
و
/usr/lib/python3.14/site-packages/flit_core-4.0.2.dist-info

---

Linux From Scratch - الإصدار 13.1-systemd

# 8.56. Packaging-26.3

وحدة packaging هي مكتبة بايثون توفر أدوات تنفذ مواصفات التوافق التشغيلي التي تمتلك سلوكاً صحيحاً واحداً محدداً (PEP440) أو تستفيد بشكل كبير من وجود تنفيذ مشترك واحد (PEP425). يتضمن ذلك أدوات للتعامل مع الإصدارات، والمحددات، والعلامات، والمتطلبات.

**وقت البناء التقريبي:**
أقل من 0.1 SBU
**مساحة القرص المطلوبة:**
3.0 ميجابايت

## 8.56.1. تثبيت Packaging

قم بتجميع packaging باستخدام الأمر التالي:

**pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD**

قم بتثبيت packaging باستخدام الأمر التالي:

**pip3 install --no-index --find-links dist packaging**

## 8.56.2. محتويات Packaging

**الأدلة المثبتة:**
/usr/lib/python3.14/site-packages/packaging
و
/usr/lib/python3.14/site-packages/packaging-26.3.dist-info

---

Linux From Scratch - الإصدار 13.1-systemd

# 8.57. Wheel-0.48.0

أداة Wheel هي مكتبة بايثون تمثل التنفيذ المرجعي لمعيار تغليف wheel الخاص ببايثون.

**وقت البناء التقريبي:**
أقل من 0.1 SBU
**مساحة القرص المطلوبة:**
768 كيلوبايت

## 8.57.1. تثبيت Wheel

قم بتجميع Wheel باستخدام الأمر التالي:

**pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD**

قم بتثبيت Wheel باستخدام الأمر التالي:

**pip3 install --no-index --find-links dist wheel**

## 8.57.2. محتويات Wheel

**البرنامج المثبت:**
wheel
**الأدلة المثبتة:**
/usr/lib/python3.14/site-packages/wheel
و
/usr/lib/python3.14/site-packages/wheel-0.48.0.dist-info

**وصف مختصر**

**wheel**
أداة لفك حزم أرشيفات wheel، أو حزمها، أو تحويلها.

---

Linux From Scratch - الإصدار 13.1-systemd

# 8.58. Setuptools-84.0.0

أداة Setuptools هي أداة تستخدم لتنزيل حزم بايثون وبنائها وتثبيتها وترقيتها وإلغاء تثبيتها.

**وقت البناء التقريبي:**
أقل من 0.1 SBU
**مساحة القرص المطلوبة:**
19 ميجابايت

## 8.58.1. تثبيت Setuptools

بناء الحزمة:

**pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD**

تثبيت الحزمة:

**pip3 install --no-index --find-links dist setuptools**

## 8.58.2. محتويات Setuptools

**الأدلة المثبتة:**
/usr/lib/python3.14/site-packages/_distutils_hack,
/usr/lib/python3.14/site-packages/pkg_resources, /usr/lib/python3.14/site-packages/setuptools, و /usr/lib/python3.14/site-packages/setuptools-84.0.0.dist-info

---

Linux From Scratch - الإصدار 13.1-systemd

# 8.59. Meson-1.12.0

نظام Meson هو نظام بناء مفتوح المصدر مصمم ليكون سريعاً للغاية وسهل الاستخدام قدر الإمكان.

**وقت البناء التقريبي:**
أقل من 0.1 SBU
**مساحة القرص المطلوبة:**
50 ميجابايت

## 8.59.1. تثبيت Meson

قم بتجميع Meson باستخدام الأمر التالي:

**pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD**

تتطلب مجموعة الاختبارات بعض الحزم التي تقع خارج نطاق LFS.

تثبيت الحزمة:

**pip3 install --no-index --find-links dist meson**
**install -vDm644 data/shell-completions/bash/meson /usr/share/bash-completion/completions/meson**
**install -vDm644 data/shell-completions/zsh/_meson /usr/share/zsh/site-functions/_meson**

**معاني معاملات التثبيت:**

-w dist

يضع ملفات wheel المنشأة في دليل dist.

--find-links dist

يثبت ملفات wheel من دليل dist.

## 8.59.2. محتويات Meson

**البرامج المثبتة:**
meson
**الدليل المثبت:**
/usr/lib/python3.14/site-packages/meson-1.12.0.dist-info و /usr/lib/python3.14/site-packages/mesonbuild

**وصف مختصر**

**meson**
نظام بناء عالي الإنتاجية.

---

Linux From Scratch - الإصدار 13.1-systemd

# 8.60. Kmod-34.2

تحتوي حزمة Kmod على مكتبات وأدوات لتحميل وحدات النواة (kernel modules).

**وقت البناء التقريبي:**
أقل من 0.1 SBU
**مساحة القرص المطلوبة:**
6.8 ميجابايت

## 8.60.1. تثبيت Kmod

تحضير Kmod للتجميع:

**mkdir -p build**
**cd       build**

**meson setup --prefix=/usr ..    \**
**--buildtype=release \**
**-D manpages=false**

**معاني خيارات التهيئة:**

-D manpages=false

يعطل هذا الخيار إنشاء صفحات الدليل (man pages) لأنها تتطلب برنامجاً خارجياً.

تجميع الحزمة:

**ninja**

تتطلب مجموعة اختبارات هذه الحزمة ترويسات النواة الخام (وليس ترويسات النواة "المنقحة" التي تم تثبيتها سابقاً)، وهو أمر خارج نطاق LFS.

الآن قم بتثبيت الحزمة:

**ninja install**

## 8.60.2. محتويات Kmod

**البرامج المثبتة:**
depmod (رابط إلى kmod), insmod (رابط إلى kmod), kmod, lsmod (رابط إلى kmod), modinfo (رابط إلى kmod), modprobe (رابط إلى kmod), و rmmod (رابط إلى kmod)
**المكتبة المثبتة:**
libkmod.so

**وصف مختصر**

**depmod**
ينشئ ملف تبعيات بناءً على الرموز التي يجدها في مجموعة الوحدات الموجودة؛ ويستخدم modprobe هذا الملف لتحميل الوحدات المطلوبة تلقائياً.

**insmod**
يثبت وحدة قابلة للتحميل في النواة التي تعمل حالياً.

**kmod**
يقوم بتحميل وإلغاء تحميل وحدات النواة.

**lsmod**
يسرد الوحدات المحملة حالياً.

**modinfo**
يفحص ملف كائن مرتبط بوحدة نواة ويعرض أي معلومات يمكن استخلاصها منه.

**modprobe**
يستخدم ملف التبعيات الذي أنشأه depmod لتحميل الوحدات ذات الصلة تلقائياً.

**rmmod**
يلغي تحميل الوحدات من النواة التي تعمل حالياً.

libkmod
تستخدم هذه المكتبة من قبل برامج أخرى لتحميل وإلغاء تحميل وحدات النواة.

---

Linux From Scratch - الإصدار 13.1-systemd

# 8.61. Coreutils-9.11

تحتوي حزمة Coreutils على برامج الأدوات الأساسية التي يحتاجها كل نظام تشغيل.

**وقت البناء التقريبي:**
1.2 SBU
**مساحة القرص المطلوبة:**
194 ميجابايت

## 8.61.1. تثبيت Coreutils

يتطلب معيار POSIX أن تتعرف برامج Coreutils على حدود الأحرف بشكل صحيح حتى في الإعدادات المحلية متعددة البايتات. تقوم الرقعة البرمجية التالية بإصلاح عدم الامتثال هذا وأخطاء أخرى متعلقة بالتدويل.

**patch -Np1 -i ../coreutils-9.11-i18n-1.patch**

### ملاحظة

تم العثور على العديد من الأخطاء في هذه الرقعة. عند الإبلاغ عن أخطاء جديدة لمطوري Coreutils، يرجى التحقق أولاً مما إذا كانت هذه الأخطاء قابلة للتكرار بدون هذه الرقعة.

الآن قم بتحضير Coreutils للتجميع:

**autoreconf -fv**
**automake -af**
**FORCE_UNSAFE_CONFIGURE=1 ./configure \**
**--prefix=/usr**

**معاني الأوامر وخيارات التهيئة:**

**autoreconf -fv**

قامت رقعة التدويل بتعديل نظام البناء، لذا يجب إعادة إنشاء ملفات التهيئة. عادةً ما نستخدم الخيار -i لتحديث الملفات المساعدة القياسية، ولكن بالنسبة لهذه الحزمة، لا يعمل ذلك لأن ملف configure.ac حدد إصداراً قديماً من gettext.

**automake -af**

لم يتم تحديث ملفات automake المساعدة بواسطة autoreconf بسبب فقدان الخيار -i. يقوم هذا الأمر بتحديثها لمنع فشل عملية البناء.

FORCE_UNSAFE_CONFIGURE=1

يسمح متغير البيئة هذا ببناء الحزمة بواسطة المستخدم root.

تجميع الحزمة:

**make**

انتقل مباشرة إلى "تثبيت الحزمة" إذا كنت لا تنوي تشغيل مجموعة الاختبارات.

الآن أصبحت مجموعة الاختبارات جاهزة للتشغيل. أولاً، قم بتشغيل الاختبارات المخصصة للعمل كمستخدم root:

**make NON_ROOT_USERNAME=tester check-root**

سنقوم بتشغيل بقية الاختبارات كمستخدم tester. تتطلب بعض الاختبارات أن يكون المستخدم عضواً في أكثر من مجموعة واحدة. لضمان عدم تخطي هذه الاختبارات، أضف مجموعة مؤقتة واجعل المستخدم tester جزءاً منها:

**groupadd -g 102 dummy -U tester**

قم بتصحيح بعض الصلاحيات حتى يتمكن المستخدم غير المتميز من تجميع وتشغيل الاختبارات:

**chown -R tester .**

---

Linux From Scratch - الإصدار 13.1-systemd

الآن قم بتشغيل الاختبارات (باستخدام /dev/null للمدخلات القياسية، وإلا فقد يتعطل اختباران إذا كنت تبني LFS في طرفية رسومية أو جلسة SSH أو GNU Screen لأن المدخلات القياسية تكون متصلة بـ PTY من التوزيعة المضيفة، ولا يمكن الوصول إلى عقدة الجهاز لهذا الـ PTY من بيئة chroot الخاصة بـ LFS):

**su tester -c "PATH=$PATH make -k RUN_EXPENSIVE_TESTS=yes check" \**
**< /dev/null**

إزالة المجموعة المؤقتة:

**groupdel dummy**

تثبيت الحزمة:

**make install**

نقل البرامج إلى المواقع المحددة بواسطة معيار FHS:

**mv -v /usr/bin/chroot /usr/sbin**
**mv -v /usr/share/man/man1/chroot.1 /usr/share/man/man8/chroot.8**
**sed -i 's/"1"/"8"/' /usr/share/man/man8/chroot.8**