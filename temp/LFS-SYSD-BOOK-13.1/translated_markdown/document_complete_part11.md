# الجزء الثاني: التحضير لعملية البناء

---

Linux From Scratch - الإصدار 13.1-systemd

# الفصل 2. تهيئة النظام المضيف

# 2.1. مقدمة

في هذا الفصل، سنقوم بفحص أدوات النظام المضيف اللازمة لبناء LFS وتثبيتها إذا لزم الأمر. بعد ذلك، سنقوم بتجهيز القسم (Partition) الذي سيستضيف نظام LFS؛ حيث سنقوم بإنشاء القسم نفسه، وبناء نظام ملفات عليه، ثم عمل عملية ربط (Mount) له.

# 2.2. متطلبات النظام المضيف

## 2.2.1. العتاد (Hardware)

يوصي محررو LFS بأن يحتوي المعالج (CPU) على أربعة أنوية على الأقل، وأن تتوفر ذاكرة وصول عشوائي (RAM) بسعة 8 جيجابايت كحد أدنى. الأنظمة الأقدم التي لا تستوفي هذه المتطلبات ستعمل أيضاً، ولكن الوقت المستغرق في بناء الحزم سيكون أطول بكثير مما هو موثق.

## 2.2.2. البرمجيات (Software)

يجب أن يحتوي النظام المضيف على البرمجيات التالية بالإصدارات الدنيا المحددة. لا ينبغي أن يشكل هذا عائقاً لمعظم توزيعات لينكس الحديثة. يرجى ملاحظة أن العديد من التوزيعات تضع ترويسات البرمجيات (Software Headers) في حزم منفصلة، غالباً ما تكون بصيغة `<package-name>-devel` أو `<package-name>-dev`؛ لذا تأكد من تثبيتها إذا كانت توزيعتك توفرها.

قد تعمل إصدارات أقدم من الحزم البرمجية المذكورة، ولكن لم يتم اختبارها.

### تحذير

يرجى الانتباه إلى أن إصدارات GCC الأحدث من 16.2.0 أو Binutils الأحدث من 2.47 لم يتم اختبارها. ومن المرجح جداً أن يتسبب إصدار GCC أحدث في تعطل عملية بناء هذا الإصدار من LFS. لا تقم بإبلاغ محرري LFS عن مثل هذه الأعطال. إذا كانت توزيعتك المضيفة تحتوي على إصدارات أحدث من هذه الحزم، فلديك عدة خيارات:

- استخدام إصدار أحدث من كتاب LFS إذا كان متاحاً.
- استخدام توزيعة مضيفة أقدم.
- خفض إصدار GCC إذا كان ذلك مدعوماً من قبل التوزيعة المضيفة.
- استخدام كتاب تطوير LFS الأحدث؛ حيث يتم عادةً إضافة التحديثات لأحدث إصدارات الحزم في LFS خلال أسبوعين إلى أربعة أسابيع من تاريخ إصدارها.

**• Bash-3.2 (يجب أن يكون `/bin/sh` رابطاً رمزياً أو صلباً يشير إلى bash)**
**• Binutils-2.13.1 (الإصدارات التي تتجاوز 2.47 قد لا تعمل لأنها لم تُختبر)**
**• Bison-2.7 (يجب أن يكون `/usr/bin/yacc` رابطاً يشير إلى bison أو نصاً برمجياً صغيراً يقوم بتشغيل bison)**
**• GNU Coreutils-8.1 أو Uutils Coreutils-0.8**
**• Diffutils-2.8.1**
**• Findutils-4.2.31**
**• Gawk-4.0.1 (يجب أن يكون `/usr/bin/awk` رابطاً يشير إلى gawk)**
**• GCC-5.4 بما في ذلك مترجم C++ وهو g++ (الإصدارات التي تتجاوز 16.2.0 قد لا تعمل لأنها لم تُختبر). كما يجب توفر المكتبات القياسية لـ C و C++ (مع الترويسات) لتمكين مترجم C++ من بناء البرامج المضيفة.**
**• Grep-2.5.1a**
**• Gzip-1.3.12**
**• Linux Kernel-5.10**

---

Linux From Scratch - الإصدار 13.1-systemd

السبب في اشتراط إصدار النواة (Kernel) هو أننا نحدد هذا الإصدار عند بناء glibc في الفصل 5 والفصل 8، وبذلك لا يتم تفعيل الحلول الالتفافية للنوى الأقدم، مما يجعل glibc المجمعة أسرع قليلاً وأصغر حجماً. حتى ديسمبر 2024، يعد الإصدار 5.10 أقدم إصدار نواة لا يزال مدعوماً من قبل مطوري النواة. قد تظل بعض الإصدارات الأقدم من 5.10 مدعومة من قبل فرق خارجية، ولكنها لا تعتبر إصدارات رسمية من المطورين الأصليين (Upstream)؛ اقرأ https://kernel.org/category/releases.html للتفاصيل.

إذا كانت نواة النظام المضيف أقدم من 5.10، فستحتاج إلى استبدالها بإصدار أكثر حداثة. هناك طريقتان للقيام بذلك: أولاً، تحقق مما إذا كان مورد لينكس الخاص بك يوفر حزمة نواة 5.10 أو أحدث، وإذا كان الأمر كذلك، يمكنك تثبيتها. أما إذا كان المورد لا يوفر حزمة نواة مقبولة، أو كنت تفضل عدم تثبيتها، فيمكنك تجميع نواة بنفسك. توجد تعليمات تجميع النواة وتهيئة محمل الإقلاع (بافتراض أن المضيف يستخدم GRUB) في الفصل 10.

