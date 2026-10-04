## 8.2.3. Deploying LFS on Multiple Systems

One of the advantages of an LFS system is that there are no files that depend on the position of files on a disk system.
**Cloning an LFS build to another computer with the same architecture as the base system is as simple as using tar on**
the LFS partition that contains the root directory (about 900MB uncompressed for a basic LFS build), copying that
file via network transfer or CD-ROM / USB stick to the new system, and expanding it. After that, a few configuration
files will have to be changed. Configuration files that may need to be updated include: /etc/hosts, /etc/fstab, /etc/

passwd, /etc/group,  /etc/shadow, and /etc/ld.so.conf.

A custom kernel may be needed for the new system, depending on differences in system hardware and the original
kernel configuration.

### Important

If you want to deploy the LFS system onto a system with a different CPU, when you build Section 8.23,
“GMP-6.3.0” and Section 8.51, “Libffi-3.8.0” you must follow the notes about overriding the architecture-
specific optimization to produce libraries suitable for both the host system and the system(s) where you'll
deploy the LFS system. Otherwise you'll get Illegal Instruction errors running LFS.

The GMP build system stores the architecture-specific optimization option used to build GMP into gmp.h,
and the build system of some package using GMP can read it from the header and use it when building the
package itself. At least the MPFR build system is known to do so. Thus simply rebuilding GMP on a complete
LFS system is not enough: you'll need to recompile MPFR and maybe other packages using GMP if you want
to “convert” a complete LFS system to be used for a different CPU.

Finally, the new system has to be made bootable via Section 10.4, “Using GRUB to Set Up the Boot Process”.

---

Linux From Scratch - Version 13.1-systemd

# 8.3. Man-pages-6.18

The Man-pages package contains over 2,400 man pages.

**Approximate build time:**
0.1 SBU
**Required disk space:**
54 MB

## 8.3.1. Installation of Man-pages

Remove two man pages for password hashing functions. Libxcrypt will provide a better version of these man pages:

**rm -v man3/crypt***

Install Man-pages by running:

**make -R GIT=false prefix=/usr install**

**The meaning of the options:**

-R

**This prevents make from setting any built-in variables. The building system of man-pages does not work well with**
built-in variables, but currently there is no way to disable them except passing -R explicitly via the command line.

GIT=false

This prevents the building system from emitting many git: command not found warnings lines.

## 8.3.2. Contents of Man-pages

**Installed files:**
various man pages

**Short Descriptions**

man pages
Describe C programming language functions, important device files, and significant configuration files

---

Linux From Scratch - Version 13.1-systemd

# 8.4. Iana-Etc-20260805

The Iana-Etc package provides data for network services and protocols.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
4.8 MB

## 8.4.1. Installation of Iana-Etc

For this package, we only need to copy the files into place:

**cp -v services protocols /etc**

## 8.4.2. Contents of Iana-Etc

**Installed files:**
/etc/protocols and /etc/services

**Short Descriptions**

/etc/protocols
Describes the various DARPA Internet protocols that are available from the TCP/IP subsystem

/etc/services
Provides a mapping between friendly textual names for internet services, and their underlying
assigned port numbers and protocol types

---

Linux From Scratch - Version 13.1-systemd

# 8.5. Glibc-2.44

The Glibc package contains the main C library. This library provides the basic routines for allocating memory, searching
directories, opening and closing files, reading and writing files, string handling, pattern matching, arithmetic, and so on.

**Approximate build time:**
11 SBU
**Required disk space:**
3.7 GB

## 8.5.1. Installation of Glibc

Some of the Glibc programs use the non-FHS compliant /var/db directory to store their runtime data. Apply the
following patch to make such programs store their runtime data in the FHS-compliant locations:

**patch -Np1 -i ../glibc-fhs-1.patch**

Fix an issue causing the tanh(3) function to crash on some old x86_64 processors, and to fix installing with multiple
**make jobs:**

**patch -Np1 -i ../glibc-2.44-upstream_fixes-1.patch**

The Glibc documentation recommends building Glibc in a dedicated build directory:

**mkdir -v build**
**cd       build**

Prepare Glibc for compilation:

**../configure --prefix=/usr                   \**
**--disable-werror                \**
**--disable-nscd                  \**
**libc_cv_slibdir=/usr/lib        \**
**--enable-stack-protector=strong \**
**--enable-kernel=5.10**

