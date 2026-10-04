# 8.20. Ninja-1.13.2

نظام Ninja هو نظام بناء صغير يركز بشكل أساسي على السرعة.

**وقت البناء التقريبي:**
0.2 SBU
**مساحة القرص المطلوبة:**
43 ميجابايت

## 8.20.1. تثبيت Ninja

**عند التشغيل، يستخدم ninja عادةً أكبر عدد ممكن من العمليات بالتوازي. وبشكل افتراضي، يكون هذا العدد هو عدد أنوية النظام مضافاً إليها اثنان. قد يؤدي هذا إلى ارتفاع درجة حرارة وحدة المعالجة المركزية (CPU)، أو استنفاد ذاكرة النظام. عند استدعاء ninja من سطر الأوامر، فإن تمرير المعامل -jN سيقوم بتحديد عدد العمليات المتوازية. بعض الحزم تدمج تنفيذ ninja بداخلها، ولا تقوم بتمرير المعامل -j إليه.**

يتيح الإجراء الاختياري أدناه للمستخدم تحديد عدد العمليات المتوازية عبر متغير بيئي يسمى `NINJAJOBS`. على سبيل المثال، تعيين:

`export NINJAJOBS=4`

**سيقوم بتحديد ninja لأربع عمليات متوازية فقط.**

**إذا كنت ترغب في جعل ninja يتعرف على المتغير البيئي NINJAJOBS، قم بتشغيل محرر التدفق التالي:**

```bash
sed -i '/int Guess/a \
int   j = 0;\
char* jobs = getenv( "NINJAJOBS" );\
if ( jobs != NULL ) j = atoi( jobs );\
if ( j > 0 ) return j;\
' src/ninja.cc
```

قم ببناء Ninja باستخدام:

```bash
python3 configure.py --bootstrap --verbose
```

**معنى خيارات البناء:**

`--bootstrap`

يجبر هذا المعامل Ninja على إعادة بناء نفسه للنظام الحالي.

`--verbose`

**يجعل هذا المعامل ملف configure.py يعرض تقدم عملية بناء Ninja.**

لا يمكن تشغيل اختبارات الحزمة في بيئة chroot لأنها تتطلب cmake. ومع ذلك، فإن الوظيفة الأساسية لهذه الحزمة يتم اختبارها بالفعل من خلال إعادة بناء نفسها (باستخدام خيار `--bootstrap`) على أي حال.

تثبيت الحزمة:

```bash
install -vm755 ninja /usr/bin/
install -vDm644 misc/bash-completion /usr/share/bash-completion/completions/ninja
install -vDm644 misc/zsh-completion  /usr/share/zsh/site-functions/_ninja
```

## 8.20.2. محتويات Ninja

**البرامج المثبتة:**
ninja

**وصف مختصر**

**ninja**
هو نظام البناء Ninja

---

Linux From Scratch - Version 13.1-systemd

# 8.21. Pkgconf-3.0.5

حزمة pkgconf هي الخليفة لـ pkg-config، وتحتوي على أداة لتمرير مسارات الترويسات (include path) و/أو مسارات المكتبات إلى أدوات البناء خلال مرحلتي التهيئة (configure) والتجميع (make) عند تثبيت الحزم.

**وقت البناء التقريبي:**
أقل من 0.1 SBU
**مساحة القرص المطلوبة:**
47 ميجابايت

## 8.21.1. تثبيت Pkgconf

أولاً، قم بمعالجة التبعية الدائرية لـ meson:

```bash
tar -xf ../meson-1.12.0.tar.gz
```

تحضير Pkgconf للتجميع:

```bash
mkdir build
cd    build
python3 ../meson-1.12.0/meson.py setup --prefix=/usr --buildtype=release ..
```

تجميع الحزمة:

```bash
ninja
```

لاختبار النتائج، قم بتنفيذ:

```bash
ninja test
```

تثبيت الحزمة:

```bash
ninja install
mv /usr/share/doc/pkgconf{,-3.0.5}
```

للحفاظ على التوافق مع Pkg-config الأصلي، قم بإنشاء رابطين رمزيين:

```bash
ln -sv pkgconf   /usr/bin/pkg-config
ln -sv pkgconf.1 /usr/share/man/man1/pkg-config.1
```

