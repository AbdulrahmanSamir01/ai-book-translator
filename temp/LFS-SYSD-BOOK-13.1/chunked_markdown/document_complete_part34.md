# 8.10. Zstd-1.5.7

Zstandard is a real-time compression algorithm, providing high compression ratios. It offers a very wide range of
compression / speed trade-offs, while being backed by a very fast decoder.

**Approximate build time:**
0.4 SBU
**Required disk space:**
88 MB

## 8.10.1. Installation of Zstd

Compile the package:

**make prefix=/usr**

### Note

In the test output there are several places that indicate 'failed'. These are expected and only 'FAIL' is an actual
test failure. There should be no test failures.

To test the results, issue:

**make check**

Install the package:

**make prefix=/usr install**

Remove the static library:

**rm -v /usr/lib/libzstd.a**

## 8.10.2. Contents of Zstd

**Installed programs:**
zstd, zstdcat (link to zstd), zstdgrep, zstdless, zstdmt (link to zstd), and unzstd (link to
zstd)
**Installed library:**
libzstd.so

**Short Descriptions**

**zstd**
Compresses or decompresses files using the ZSTD format

**zstdgrep**
**Runs grep on ZSTD compressed files**

**zstdless**
**Runs less on ZSTD compressed files**

libzstd
The library implementing lossless data compression, using the ZSTD algorithm

---

Linux From Scratch - Version 13.1-systemd

# 8.11. File-5.48

The File package contains a utility for determining the type of a given file or files.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
21 MB

## 8.11.1. Installation of File

Prepare File for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

## 8.11.2. Contents of File

**Installed programs:**
file
**Installed library:**
libmagic.so

**Short Descriptions**

**file**
Tries to classify each given file; it does this by performing several tests—file system tests, magic number
tests, and language tests

libmagic
**Contains routines for magic number recognition, used by the file program**

---

Linux From Scratch - Version 13.1-systemd

# 8.12. Readline-8.3

The Readline package is a set of libraries that offer command-line editing and history capabilities.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
17 MB

## 8.12.1. Installation of Readline

Reinstalling Readline will cause the old libraries to be moved to <libraryname>.old. While this is normally not a
**problem, in some cases it can trigger a linking bug in ldconfig. This can be avoided by issuing the following two seds:**

**sed -i '/MV.*old/d' Makefile.in**
**sed -i '/{OLDSUFF}/c:' support/shlib-install**

Prevent hard coding library search paths (rpath) into the shared libraries. This package does not need rpath for an
installation into the standard location, and rpath may sometimes cause unwanted effects or even security issues:

**sed -i 's/-Wl,-rpath,[^ ]*//' support/shobj-conf**

Fix a problem identified upstream specifically for this version of readline:

**sed -e '270a\**
**else\**
**chars_avail = 1;'      \**
**-e '288i\   result = -1;' \**
**-i.orig input.c**

Prepare Readline for compilation:

**./configure --prefix=/usr    \**
**--disable-static \**
**--with-curses    \**
**--docdir=/usr/share/doc/readline-8.3**

**The meaning of the new configure option:**

--with-curses

This option tells Readline that it can find the termcap library functions in the curses library, not a separate termcap
library. This will generate the correct readline.pc file.

Compile the package:

**make SHLIB_LIBS="-lncursesw"**

**The meaning of the make option:**

SHLIB_LIBS="-lncursesw"

This option forces Readline to link against the libncursesw library. For details see the “Shared Libraries” section
in the package's README file.

This package does not come with a test suite.

Install the package:

**make install**

If desired, install the documentation:

**install -v -m644 doc/*.{ps,pdf,html,dvi} /usr/share/doc/readline-8.3**

---

Linux From Scratch - Version 13.1-systemd

## 8.12.2. Contents of Readline

**Installed libraries:**
libhistory.so and libreadline.so
**Installed directories:**
/usr/include/readline and /usr/share/doc/readline-8.3

**Short Descriptions**

libhistory
Provides a consistent user interface for recalling lines of history

libreadline
Provides a set of commands for manipulating text entered in an interactive session of a program

---

Linux From Scratch - Version 13.1-systemd

# 8.13. Pcre2-10.47

The pcre2 package contains a new generation of the Perl Compatible Regular Expression libraries.

**Approximate build time:**
0.2 SBU
**Required disk space:**
28 MB

## 8.13.1. Installation of Pcre2

Prepare pcre2 for compilation:

**./configure --prefix=/usr                       \**
**--docdir=/usr/share/doc/pcre2-10.47 \**
**--enable-unicode                    \**
**--enable-jit                        \**
**--enable-pcre2-16                   \**
**--enable-pcre2-32                   \**
**--enable-pcre2grep-libz             \**
**--enable-pcre2grep-libbz2           \**
**--enable-pcre2test-libreadline      \**
**--disable-static**

**The meaning of the new configure options:**

--enable-unicode

This option enables Unicode support and includes the functions for handling UTF-8/16/32 character strings in
the library.

--enable-jit

This option enables Just-in-time compiling, which can greatly speed up pattern matching.

--enable-pcre2-16

This option enables 16 bit character support.

--enable-pcre2-32

This option enables 32 bit character support.

--enable-pcre2grep-libz

This option adds support for reading .gz compressed files to pcre2grep.

--enable-pcre2grep-libbz2

This option adds support for reading .bz2 compressed files to pcre2grep.

--enable-pcre2test-libreadline

This option adds line editing and history features to the pcre2test program.

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

---

Linux From Scratch - Version 13.1-systemd

## 8.13.2. Contents of Pcre2

**Installed programs:**
pcre2grep and pcre2test
**Installed library:**
libpcre2-8.so, libpcre2-16.so, libpcre2-32.so, and libpcre2-posix.so

**Short Descriptions**

**pcre2grep**
is a version of grep that understands Perl compatible regular expressions

**pcre2test**
can test a Perl compatible regular expression

---

Linux From Scratch - Version 13.1-systemd

# 8.14. M4-1.4.21

The M4 package contains a macro processor.

**Approximate build time:**
0.4 SBU
**Required disk space:**
62 MB

## 8.14.1. Installation of M4

Prepare M4 for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

## 8.14.2. Contents of M4

**Installed program:**
m4

**Short Descriptions**

**m4**
Copies the given files while expanding the macros that they contain. These macros are either built-in or user-
**defined and can take any number of arguments. Besides performing macro expansion, m4 has built-in functions**
for including named files, running Unix commands, performing integer arithmetic, manipulating text, recursion,
**etc. The m4 program can be used either as a front end to a compiler or as a macro processor in its own right**

---

Linux From Scratch - Version 13.1-systemd

# 8.15. Bc-7.0.3

The Bc package contains an arbitrary precision numeric processing language.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
7.8 MB

## 8.15.1. Installation of Bc

Prepare Bc for compilation:

**CC='gcc -std=c99' ./configure --prefix=/usr -G -O3 -r**

**The meaning of the configure options:**

CC='gcc -std=c99'

This parameter specifies the compiler and C standard to use.

-G

Omit parts of the test suite that won't work until the bc program has been installed.

-O3

Specify the optimization to use.

-r

Enable the use of Readline to improve the line editing feature of bc.

Compile the package:

**make**

To test bc, run:

**make test**

Install the package:

**make install**

## 8.15.2. Contents of Bc

**Installed programs:**
bc and dc

**Short Descriptions**

**bc**
A command line calculator

**dc**
A reverse-polish command line calculator

---

Linux From Scratch - Version 13.1-systemd