**The meaning of the configure options:**

--disable-werror

This option disables the -Werror option passed to GCC. This is necessary for running the test suite.

--enable-kernel=5.10

This option tells the build system that this Glibc may be used with kernels as old as 5.10. This means generating
workarounds in case a system call introduced in a later version cannot be used.

--enable-stack-protector=strong

This option increases system security by adding extra code to check for buffer overflows, such as stack smashing
attacks. Note that Glibc always explicitly overrides the default of GCC, so this option is still needed even though
we've already specified --enable-default-ssp for GCC.

--disable-nscd

Do not build the name service cache daemon which is no longer used.

libc_cv_slibdir=/usr/lib

This variable sets the correct library for all systems. We do not want lib64 to be used.

Compile the package:

**make**

---

Linux From Scratch - Version 13.1-systemd

### Important

In this section, the test suite for Glibc is considered critical. Do not skip it under any circumstance.

Generally a few tests do not pass. The test failures listed below are usually safe to ignore.

**make check**

You may see some test failures. The Glibc test suite is somewhat dependent on the host system. A few failures out of
over 6000 tests can generally be ignored. This is a list of the most common issues seen for recent versions of LFS:

• io/tst-lchmod is known to fail in the LFS chroot environment.

• Some tests, for example nss/tst-nss-files-hosts-multi and nptl/tst-thread-affinity* are known to fail due to a timeout
(especially when the system is relatively slow and/or running the test suite with multiple parallel make jobs).
These tests can be identified with:

**grep "Timed out" $(find -name \*.out)**

**It's possible to re-run a single test with enlarged timeout with TIMEOUTFACTOR=<factor> make test t=<test**

**name>. For example, TIMEOUTFACTOR=10 make test t=nss/tst-nss-files-hosts-multi will re-run nss/tst-nss-**
files-hosts-multi with ten times the original timeout.

• Additionally, some tests may fail with a relatively old CPU model (for example elf/tst-cpu-features-cpuinfo) or
host kernel version (for example stdlib/tst-arc4random-thread), or with a host kernel newer than 7.1.8.

Though it is a harmless message, the install stage of Glibc will complain about the absence of /etc/ld.so.conf. Prevent
this warning with:

**touch /etc/ld.so.conf**

Fix the Makefile to skip an outdated sanity check that fails with a modern Glibc configuration:

**sed '/test-installation/s@$(PERL)@echo not running@' -i ../Makefile**

---

Linux From Scratch - Version 13.1-systemd

### Important

If upgrading Glibc to a new minor version (for example, from Glibc-2.36 to Glibc-2.44) on a running LFS
system, you need to take some extra precautions to avoid breaking the system:

• Upgrading Glibc on a LFS system prior to 11.0 (exclusive) is not supported. Rebuild LFS if you are
running such an old LFS system but you need a newer Glibc.

• If upgrading on a LFS system prior to 12.0 (exclusive), install Libxcrypt following Section 8.29,
**“Libxcrypt-4.5.2.” In addition to a normal Libxcrypt installation, you MUST follow the note in**
**Libxcrypt section to install libcrypt.so.1* (replacing libcrypt.so.1 from the prior Glibc**
**installation).**

**• If upgrading on a LFS system prior to 12.1 (exclusive), remove the nscd program:**

**rm -f /usr/sbin/nscd**

If this system (prior to LFS 12.1, exclusive) is based on Systemd, it's also needed to disable and stop the
**nscd service now:**

**systemctl disable --now nscd**

**• Upgrade the kernel and reboot if it's older than 5.10 (check the current version with uname -r) or if you**
want to upgrade it anyway, following Section 10.3, “Linux-7.1.8.”

**• Upgrade the kernel API headers if it's older than 5.10 (check the current version with cat /usr/include/**
**linux/version.h) or if you want to upgrade it anyway, following Section 5.4, “Linux-7.1.8 API Headers”**
**(but removing $LFS from the cp command).**

• Perform a DESTDIR installation and upgrade the Glibc shared libraries on the system using one single
**install command:**

