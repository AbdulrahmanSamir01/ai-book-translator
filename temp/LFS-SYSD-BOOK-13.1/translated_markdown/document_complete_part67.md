# 11.5. البداية بعد بناء LFS

## 11.5.1. تحديد الخطوة التالية

الآن وقد اكتمل بناء LFS وأصبح لديك نظام قابل للإقلاع، ماذا تفعل بعد ذلك؟ الخطوة التالية هي تحديد كيفية استخدام هذا النظام.
بشكل عام، هناك فئتان رئيسيتان للنظر فيهما: محطة عمل (Workstation) أو خادم (Server). وفي الواقع، هاتان الفئتان ليستا متنافيتين؛ إذ يمكن دمج التطبيقات المطلوبة لكل فئة في نظام واحد، ولكن دعنا نستعرضهما بشكل منفصل في الوقت الحالي.

يُعد الخادم الفئة الأبسط، حيث يتكون عادةً من خادم ويب مثل Apache HTTP Server وخادم قاعدة بيانات مثل MariaDB، ومع ذلك، يمكن إضافة خدمات أخرى. كما تندرج أنظمة التشغيل المدمجة في الأجهزة ذات الغرض الواحد ضمن هذه الفئة.

من ناحية أخرى، تُعد محطة العمل أكثر تعقيداً بكثير؛ فهي تتطلب عادةً بيئة مستخدم رسومية مثل LXDE أو XFCE أو KDE أو Gnome، تعتمد على بيئة رسومية أساسية ومجموعة من التطبيقات الرسومية مثل متصفح Firefox، أو عميل البريد Thunderbird، أو حزمة LibreOffice المكتبية. وتتطلب هذه التطبيقات مئات الحزم الإضافية من تطبيقات الدعم والمكتبات (حسب القدرات المطلوبة).

بالإضافة إلى ما سبق، هناك مجموعة من تطبيقات إدارة النظام التي تناسب جميع أنواع الأنظمة، وجميع هذه التطبيقات موجودة في كتاب BLFS. لا تتوفر جميع الحزم في كل بيئة؛ فعلى سبيل المثال، لا يُعد `dhcpcd` مناسباً عادةً للخوادم، بينما تكون `wireless_tools` مفيدة فقط لأنظمة الحواسيب المحمولة.

## 11.5.2. العمل في بيئة LFS أساسية

عندما تقوم بالإقلاع في نظام LFS لأول مرة، ستجد جميع الأدوات الداخلية اللازمة لبناء حزم إضافية، ولكن لسوء الحظ، تكون بيئة المستخدم شحيحة للغاية. هناك عدة طرق لتحسين ذلك:

---

Linux From Scratch - الإصدار 13.1-systemd

**11.5.2.1. العمل من النظام المضيف لـ LFS عبر بيئة chroot**

توفر هذه الطريقة بيئة رسومية كاملة حيث يتوفر متصفح كامل الميزات وإمكانيات النسخ واللصق. وتسمح هذه الطريقة باستخدام تطبيقات مثل نسخة `wget` الموجودة في النظام المضيف لتنزيل مصادر الحزم إلى موقع متاح عند العمل داخل بيئة chroot.

من أجل بناء الحزم بشكل صحيح داخل chroot، يجب أن تتذكر ربط أنظمة الملفات الافتراضية إذا لم تكن مربوطة بالفعل. إحدى طرق القيام بذلك هي إنشاء نص برمجي على النظام المضيف (HOST):

