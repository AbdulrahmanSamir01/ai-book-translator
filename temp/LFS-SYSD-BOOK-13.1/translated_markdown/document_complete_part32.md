### ملاحظة

تستخدم مكتبة Glibc الآن مكتبة `libidn2` عند تحليل أسماء النطاقات المدوّلة (Internationalized Domain Names). وتعتبر هذه المكتبة تبعية لوقت التشغيل (run time dependency). إذا كنت بحاجة إلى هذه الميزة، يمكنك العثور على تعليمات تثبيت `libidn2` في صفحة `libidn2` الخاصة بكتاب BLFS.

---

Linux From Scratch - الإصدار 13.1-systemd

## 8.5.2. تهيئة Glibc

**8.5.2.1. إضافة ملف nsswitch.conf**

يجب إنشاء ملف `/etc/nsswitch.conf` لأن الإعدادات الافتراضية في Glibc لا تعمل بشكل جيد في البيئات الشبكية.

قم بإنشاء ملف `/etc/nsswitch.conf` جديد عن طريق تشغيل الأمر التالي:

**cat > /etc/nsswitch.conf << "EOF"**

# Begin /etc/nsswitch.conf

passwd: files systemd
group: files systemd
shadow: files systemd

hosts: mymachines resolve [!UNAVAIL=return] files myhostname dns
networks: files

protocols: files
services: files
ethers: files
rpc: files

# End /etc/nsswitch.conf
**EOF**

**8.5.2.2. إضافة بيانات المنطقة الزمنية (Time Zone Data)**

قم بتثبيت وإعداد بيانات المنطقة الزمنية باستخدام الأوامر التالية:

**tar -xf ../../tzdata2026c.tar.gz**

**ZONEINFO=/usr/share/zoneinfo**
**mkdir -pv $ZONEINFO/{posix,right}**

**for tz in etcetera southamerica northamerica europe africa antarctica  \**
**asia australasia backward; do**
**zic -L /dev/null   -d $ZONEINFO       ${tz}**
**zic -L /dev/null   -d $ZONEINFO/posix ${tz}**
**zic -L leapseconds -d $ZONEINFO/right ${tz}**
**done**

**cp -v zone.tab zone1970.tab iso3166.tab $ZONEINFO**
**zic -d $ZONEINFO -p America/New_York**
**unset ZONEINFO tz**

**شرح أوامر zic:**

`zic -L /dev/null ...`

يقوم هذا الأمر بإنشاء مناطق زمنية بمعيار POSIX بدون أي ثوانٍ كبيسة (leap seconds). ومن المتعارف عليه وضع هذه الملفات في كل من `zoneinfo` و `zoneinfo/posix`. ومن الضروري وضع مناطق POSIX الزمنية في `zoneinfo`؛ وإلا ستظهر أخطاء في مجموعات الاختبار المختلفة. في الأنظمة المدمجة (Embedded Systems)، حيث تكون المساحة محدودة ولا تنوي تحديث المناطق الزمنية أبداً، يمكنك توفير 1.9 ميجابايت بعدم استخدام دليل `posix` ولكن قد تسبب بعض التطبيقات أو مجموعات الاختبار بعض الإخفاقات.

`zic -L leapseconds ...`

يقوم هذا الأمر بإنشاء مناطق زمنية دقيقة (right time zones)، بما في ذلك الثواني الكبيسة. في الأنظمة المدمجة، حيث تكون المساحة محدودة ولا تنوي تحديث المناطق الزمنية أو لا تهتم بالوقت الدقيق، يمكنك توفير 1.9 ميجابايت عن طريق حذف دليل `right`.

---

Linux From Scratch - الإصدار 13.1-systemd

`zic ... -p ...`

يقوم هذا الأمر بإنشاء ملف `posixrules`. لقد استخدمنا نيويورك لأن معيار POSIX يتطلب أن تكون قواعد التوقيت الصيفي متوافقة مع القواعد الأمريكية.

إحدى الطرق لتحديد المنطقة الزمنية المحلية هي تشغيل السكربت التالي:

**tzselect**

بعد الإجابة على بضعة أسئلة حول الموقع، سيقوم السكربت بإخراج اسم المنطقة الزمنية (مثلاً: `America/Edmonton`). هناك أيضاً بعض المناطق الزمنية الأخرى المتاحة في `/usr/share/zoneinfo` مثل `Canada/Eastern` أو `EST5EDT` والتي قد لا يحددها السكربت ولكن يمكن استخدامها.

بعد ذلك، قم بإنشاء ملف `/etc/localtime` عن طريق تشغيل:

**ln -sfv /usr/share/zoneinfo/<xxx> /etc/localtime**

