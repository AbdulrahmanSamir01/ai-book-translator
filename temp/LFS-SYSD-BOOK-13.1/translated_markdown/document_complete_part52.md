# 8.75. MarkupSafe-3.0.3

MarkupSafe هي وحدة بايثون (Python module) تقوم بتنفيذ سلسلة نصوص آمنة لترميز XML/HTML/XHTML.

**وقت البناء التقريبي:**
أقل من 0.1 SBU
**مساحة القرص المطلوبة:**
696 كيلوبايت

## 8.75.1. تثبيت MarkupSafe

قم بتجميع MarkupSafe باستخدام الأمر التالي:

**pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD**

هذه الحزمة لا تأتي مع مجموعة اختبارات.

تثبيت الحزمة:

**pip3 install --no-index --find-links dist Markupsafe**

## 8.75.2. محتويات MarkupSafe

**دليل التثبيت:**
/usr/lib/python3.14/site-packages/MarkupSafe-3.0.3.dist-info

---

Linux From Scratch - Version 13.1-systemd

# 8.76. Jinja2-3.1.6

Jinja2 هي وحدة بايثون تقوم بتنفيذ لغة قوالب بسيطة بأسلوب بايثوني (pythonic).

**وقت البناء التقريبي:**
أقل من 0.1 SBU
**مساحة القرص المطلوبة:**
2.7 ميجابايت

## 8.76.1. تثبيت Jinja2

بناء الحزمة:

**pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD**

تثبيت الحزمة:

**pip3 install --no-index --find-links dist Jinja2**

## 8.76.2. محتويات Jinja2

**دليل التثبيت:**
/usr/lib/python3.14/site-packages/Jinja2-3.1.6.dist-info

---

Linux From Scratch - Version 13.1-systemd

# 8.77. Systemd-261.2

تحتوي حزمة systemd على البرامج المسؤولة عن التحكم في بدء تشغيل النظام، وتشغيله، وإيقافه.

**وقت البناء التقريبي:**
1.2 SBU
**مساحة القرص المطلوبة:**
396 ميجابايت

## 8.77.1. تثبيت systemd

قم بإزالة مجموعتين غير مطلوبتين، render و sgx، من قواعد udev الافتراضية:

**sed -e 's/GROUP="render"/GROUP="video"/' \**
**-e 's/GROUP="sgx", //'               \**
**-i rules.d/50-udev-default.rules.in**

تحضير systemd للتجميع:

**mkdir -p build**
**cd       build**

**meson setup ..                \**
**--prefix=/usr           \**
**--buildtype=release     \**
**-D default-dnssec=no    \**
**-D firstboot=false      \**
**-D install-tests=false  \**
**-D ldconfig=false       \**
**-D sysusers=false       \**
**-D rpmmacrosdir=no      \**
**-D homed=disabled       \**
**-D man=disabled         \**
**-D mode=release         \**
**-D pamconfdir=no        \**
**-D dev-kvm-mode=0660    \**
**-D nobody-group=nogroup \**
**-D sysupdate=disabled   \**
**-D ukify=disabled       \**
**-D docdir=/usr/share/doc/systemd-261.2**

**معاني خيارات meson:**

--buildtype=release

هذا المفتاح يتجاوز نوع البناء الافتراضي ("debug")، والذي ينتج ملفات ثنائية غير محسنة.

-D default-dnssec=no

هذا المفتاح يقوم بإيقاف دعم DNSSEC التجريبي.

-D firstboot=false

هذا المفتاح يمنع تثبيت خدمات systemd المسؤولة عن تهيئة النظام للمرة الأولى. هذه الخدمات غير مفيدة في LFS لأن كل شيء يتم يدوياً.

-D install-tests=false

هذا المفتاح يمنع تثبيت الاختبارات المجمعة.

-D ldconfig=false

**هذا المفتاح يمنع تثبيت وحدة systemd التي تقوم بتشغيل ldconfig عند الإقلاع؛ وهذا غير مفيد للتوزيعات المبنية من المصدر مثل LFS، كما أنه يجعل وقت الإقلاع أطول. قم بإزالة هذا الخيار لتمكين تشغيل ldconfig عند الإقلاع.**

---

Linux From Scratch - Version 13.1-systemd

-D sysusers=false

هذا المفتاح يمنع تثبيت خدمات systemd المسؤولة عن تهيئة ملفي /etc/group و /etc/passwd. لقد تم إنشاء كلا الملفين في الفصل السابق. هذا البرنامج الخفي (daemon) غير مفيد في نظام LFS لأن حسابات المستخدمين يتم إنشاؤها يدوياً.

-D rpmmacrosdir=no

هذا المفتاح يعطل تثبيت ماكرو RPM لاستخدامه مع systemd، لأن LFS لا يدعم RPM.

-D homed=disabled

إزالة البرنامج الخفي الذي يمتلك تبعيات لا تقع ضمن نطاق LFS.

-D man=disabled

منع توليد صفحات الدليل (man pages) لتجنب التبعيات الإضافية. سنقوم بتثبيت صفحات دليل مجمعة مسبقاً لـ systemd من أرشيف tarball.

-D mode=release

تعطيل بعض الميزات التي يعتبرها المطورون الأصليون (upstream) تجريبية.

-D pamconfdir=no

منع تثبيت ملف تهيئة PAM غير فعال على LFS.

-D dev-kvm-mode=0660