```bash
cat > ~/mount-virt.sh << "EOF"
#!/bin/bash

function mountbind
{
if ! mountpoint $LFS/$1 >/dev/null; then
$SUDO mount --bind /$1 $LFS/$1
echo $LFS/$1 mounted
else
echo $LFS/$1 already mounted
fi
}

function mounttype
{
if ! mountpoint $LFS/$1 >/dev/null; then
$SUDO mount -t $2 $3 $4 $5 $LFS/$1
echo $LFS/$1 mounted
else
echo $LFS/$1 already mounted
fi
}

if [ $EUID -ne 0 ]; then
SUDO=sudo
else
SUDO=""
fi

if [ x$LFS == x ]; then
echo "LFS not set"
exit 1
fi

mountbind dev
mounttype dev/pts devpts devpts -o gid=5,mode=620
mounttype proc    proc   proc
mounttype sys     sysfs  sysfs
mounttype run     tmpfs  run
if [ -h $LFS/dev/shm ]; then
install -v -d -m 1777 $LFS$(realpath /dev/shm)
else
mounttype dev/shm tmpfs tmpfs -o nosuid,nodev
fi

#mountbind usr/src
#mountbind boot
#mountbind home
EOF
```

لاحظ أن الأوامر الثلاثة الأخيرة في النص البرمجي معطلة (بواسطة التعليق `#`). تكون هذه الأوامر مفيدة إذا كانت تلك الأدلة مربوطة كأقسام منفصلة على النظام المضيف وسيتم ربطها عند إقلاع نظام LFS/BLFS المكتمل.

---

Linux From Scratch - الإصدار 13.1-systemd

يمكن تشغيل النص البرمجي باستخدام `bash ~/mount-virt.sh` إما كمستخدم عادي (وهو الموصى به) أو كجذر (root). إذا تم تشغيله كمستخدم عادي، فإن `sudo` مطلوب على النظام المضيف.

مسألة أخرى يثيرها النص البرمجي هي مكان تخزين ملفات الحزم التي تم تنزيلها. هذا الموقع اختياري؛ يمكن أن يكون في دليل المنزل لمستخدم عادي مثل `~/sources` أو في موقع عام مثل `/usr/src`. توصيتنا هي عدم خلط مصادر BLFS ومصادر LFS في دليل `/sources` (من داخل بيئة chroot). وفي كل الأحوال، يجب أن تكون الحزم قابلة للوصول من داخل بيئة chroot.

ميزة تسهيل أخيرة مقدمة هنا هي تسريع عملية الدخول إلى بيئة chroot. يمكن القيام بذلك عن طريق إنشاء اسم مستعار (alias) في ملف `~/.bashrc` الخاص بالمستخدم على النظام المضيف:

```bash
alias lfs='sudo /usr/sbin/chroot /mnt/lfs /usr/bin/env -i HOME=/root TERM="$TERM" PS1="\u:\w\\$ " PATH=/usr/bin:/usr/sbin /bin/bash --login'
```

هذا الاسم المستعار معقد قليلاً بسبب علامات الاقتباس ومستويات رموز الهروب (backslash). يجب أن يكون بالكامل في سطر واحد. (تم تقسيم الأمر أعلاه في النص الأصلي لأغراض العرض فقط).

**11.5.2.2. العمل عن بُعد عبر ssh**

توفر هذه الطريقة أيضاً بيئة رسومية كاملة، ولكنها تتطلب أولاً تثبيت `sshd` على نظام LFS، وعادة ما يتم ذلك داخل chroot. كما تتطلب جهاز كمبيوتر ثانٍ. تتميز هذه الطريقة بالبساطة لأنها لا تتطلب تعقيدات بيئة chroot، كما أنها تستخدم النواة التي بنيتها في LFS لجميع الحزم الإضافية، وتوفر نظاماً كاملاً لتثبيت الحزم.

يمكنك استخدام الأمر `scp` لرفع مصادر الحزم المراد بناؤها إلى نظام LFS. أما إذا كنت ترغب في تنزيل المصادر مباشرة على نظام LFS، فقم بتثبيت `libtasn1` و `p11-kit` و `make-ca` و `wget` داخل chroot (أو ارفع مصادرها باستخدام `scp` بعد إقلاع نظام LFS).

**11.5.2.3. العمل من سطر أوامر LFS**

