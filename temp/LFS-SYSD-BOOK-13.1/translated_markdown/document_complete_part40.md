### هام

في هذا القسم، تُعتبر مجموعة اختبارات GCC مهمة، ولكنها تستغرق وقتاً طويلاً. لذا، نُشجع من يقومون ببناء النظام للمرة الأولى على تشغيل مجموعة الاختبارات. يمكن تقليل وقت تشغيل الاختبارات بشكل كبير عن طريق إضافة `-jx` إلى أمر `make -k check` المذكور أدناه، **حيث تمثل x عدد أنوية المعالج (CPU cores) في نظامك.**

قد يحتاج GCC إلى مساحة أكبر في المكدس (stack space) عند تجميع بعض أنماط الكود المعقدة للغاية. وكإجراء احترازي للتوزيعات المضيفة التي تفرض حداً ضيقاً للمكدس، قم بتعيين الحد الأقصى الصلب (hard limit) لحجم المكدس ليكون غير محدود بشكل صريح. في معظم التوزيعات المضيفة (وفي نظام LFS النهائي)، يكون الحد الصلب غير محدود افتراضياً، ولكن لا ضرر من تعيينه صراحةً. ليس من الضروري تغيير الحد المرن (soft limit) لحجم المكدس لأن GCC سيقوم بتعيينه تلقائياً إلى قيمة مناسبة، طالما أن هذه القيمة لا تتجاوز الحد الصلب:

**ulimit -s -H unlimited**

قم باختبار النتائج كمستخدم غير متميز الصلاحيات، ولكن لا تتوقف عند حدوث أخطاء:

**chown -R tester .**
**su tester -c "PATH=$PATH make -k check"**

لاستخراج ملخص لنتائج مجموعة الاختبارات، قم بتشغيل:

**../contrib/test_summary -t**

**لتصفية المخرجات وإظهار الملخصات فقط، قم بتمرير المخرجات عبر `grep -A7 Summ`.**

يمكن مقارنة النتائج بتلك الموجودة على الرابطين التاليين: https://www.linuxfromscratch.org/lfs/build-logs/13.1/ و https://gcc.gnu.org/ml/gcc-testresults/.

في اختبارات `gcc.target/i386` من المعروف أن الاختبارات التالية تفشل: `auto-init-padding-9.c` و `builtin-memmove-*.c` و `mem{cpy,set}-pr120683-*.c` و `pr111657-1.c` و `pr115102.c` و `pr116896.c` و `pr120881-2a.c` و `pr122343-4a.c`. كما أن الاختبار المسمى `shift-gf2p8affine-2.c` يفشل إذا كان المعالج لا يدعم تقنية AVX512.

---

Linux From Scratch - الإصدار 13.1-systemd

في اختبارات `g++.target/i386` من المعروف أن الاختبارات التالية تفشل: `memset-pr108585-1{a,b}.C` و `mv{,c}-symbols*.C` و `pr112824-2.C` و `pr116896-1.C`.

بالإضافة إلى ذلك، من المعروف أن الاختبارات `gcc.dg/ipa/pr122458.c` و `gcc.dg/lto/toplevel-*-asm-*` و `gcc.dg/plugin/crash-test-nested-*.c` تفشل. أما الاختبار `g++.dg/gomp/deprecate-1.C` فيفشل أحياناً.

لقد قام محررو LFS بالتحقيق في هذه الإخفاقات وأكدوا أنها لا تشير إلى أي مشكلة حرجة. معظم هذه الإخفاقات تعود إلى أن كاتب حالة الاختبار لم يتوقع استخدام `--enable-default-ssp` أو `--enable-default-pie`.

لا يمكن تجنب بعض الإخفاقات غير المتوقعة دائماً، وفي بعض الحالات تعتمد إخفاقات الاختبارات على العتاد المحدد للنظام. ما لم تكن نتائج الاختبارات مختلفة تماماً عن تلك الموجودة في الرابط أعلاه، فمن الآمن الاستمرار.

قم بتثبيت الحزمة:

**make install**

دليل بناء GCC مملوك الآن للمستخدم `tester` ، وبالتالي فإن ملكية دليل الترويسات المثبت (ومحتوياته) غير صحيحة. قم بتغيير الملكية إلى المستخدم والمجموعة root:

**chown -v -R root:root $(gcc -print-file-name=include){,-fixed}**

قم بإنشاء رابط رمزي يتطلبه معيار FHS لأسباب "تاريخية".

**ln -svr /usr/bin/cpp /usr/lib**

**تستخدم العديد من الحزم الاسم `cc` لاستدعاء مجمّع لغة C. لقد قمنا بالفعل بإنشاء `cc` كرابط رمزي في مرحلة `gcc-pass2` ، لذا قم بإنشاء صفحة الدليل (man page) الخاصة به كرابط رمزي أيضاً:**

**ln -sv gcc.1 /usr/share/man/man1/cc.1**

أضف رابطاً رمزياً للتوافق لتمكين بناء البرامج باستخدام تحسين وقت الربط (LTO):