قاعدة udev الافتراضية تسمح لجميع المستخدمين بالوصول إلى /dev/kvm، وهو ما يعتبره المحررون أمراً خطيراً. هذا الخيار يتجاوز ذلك.

-D nobody-group=nogroup

إبلاغ الحزمة أن اسم المجموعة ذات المعرف GID 65534 هو nogroup.

-D sysupdate=disabled

**لا تقم بتثبيت أداة systemd-sysupdate. لقد صُممت لتحديث التوزيعات الثنائية تلقائياً، لذا فهي عديمة الفائدة** لنظام لينكس أساسي مبني من المصدر. كما أنها ستبلغ عن أخطاء عند الإقلاع إذا تم تفعيلها دون تهيئتها بشكل صحيح.

-D ukify=disabled

**لا تقم بتثبيت نص systemd-ukify البرمجي. يتطلب هذا النص عند التشغيل وحدة pefile الخاصة ببايثون، والتي لا يوفرها LFS ولا BLFS.**

تجميع الحزمة:

**ninja**

هناك اختبار يقوم بإنشاء نقطة ربط في /tmp لا يمكننا تنظيفها بسهولة بعد تشغيل مجموعة الاختبارات، كما أن بعض الاختبارات تتطلب ملف /etc/os-release أساسي. لاختبار النتائج، قم بإنشاء هذا الملف وتشغيل مجموعة الاختبارات في مساحة أسماء ربط (mount namespace) منفصلة (بحيث تكون نقطة الربط مرئية فقط لمجموعة الاختبارات ويتم تنظيفها تلقائياً بعد الانتهاء):

**echo 'NAME="Linux From Scratch"' > /etc/os-release**
**unshare -m ninja test**

من المعروف أن ثلاثة اختبارات تفشل في بيئة chroot الخاصة بـ LFS ولكنها تنجح في التثبيت الكامل: core - systemd:test-namespace، و test - systemd:test-chase، و tmpfiles - systemd:test-systemd-tmpfiles. قد تفشل بعض الاختبارات الإضافية لأنها تعتمد على خيارات تهيئة مختلفة للنواة. الاختبار المسمى test - systemd:test-copy قد ينتهي وقته (time out) بسبب ازدحام الإدخال/الإخراج عند استخدام عدد كبير من المهام المتوازية، ولكنه سينجح إذا تم تشغيله بمفرده عبر الأمر meson test test-copy.

تثبيت الحزمة:

**ninja install**

---

Linux From Scratch - Version 13.1-systemd

تثبيت صفحات الدليل:

**tar -xf ../../systemd-man-pages-261.2.tar.xz \**
**--no-same-owner --strip-components=1     \**
**-C /usr/share/man**

**إنشاء ملف /etc/machine-id المطلوب بواسطة systemd-journald:**

**systemd-machine-id-setup**

إعداد هيكل الأهداف (target structure) الأساسي:

**systemctl preset-all**

## 8.77.2. محتويات systemd

**البرامج المثبتة:**
bootctl, busctl, coredumpctl, halt (رابط رمزي إلى systemctl), hostnamectl, init, journalctl, kernel-install, localectl, loginctl, machinectl, mount.ddi (رابط رمزي إلى systemd-dissect), networkctl, oomctl, portablectl, poweroff (رابط رمزي إلى systemctl), reboot (رابط رمزي إلى systemctl), resolvconf (رابط رمزي إلى resolvectl), resolvectl, run0 (رابط رمزي إلى systemd-run), runlevel (رابط رمزي إلى systemctl), shutdown (رابط رمزي إلى systemctl), systemctl, systemd-ac-power, systemd-analyze, systemd-ask-password, systemd-cat, systemd-cgls, systemd-cgtop, systemd-confext (رابط رمزي إلى systemd-sysext), systemd-creds, systemd-delta, systemd-detect-virt, systemd-dissect, systemd-escape, systemd-hwdb, systemd-id128, systemd-inhibit, systemd-machine-id-setup, systemd-mount, systemd-notify, systemd-nspawn, systemd-path, systemd-pty-forward, systemd-repart, systemd-resolve (رابط رمزي إلى resolvectl), systemd-run, systemd-socket-activate, systemd-stdio-bridge, systemd-sysext, systemd-tmpfiles, systemd-tty-ask-password-agent, systemd-vpick, systemd-umount (رابط رمزي إلى systemd-mount), timedatectl, udevadm, userdbctl, and varlinkctl

**المكتبات المثبتة:**
libnss_myhostname.so.2, libnss_mymachines.so.2, libnss_resolve.so.2, libnss_systemd.so.2, libsystemd.so, libsystemd-shared-261.2.so (في /usr/lib/systemd), و libudev.so

**الأدلة المثبتة:**
/etc/binfmt.d, /etc/init.d, /etc/kernel, /etc/modules-load.d, /etc/sysctl.d, /etc/systemd, /etc/tmpfiles.d, /etc/udev, /etc/xdg/systemd, /usr/include/systemd, /usr/lib/binfmt.d, /usr/lib/credstore, /usr/lib/environment.d, /usr/lib/kernel, /usr/lib/modprobe.d, /usr/lib/modules-load.d, /usr/lib/systemd, /usr/lib/udev, /usr/lib/sysctl.d, /usr/lib/systemd, /usr/lib/tmpfiles.d, /usr/share/doc/systemd-261.2, /usr/share/factory, /usr/share/systemd, /var/lib/systemd, و /var/log/journal