## 8.81.2. محتويات حزمة Util-linux

**البرامج المثبتة:**
addpart, agetty, blkdiscard, blkid, blkzone, blockdev, cal, cfdisk, chcpu, chmem, choom,
chrt, col, colcrt, colrm, column, ctrlaltdel, delpart, dmesg, eject, fallocate, fdisk, fincore,
findfs, findmnt, flock, fsck, fsck.cramfs, fsck.minix, fsfreeze, fstrim, getopt, hardlink,
hexdump, hwclock, i386 (رابط إلى setarch), ionice, ipcmk, ipcrm, ipcs, irqtop, isosize, kill,
last, lastb (رابط إلى last), ldattach, linux32 (رابط إلى setarch), linux64 (رابط إلى setarch), logger,
look, losetup, lsblk, lscpu, lsipc, lsirq, lsfd, lslocks, lslogins, lsmem, lsns, mcookie,
mesg, mkfs, mkfs.bfs, mkfs.cramfs, mkfs.minix, mkswap, more, mount, mountpoint,
namei, nsenter, partx, pivot_root, prlimit, readprofile, rename, renice, resizepart, rev,
rfkill, rtcwake, script, scriptlive, scriptreplay, setarch, setsid, setterm, sfdisk, sulogin,
swaplabel, swapoff, swapon, switch_root, taskset, uclampset, ul, umount, uname26 (رابط
إلى setarch), unshare, utmpdump, uuidd, uuidgen, uuidparse, wall, wdctl, whereis, wipefs,
x86_64 (رابط إلى setarch), و zramctl

**المكتبات المثبتة:**
libblkid.so, libfdisk.so, libmount.so, libsmartcols.so, و libuuid.so

**الأدلة المثبتة:**
/usr/include/blkid,
/usr/include/libfdisk,
/usr/include/libmount,
/usr/include/
libsmartcols, /usr/include/uuid, /usr/share/doc/util-linux-2.42.2, و /var/lib/hwclock

**وصف موجز**

**addpart**
يُخطر نواة لينكس بوجود أقسام (partitions) جديدة.

**agetty**
**يفتح منفذ tty، ويطلب اسم تسجيل الدخول، ثم يستدعي برنامج تسجيل الدخول.**

**blkdiscard**
يقوم بإلغاء القطاعات (sectors) على جهاز ما.

**blkid**
أداة سطر أوامر لتحديد وطباعة سمات أجهزة الكتل (block devices).

**blkzone**
يُستخدم لإدارة أجهزة كتل التخزين ذات المناطق (zoned storage).

**blockdev**
يسمح للمستخدمين باستدعاء دوال ioctls الخاصة بأجهزة الكتل من سطر الأوامر.

**cal**
يعرض تقويماً بسيطاً.

**cfdisk**
يتعامل مع جدول الأقسام للجهاز المحدد.

**chcpu**
يعدل حالة وحدات المعالجة المركزية (CPUs).

**chmem**
يقوم بتهيئة الذاكرة.

**choom**
يعرض ويضبط درجات OOM-killer، المستخدمة لتحديد أي عملية يجب إنهاؤها أولاً عندما تنفد الذاكرة في لينكس.

**chrt**
يتعامل مع سمات الوقت الفعلي (real-time) لعملية ما.

**col**
يقوم بتصفية تغذيات الأسطر العكسية.

**colcrt**
**يصفي مخرجات nroff للطرفيات التي تفتقر إلى بعض القدرات، مثل الكتابة الفوقية وأنصاف الأسطر.**

**colrm**
يقوم بتصفية الأعمدة المحددة.

**column**
ينسق ملفاً معيناً في أعمدة متعددة.

**ctrlaltdel**
يضبط وظيفة مجموعة مفاتيح Ctrl+Alt+Del لتكون إعادة تشغيل صلبة (hard reset) أو مرنة (soft reset).

**delpart**
يطلب من نواة لينكس إزالة قسم ما.

