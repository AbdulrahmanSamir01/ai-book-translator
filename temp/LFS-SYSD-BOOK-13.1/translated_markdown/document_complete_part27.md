# 7.5. إنشاء الأدلة

حان الوقت الآن لإنشاء هيكل الأدلة الكامل في نظام ملفات LFS.

### ملاحظة

بعض الأدلة المذكورة في هذا القسم قد تكون قد أُنشئت بالفعل في وقت سابق بناءً على تعليمات صريحة، أو أثناء تثبيت بعض الحزم. لقد تمت إعادتها أدناه من أجل الاكتمال.

قم بإنشاء بعض الأدلة على مستوى الجذر (root) والتي لم تكن ضمن المجموعة المحدودة المطلوبة في الفصول السابقة عبر تنفيذ الأمر التالي:

**mkdir -pv /{boot,home,mnt,opt,srv}**

---

Linux From Scratch - Version 13.1-systemd

قم بإنشاء مجموعة الأدلة الفرعية المطلوبة أسفل مستوى الجذر عبر تنفيذ الأوامر التالية:

**mkdir -pv /etc/{opt,sysconfig}**
**mkdir -pv /lib/firmware**
**mkdir -pv /media/{floppy,cdrom}**
**mkdir -pv /usr/{,local/}{include,src}**
**mkdir -pv /usr/lib/locale**
**mkdir -pv /usr/local/{bin,lib,sbin}**
**mkdir -pv /usr/{,local/}share/{color,dict,doc,info,locale,man}**
**mkdir -pv /usr/{,local/}share/{misc,terminfo,zoneinfo}**
**mkdir -pv /usr/{,local/}share/man/man{1..8}**
**mkdir -pv /var/{cache,local,log,mail,opt,spool}**
**mkdir -pv /var/lib/{color,misc,locate}**

**ln -sfv /run /var/run**
**ln -sfv /run/lock /var/lock**

**install -dv -m 0750 /root**
**install -dv -m 1777 /tmp /var/tmp**

يتم إنشاء الأدلة افتراضياً بوضع صلاحيات 755، ولكن هذا ليس مرغوباً في كل مكان. في الأوامر أعلاه، تم إجراء تغييرين: أحدهما على الدليل الرئيسي للمستخدم root، والآخر على أدلة الملفات المؤقتة.

يضمن تغيير الوضع الأول ألا يتمكن أي شخص من الدخول إلى دليل /root — تماماً كما يفعل المستخدم العادي مع دليله الرئيسي. أما تغيير الوضع الثاني فيضمن أن أي مستخدم يمكنه الكتابة في دليلي /tmp و /var/tmp، ولكن لا يمكنه حذف ملفات مستخدم آخر منهما. يتم حظر الأمر الأخير بواسطة ما يسمى بـ "البت اللاصق" (sticky bit)، وهو البت الأعلى (1) في قناع البتات 1777.

## 7.5.1. ملاحظة حول الامتثال لمعيار FHS

