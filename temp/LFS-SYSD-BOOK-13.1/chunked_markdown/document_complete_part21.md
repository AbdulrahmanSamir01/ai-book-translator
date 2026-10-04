# Chapter 5. Compiling a Cross-Toolchain

# 5.1. Introduction

This chapter shows how to build a cross-compiler and its associated tools. Although here cross-compilation is faked,
the principles are the same as for a real cross-toolchain.

The programs compiled in this chapter will be installed under the $LFS/tools directory to keep them separate from the
files installed in the following chapters. The libraries, on the other hand, are installed into their final place, since they
pertain to the system we want to build.

---

Linux From Scratch - Version 13.1-systemd

# 5.2. Binutils-2.47 - Pass 1

The Binutils package contains a linker, an assembler, and other tools for handling object files.
**Approximate build time:**
1 SBU
**Required disk space:**
691 MB

## 5.2.1. Installation of Cross Binutils

### Note

Go back and re-read the notes in the section titled General Compilation Instructions. Understanding the notes
labeled important can save you a lot of problems later.

It is important that Binutils be the first package compiled because both Glibc and GCC perform various tests on the
available linker and assembler to determine which of their own features to enable.

The Binutils documentation recommends building Binutils in a dedicated build directory:

**mkdir -v build**
**cd       build**

### Note

In order for the SBU values listed in the rest of the book to be of any use, measure the time it takes to build
this package from the configuration, up to and including the first install. To achieve this easily, wrap the
**commands in a time command like this: time { ../configure ... && make && make install; }.**

Now prepare Binutils for compilation:

**../configure --prefix=$LFS/tools \**
**--with-sysroot=$LFS \**
**--target=$LFS_TGT   \**
**--disable-nls       \**
**--enable-gprofng=no \**
**--disable-werror    \**
**--enable-new-dtags  \**
**--enable-default-hash-style=gnu**

**The meaning of the configure options:**

### Note
**Contrary to other packages, not all the options listed below appear when running ./configure --help. For**
**example, to find the --with-sysroot option, you have to run ld/configure --help. All the options can be listed**
**at once with ./configure --help=recursive.**

--prefix=$LFS/tools

This tells the configure script to prepare to install the Binutils programs in the $LFS/tools directory.

--with-sysroot=$LFS

For cross compilation, this tells the build system to look in $LFS for the target system libraries as needed.

--target=$LFS_TGT

Because the machine description in the LFS_TGT variable is slightly different than the value returned by the
**config.guess script, this switch will tell the configure script to adjust binutil's build system for building a cross**
linker.

---

Linux From Scratch - Version 13.1-systemd

--disable-nls

This disables internationalization as i18n is not needed for the temporary tools.

--enable-gprofng=no

This disables building gprofng which is not needed for the temporary tools.

--disable-werror

This prevents the build from stopping in the event that there are warnings from the host's compiler.

--enable-new-dtags

This makes the linker use the “runpath” tag for embedding library search paths into executables and shared
libraries, instead of the traditional “rpath” tag. It makes debugging dynamically linked executables easier and
works around potential issues in the test suite of some packages.

--enable-default-hash-style=gnu

By default, the linker would generate both the GNU-style hash table and the classic ELF hash table for shared
libraries and dynamically linked executables. The hash tables are only intended for a dynamic linker to perform
symbol lookup. On LFS the dynamic linker (provided by the Glibc package) will always use the GNU-style hash
table which is faster to query. So the classic ELF hash table is completely useless. This makes the linker only
generate the GNU-style hash table by default, so we can avoid wasting time to generate the classic ELF hash table
when we build the packages, or wasting disk space to store it.

Continue with compiling the package:

**make**

Install the package:

**make install**

Details on this package are located in Section 8.22.2, “Contents of Binutils.”

---

Linux From Scratch - Version 13.1-systemd

# 5.3. GCC-16.2.0 - Pass 1

The GCC package contains the GNU compiler collection, which includes the C and C++ compilers.

**Approximate build time:**
4.3 SBU
**Required disk space:**
5.8 GB

## 5.3.1. Installation of Cross GCC

GCC requires the GMP, MPFR and MPC packages. As these packages may not be included in your host distribution,
they will be built with GCC. Unpack each package into the GCC source directory and rename the resulting directories
so the GCC build procedures will automatically use them:

### Note

There are frequent misunderstandings about the instructions here. The procedures are the same as every other
package, as explained earlier (Package build instructions). First, extract the gcc-16.2.0 tarball from the sources
directory, and then change to the directory created. Only then should you proceed with the instructions below.