استبدل `<xxx>` باسم المنطقة الزمنية التي اخترتها (مثلاً: `Canada/Eastern`).

**8.5.2.3. تهيئة المحمل الديناميكي (Dynamic Loader)**

بشكل افتراضي، يقوم المحمل الديناميكي (`/lib/ld-linux.so.2`) بالبحث في `/usr/lib` عن المكتبات المشتركة التي تحتاجها البرامج أثناء تشغيلها. ومع ذلك، إذا كانت هناك مكتبات في أدلة أخرى غير `/usr/lib` فيجب إضافتها إلى ملف `/etc/ld.so.conf` لكي يتمكن المحمل الديناميكي من العثور عليها. هناك دليلان يُعرفان عادةً باحتوائهما على مكتبات إضافية وهما `/usr/local/lib` و `/opt/lib`؛ لذا قم بإضافة هذين الدليلين إلى مسار بحث المحمل الديناميكي.

قم بإنشاء ملف `/etc/ld.so.conf` جديد عن طريق تشغيل ما يلي:

**cat > /etc/ld.so.conf << "EOF"**

# Begin /etc/ld.so.conf
/usr/local/lib
/opt/lib

**EOF**

إذا رغبت في ذلك، يمكن للمحمل الديناميكي أيضاً البحث في دليل معين وتضمين محتويات الملفات الموجودة هناك. عموماً، تكون الملفات في دليل التضمين هذا عبارة عن سطر واحد يحدد مسار المكتبة المطلوب. لإضافة هذه الميزة، قم بتشغيل الأوامر التالية:

**cat >> /etc/ld.so.conf << "EOF"**