## 8.21.2. محتويات Pkgconf

**البرامج المثبتة:**
pkgconf، و pkg-config (رابط إلى pkgconf)، و bomtool
**المكتبات المثبتة:**
libpkgconf.so
**الدليل المثبت:**
/usr/share/doc/pkgconf-3.0.5

**وصف مختصر**

**pkgconf**
يعيد المعلومات الوصفية (meta information) للمكتبة أو الحزمة المحددة.

**bomtool**
ينشئ قائمة مواد البرمجيات (Software Bill Of Materials) من ملفات .pc الخاصة بـ pkg-config.

**libpkgconf.so**
تحتوي على معظم وظائف pkgconf، مما يسمح لأدوات أخرى مثل بيئات التطوير المتكاملة (IDEs) والمجمّعات باستخدام أطر عملها.

---

Linux From Scratch - Version 13.1-systemd

# 8.22. Binutils-2.47

تحتوي حزمة Binutils على رابط (linker)، ومجمّع (assembler)، وأدوات أخرى للتعامل مع ملفات الكائنات.

**وقت البناء التقريبي:**
1.7 SBU
**مساحة القرص المطلوبة:**
817 ميجابايت

## 8.22.1. تثبيت Binutils

توصي وثائق Binutils ببنائها في دليل بناء مخصص:

```bash
mkdir -v build
cd       build
```

تحضير Binutils للتجميع:

```bash
../configure --prefix=/usr       \
--sysconfdir=/etc   \
--enable-ld=default \
--enable-plugins    \
--enable-shared     \
--disable-werror    \
--enable-64-bit-bfd \
--enable-new-dtags  \
--with-system-zlib  \
--with-lib-path=/usr/lib \
--enable-default-hash-style=gnu
```

**معنى معاملات التهيئة الجديدة:**

`--enable-ld=default`

بناء رابط bfd الأصلي وتثبيته كـ ld (الرابط الافتراضي) و ld.bfd.

`--enable-plugins`

تفعيل دعم الإضافات (plugins) للرابط.

`--with-system-zlib`

استخدام مكتبة zlib المثبتة بدلاً من بناء النسخة المضمنة.

`--with-lib-path=/usr/lib`

**تحديد المسار الذي يبحث فيه الرابط (ld). بشكل افتراضي، يبحث في عدة أدلة غير موجودة في LFS بخلاف /usr/lib، وخاصة دليل /usr/lib64 الذي نتجنبه عمداً. في حال تم إنشاء /usr/lib64 عن طريق الخطأ وملؤه ببعض المكتبات، فإن جعل ld لا يبحث في هذا المسار يمكن أن يكشف المشكلة مبكراً من خلال فشل العثور على تلك المكتبات وقت التجميع بدلاً من وقت التشغيل.**

تجميع الحزمة:

```bash
make tooldir=/usr
```

**معنى معامل make:**

`tooldir=/usr`

عادةً ما يتم تعيين tooldir (الدليل الذي ستوضع فيه الملفات التنفيذية في النهاية) إلى `$(exec_prefix)/$(target_alias)`. على سبيل المثال، أجهزة x86_64 ستقوم بتوسيع ذلك إلى `/usr/x86_64-pc-linux-gnu`. وبما أن هذا نظام مخصص، فإن هذا الدليل الخاص بالهدف في /usr ليس مطلوباً. يتم استخدام `$(exec_prefix)/$(target_alias)` إذا كان النظام يُستخدم للتجميع المتقاطع (على سبيل المثال، تجميع حزمة على جهاز Intel لإنتاج كود يمكن تنفيذه على أجهزة PowerPC).

---

Linux From Scratch - Version 13.1-systemd

### هام

تعتبر مجموعة الاختبارات لـ Binutils في هذا القسم حرجة للغاية. لا تتجاهلها تحت أي ظرف من الظروف.

اختبار النتائج:

```bash
make -k check
```

للحصول على قائمة بالاختبارات الفاشلة، قم بتشغيل:

```bash
grep '^FAIL:' $(find -name '*.log')
```

من المعروف أن هناك اختباراً واحداً متعلقاً بـ gprofng يفشل عادةً.

تثبيت الحزمة:

```bash
make tooldir=/usr install
```

إزالة المكتبات الاستاتيكية غير الضرورية والملفات الأخرى:

```bash
rm -rfv /usr/lib/lib{bfd,ctf,ctf-nobfd,gprofng,opcodes,sframe}.a \
/usr/share/doc/gprofng/
```

## 8.22.2. محتويات Binutils

**البرامج المثبتة:**
addr2line, ar, as, c++filt, dwp, elfedit, gprof, gprofng, ld, ld.bfd, nm, objcopy, objdump, ranlib, readelf, size, strings, و strip
**المكتبات المثبتة:**
libbfd.so, libctf.so, libctf-nobfd.so, libgprofng.so, libopcodes.so, و libsframe.so
**الدليل المثبت:**
/usr/lib/ldscripts

**وصف مختصر**

**addr2line**
يترجم عناوين البرنامج إلى أسماء ملفات وأرقام أسطر؛ فبإعطائه عنواناً واسم ملف تنفيذي، يستخدم معلومات التصحيح في الملف لتحديد ملف المصدر ورقم السطر المرتبطين بهذا العنوان.

**ar**
إنشاء وتعديل واستخراج الملفات من الأرشيفات.

**as**
**مجمّع (assembler) يقوم بتجميع مخرجات gcc إلى ملفات كائنات.**

**c++filt**
يستخدمه الرابط لفك تشفير (de-mangle) رموز C++ و Java ولمنع تضارب الدوال المحملة بشكل زائد (overloaded functions).

**dwp**
أداة تغليف DWARF.

**elfedit**
يحدث ترويسات ELF لملفات ELF.

**gprof**
يعرض بيانات ملف تعريف مخطط الاستدعاءات (call graph profile data).

**gprofng**
يجمع ويحلل بيانات الأداء.

**ld**
رابط يدمج عدداً من ملفات الكائنات والأرشيفات في ملف واحد، مع إعادة توطين بياناتها وربط مراجع الرموز.

**ld.bfd**
**رابط صلب إلى ld.**

**nm**
يسرد الرموز الموجودة في ملف كائنات معين.

**objcopy**
يترجم نوعاً من ملفات الكائنات إلى نوع آخر.

---

Linux From Scratch - Version 13.1-systemd

**objdump**
يعرض معلومات حول ملف كائنات معين، مع خيارات للتحكم في المعلومات المحددة المراد عرضها؛ هذه المعلومات مفيدة للمبرمجين الذين يعملون على أدوات التجميع.

**ranlib**
ينشئ فهرساً لمحتويات الأرشيف ويخزنه بداخله؛ يسرد الفهرس جميع الرموز المحددة بواسطة أعضاء الأرشيف التي تكون ملفات كائنات قابلة لإعادة التوطين.

**readelf**
يعرض معلومات حول الثنائيات من نوع ELF.

**size**
يسرد أحجام الأقسام والحجم الإجمالي لملفات الكائنات المحددة.

**strings**
يستخرج من كل ملف معطى تسلسلات الأحرف القابلة للطباعة التي لا يقل طولها عن طول محدد (الافتراضي هو أربعة)؛ بالنسبة لملفات الكائنات، يطبع افتراضياً السلاسل من أقسام التهيئة والتحميل فقط، بينما يمسح الملف بالكامل في أنواع الملفات الأخرى.

**strip**
يقوم بعملية التجريد (stripping) للرموز من ملفات الكائنات.

**libbfd**
مكتبة واصف الملفات الثنائية (Binary File Descriptor).

**libctf**
مكتبة دعم التصحيح لتنسيق أنواع ANSI-C المتوافق.

**libctf-nobfd**
نسخة من libctf لا تستخدم وظائف libbfd.

**libgprofng**
**مكتبة تحتوي على معظم الروتينات المستخدمة بواسطة gprofng.**

**libopcodes**
مكتبة للتعامل مع أكواد العمليات (opcodes) — وهي النسخ "النصية المقروءة" لتعليمات المعالج؛ **تُستخدم لبناء أدوات مثل objdump.**

**libsframe**
مكتبة لدعم تتبع المكدس (backtracing) المباشر باستخدام مفكك بسيط (unwinder).

---

Linux From Scratch - Version 13.1-systemd