**tar -xf ../mpfr-4.2.2.tar.xz**
**mv -v mpfr-4.2.2 mpfr**
**tar -xf ../gmp-6.3.0.tar.xz**
**mv -v gmp-6.3.0 gmp**
**tar -xf ../mpc-1.4.1.tar.xz**
**mv -v mpc-1.4.1 mpc**

On x86_64 hosts, set the default directory name for 64-bit libraries to “lib”:

**case $(uname -m) in**
**x86_64)**
**sed -e '/m64=/s/lib64/lib/' \**
**-i.orig gcc/config/i386/t-linux64**
**;;**
**esac**

### Note

**This example demonstrates the use of the -i.orig switch. It makes the sed copy the t-linux64 file to t-**

**linux64.orig, and then edit the original t-linux64 file inplace. So you may run diff -u gcc/config/i386/t-**
**linux64{.orig,} to visualize the change done by the sed command afterwards. We'll simply use -i (which just**
edits the original file inplace without copying it) for all other packages in the book, but you can change it to

-i.orig in any case you want to keep a copy of the original file.

The GCC documentation recommends building GCC in a dedicated build directory:

**mkdir -v build**
**cd       build**

---

Linux From Scratch - Version 13.1-systemd

Prepare GCC for compilation:

**../configure                  \**
**--target=$LFS_TGT         \**
**--prefix=$LFS/tools       \**
**--with-glibc-version=2.44 \**
**--with-sysroot=$LFS       \**
**--with-newlib             \**
**--without-headers         \**
**--enable-default-pie      \**
**--enable-default-ssp      \**
**--disable-fixincludes     \**
**--disable-nls             \**
**--disable-shared          \**
**--disable-multilib        \**
**--disable-threads         \**
**--disable-libatomic       \**
**--disable-libgomp         \**
**--disable-libquadmath     \**
**--disable-libssp          \**
**--disable-libvtv          \**
**--disable-libstdcxx       \**
**--enable-languages=c,c++**

**The meaning of the configure options:**

--with-glibc-version=2.44

This option specifies the version of Glibc which will be used on the target. It is not relevant to the libc of the
host distro because everything compiled by pass1 GCC will run in the chroot environment, which is isolated from
libc of the host distro.

--with-newlib

Since a working C library is not yet available, this ensures that the inhibit_libc constant is defined when building
libgcc. This prevents the compiling of any code that requires libc support.

--without-headers

When creating a complete cross-compiler, GCC requires standard headers compatible with the target system. For
our purposes these headers will not be needed. This switch prevents GCC from looking for them.

--enable-default-pie and --enable-default-ssp

Those switches allow GCC to compile programs with some hardening security features (more information on
those in the note on PIE and SSP in chapter 8) by default. They are not strictly needed at this stage, since the
compiler will only produce temporary executables. But it is cleaner to have the temporary packages be as close
as possible to the final ones.

--disable-fixincludes

By default, during the installation of GCC some system headers would be “fixed” to be used with GCC. At this
point we've installed no headers for the cross-compiler to use, so building the auxiliary programs for the “fix”
would just waste time. This switch disables the “fix” and skips the build of those programs.

--disable-shared

This switch forces GCC to link its internal libraries statically. We need this because the shared libraries require
Glibc, which is not yet installed on the target system.

--disable-multilib

On x86_64, LFS does not support a multilib configuration. This switch is harmless for x86.

---

Linux From Scratch - Version 13.1-systemd

--disable-threads, --disable-libatomic, --disable-libgomp, --disable-libquadmath, --disable-libssp, --

disable-libvtv, --disable-libstdcxx

These switches disable support for threading, libatomic, libgomp, libquadmath, libssp, libvtv, and the C++ standard
library respectively. These features may fail to compile when building a cross-compiler and are not necessary for
the task of cross-compiling the temporary libc.

--enable-languages=c,c++

This option ensures that only the C and C++ compilers are built. These are the only languages needed now.

Compile GCC by running:

**make**

Install the package:

**make install**

This build of GCC has installed a couple of internal system headers. Normally one of them, limits.h, would in turn
include the corresponding system limits.h header, in this case, $LFS/usr/include/limits.h. However, at the time of
this build of GCC $LFS/usr/include/limits.h does not exist, so the internal header that has just been installed is a
partial, self-contained file and does not include the extended features of the system header. This is adequate for building
Glibc, but the full internal header will be needed later. Create a full version of the internal header using a command
that is identical to what the GCC build system does in normal circumstances:

**cat ../gcc/{limitx,glimits,limity}.h  > \**
**$($LFS_TGT-gcc -print-file-name=include)/limits.h**

Details on this package are located in Section 8.32.2, “Contents of GCC.”

---

Linux From Scratch - Version 13.1-systemd