# Add an include directory
include /etc/ld.so.conf.d/*.conf

**EOF**
**mkdir -pv /etc/ld.so.conf.d**

---

Linux From Scratch - الإصدار 13.1-systemd

## 8.5.3. محتويات Glibc

**البرامج المثبتة:**
`gencat`, `getconf`, `getent`, `iconv`, `iconvconfig`, `ldconfig`, `ldd`, `lddlibc4`, `ld.so` (رابط رمزي إلى `ld-linux-x86-64.so.2` أو `ld-linux.so.2`), `locale`, `localedef`, `makedb`, `mtrace`, `pcprofiledump`, `pldd`, `sln`, `sotruss`, `sprof`, `tzselect`, `xtrace`, `zdump`, و `zic`

**المكتبات المثبتة:**
`ld-linux-x86-64.so.2`, `ld-linux.so.2`, `libBrokenLocale.{a,so}`, `libanl.{a,so}`, `libc.{a,so}`, `libc_nonshared.a`, `libc_malloc_debug.so`, `libdl.{a,so.2}`, `libg.a`, `libm.{a,so}`, `libmcheck.a`, `libmemusage.so`, `libmvec.{a,so}`, `libnsl.so.1`, `libnss_compat.so`, `libnss_dns.so`, `libnss_files.so`, `libnss_hesiod.so`, `libpcprofile.so`, `libpthread.{a,so.0}`, `libresolv.{a,so}`, `librt.{a,so.1}`, `libthread_db.so`, و `libutil.{a,so.1}`

**الأدلة المثبتة:**
`/usr/include/arpa`, `/usr/include/bits`, `/usr/include/gnu`, `/usr/include/net`, `/usr/include/netash`, `/usr/include/netatalk`, `/usr/include/netax25`, `/usr/include/neteconet`, `/usr/include/netinet`, `/usr/include/netipx`, `/usr/include/netiucv`, `/usr/include/netpacket`, `/usr/include/netrom`, `/usr/include/netrose`, `/usr/include/nfs`, `/usr/include/protocols`, `/usr/include/rpc`, `/usr/include/sys`, `/usr/lib/audit`, `/usr/lib/gconv`, `/usr/lib/locale`, `/usr/libexec/getconf`, `/usr/share/i18n`, `/usr/share/zoneinfo`, و `/var/lib/nss_db`

**وصف موجز**

**gencat**
يولد كتالوجات الرسائل.

**getconf**
يعرض قيم تهيئة النظام للمتغيرات الخاصة بنظام الملفات.

**getent**
يجلب إدخالات من قاعدة بيانات إدارية.

**iconv**
يقوم بتحويل مجموعات الأحرف.

**iconvconfig**
ينشئ ملفات تهيئة لوحدات `iconv` سريعة التحميل.

**ldconfig**
يهيئ روابط وقت التشغيل للرابط الديناميكي.

**ldd**
يحدد المكتبات المشتركة المطلوبة لكل برنامج أو مكتبة مشتركة معطاة.

**lddlibc4**
يساعد `ldd` في التعامل مع ملفات الكائنات. هذا البرنامج غير موجود في المعماريات الحديثة مثل x86_64.

**locale**
يطبع معلومات متنوعة عن الإعدادات المحلية الحالية.

**localedef**
يجمع مواصفات الإعدادات المحلية.

**makedb**
ينشئ قاعدة بيانات بسيطة من مدخلات نصية.

**mtrace**
يقرأ ويفسر ملف تتبع الذاكرة ويعرض ملخصاً بتنسيق قابل للقراءة.

**pcprofiledump**
يفرغ المعلومات الناتجة عن تحليل أداء الحاسوب (PC profiling).

**pldd**
يسرد الكائنات المشتركة الديناميكية المستخدمة من قبل العمليات الجارية.

**sln**
برنامج `ln` مرتبط استاتيكياً.

**sotruss**
يتتبع استدعاءات إجراءات المكتبات المشتركة لأمر محدد.

**sprof**
يقرأ ويعرض بيانات تحليل أداء الكائنات المشتركة.

**tzselect**
يسأل المستخدم عن موقع النظام ويقدم وصف المنطقة الزمنية المقابلة.

**xtrace**
يتتبع تنفيذ البرنامج عن طريق طباعة الدالة التي يتم تنفيذها حالياً.

**zdump**
أداة تفريغ بيانات المنطقة الزمنية.

**zic**
مجمّع المناطق الزمنية.

`ld-*.so`
البرنامج المساعد للملفات التنفيذية ذات المكتبات المشتركة.

---

Linux From Scratch - الإصدار 13.1-systemd

`libBrokenLocale`
تستخدم داخلياً بواسطة Glibc كـ "حل ترقيعي" (hack) لتشغيل البرامج المعطوبة (مثل بعض تطبيقات Motif). راجع التعليقات في `glibc-2.44/locale/broken_cur_max.c` لمزيد من المعلومات.

`libanl`
مكتبة وهمية لا تحتوي على دوال. كانت سابقاً مكتبة البحث عن الأسماء غير المتزامنة، والتي أصبحت دوالها الآن جزءاً من `libc`.

`libc`
مكتبة لغة C الرئيسية.

`libc_malloc_debug`
تفعّل فحص تخصيص الذاكرة عند تحميلها مسبقاً.

`libdl`
مكتبة وهمية لا تحتوي على دوال. كانت سابقاً مكتبة واجهة الربط الديناميكي، والتي أصبحت دوالها الآن جزءاً من `libc`.

`libg`
مكتبة وهمية لا تحتوي على دوال. كانت سابقاً مكتبة وقت التشغيل لـ `g++`.

`libm`
المكتبة الرياضية.

`libmvec`
مكتبة الرياضيات الشعاعية (vector math)، يتم ربطها عند الحاجة عند استخدام `libm`.

`libmcheck`
تفعّل فحص تخصيص الذاكرة عند الربط بها.

`libmemusage`
تستخدم بواسطة `memusage` للمساعدة في جمع معلومات حول استخدام الذاكرة لبرنامج ما.

`libnsl`
مكتبة خدمات الشبكة، وهي الآن قديمة/مهجورة.

`libnss_*`
وحدات تبديل خدمة الأسماء (Name Service Switch)، تحتوي على دوال لتحليل أسماء المضيفين، وأسماء المستخدمين، وأسماء المجموعات، والأسماء المستعارة، والخدمات، والبروتوكولات، إلخ. يتم تحميلها بواسطة `libc` وفقاً للتهيئة في `/etc/nsswitch.conf`.

`libpcprofile`
يمكن تحميلها مسبقاً لتحليل أداء ملف تنفيذي.

`libpthread`
مكتبة وهمية لا تحتوي على دوال. كانت سابقاً تحتوي على الدوال التي توفر معظم الواجهات المحددة في ملحقات خيوط POSIX.1c وواجهات السيمفور (semaphore) المحددة في ملحقات POSIX.1b للوقت الحقيقي، والآن أصبحت هذه الدوال جزءاً من `libc`.

`libresolv`
تحتوي على دوال لإنشاء وإرسال وتفسير الحزم المرسلة إلى خوادم أسماء النطاقات على الإنترنت.

`librt`
تحتوي على الدوال التي توفر معظم الواجهات المحددة في ملحقات POSIX.1b للوقت الحقيقي.

`libthread_db`
تحتوي على دوال مفيدة لبناء مصححات الأخطاء (debuggers) للبرامج متعددة الخيوط.

`libutil`
مكتبة وهمية لا تحتوي على دوال. كانت سابقاً تحتوي على كود للدوال "القياسية" المستخدمة في العديد من أدوات يونكس المختلفة. هذه الدوال الآن جزء من `libc`.

---

Linux From Scratch - الإصدار 13.1-systemd