### Important

In this section, the test suite for GCC is considered important, but it takes a long time. First-time builders are
encouraged to run the test suite. The time to run the tests can be reduced significantly by adding -jx to the
**make -k check command below, where x is the number of CPU cores on your system.**

GCC may need more stack space compiling some extremely complex code patterns. As a precaution for the host distros
with a tight stack limit, explicitly set the stack size hard limit to infinite. On most host distros (and the final LFS system)
the hard limit is infinite by default, but there is no harm done by setting it explicitly. It's not necessary to change the
stack size soft limit because GCC will automatically set it to an appropriate value, as long as the value does not exceed
the hard limit:

**ulimit -s -H unlimited**

Test the results as a non-privileged user, but do not stop at errors:

**chown -R tester .**
**su tester -c "PATH=$PATH make -k check"**

To extract a summary of the test suite results, run:

**../contrib/test_summary -t**

**To filter out only the summaries, pipe the output through grep -A7 Summ.**

Results can be compared with those located at https://www.linuxfromscratch.org/lfs/build-logs/13.1/ and https://gcc.
gnu.org/ml/gcc-testresults/.

In the gcc.target/i386 tests, the tests named auto-init-padding-9.c, builtin-memmove-*.c, mem{cpy,set}-pr120683-

*.c, pr111657-1.c, pr115102.c, pr116896.c, pr120881-2a.c, and pr122343-4a.c are known to fail. The test named shift-

gf2p8affine-2.c is known to fail if the processor does not support AVX512.

---

Linux From Scratch - Version 13.1-systemd

In the g++.target/i386 tests, the tests named memset-pr108585-1{a,b}.C, mv{,c}-symbols*.C, pr112824-2.C, and

pr116896-1.C are known to fail.

Additionally, the tests gcc.dg/ipa/pr122458.c, gcc.dg/lto/toplevel-*-asm-*, and gcc.dg/plugin/crash-test-

nested-*.c are known to fail. The test g++.dg/gomp/deprecate-1.C is known to fail sometimes.

The LFS editors have investigated those failures and confirmed none indicates a critical issue. Most of them are because
the test case author did not anticipate --enable-default-ssp or --enable-default-pie.

A few unexpected failures cannot always be avoided. In some cases test failures depend on the specific hardware of the
system. Unless the test results are vastly different from those at the above URL, it is safe to continue.

Install the package:

**make install**

The GCC build directory is owned by  tester now, and the ownership of the installed header directory (and its content)
is incorrect. Change the ownership to the root user and group:

**chown -v -R root:root $(gcc -print-file-name=include){,-fixed}**

Create a symlink required by the FHS for "historical" reasons.

**ln -svr /usr/bin/cpp /usr/lib**

**Many packages use the name cc to call the C compiler. We've already created cc as a symlink in gcc-pass2, create its**
man page as a symlink as well:

**ln -sv gcc.1 /usr/share/man/man1/cc.1**

Add a compatibility symlink to enable building programs with Link Time Optimization (LTO):

**ln -sfvr $(gcc -print-prog-name=liblto_plugin.so) /usr/lib/bfd-plugins/**

Now that our final toolchain is in place, it is important to again ensure that compiling and linking will work as expected.
We do this by performing some sanity checks:

**echo 'int main(){}' | cc -x c - -v -Wl,--verbose &> dummy.log**
**readelf -l a.out | grep ': /lib'**

There should be no errors, and the output of the last command will be (allowing for platform-specific differences in
the dynamic linker name):

[Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]

Now make sure that we're set up to use the correct start files:

**grep -E -o '/usr/lib.*/S?crt[1in].*succeeded' dummy.log**

The output of the last command should be:

/usr/lib/gcc/x86_64-pc-linux-gnu/16.2.0/../../../../lib/Scrt1.o succeeded
/usr/lib/gcc/x86_64-pc-linux-gnu/16.2.0/../../../../lib/crti.o succeeded
/usr/lib/gcc/x86_64-pc-linux-gnu/16.2.0/../../../../lib/crtn.o succeeded

Depending on your machine architecture, the above may differ slightly. The difference will be the name of the directory
**after /usr/lib/gcc. The important thing to look for here is that gcc has found all three crt*.o files under the /usr/**

lib directory.

Verify that the compiler is searching for the correct header files:

**grep -B4 '^ /usr/include' dummy.log**

---

Linux From Scratch - Version 13.1-systemd

This command should return the following output:

#include <...> search starts here:
/usr/lib/gcc/x86_64-pc-linux-gnu/16.2.0/include
/usr/local/include
/usr/lib/gcc/x86_64-pc-linux-gnu/16.2.0/include-fixed
/usr/include

Again, the directory named after your target triplet may be different than the above, depending on your system
architecture.

Next, verify that the new linker is being used with the correct search paths:

**grep 'SEARCH.*/usr/lib' dummy.log |sed 's|; |\n|g'**

References to paths that have components with '-linux-gnu' should be ignored, but otherwise the output of the last
command should be:

SEARCH_DIR("/usr/x86_64-pc-linux-gnu/lib64")
SEARCH_DIR("/usr/lib");
SEARCH_DIR("/usr/x86_64-pc-linux-gnu/lib")

A 32-bit system may use a few other directories. For example, here is the output from an i686 machine:

SEARCH_DIR("/usr/i686-pc-linux-gnu/lib32")
SEARCH_DIR("/usr/local/lib32")
SEARCH_DIR("/lib32")
SEARCH_DIR("/usr/lib32")
SEARCH_DIR("/usr/i686-pc-linux-gnu/lib")
SEARCH_DIR("/usr/local/lib")
SEARCH_DIR("/lib")
SEARCH_DIR("/usr/lib");

Next make sure that we're using the correct libc:

**grep "/lib.*/libc.so.6 " dummy.log**

The output of the last command should be:

attempt to open /usr/lib/libc.so.6 succeeded

Make sure GCC is using the correct dynamic linker:

**grep found dummy.log**

The output of the last command should be (allowing for platform-specific differences in dynamic linker name):

found ld-linux-x86-64.so.2 at /usr/lib/ld-linux-x86-64.so.2

If the output does not appear as shown above or is not received at all, then something is seriously wrong. Investigate
and retrace the steps to find out where the problem is and correct it. Any issues should be resolved before continuing
with the process.

Once everything is working correctly, clean up the test files:

**rm -v a.out dummy.log**

Finally, move a misplaced file:

**mkdir -pv /usr/share/gdb/auto-load/usr/lib**
**mv -v /usr/lib/*gdb.py /usr/share/gdb/auto-load/usr/lib**

---

Linux From Scratch - Version 13.1-systemd

## 8.32.2. Contents of GCC

**Installed programs:**
c++, cc (link to gcc), cpp, g++, gcc, gcc-ar, gcc-nm, gcc-ranlib, gcov, gcov-dump, gcov-
tool, and lto-dump
**Installed libraries:**
libasan.{a,so}, libatomic.{a,so}, libcc1.so, libgcc.a, libgcc_eh.a, libgcc_s.so, libgcov.a,
libgomp.{a,so}, libhwasan.{a,so}, libitm.{a,so}, liblsan.{a,so}, liblto_plugin.so,
libquadmath.{a,so}, libssp.{a,so}, libssp_nonshared.a, libstdc++.{a,so}, libstdc++exp.a,
libstdc++fs.a, libsupc++.a, libtsan.{a,so}, and libubsan.{a,so}
**Installed directories:**
/usr/include/c++, /usr/lib/gcc, /usr/libexec/gcc, and /usr/share/gcc-16.2.0

**Short Descriptions**

**c++**
The C++ compiler

**cc**
The C compiler

**cpp**
The C preprocessor; it is used by the compiler to expand the #include, #define, and similar
directives in the source files

**g++**
The C++ compiler

**gcc**
The C compiler

**gcc-ar**
**A wrapper around ar that adds a plugin to the command line. This program is only used to add**
"link time optimization" and is not useful with the default build options.

**gcc-nm**
**A wrapper around nm that adds a plugin to the command line. This program is only used to add**
"link time optimization" and is not useful with the default build options.

**gcc-ranlib**
**A wrapper around ranlib that adds a plugin to the command line. This program is only used to**
add "link time optimization" and is not useful with the default build options.

**gcov**
A coverage testing tool; it is used to analyze programs to determine where optimizations will
have the greatest effect

**gcov-dump**
Offline gcda and gcno profile dump tool

**gcov-tool**
Offline gcda profile processing tool

**lto-dump**
Tool for dumping object files produced by GCC with LTO enabled

libasan
The Address Sanitizer runtime library

libatomic
GCC atomic built-in runtime library

libcc1
A library that allows GDB to make use of GCC

libgcc
**Contains run-time support for gcc**

libgcov
This library is linked into a program when GCC is instructed to enable profiling

libgomp
GNU implementation of the OpenMP API for multi-platform shared-memory parallel
programming in C/C++ and Fortran

libhwasan
The Hardware-assisted Address Sanitizer runtime library

libitm
The GNU transactional memory library

liblsan
The Leak Sanitizer runtime library

liblto_plugin
GCC's LTO plugin allows Binutils to process object files produced by GCC with LTO enabled

libquadmath
GCC Quad Precision Math Library API

---

Linux From Scratch - Version 13.1-systemd

libssp
Contains routines supporting GCC's stack-smashing protection functionality. Normally it is not
used, because Glibc also provides those routines.

libstdc++
The standard C++ library

libstdc++exp
Experimental C++ Contracts library

libstdc++fs
ISO/IEC TS 18822:2015 Filesystem library

libsupc++
Provides supporting routines for the C++ programming language

libtsan
The Thread Sanitizer runtime library

libubsan
The Undefined Behavior Sanitizer runtime library

---

Linux From Scratch - Version 13.1-systemd