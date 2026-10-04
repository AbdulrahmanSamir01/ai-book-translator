### ملاحظة
يقوم فريق Linux From Scratch بإنشاء ملف tarball خاص به لصفحات الدليل (man pages) باستخدام الكود المصدري لـ systemd، وذلك لتجنب التبعيات غير الضرورية.

**• Tar (1.35) - 2,263 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/tar/
التحميل: https://ftpmirror.gnu.org/tar/tar-1.35.tar.xz
مجموع MD5: a2d8042658cfd8ea939e6d911eaf4152

**• Tcl (8.6.18) - 11,540 KB:**
الصفحة الرئيسية: https://tcl.sourceforge.net/
التحميل: https://downloads.sourceforge.net/tcl/tcl8.6.18-src.tar.gz
مجموع MD5: acfe0c9f7d0c626ecf026e834a888da6

**• Tcl Documentation (8.6.18) - 1,172 KB:**
التحميل: https://downloads.sourceforge.net/tcl/tcl8.6.18-html.tar.gz
مجموع MD5: 54d1ff0f5eee4e81e5cdaa4baa343397

**• Texinfo (7.3) - 6,778 KB:**
الصفحة الرئيسية: https://www.gnu.org/software/texinfo/
التحميل: https://ftpmirror.gnu.org/texinfo/texinfo-7.3.tar.xz
مجموع MD5: 915a09fcdfc2bf0f5ecf9e556d5698ff

**• Time Zone Data (2026c) - 465 KB:**
الصفحة الرئيسية: https://www.iana.org/time-zones
التحميل: https://www.iana.org/time-zones/repository/releases/tzdata2026c.tar.gz
مجموع MD5: bff7174205cefab793e3b24271ef2f45

**• Util-linux (2.42.2) - 10,409 KB:**
الصفحة الرئيسية: https://git.kernel.org/pub/scm/utils/util-linux/util-linux.git/
التحميل: https://www.kernel.org/pub/linux/utils/util-linux/v2.42/util-linux-2.42.2.tar.xz
مجموع MD5: 1d70131b70abda3dec3b37e282a20c96

---

Linux From Scratch - الإصدار 13.1-systemd

**• Vim (9.2.1025) - 19,662 KB:**
الصفحة الرئيسية: https://www.vim.org
التحميل: https://github.com/vim/vim/archive/v9.2.1025/vim-9.2.1025.tar.gz
مجموع MD5: 060c9c0d7e2bdb5e5d80daad596cae02

### ملاحظة
يتغير إصدار vim يومياً. للحصول على أحدث إصدار، تفضل بزيارة https://github.com/vim/vim/tags.

**• Wheel (0.48.0) - 65 KB:**
الصفحة الرئيسية: https://pypi.org/project/wheel/
التحميل: https://pypi.org/packages/source/w/wheel/wheel-0.48.0.tar.gz
مجموع MD5: f668e4885de814378b332eceea04a8a0

**• Xz Utils (5.8.3) - 1,512 KB:**
الصفحة الرئيسية: https://tukaani.org/xz
التحميل: https://github.com//tukaani-project/xz/releases/download/v5.8.3/xz-5.8.3.tar.xz
مجموع MD5: a02753f34e5546d20213b87f876a0933

**• Zlib (1.3.2) - 1,468 KB:**
الصفحة الرئيسية: https://zlib.net/
التحميل: https://zlib.net/fossils/zlib-1.3.2.tar.gz
مجموع MD5: a1e6c958597af3c67d162995a342138a

**• Zstd (1.5.7) - 2,378 KB:**
الصفحة الرئيسية: https://facebook.github.io/zstd/
التحميل: https://github.com/facebook/zstd/releases/download/v1.5.7/zstd-1.5.7.tar.gz
مجموع MD5: 780fc1896922b1bc52a4e90980cdda48

إجمالي حجم هذه الحزم: حوالي 628 ميجابايت

# 3.3. الرقع البرمجية المطلوبة

بالإضافة إلى الحزم، هناك حاجة إلى عدة رقع برمجية (patches). تقوم هذه الرقع بتصحيح أي أخطاء في الحزم والتي ينبغي للمطور الأصلي إصلاحها، كما تجري تعديلات طفيفة لجعل التعامل مع الحزم أكثر سهولة. ستحتاج إلى الرقع التالية لبناء نظام LFS:

**• رقعة توثيق Bzip2 - 1.6 KB:**
التحميل: https://www.linuxfromscratch.org/patches/lfs/13.1/bzip2-1.0.8-install_docs-1.patch
مجموع MD5: 6a5ac7e89b791aae556de0f745916f7f

**• رقعة إصلاحات التدويل لـ Coreutils - 67 KB:**
التحميل: https://www.linuxfromscratch.org/patches/lfs/13.1/coreutils-9.11-i18n-1.patch
مجموع MD5: 900d64d9936516b68613271c9ebc0059

**• رقعة Expect GCC15 - 12 KB:**
التحميل: https://www.linuxfromscratch.org/patches/lfs/13.1/expect-5.45.4-gcc15-1.patch
مجموع MD5: 0ca4d6bb8d572fbcdb13cb36cd34833e

**• رقعة إصلاحات المطورين الأصليين لـ Glibc - 172 KB:**
التحميل: https://www.linuxfromscratch.org/patches/lfs/13.1/glibc-2.44-upstream_fixes-1.patch
مجموع MD5: 990574184b25aa3029a2444e81865098

---

Linux From Scratch - الإصدار 13.1-systemd

**• رقعة Glibc FHS - 2.8 KB:**
التحميل: https://www.linuxfromscratch.org/patches/lfs/13.1/glibc-fhs-1.patch
مجموع MD5: 9a5997c3452909b1769918c759eff8a2

**• رقعة إصلاح Backspace/Delete لـ Kbd - 12 KB:**
التحميل: https://www.linuxfromscratch.org/patches/lfs/13.1/kbd-2.10.0-backspace-1.patch
مجموع MD5: f75cca16a38da6caa7d52151f7136895

**• رقعة Python Openssl4 - 38 KB:**
التحميل: https://www.linuxfromscratch.org/patches/lfs/13.1/Python-3.14.7-openssl_4-1.patch
مجموع MD5: 597d7737df1b4ea4e184c193da523050

**• رقعة المطورين الأصليين لـ Tar - 4.3 KB:**
التحميل: https://www.linuxfromscratch.org/patches/lfs/13.1/tar-1.35-acl_fix-1.patch
مجموع MD5: dbab49e317105539611866dac5dd54f6

إجمالي حجم هذه الرقع: حوالي 309.7 كيلوبايت

بالإضافة إلى الرقع المطلوبة أعلاه، توجد مجموعة من الرقع الاختيارية التي أنشأها مجتمع LFS. تحل هذه الرقع الاختيارية مشاكل بسيطة أو تفعل وظائف غير مفعلة افتراضياً. يمكنك تصفح قاعدة بيانات الرقع الموجودة في https://www.linuxfromscratch.org/patches/downloads/ والحصول على أي رقع إضافية تناسب احتياجات نظامك.

---

Linux From Scratch - الإصدار 13.1-systemd

# الفصل 4. التحضيرات النهائية

# 4.1. مقدمة

في هذا الفصل، سنقوم ببعض المهام الإضافية للتحضير لبناء النظام المؤقت. سنقوم بإنشاء مجموعة من الأدلة في `$LFS` (والتي سنقوم بتثبيت الأدوات المؤقتة فيها)، وإضافة مستخدم غير متميز الصلاحيات، وإنشاء بيئة بناء مناسبة لهذا المستخدم. سنقوم أيضاً بشرح وحدات الزمن ("SBUs") التي نستخدمها لقياس الوقت المستغرق لبناء حزم LFS، وتوفير بعض المعلومات حول مجموعات اختبار الحزم.

# 4.2. إنشاء تخطيط أدلة محدود في نظام ملفات LFS

في هذا القسم، نبدأ بملء نظام ملفات LFS بالأجزاء التي ستشكل نظام لينكس النهائي. الخطوة الأولى هي إنشاء تسلسل هرمي محدود للأدلة، بحيث يمكن تثبيت البرامج التي تم تجميعها في الفصل 6 (وكذلك glibc و libstdc++ في الفصل 5) في مواقعها النهائية. نفعل ذلك لكي يتم استبدال تلك البرامج المؤقتة عندما يتم بناء الإصدارات النهائية في الفصل 8.

قم بإنشاء تخطيط الأدلة المطلوب عن طريق تنفيذ الأوامر التالية بصلاحيات root:

```bash
mkdir -pv $LFS/{etc,var} $LFS/usr/{bin,lib,sbin}

for i in bin lib sbin; do
ln -sv usr/$i $LFS/$i
done

case $(uname -m) in
x86_64) mkdir -pv $LFS/lib64 ;;
esac
```