**make DESTDIR=$PWD/dest install**
**install -vm755 dest/usr/lib/*.so.* /usr/lib**

**It's imperative to strictly follow these steps above unless you completely understand what you are doing. Any**
**unexpected deviation may render the system completely unusable. YOU ARE WARNED.**

**Then continue to run the make install command, the sed command against /usr/bin/ldd, and the commands**
to install the locales. Once they are finished, reboot the system immediately.

When the system has successfully rebooted, if you are running a LFS system prior to 12.0 (exclusive) where
GCC was not built with the --disable-fixincludes option, move two GCC headers into a better location and
remove the stale “fixed” copies of the Glibc headers:

**DIR=$(dirname $(gcc -print-libgcc-file-name))**
**[ -e $DIR/include/limits.h ]    || mv $DIR/include{-fixed,}/limits.h**
**[ -e $DIR/include/syslimits.h ] || mv $DIR/include{-fixed,}/syslimits.h**
**rm -rfv $DIR/include-fixed/***
**unset DIR**

Install the package:

**make install**

**Fix a hardcoded path to the executable loader in the ldd script:**

**sed '/RTLDLIST=/s@/usr@@g' -i /usr/bin/ldd**

---

Linux From Scratch - Version 13.1-systemd

Next, install the locales that can make the system respond in a different language. None of these locales are required,
but if some of them are missing, the test suites of some packages will skip important test cases.

**Individual locales can be installed using the localedef program. E.g., the second localedef command below combines**
the /usr/share/i18n/locales/cs_CZ charset-independent locale definition with the /usr/share/i18n/charmaps/UTF-8.

gz charmap definition and appends the result to the /usr/lib/locale/locale-archive file. The following instructions
will install the minimum set of locales necessary for the optimal coverage of tests:

**localedef -i C -f UTF-8 C.UTF-8**
**localedef -i cs_CZ -f UTF-8 cs_CZ.UTF-8**
**localedef -i de_DE -f ISO-8859-1 de_DE**
**localedef -i de_DE@euro -f ISO-8859-15 de_DE@euro**
**localedef -i de_DE -f UTF-8 de_DE.UTF-8**
**localedef -i el_GR -f ISO-8859-7 el_GR**
**localedef -i en_GB -f ISO-8859-1 en_GB**
**localedef -i en_GB -f UTF-8 en_GB.UTF-8**
**localedef -i en_HK -f ISO-8859-1 en_HK**
**localedef -i en_PH -f ISO-8859-1 en_PH**
**localedef -i en_US -f ISO-8859-1 en_US**
**localedef -i en_US -f UTF-8 en_US.UTF-8**
**localedef -i es_ES -f ISO-8859-15 es_ES@euro**
**localedef -i es_MX -f ISO-8859-1 es_MX**
**localedef -i fa_IR -f UTF-8 fa_IR**
**localedef -i fr_FR -f ISO-8859-1 fr_FR**
**localedef -i fr_FR@euro -f ISO-8859-15 fr_FR@euro**
**localedef -i fr_FR -f UTF-8 fr_FR.UTF-8**
**localedef -i is_IS -f ISO-8859-1 is_IS**
**localedef -i is_IS -f UTF-8 is_IS.UTF-8**
**localedef -i it_IT -f ISO-8859-1 it_IT**
**localedef -i it_IT -f ISO-8859-15 it_IT@euro**
**localedef -i it_IT -f UTF-8 it_IT.UTF-8**
**localedef -i ja_JP -f EUC-JP ja_JP**
**localedef -i ja_JP -f UTF-8 ja_JP.UTF-8**
**localedef -i nl_NL@euro -f ISO-8859-15 nl_NL@euro**
**localedef -i ru_RU -f KOI8-R ru_RU.KOI8-R**
**localedef -i ru_RU -f UTF-8 ru_RU.UTF-8**
**localedef -i se_NO -f UTF-8 se_NO.UTF-8**
**localedef -i ta_IN -f UTF-8 ta_IN.UTF-8**
**localedef -i tr_TR -f UTF-8 tr_TR.UTF-8**
**localedef -i zh_CN -f GB18030 zh_CN.GB18030**
**localedef -i zh_HK -f BIG5-HKSCS zh_HK.BIG5-HKSCS**
**localedef -i zh_TW -f UTF-8 zh_TW.UTF-8**

In addition, install the locale for your own country, language and character set.

Alternatively, install all the locales listed in the glibc-2.44/localedata/SUPPORTED file (it includes every locale listed
above and many more) at once with the following time-consuming command:

**make localedata/install-locales**