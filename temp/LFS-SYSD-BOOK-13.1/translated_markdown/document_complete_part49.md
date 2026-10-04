# 8.65. GRUB-2.14

تحتوي حزمة GRUB على محمل الإقلاع الموحد (GRand Unified Bootloader).

### ملاحظة

تم تقسيم هذه الصفحة إلى عدة أقسام تهدف إلى التثبيت وفقاً لطريقة إقلاع محددة (BIOS، و UEFI 64-بت، و UEFI 32-بت). لا يمكن بناء GRUB لجميع بنيات طرق الإقلاع في وقت واحد.

يمكنك تخطي الأقسام الأخرى والانتقال مباشرة إلى طريقة الإقلاع التي تحتاجها. إذا كنت في شك، يمكنك اتباع جميع الأقسام على حساب زيادة وقت البناء. بعد تثبيت الدعم الخاص بطريقة الإقلاع لديك، استمر في بناء بقية الحزم في هذا الفصل. سيتم مناقشة جعل نظام LFS الخاص بك قابلاً للإقلاع باستخدام GRUB في القسم 10.4، "استخدام GRUB لإعداد عملية الإقلاع".

### تحذير

قم بإلغاء تعيين أي متغيرات بيئية قد تؤثر على عملية البناء:

**unset {C,CPP,CXX,LD}FLAGS**

لا تحاول "ضبط" هذه الحزمة باستخدام أعلام تجميع مخصصة؛ فهذه الحزمة هي محمل إقلاع (bootloader)، والعمليات منخفضة المستوى في الكود المصدري قد تتعطل بسبب التحسينات القوية (aggressive optimization).

**وقت البناء التقريبي:**
1.0 SBU
**مساحة القرص المطلوبة:**
245 ميجابايت

## 8.65.1. تثبيت GRUB لنظام BIOS

أولاً، قم بإصلاح خطأ (bug) ظهر في الإصدار grub-2.14:

**sed 's/--image-base/--nonexist-linker-option/' -i configure**

جهز GRUB للتجميع:

**./configure --prefix=/usr     \**
**--sysconfdir=/etc \**
**--disable-efiemu  \**
**--disable-werror**

**معنى خيارات التهيئة الجديدة:**

`--disable-werror`

يسمح هذا الخيار بإتمام عملية البناء رغم وجود تحذيرات ناتجة عن الإصدارات الأحدث من Flex.

`--disable-efiemu`

يقلل هذا الخيار من حجم ما يتم بناؤه عن طريق تعطيل ميزة معينة وإزالة بعض برامج الاختبار غير الضرورية لنظام LFS.

قم بتجميع الحزمة:

**make**

لا يُنصح بتشغيل مجموعة الاختبارات لهذه الحزمة، حيث تعتمد معظم الاختبارات على حزم غير متوفرة في بيئة LFS المحدودة. إذا كنت ترغب في تشغيل الاختبارات على أي حال، فقم بتنفيذ `make check`.

ثبّت الحزمة:

**make install**

---

Linux From Scratch - Version 13.1-systemd

## 8.65.2. تثبيت GRUB لنظام UEFI 64-بت

إذا كنت ترغب في الإقلاع باستخدام UEFI 64-بت، يجب عليك بناء الدعم الخاص به.

أولاً، إذا كنت قد بنيت GRUB من القسم السابق، قم بتنظيف شجرة المصدر:

**make clean**

الآن قم بتهيئة GRUB لدعم UEFI 64-بت:

**./configure --prefix=/usr       \**
**--sysconfdir=/etc   \**
**--target=x86_64     \**
**--with-platform=efi \**
**--disable-efiemu    \**
**--disable-werror**

**معنى خيارات التهيئة الجديدة:**

`--target=x86_64`

يحدد أن بنية البرنامج الثابت (firmware) لـ UEFI هي x86_64، والتي يجب أن يستهدفها GRUB.

`--with-platform=efi`