**dmesg**
يقوم بتفريغ رسائل إقلاع النواة.

**eject**
يخرج الوسائط القابلة للإزالة.

**fallocate**
يخصص مساحة مسبقاً لملف ما.

---

Linux From Scratch - Version 13.1-systemd

**fdisk**
يتعامل مع جدول الأقسام للجهاز المحدد.

**fincore**
يحسب صفحات محتويات الملفات الموجودة في الذاكرة المركزية (core).

**findfs**
يجد نظام ملفات، إما عن طريق التسمية (label) أو المعرف الفريد عالمياً (UUID).

**findmnt**
واجهة سطر أوامر لمكتبة libmount للتعامل مع ملفات mountinfo و fstab و mtab.

**flock**
يستحوذ على قفل ملف ثم ينفذ أمراً مع الاحتفاظ بهذا القفل.

**fsck**
يُستخدم لفحص أنظمة الملفات وإصلاحها اختيارياً.

**fsck.cramfs**
يجري فحص الاتساق على نظام ملفات Cramfs على الجهاز المحدد.

**fsck.minix**
يجري فحص الاتساق على نظام ملفات Minix على الجهاز المحدد.

**fsfreeze**
عبارة عن نص برمجي غلافي (wrapper) بسيط جداً حول عمليات مشغل النواة FIFREEZE/FITHAW ioctl.

**fstrim**
يتخلص من الكتل غير المستخدمة على نظام ملفات مربوط.

**getopt**
يحلل الخيارات في سطر الأوامر المعطى.

**hardlink**
يدمج الملفات المكررة عن طريق إنشاء روابط صلبة.

**hexdump**
يقوم بتفريغ الملف المعطى بصيغة سداسية عشرية، أو عشرية، أو ثمانية، أو ascii.

**hwclock**
يقرأ أو يضبط ساعة الأجهزة للنظام، وتسمى أيضاً ساعة الوقت الفعلي (RTC) أو ساعة نظام الإدخال والإخراج الأساسي (BIOS).

**i386**
رابط رمزي إلى setarch.

**ionice**
يجلب أو يضبط فئة وجدولة الأولوية للإدخال والإخراج (io) لبرنامج ما.

**ipcmk**
ينشئ موارد متنوعة للتواصل بين العمليات (IPC).

**ipcrm**
يزيل مورد التواصل بين العمليات (IPC) المحدد.

**ipcs**
يوفر معلومات عن حالة التواصل بين العمليات (IPC).

**irqtop**
يعرض معلومات عداد مقاطعات النواة في عرض يشبه أداة top(1).

**isosize**
يبلغ عن حجم نظام ملفات iso9660.

**kill**
يرسل إشارات إلى العمليات.

**last**
يعرض المستخدمين الذين سجلوا دخولهم (وخروجهم) مؤخراً، من خلال البحث في ملف /var/log/wtmp؛ كما يعرض عمليات إقلاع النظام، وإيقاف التشغيل، وتغييرات مستوى التشغيل (run-level).

**lastb**
يعرض محاولات تسجيل الدخول الفاشلة، كما هي مسجلة في /var/log/btmp.

**ldattach**
يربط انضباط السطر (line discipline) بسطر تسلسلي.

**linux32**
رابط رمزي إلى setarch.

**linux64**
رابط رمزي إلى setarch.

**logger**
يدخل الرسالة المعطاة في سجل النظام.

**look**
يعرض الأسطر التي تبدأ بالسلسلة النصية المعطاة.

**losetup**
يجهز ويتحكم في أجهزة الحلقة (loop devices).

**lsblk**
يسرد معلومات عن جميع أجهزة الكتل أو أجهزة محددة منها بتنسيق شجري.

**lscpu**
يطبع معلومات بنية وحدة المعالجة المركزية (CPU).

**lsfd**
**يعرض معلومات عن الملفات المفتوحة؛ ويحل محل lsof.**