تعتمد شجرة الأدلة هذه على معيار تسلسل الملفات (FHS) (المتاح على https://refspecs.linuxfoundation.org/fhs.shtml). يحدد معيار FHS أيضاً الوجود الاختياري لأدلة إضافية مثل /usr/local/games و /usr/share/games. في LFS، نقوم بإنشاء الأدلة الضرورية حقاً فقط. ومع ذلك، يمكنك إنشاء المزيد من الأدلة إذا رغبت في ذلك.

### تحذير

لا يفرض معيار FHS وجود الدليل /usr/lib64، وقد قرر محررو LFS عدم استخدامه. لكي تعمل التعليمات في LFS و BLFS بشكل صحيح، من الضروري ألا يكون هذا الدليل موجوداً. يجب عليك التحقق من عدم وجوده من وقت لآخر، لأنه من السهل إنشاؤه عن غير قصد، وهذا سيؤدي على الأرجح إلى تعطل نظامك.

# 7.6. إنشاء الملفات والروابط الرمزية الأساسية

تاريخياً، كان لينكس يحتفظ بقائمة بأنظمة الملفات المربوطة في الملف /etc/mtab. أما النوى الحديثة فتحتفظ بهذه القائمة داخلياً وتعرضها للمستخدم عبر نظام ملفات /proc. لتلبية احتياجات الأدوات التي تتوقع العثور على /etc/mtab، قم بإنشاء الرابط الرمزي التالي:

**ln -sv /proc/self/mounts /etc/mtab**

قم بإنشاء ملف /etc/hosts أساسي ليتم الرجوع إليه في بعض مجموعات الاختبار، وفي أحد ملفات تهيئة Perl أيضاً:

**cat > /etc/hosts << EOF**
127.0.0.1  localhost $(hostname)
::1        localhost
**EOF**

---

Linux From Scratch - Version 13.1-systemd

لكي يتمكن المستخدم root من تسجيل الدخول ولكي يتم التعرف على الاسم "root"، يجب أن تكون هناك إدخالات ذات صلة في ملفي /etc/passwd و /etc/group.

أنشئ ملف /etc/passwd عن طريق تشغيل الأمر التالي:

**cat > /etc/passwd << "EOF"**
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/dev/null:/usr/bin/false
daemon:x:6:6:Daemon User:/dev/null:/usr/bin/false
messagebus:x:18:18:D-Bus Message Daemon User:/run/dbus:/usr/bin/false
systemd-journal-gateway:x:73:73:systemd Journal Gateway:/:/usr/bin/false
systemd-journal-remote:x:74:74:systemd Journal Remote:/:/usr/bin/false
systemd-journal-upload:x:75:75:systemd Journal Upload:/:/usr/bin/false
systemd-network:x:76:76:systemd Network Management:/:/usr/bin/false
systemd-resolve:x:77:77:systemd Resolver:/:/usr/bin/false
systemd-timesync:x:78:78:systemd Time Synchronization:/:/usr/bin/false
systemd-coredump:x:79:79:systemd Core Dumper:/:/usr/bin/false
uuidd:x:80:80:UUID Generation Daemon User:/dev/null:/usr/bin/false
systemd-oom:x:81:81:systemd Out Of Memory Daemon:/:/usr/bin/false
nobody:x:65534:65534:Unprivileged User:/dev/null:/usr/bin/false
**EOF**

سيتم تعيين كلمة المرور الفعلية لـ root لاحقاً.

أنشئ ملف /etc/group عن طريق تشغيل الأمر التالي:

**cat > /etc/group << "EOF"**
root:x:0:
bin:x:1:daemon
sys:x:2:
kmem:x:3:
tape:x:4:
tty:x:5:
daemon:x:6:
floppy:x:7:
disk:x:8:
lp:x:9:
dialout:x:10:
audio:x:11:
video:x:12:
utmp:x:13:
clock:x:14:
cdrom:x:15:
adm:x:16:
messagebus:x:18:
systemd-journal:x:23:
input:x:24:
mail:x:34:
kvm:x:61:
systemd-journal-gateway:x:73:
systemd-journal-remote:x:74:
systemd-journal-upload:x:75:
systemd-network:x:76:
systemd-resolve:x:77:
systemd-timesync:x:78:
systemd-coredump:x:79:
uuidd:x:80:
systemd-oom:x:81:
wheel:x:97:
users:x:999:
nogroup:x:65534:
**EOF**

---

Linux From Scratch - Version 13.1-systemd

المجموعات التي تم إنشاؤها ليست جزءاً من أي معيار — بل هي مجموعات تم تحديدها جزئياً بناءً على متطلبات تهيئة Udev في الفصل 9، وجزئياً بناءً على الاصطلاحات الشائعة المستخدمة في عدد من توزيعات لينكس الحالية. بالإضافة إلى ذلك، تعتمد بعض مجموعات الاختبار على مستخدمين أو مجموعات محددة. توصي القاعدة القياسية للينكس (LSB، المتاحة على https://refspecs.linuxfoundation.org/lsb.shtml) فقط بوجود مجموعة bin بمعرف مجموعة (GID) رقم 1، بالإضافة إلى مجموعة root بمعرف 0. يُستخدم المعرف 5 على نطاق واسع لمجموعة tty، كما يُستخدم الرقم 5 في systemd لنظام ملفات devpts. يمكن لمسؤول النظام اختيار جميع أسماء المجموعات ومعرفات GID الأخرى بحرية لأن البرامج المكتوبة جيداً لا تعتمد على أرقام GID، بل تستخدم اسم المجموعة.

يستخدم النواة المعرف 65534 لـ NFS ومساحات أسماء المستخدمين المنفصلة للمستخدمين والمجموعات غير المحددة (تلك التي توجد على خادم NFS أو في مساحة أسماء المستخدم الأصلية، ولكنها "لا توجد" على الجهاز المحلي أو في مساحة الأسماء المنفصلة). نقوم بتعيين nobody و nogroup لتجنب وجود معرف بدون اسم. ولكن قد تتعامل التوزيعات الأخرى مع هذا المعرف بشكل مختلف، لذا لا ينبغي لأي برنامج قابل للنقل أن يعتمد على هذا التعيين.

تحتاج بعض الاختبارات في الفصل 8 إلى مستخدم عادي. سنقوم بإضافة هذا المستخدم هنا وحذف هذا الحساب في نهاية ذلك الفصل.

**echo "tester:x:101:101::/home/tester:/bin/bash" >> /etc/passwd**
**echo "tester:x:101:" >> /etc/group**
**install -o tester -d /home/tester**

لإزالة مطالبة "I have no name!"، ابدأ غلاف (shell) جديداً. بما أنه قد تم إنشاء ملفي /etc/passwd و /etc/group، فإن تحليل أسماء المستخدمين والمجموعات سيعمل الآن:

**exec /usr/bin/bash --login**

تستخدم برامج login و agetty و init (وغيرها) عدداً من ملفات السجل لتسجيل معلومات مثل من قام بتسجيل الدخول إلى النظام ومتى. ومع ذلك، لن تكتب هذه البرامج في ملفات السجل إذا لم تكن موجودة بالفعل. قم بتهيئة ملفات السجل ومنحها الصلاحيات المناسبة:

**touch /var/log/{btmp,lastlog,faillog,wtmp}**
**chgrp -v utmp /var/log/lastlog**
**chmod -v 664  /var/log/lastlog**
**chmod -v 600  /var/log/btmp**

يسجل ملف /var/log/wtmp جميع عمليات تسجيل الدخول والخروج. ويسجل ملف /var/log/lastlog وقت آخر تسجيل دخول لكل مستخدم. ويسجل ملف /var/log/faillog محاولات تسجيل الدخول الفاشلة. أما ملف /var/log/btmp فيسجل محاولات تسجيل الدخول الخاطئة.

### ملاحظة

يسجل ملف /run/utmp المستخدمين الذين قاموا بتسجيل الدخول حالياً. يتم إنشاء هذا الملف ديناميكياً عندما يقوم المستخدم بتسجيل الدخول إلى النظام.

### ملاحظة

تستخدم ملفات utmp و wtmp و btmp و lastlog أعداداً صحيحة 32-بت للطوابع الزمنية، وستتعطل بشكل أساسي بعد عام 2038. توقفت العديد من الحزم عن استخدامها، وستتوقف حزم أخرى عن ذلك. من الأفضل على الأرجح اعتبارها قديمة/مهجورة.

---

Linux From Scratch - Version 13.1-systemd