تتطلب هذه الطريقة تثبيت `libtasn1` و `p11-kit` و `make-ca` و `wget` و `gpm` و `links` (أو `lynx`) داخل chroot، ثم إعادة الإقلاع في نظام LFS الجديد. في هذه المرحلة، يحتوي النظام الافتراضي على ست وحدات تحكم افتراضية (virtual consoles). التبديل بين الوحدات سهل باستخدام تركيبات المفاتيح `Alt+Fx` حيث تكون `Fx` بين F1 و F6. كما تقوم تركيبات `Alt+←` و `Alt+→` بتغيير وحدة التحكم أيضاً.

في هذه المرحلة، يمكنك تسجيل الدخول إلى وحدتي تحكم افتراضيتين مختلفتين وتشغيل متصفح `links` أو `lynx` في إحدى الوحدات و `bash` في الأخرى. يتيح برنامج GPM بعد ذلك نسخ الأوامر من المتصفح باستخدام زر الماوس الأيسر، ثم التبديل إلى الوحدة الأخرى ولصقها.

### ملاحظة

كملاحظة جانبية، يمكن أيضاً التبديل بين وحدات التحكم الافتراضية من داخل نافذة X Window باستخدام تركيب المفاتيح `Ctrl+Alt+Fx` ، ولكن عملية النسخ بالماوس لا تعمل بين الواجهة الرسومية ووحدة التحكم الافتراضية. يمكنك العودة إلى عرض X Window باستخدام تركيب `Ctrl+Alt+Fx` ، حيث تكون `Fx` عادةً F1 ولكن قد تكون F7.

---

Linux From Scratch - الإصدار 13.1-systemd

# الجزء الخامس. الملاحق

---

Linux From Scratch - الإصدار 13.1-systemd

# الملحق أ. الاختصارات والمصطلحات

**ABI**
واجهة التطبيق الثنائية (Application Binary Interface)

**ALFS**
نظام LFS المؤتمت (Automated Linux From Scratch)

**API**
واجهة برمجة التطبيقات (Application Programming Interface)

**ASCII**
الكود الأمريكي القياسي لتبادل المعلومات (American Standard Code for Information Interchange)

**BIOS**
نظام الإدخال/الإخراج الأساسي (Basic Input/Output System)

**BLFS**
ما بعد LFS (Beyond Linux From Scratch)

**BSD**
توزيع بركلي للبرمجيات (Berkeley Software Distribution)

**chroot**
تغيير الجذر (change root)

**CMOS**
أشباه الموصلات المعدنية المكملة (Complementary Metal Oxide Semiconductor)

**COS**
فئة الخدمة (Class Of Service)

**CPU**
وحدة المعالجة المركزية (Central Processing Unit)

**CRC**
فحص التكرار الدوري (Cyclic Redundancy Check)

**CVS**
نظام الإصدارات المتزامنة (Concurrent Versions System)

**DHCP**
بروتوكول تهيئة المضيف الديناميكي (Dynamic Host Configuration Protocol)

**DNS**
نظام أسماء النطاقات (Domain Name Service)

**EGA**
محول الرسوميات المحسن (Enhanced Graphics Adapter)

**ELF**
تنسيق الملفات القابلة للتنفيذ والربط (Executable and Linkable Format)

**EOF**
نهاية الملف (End of File)

**EQN**
المعادلات (equation)

**ext2**
نظام الملفات الممتد الثاني (second extended file system)

**ext3**
نظام الملفات الممتد الثالث (third extended file system)

**ext4**
نظام الملفات الممتد الرابع (fourth extended file system)

**FAQ**
الأسئلة الشائعة (Frequently Asked Questions)

**FHS**
معيار تسلسل الملفات (Filesystem Hierarchy Standard)

**FIFO**
ما يدخل أولاً يخرج أولاً (First-In, First Out)

**FQDN**
اسم النطاق المؤهل بالكامل (Fully Qualified Domain Name)