يحدد أن EFI هي المنصة التي يجب أن يستهدفها GRUB. وبالتزامن مع `--target=x86_64` سيتمكن GRUB من استهداف منصة x86_64-efi.

قم بتجميع الحزمة لدعم UEFI 64-بت:

**make**

ثبّت الدعم الخاص بـ UEFI 64-بت:

**make install**

## 8.65.3. تثبيت GRUB لنظام UEFI 32-بت

إذا كنت ترغب في الإقلاع باستخدام UEFI 32-بت (وهو أمر نادر جداً)، يجب عليك بناء الدعم الخاص به.

أولاً، إذا كنت قد بنيت GRUB من أي من الأقسام السابقة، قم بتنظيف شجرة المصدر:

**make clean**

الآن قم بتهيئة GRUB لدعم UEFI 32-بت:

**./configure --prefix=/usr       \**
**--sysconfdir=/etc   \**
**--target=i386       \**
**--with-platform=efi \**
**--disable-efiemu    \**
**--disable-werror**

**معنى خيارات التهيئة الجديدة:**

`--target=i386`

يحدد أن بنية البرنامج الثابت لـ UEFI هي i386/32-بت، والتي يجب أن يستهدفها GRUB. وبالتزامن مع `--with-platform=efi` سيتمكن GRUB من استهداف منصة i386-efi.

قم بتجميع الحزمة لدعم UEFI 32-بت:

**make**

---

Linux From Scratch - Version 13.1-systemd

ثبّت الدعم الخاص بـ UEFI 32-بت:

**make install**

## 8.65.4. محتويات GRUB

**البرامج المثبتة:**
`grub-bios-setup`, `grub-editenv`, `grub-file`, `grub-fstest`, `grub-glue-efi`, `grub-install`, `grub-kbdcomp`, `grub-macbless`, `grub-menulst2cfg`, `grub-mkconfig`, `grub-mkimage`, `grub-mklayout`, `grub-mknetdir`, `grub-mkpasswd-pbkdf2`, `grub-mkrelpath`, `grub-mkrescue`, `grub-mkstandalone`, `grub-ofpathname`, `grub-probe`, `grub-reboot`, `grub-render-label`, `grub-script-check`, `grub-set-default`, `grub-sparc64-setup`, و `grub-syslinux2cfg`

**الأدلة المثبتة:**
`/usr/lib/grub`, `/etc/grub.d`, `/usr/share/grub`, و `/boot/grub` (عند تشغيل `grub-install` لأول مرة)

### ملاحظة

سيحتوي الدليل `/usr/lib/grub` على محتويات مختلفة بناءً على المنصة (أو المنصات) التي قمت بتثبيت GRUB لها؛ حيث ستكون هناك وحدات (modules) GRUB مختلفة لكل منصة.

**وصف موجز**

**grub-bios-setup**
برنامج مساعد لـ `grub-install`.

**grub-editenv**
أداة لتحرير كتلة البيئة (environment block).

**grub-file**
يتحقق مما إذا كان الملف المعطى من النوع المحدد.

**grub-fstest**
أداة لتصحيح أخطاء برنامج تشغيل نظام الملفات.

**grub-glue-efi**
يدمج الملفات الثنائية 32-بت و 64-بت في ملف واحد (لأجهزة Apple).

**grub-install**
يثبت GRUB على القرص الخاص بك.

**grub-kbdcomp**
نص برمجي يحول تخطيط xkb إلى تخطيط يتعرف عليه GRUB.

**grub-macbless**
يقوم بعملية "bless" بنمط Mac لأنظمة ملفات HFS أو HFS+ (عملية bless خاصة بأجهزة Apple وتجعل الجهاز قابلاً للإقلاع).

**grub-menulst2cfg**
يحول ملف `menu.lst` الخاص بـ GRUB Legacy إلى ملف `grub.cfg` لاستخدامه مع GRUB 2.

**grub-mkconfig**
ينشئ ملف `grub.cfg`.

**grub-mkimage**
ينشئ صورة قابلة للإقلاع من GRUB.