سيتم تجميع البرامج في الفصل 6 باستخدام مجمع متقاطع (Cross-compiler) (يمكن العثور على مزيد من التفاصيل في قسم الملاحظات الفنية لسلسلة الأدوات). سيتم تثبيت هذا المجمع المتقاطع في دليل خاص لفصله عن البرامج الأخرى. بينما لا تزال تعمل بصلاحيات root، قم بإنشاء ذلك الدليل باستخدام هذا الأمر:

```bash
mkdir -pv $LFS/tools
```

### ملاحظة
لقد قرر محررو LFS عمداً عدم استخدام دليل `/usr/lib64`. تم اتخاذ عدة خطوات للتأكد من أن سلسلة الأدوات لن تستخدمه. إذا ظهر هذا الدليل لأي سبب (سواء بسبب خطأ في اتباع التعليمات، أو لأنك قمت بتثبيت حزمة ثنائية أنشأته بعد الانتهاء من LFS)، فقد يؤدي ذلك إلى تعطل نظامك. يجب أن تتأكد دائماً من عدم وجود هذا الدليل.

# 4.3. إضافة مستخدم LFS

عند تسجيل الدخول كمستخدم root، يمكن لخطأ واحد أن يتلف أو يدمر النظام. لذلك، يتم بناء الحزم في الفصلين القادمين كمستخدم غير متميز الصلاحيات. يمكنك استخدام اسم المستخدم الخاص بك، ولكن لتسهيل إعداد بيئة عمل نظيفة، سنقوم بإنشاء مستخدم جديد يسمى `lfs` كعضو في مجموعة جديدة (تسمى أيضاً `lfs`) وتشغيل الأوامر بصفتنا `lfs` أثناء عملية التثبيت. بصفتك root، نفذ الأوامر التالية لإضافة المستخدم الجديد:

```bash
groupadd lfs
useradd -s /bin/bash -g lfs -m -k /dev/null lfs
```

**إليك معنى خيارات سطر الأوامر:**

`-s /bin/bash`
**يجعل bash هو الغلاف (shell) الافتراضي للمستخدم lfs.**

---

Linux From Scratch - الإصدار 13.1-systemd

`-g lfs`
هذا الخيار يضيف المستخدم lfs إلى المجموعة lfs.

`-m`
هذا ينشئ دليلاً منزلياً للمستخدم lfs.

`-k /dev/null`
يمنع هذا المعامل إمكانية نسخ الملفات من دليل الهيكل (الافتراضي هو `/etc/skel`) عن طريق تغيير موقع الإدخال إلى جهاز null الخاص.

`lfs`
هذا هو اسم المستخدم الجديد.

إذا كنت ترغب في تسجيل الدخول كـ lfs أو الانتقال إلى lfs من مستخدم غير root (على عكس الانتقال إلى المستخدم lfs عند تسجيل الدخول كـ root، وهو ما لا يتطلب وجود كلمة مرور للمستخدم lfs)، فأنت بحاجة إلى تعيين كلمة مرور لـ lfs. نفذ الأمر التالي كمستخدم root لتعيين كلمة المرور:

```bash
passwd lfs
```

امنح lfs وصولاً كاملاً إلى جميع الأدلة الموجودة تحت `$LFS` بجعل lfs هو المالك:

```bash
chown -v lfs $LFS/{usr{,/*},var,etc,tools}
case $(uname -m) in
x86_64) chown -v lfs $LFS/lib64 ;;
esac
```

### ملاحظة
**في بعض الأنظمة المضيفة، لا يكتمل أمر `su` التالي بشكل صحيح ويقوم بتعليق تسجيل الدخول للمستخدم lfs في الخلفية. إذا لم يظهر الموجه "lfs:~$" فوراً، فإن إدخال الأمر `fg` سيحل المشكلة.**

بعد ذلك، ابدأ غلافاً (shell) يعمل كمستخدم lfs. يمكن القيام بذلك عن طريق تسجيل الدخول كـ lfs على وحدة تحكم افتراضية، أو باستخدام أمر تبديل المستخدم التالي:

```bash
su - lfs
```

**تخبر علامة "-" أمر `su` ببدء غلاف تسجيل دخول (login shell) بدلاً من غلاف غير تسجيل دخول. الفرق بين هذين النوعين من الأغلفة موضح بالتفصيل في `bash(1)` و `info bash`.**