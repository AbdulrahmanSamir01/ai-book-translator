# 8.37. Bison-3.8.2

The Bison package contains a parser generator.

**Approximate build time:**
2.1 SBU
**Required disk space:**
63 MB

## 8.37.1. Installation of Bison

Prepare Bison for compilation:

**./configure --prefix=/usr --docdir=/usr/share/doc/bison-3.8.2**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

## 8.37.2. Contents of Bison

**Installed programs:**
bison and yacc
**Installed library:**
liby.a
**Installed directory:**
/usr/share/bison

**Short Descriptions**

**bison**
Generates, from a series of rules, a program for analyzing the structure of text files; Bison is a replacement
for Yacc (Yet Another Compiler Compiler)

**yacc**
**A wrapper for bison, meant for programs that still call yacc instead of bison; it calls bison with the -y option**

liby
The Yacc library containing implementations of Yacc-compatible yyerror and main functions; this library is
normally not very useful, but POSIX requires it

---

Linux From Scratch - Version 13.1-systemd

# 8.38. Grep-3.12

The Grep package contains programs for searching through the contents of files.

**Approximate build time:**
0.5 SBU
**Required disk space:**
48 MB

## 8.38.1. Installation of Grep

First, remove a warning about using egrep and fgrep that makes tests on some packages fail:

**sed -i "s/echo/#echo/" src/egrep.sh**

Prepare Grep for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

## 8.38.2. Contents of Grep

**Installed programs:**
egrep, fgrep, and grep

**Short Descriptions**

**egrep**
**Prints lines matching an extended regular expression. It is obsolete, use grep -E instead**

**fgrep**
**Prints lines matching a list of fixed strings. It is obsolete, use grep -F instead**

**grep**
Prints lines matching a basic regular expression

---

Linux From Scratch - Version 13.1-systemd

# 8.39. Bash-5.3

The Bash package contains the Bourne-Again Shell.

**Approximate build time:**
1.4 SBU
**Required disk space:**
56 MB

## 8.39.1. Installation of Bash

Prepare Bash for compilation:

**./configure --prefix=/usr             \**
**--without-bash-malloc     \**
**--with-installed-readline \**
**--docdir=/usr/share/doc/bash-5.3**

**The meaning of the new configure option:**

--with-installed-readline

This option tells Bash to use the readline library that is already installed on the system rather than using its own
readline version.

Compile the package:

**make**

Skip down to “Install the package” if not running the test suite.

To prepare the tests, ensure that the tester user can write to the sources tree:

**chown -R tester .**

The test suite of this package is designed to be run as a non-root user who owns the terminal connected to standard
input. To satisfy the requirement, spawn a new pseudo terminal using Expect and run the tests as the tester user:

**LC_ALL=C.UTF-8 su -s /usr/bin/expect tester << "EOF"**
**set timeout -1**
**spawn make tests**
**expect eof**
**lassign [wait] _ _ _ value**
**exit $value**
**EOF**

**The test suite uses diff to detect the difference between test script output and the expected output. Any output from diff**
(prefixed with < and >) indicates a test failure, unless there is a message saying the difference can be ignored. The test
named run-builtins is known to fail on some host distros with a difference on the 479 and 480 lines of the output.
Some other tests need the zh_TW.BIG5 and ja_JP.SJIS locales, they are known to fail unless those locales are installed.

Install the package:

**make install**

**Run the newly compiled bash program (replacing the one that is currently being executed):**

**exec /usr/bin/bash --login**

## 8.39.2. Contents of Bash

**Installed programs:**
bash, bashbug, and sh (link to bash)
**Installed directory:**
/usr/include/bash, /usr/lib/bash, and /usr/share/doc/bash-5.3

---

Linux From Scratch - Version 13.1-systemd

**Short Descriptions**

**bash**
A widely-used command interpreter; it performs many types of expansions and substitutions on a given
command line before executing it, thus making this interpreter a powerful tool

**bashbug**
**A shell script to help the user compose and mail standard formatted bug reports concerning bash**

**sh**
**A symlink to the bash program; when invoked as sh, bash tries to mimic the startup behavior of historical**
**versions of sh as closely as possible, while conforming to the POSIX standard as well**

---

Linux From Scratch - Version 13.1-systemd

# 8.40. Libtool-2.6.2

The Libtool package contains the GNU generic library support script. It makes the use of shared libraries simpler with
a consistent, portable interface.

**Approximate build time:**
0.6 SBU
**Required disk space:**
50 MB

## 8.40.1. Installation of Libtool

Prepare Libtool for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

Remove a static library only useful for the test suite:

**rm -fv /usr/lib/libltdl.a**

## 8.40.2. Contents of Libtool

**Installed programs:**
libtool and libtoolize
**Installed libraries:**
libltdl.so
**Installed directories:**
/usr/include/libltdl and /usr/share/libtool

**Short Descriptions**

**libtool**
Provides generalized library-building support services

**libtoolize**
**Provides a standard way to add libtool support to a package**

libltdl
Hides the various difficulties of opening dynamically loaded libraries

---

Linux From Scratch - Version 13.1-systemd

# 8.41. GDBM-1.26

The GDBM package contains the GNU Database Manager. It is a library of database functions that uses extensible
hashing and works like the standard UNIX dbm. The library provides primitives for storing key/data pairs, searching
and retrieving the data by its key and deleting a key along with its data.

**Approximate build time:**
0.2 SBU
**Required disk space:**
13 MB

## 8.41.1. Installation of GDBM

Prepare GDBM for compilation:

**./configure --prefix=/usr    \**
**--disable-static \**
**--enable-libgdbm-compat**

**The meaning of the configure option:**

--enable-libgdbm-compat

This switch enables building the libgdbm compatibility library. Some packages outside of LFS may require the
older DBM routines it provides.

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

## 8.41.2. Contents of GDBM

**Installed programs:**
gdbm_dump, gdbm_load, and gdbmtool
**Installed libraries:**
libgdbm.so and libgdbm_compat.so

**Short Descriptions**

**gdbm_dump**
Dumps a GDBM database to a file

**gdbm_load**
Recreates a GDBM database from a dump file

**gdbmtool**
Tests and modifies a GDBM database

libgdbm
Contains functions to manipulate a hashed database

libgdbm_compat
Compatibility library containing older DBM functions

---

Linux From Scratch - Version 13.1-systemd

# 8.42. Gperf-3.3

Gperf generates a perfect hash function from a key set.

**Approximate build time:**
0.2 SBU
**Required disk space:**
12 MB

## 8.42.1. Installation of Gperf

Prepare Gperf for compilation:

**./configure --prefix=/usr --docdir=/usr/share/doc/gperf-3.3**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

## 8.42.2. Contents of Gperf

**Installed program:**
gperf
**Installed directory:**
/usr/share/doc/gperf-3.3

**Short Descriptions**

**gperf**
Generates a perfect hash from a key set

---

Linux From Scratch - Version 13.1-systemd