**FTP**
بروتوكول نقل الملفات (File Transfer Protocol)

**GB**
جيجابايت (Gigabytes)

**GCC**
مجموعة مجمّعات GNU (GNU Compiler Collection)

**GID**
معرف المجموعة (Group Identifier)

**GMT**
توقيت غرينتش (Greenwich Mean Time)

**HTML**
لغة توصيف النصوص التشعبية (Hypertext Markup Language)

**IDE**
إلكترونيات الأقراص المتكاملة (Integrated Drive Electronics)

**IEEE**
معهد مهندسي الكهرباء والإلكترونيات (Institute of Electrical and Electronic Engineers)

---

Linux From Scratch - الإصدار 13.1-systemd

**IO**
الإدخال/الإخراج (Input/Output)

**IP**
بروتوكول الإنترنت (Internet Protocol)

**IPC**
التواصل بين العمليات (Inter-Process Communication)

**IRC**
دردشة تتابع الإنترنت (Internet Relay Chat)

**ISO**
المنظمة الدولية للمعايير (International Organization for Standardization)

**ISP**
مزود خدمة الإنترنت (Internet Service Provider)

**KB**
كيلوبايت (Kilobytes)

**LED**
الصمام الثنائي الباعث للضوء (Light Emitting Diode)

**LFS**
لينكس من الصفر (Linux From Scratch)

**LSB**
القاعدة القياسية للينكس (Linux Standard Base)

**MB**
ميجابايت (Megabytes)

**MBR**
سجل الإقلاع الرئيسي (Master Boot Record)

**MD5**
مجموع رسالة MD5 (Message Digest 5)

**NIC**
بطاقة واجهة الشبكة (Network Interface Card)

**NLS**
دعم اللغات الأصلية (Native Language Support)

**NNTP**
بروتوكول نقل أخبار الشبكة (Network News Transport Protocol)

**NPTL**
مكتبة خيوط POSIX الأصلية (Native POSIX Threading Library)

**OSS**
نظام الصوت المفتوح (Open Sound System)

**PCH**
ترويسات مجمعة مسبقاً (Pre-Compiled Headers)

**PCRE**
التعبيرات النمطية المتوافقة مع بيرل (Perl Compatible Regular Expression)

**PID**
معرف العملية (Process Identifier)

**PTY**
طرفية وهمية (pseudo terminal)

**QOS**
جودة الخدمة (Quality Of Service)

**RAM**
ذاكرة الوصول العشوائي (Random Access Memory)

**RPC**
استدعاء الإجراءات عن بُعد (Remote Procedure Call)

**RTC**
ساعة الوقت الحقيقي (Real Time Clock)

**SBU**
وحدة بناء النظام القياسية (Standard Build Unit)

**SCO**
عملية سانتا كروز (The Santa Cruz Operation)

**SHA1**
خوارزمية التجزئة الآمنة 1 (Secure-Hash Algorithm 1)

**TLDP**
مشروع توثيق لينكس (The Linux Documentation Project)

**TFTP**
بروتوكول نقل الملفات البسيط (Trivial File Transfer Protocol)

**TLS**
تخزين محلي للخيوط (Thread-Local Storage)

**UID**
معرف المستخدم (User Identifier)

**umask**
قناع إنشاء ملفات المستخدم (user file-creation mask)

**USB**
الناقل التسلسلي العام (Universal Serial Bus)

**UTC**
التوقيت العالمي المنسق (Coordinated Universal Time)

---

Linux From Scratch - الإصدار 13.1-systemd

**UUID**
المعرف الفريد عالمياً (Universally Unique Identifier)

**VC**
وحدة تحكم افتراضية (Virtual Console)

**VGA**
مصفوفة رسوميات الفيديو (Video Graphics Array)

**VT**
طرفية افتراضية (Virtual Terminal)

---

Linux From Scratch - الإصدار 13.1-systemd