**ln -sfvr $(gcc -print-prog-name=liblto_plugin.so) /usr/lib/bfd-plugins/**

الآن وبعد أن أصبحت سلسلة الأدوات النهائية في مكانها، من المهم التأكد مرة أخرى من أن عمليات التجميع والربط ستعمل كما هو متوقع. نقوم بذلك عن طريق إجراء بعض الفحوصات الأولية:

**echo 'int main(){}' | cc -x c - -v -Wl,--verbose &> dummy.log**
**readelf -l a.out | grep ': /lib'**

يجب ألا تكون هناك أخطاء، وستكون مخرجات الأمر الأخير كما يلي (مع مراعاة الاختلافات حسب المنصة في اسم الرابط الديناميكي):

`[Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]`

الآن تأكد من أننا مهيؤون لاستخدام ملفات البدء الصحيحة:

**grep -E -o '/usr/lib.*/S?crt[1in].*succeeded' dummy.log**

يجب أن تكون مخرجات الأمر الأخير:

`/usr/lib/gcc/x86_64-pc-linux-gnu/16.2.0/../../../../lib/Scrt1.o succeeded`
`/usr/lib/gcc/x86_64-pc-linux-gnu/16.2.0/../../../../lib/crti.o succeeded`
`/usr/lib/gcc/x86_64-pc-linux-gnu/16.2.0/../../../../lib/crtn.o succeeded`

اعتماداً على بنية جهازك، قد تختلف النتائج أعلاه قليلاً. سيكون الاختلاف في اسم الدليل **بعد `/usr/lib/gcc`. الشيء المهم الذي يجب البحث عنه هنا هو أن gcc قد وجد جميع ملفات `crt*.o` الثلاثة تحت دليل `/usr/lib`.**

تحقق من أن المجمّع يبحث عن ملفات الترويسات الصحيحة:

**grep -B4 '^ /usr/include' dummy.log**

---

Linux From Scratch - الإصدار 13.1-systemd

يجب أن يعيد هذا الأمر المخرجات التالية:

`#include <...> search starts here:`
`/usr/lib/gcc/x86_64-pc-linux-gnu/16.2.0/include`
`/usr/local/include`
`/usr/lib/gcc/x86_64-pc-linux-gnu/16.2.0/include-fixed`
`/usr/include`

مرة أخرى، قد يختلف الدليل المسمى باسم الثلاثية النظامية الخاصة بك عن المذكور أعلاه، اعتماداً على بنية نظامك.

بعد ذلك، تحقق من استخدام الرابط الجديد مع مسارات البحث الصحيحة:

**grep 'SEARCH.*/usr/lib' dummy.log |sed 's|; \n|g'**

يجب تجاهل الإشارات إلى المسارات التي تحتوي على مكونات تتضمن `-linux-gnu` ، ولكن بخلاف ذلك، يجب أن تكون مخرجات الأمر الأخير:

`SEARCH_DIR("/usr/x86_64-pc-linux-gnu/lib64")`
`SEARCH_DIR("/usr/lib");`
`SEARCH_DIR("/usr/x86_64-pc-linux-gnu/lib")`

قد يستخدم نظام 32-بت بعض الأدلة الأخرى. على سبيل المثال، إليك المخرجات من جهاز i686:

`SEARCH_DIR("/usr/i686-pc-linux-gnu/lib32")`
`SEARCH_DIR("/usr/local/lib32")`
`SEARCH_DIR("/lib32")`
`SEARCH_DIR("/usr/lib32")`
`SEARCH_DIR("/usr/i686-pc-linux-gnu/lib")`
`SEARCH_DIR("/usr/local/lib")`
`SEARCH_DIR("/lib")`
`SEARCH_DIR("/usr/lib");`

بعد ذلك، تأكد من أننا نستخدم مكتبة libc الصحيحة:

**grep "/lib.*/libc.so.6 " dummy.log**

يجب أن تكون مخرجات الأمر الأخير:

`attempt to open /usr/lib/libc.so.6 succeeded`

تأكد من أن GCC يستخدم الرابط الديناميكي الصحيح:

**grep found dummy.log**

يجب أن تكون مخرجات الأمر الأخير (مع مراعاة الاختلافات حسب المنصة في اسم الرابط الديناميكي):

`found ld-linux-x86-64.so.2 at /usr/lib/ld-linux-x86-64.so.2`

إذا لم تظهر المخرجات كما هو موضح أعلاه أو لم يتم استلامها على الإطلاق، فهذا يعني أن هناك خطأً جسيماً. قم بالتحقيق ومراجعة الخطوات لمعرفة مكان المشكلة وتصحيحها. يجب حل أي مشكلات قبل المتابعة في العملية.

بمجرد أن يعمل كل شيء بشكل صحيح، قم بتنظيف ملفات الاختبار:

**rm -v a.out dummy.log**

أخيراً، قم بنقل ملف في غير مكانه:

**mkdir -pv /usr/share/gdb/auto-load/usr/lib**
**mv -v /usr/lib/*gdb.py /usr/share/gdb/auto-load/usr/lib**

---

Linux From Scratch - الإصدار 13.1-systemd

## 8.32.2. محتويات GCC

**البرامج المثبتة:**
`c++`, `cc` (رابط إلى gcc), `cpp`, `g++`, `gcc`, `gcc-ar`, `gcc-nm`, `gcc-ranlib`, `gcov`, `gcov-dump`, `gcov-tool`, و `lto-dump`

**المكتبات المثبتة:**
`libasan.{a,so}`, `libatomic.{a,so}`, `libcc1.so`, `libgcc.a`, `libgcc_eh.a`, `libgcc_s.so`, `libgcov.a`, `libgomp.{a,so}`, `libhwasan.{a,so}`, `libitm.{a,so}`, `liblsan.{a,so}`, `liblto_plugin.so`, `libquadmath.{a,so}`, `libssp.{a,so}`, `libssp_nonshared.a`, `libstdc++.{a,so}`, `libstdc++exp.a`, `libstdc++fs.a`, `libsupc++.a`, `libtsan.{a,so}`, و `libubsan.{a,so}`

**الأدلة المثبتة:**
`/usr/include/c++`, `/usr/lib/gcc`, `/usr/libexec/gcc`, و `/usr/share/gcc-16.2.0`

**أوصاف مختصرة**

**c++**
مجمّع لغة C++

**cc**
مجمّع لغة C

**cpp**
المعالج المسبق للغة C؛ يستخدمه المجمّع لتوسيع توجيهات `#include` و `#define` والتوجيهات المماثلة في الملفات المصدرية

**g++**
مجمّع لغة C++

**gcc**
مجمّع لغة C

**gcc-ar**
**غلاف حول `ar` يضيف إضافة (plugin) إلى سطر الأوامر. يُستخدم هذا البرنامج فقط لإضافة "تحسين وقت الربط" (LTO) وليس مفيداً مع خيارات البناء الافتراضية.**

**gcc-nm**
**غلاف حول `nm` يضيف إضافة إلى سطر الأوامر. يُستخدم هذا البرنامج فقط لإضافة "تحسين وقت الربط" وليس مفيداً مع خيارات البناء الافتراضية.**

**gcc-ranlib**
**غلاف حول `ranlib` يضيف إضافة إلى سطر الأوامر. يُستخدم هذا البرنامج فقط لإضافة "تحسين وقت الربط" وليس مفيداً مع خيارات البناء الافتراضية.**

**gcov**
أداة اختبار التغطية؛ تُستخدم لتحليل البرامج لتحديد أين سيكون للتحسينات التأثير الأكبر

**gcov-dump**
أداة تفريغ ملفات تعريف `gcda` و `gcno` دون اتصال

**gcov-tool**
أداة معالجة ملفات تعريف `gcda` دون اتصال

**lto-dump**
أداة لتفريغ ملفات الكائنات التي ينتجها GCC مع تفعيل LTO

**libasan**
مكتبة وقت التشغيل لـ Address Sanitizer

**libatomic**
مكتبة وقت التشغيل المدمجة للعمليات الذرية في GCC

**libcc1**
مكتبة تسمح لـ GDB بالاستفادة من GCC

**libgcc**
**تحتوي على دعم وقت التشغيل لـ gcc**

**libgcov**
يتم ربط هذه المكتبة في البرنامج عندما يتم توجيه GCC لتمكين تحليل الأداء (profiling)

**libgomp**
تنفيذ GNU لواجهة OpenMP للبرمجة المتوازية ذات الذاكرة المشتركة متعددة المنصات في لغات C/C++ و Fortran

**libhwasan**
مكتبة وقت التشغيل لـ Hardware-assisted Address Sanitizer

**libitm**
مكتبة GNU للذاكرة المعاملاتية (transactional memory)

**liblsan**
مكتبة وقت التشغيل لـ Leak Sanitizer

**liblto_plugin**
إضافة LTO الخاصة بـ GCC تسمح لـ Binutils بمعالجة ملفات الكائنات التي ينتجها GCC مع تفعيل LTO

**libquadmath**
واجهة مكتبة الحسابات الرياضية ذات الدقة الرباعية في GCC

---

Linux From Scratch - الإصدار 13.1-systemd

**libssp**
تحتوي على روتينيات تدعم ميزة تحطيم المكدس (stack-smashing protection) في GCC. عادة لا تُستخدم لأن Glibc توفر هذه الروتينيات أيضاً.

**libstdc++**
مكتبة C++ القياسية

**libstdc++exp**
مكتبة عقود C++ التجريبية

**libstdc++fs**
مكتبة نظام الملفات ISO/IEC TS 18822:2015

**libsupc++**
توفر روتينيات داعمة للغة برمجة C++

**libtsan**
مكتبة وقت التشغيل لـ Thread Sanitizer

**libubsan**
مكتبة وقت التشغيل لـ Undefined Behavior Sanitizer

---

Linux From Scratch - الإصدار 13.1-systemd