**grub-mklayout**
ينشئ ملف تخطيط لوحة مفاتيح لـ GRUB.

**grub-mknetdir**
يجهز دليل الإقلاع عبر الشبكة (netboot) لـ GRUB.

**grub-mkpasswd-pbkdf2**
ينشئ كلمة مرور مشفرة بنظام PBKDF2 لاستخدامها في قائمة الإقلاع.

**grub-mkrelpath**
يجعل مسار النظام نسبياً بالنسبة للجذر.

**grub-mkrescue**
ينشئ صورة قابلة للإقلاع من GRUB مناسبة لقرص مرن، أو CDROM/DVD، أو وحدة تخزين USB.

**grub-mkstandalone**
ينشئ صورة مستقلة (standalone image).

**grub-ofpathname**
برنامج مساعد يطبع المسار المؤدي إلى جهاز GRUB.

**grub-probe**
يفحص معلومات الجهاز لمسار أو جهاز معين.

**grub-reboot**
يحدد إدخال الإقلاع الافتراضي لـ GRUB لعملية الإقلاع القادمة فقط.

**grub-render-label**
يعالج ملف `.disk_label` الخاص بأجهزة Apple Mac.

---

Linux From Scratch - Version 13.1-systemd

**grub-script-check**
يفحص نص تهيئة GRUB بحثاً عن أخطاء في الصيغة (syntax errors).

**grub-set-default**
يحدد إدخال الإقلاع الافتراضي لـ GRUB.

**grub-sparc64-setup**
برنامج مساعد لـ `grub-setup`.

**grub-syslinux2cfg**
يحول ملف تهيئة syslinux إلى تنسيق `grub.cfg`.

---

Linux From Scratch - Version 13.1-systemd

# 8.66. Gzip-1.14

تحتوي حزمة Gzip على برامج لضغط الملفات وفك ضغطها.

**وقت البناء التقريبي:**
0.1 SBU
**مساحة القرص المطلوبة:**
21 ميجابايت

## 8.66.1. تثبيت Gzip

جهز Gzip للتجميع:

**./configure --prefix=/usr**

قم بتجميع الحزمة:

**make**

لاختبار النتائج، نفذ الأمر التالي:

**make check**

ثبّت الحزمة:

**make install**

## 8.66.2. محتويات Gzip

**البرامج المثبتة:**
`gunzip`, `gzexe`, `gzip`, `uncompress` (رابط صلب مع gunzip), `zcat`, `zcmp`, `zdiff`, `zegrep`, `zfgrep`, `zforce`, `zgrep`, `zless`, `zmore`, و `znew`

**وصف موجز**

**gunzip**
يفك ضغط الملفات المضغوطة بصيغة gzip.

**gzexe**
ينشئ ملفات تنفيذية ذاتية فك الضغط.

**gzip**
يضغط الملفات المعطاة باستخدام ترميز Lempel-Ziv (LZ77).

**uncompress**
يفك ضغط الملفات المضغوطة.

**zcat**
يفك ضغط ملفات gzip المعطاة إلى المخرج القياسي.

**zcmp**
يشغل الأمر `cmp` على ملفات gzip.

**zdiff**
يشغل الأمر `diff` على ملفات gzip.

**zegrep**
يشغل الأمر `egrep` على ملفات gzip.

**zfgrep**
يشغل الأمر `fgrep` على ملفات gzip.

**zforce**
يفرض امتداد `.gz` على جميع الملفات المعطاة التي هي بالفعل ملفات gzip، حتى لا يقوم `gzip` بضغطها مرة أخرى؛ وهذا مفيد عندما يتم اقتطاع أسماء الملفات أثناء نقلها.

**zgrep**
يشغل الأمر `grep` على ملفات gzip.

**zless**
يشغل الأمر `less` على ملفات gzip.

**zmore**
يشغل الأمر `more` على ملفات gzip.

**znew**
يعيد ضغط الملفات من تنسيق compress إلى تنسيق gzip (من `.Z` إلى `.gz`).

---

Linux From Scratch - Version 13.1-systemd