نحن نشترط أن تدعم نواة المضيف الطرفية الوهمية (PTY) لمعيار UNIX 98. يجب أن تكون هذه الميزة مفعلة في جميع توزيعات سطح المكتب أو الخوادم التي تأتي بنواة Linux 5.10 أو أحدث. إذا كنت تقوم ببناء نواة مضيفة مخصصة، فتأكد من ضبط `CONFIG_UNIX98_PTYS` على `y` في تهيئة النواة.

**• M4-1.4.10**
**• Make-4.0**
**• Patch-2.5.4**
**• Perl-5.8.8**
**• Python-3.4**
**• Sed-4.1.5**
**• Tar-1.22**
**• Texinfo-5.0**
**• Xz-5.0.0**

بالإضافة إلى ذلك، إذا كنت بحاجة إلى إنشاء قسم نظام EFI جديد (ESP، راجع القسم 2.5 "إنشاء نظام ملفات على القسم" للتفاصيل)، فستحتاج إلى `dosfstools`.

### هام

لاحظ أن الروابط الرمزية (Symlinks) المذكورة أعلاه مطلوبة لبناء نظام LFS باستخدام التعليمات الواردة في هذا الكتاب. الروابط الرمزية التي تشير إلى برمجيات أخرى (مثل dash أو mawk وغيرها) قد تعمل، ولكنها غير مختبرة أو مدعومة من قبل فريق تطوير LFS، وقد تتطلب إما الانحراف عن التعليمات أو إضافة رقع برمجية (Patches) لبعض الحزم.

للتحقق مما إذا كان نظامك المضيف يحتوي على جميع الإصدارات المناسبة، والقدرة على تجميع البرامج، قم بتشغيل الأوامر التالية:

**cat > version-check.sh << "EOF"**
#!/bin/bash

# A script to list version numbers of critical development tools

# If you have tools installed in other directories, adjust PATH here AND

# in ~lfs/.bashrc (section 4.4) as well.

LC_ALL=C
PATH=/usr/bin:/bin

bail() { echo "FATAL: $1"; exit 1; }
grep --version > /dev/null 2> /dev/null || bail "grep does not work"
sed '' /dev/null || bail "sed does not work"
sort   /dev/null || bail "sort does not work"

---

Linux From Scratch - الإصدار 13.1-systemd

ver_check()
{
if ! type -p $2 &>/dev/null
then
echo "ERROR: Cannot find $2 ($1)"; return 1;
fi
v=$($2 --version 2>&1 | grep -E -o '[0-9]+\.[0-9\.]+[a-z]*' | head -n1)
if printf '%s\n' $3 $v | sort --version-sort --check &>/dev/null
then
printf "OK:    %-9s %-6s >= $3\n" "$1" "$v"; return 0;
else
printf "ERROR: %-9s is TOO OLD ($3 or later required)\n" "$1";
return 1;
fi
}

ver_kernel()
{
kver=$(uname -r | grep -E -o '^[0-9\.]+')
if printf '%s\n' $1 $kver | sort --version-sort --check &>/dev/null
then
printf "OK:    Linux Kernel $kver >= $1\n"; return 0;
else
printf "ERROR: Linux Kernel ($kver) is TOO OLD ($1 or later required)\n" "$kver";
return 1;
fi
}

# Coreutils first because --version-sort needs Coreutils >= 7.0
if sort --version |& grep -q uutils; then
ver_check Coreutils  sort     0.8 || bail "Uutils Coreutils too old, stop"
else
ver_check Coreutils  sort     8.1 || bail "GNU Coreutils too old, stop"
fi
ver_check Bash           bash     3.2
ver_check Binutils       ld       2.13.1
ver_check Bison          bison    2.7
ver_check Diffutils      diff     2.8.1
ver_check Findutils      find     4.2.31
ver_check Gawk           gawk     4.0.1
ver_check GCC            gcc      5.4
ver_check "GCC (C++)"    g++      5.4
ver_check Grep           grep     2.5.1a
ver_check Gzip           gzip     1.3.12
ver_check M4             m4       1.4.10
ver_check Make           make     4.0
ver_check Patch          patch    2.5.4
ver_check Perl           perl     5.8.8
ver_check Python         python3  3.4
ver_check Sed            sed      4.1.5
ver_check Tar            tar      1.22
ver_check Texinfo        texi2any 5.0
ver_check Xz             xz       5.0.0
ver_kernel 5.10

if mount | grep -q 'devpts on /dev/pts' && [ -e /dev/ptmx ]
then echo "OK:    Linux Kernel supports UNIX 98 PTY";
else echo "ERROR: Linux Kernel does NOT support UNIX 98 PTY"; fi

alias_check() {
if $1 --version 2>&1 | grep -qi $2
then printf "OK:    %-4s is $2\n" "$1";
else printf "ERROR: %-4s is NOT $2\n" "$1"; fi

---

Linux From Scratch - الإصدار 13.1-systemd

}
echo "Aliases:"
alias_check awk GNU
alias_check yacc Bison
alias_check sh Bash

echo "Compiler check:"
if printf "int main(){}" | g++ -x c++ -
then echo "OK:    g++ works";
else echo "ERROR: g++ does NOT work"; fi
rm -f a.out

if [ "$(nproc)" = "" ]; then
echo "ERROR: nproc is not available or it produces empty output"
else
echo "OK: nproc reports $(nproc) logical cores are available"
fi
**EOF**

**bash version-check.sh**