**lsipc**
يطبع معلومات عن مرافق التواصل بين العمليات (IPC) المستخدمة حالياً في النظام.

---

Linux From Scratch - Version 13.1-systemd

**lsirq**
يعرض معلومات عداد مقاطعات النواة.

**lslocks**
يسرد أقفال النظام المحلية.

**lslogins**
يسرد معلومات عن المستخدمين والمجموعات وحسابات النظام.

**lsmem**
يسرد نطاقات الذاكرة المتاحة مع حالة اتصالها (online status).

**lsns**
يسرد مساحات الأسماء (namespaces).

**mcookie**
**يولد ملفات تعريف ارتباط سحرية (أرقام سداسية عشرية عشوائية بطول 128 بت) لبرنامج xauth.**

**mesg**
يتحكم في ما إذا كان بإمكان المستخدمين الآخرين إرسال رسائل إلى طرفية المستخدم الحالي.

**mkfs**
يبني نظام ملفات على جهاز (عادةً ما يكون قسم قرص صلب).

**mkfs.bfs**
ينشئ نظام ملفات bfs الخاص بـ Santa Cruz Operations (SCO).

**mkfs.cramfs**
ينشئ نظام ملفات cramfs.

**mkfs.minix**
ينشئ نظام ملفات Minix.

**mkswap**
يهيئ الجهاز أو الملف المعطى ليتم استخدامه كمساحة تبديل (swap area).

**more**
مرشح لاستعراض النصوص صفحة تلو الأخرى.

**mount**
يربط نظام الملفات الموجود على الجهاز المعطى بدليل محدد في شجرة نظام الملفات.

**mountpoint**
يتحقق مما إذا كان الدليل عبارة عن نقطة ربط (mountpoint).

**namei**
يعرض الروابط الرمزية في المسارات المعطاة.

**nsenter**
يشغل برنامجاً باستخدام مساحات أسماء لعمليات أخرى.

**partx**
يخبر النواة بوجود وترقيم الأقسام الموجودة على القرص.

**pivot_root**
يجعل نظام الملفات المعطى هو نظام ملفات الجذر الجديد للعملية الحالية.

**prlimit**
يجلب ويضبط حدود موارد العملية.

**readprofile**
يقرأ معلومات تحليل أداء النواة (kernel profiling).

**rename**
يعيد تسمية الملفات المعطاة، مستبدلاً سلسلة نصية معينة بأخرى.

**renice**
يغير أولوية العمليات الجارية.

**resizepart**
يطلب من نواة لينكس تغيير حجم قسم ما.

**rev**
يعكس أسطر ملف معين.

**rfkill**
أداة لتمكين وتعطيل الأجهزة اللاسلكية.

**rtcwake**
يُستخدم لإدخال النظام في حالة سكون حتى وقت الاستيقاظ المحدد.

**script**
ينشئ نسخة نصية (typescript) من جلسة طرفية.

**scriptlive**
يعيد تشغيل النسخ النصية للجلسات باستخدام معلومات التوقيت.

**scriptreplay**
يعيد تشغيل النسخ النصية باستخدام معلومات التوقيت.

**setarch**
يغير البنية المبلغ عنها في بيئة برنامج جديدة، ويضبط أعلام الشخصية (personality flags).

**setsid**
يشغل البرنامج المعطى في جلسة جديدة.

**setterm**
يضبط سمات الطرفية.

**sfdisk**
أداة للتعامل مع جدول أقسام القرص.

**sulogin**
**يسمح للمستخدم الجذر (root) بتسجيل الدخول؛ وعادةً ما يتم استدعاؤه بواسطة init عندما يدخل النظام في وضع المستخدم الواحد (single user mode).**

**swaplabel**
يجري تغييرات على المعرف الفريد عالمياً (UUID) وتسمية مساحة التبديل.

---

Linux From Scratch - Version 13.1-systemd

**swapoff**
يعطل الأجهزة والملفات المستخدمة في عمليات التصفح والتبديل (paging and swapping).