# 6.12. Make-4.4.1

The Make package contains a program for controlling the generation of executables and other non-source files of a
package from source files.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
15 MB

## 6.12.1. Installation of Make

Prepare Make for compilation:

**./configure --prefix=/usr   \**
**--host=$LFS_TGT \**
**--build=$(build-aux/config.guess)**

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

Details on this package are located in Section 8.70.2, “Contents of Make.”

---

Linux From Scratch - Version 13.1-systemd

# 6.13. Patch-2.8

The Patch package contains a program for modifying or creating files by applying a “patch” file typically created by
**the diff program.**

**Approximate build time:**
0.1 SBU
**Required disk space:**
14 MB

## 6.13.1. Installation of Patch

Prepare Patch for compilation:

**./configure --prefix=/usr   \**
**--host=$LFS_TGT \**
**--build=$(build-aux/config.guess)**

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

Details on this package are located in Section 8.71.2, “Contents of Patch.”

---

Linux From Scratch - Version 13.1-systemd

# 6.14. Sed-4.10

The Sed package contains a stream editor.

**Approximate build time:**
0.1 SBU
**Required disk space:**
27 MB

## 6.14.1. Installation of Sed

Prepare Sed for compilation:

**./configure --prefix=/usr   \**
**--host=$LFS_TGT \**
**--build=$(./build-aux/config.guess)**

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

Details on this package are located in Section 8.34.2, “Contents of Sed.”

---

Linux From Scratch - Version 13.1-systemd

# 6.15. Tar-1.35

The Tar package provides the ability to create tar archives as well as perform various other kinds of archive
manipulation. Tar can be used on previously created archives to extract files, to store additional files, or to update or
list files which were already stored.

**Approximate build time:**
0.1 SBU
**Required disk space:**
43 MB

## 6.15.1. Installation of Tar

Prepare Tar for compilation:

**./configure --prefix=/usr   \**
**--host=$LFS_TGT \**
**--build=$(build-aux/config.guess)**

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

Details on this package are located in Section 8.72.2, “Contents of Tar.”

---

Linux From Scratch - Version 13.1-systemd

# 6.16. Xz-5.8.3

The Xz package contains programs for compressing and decompressing files. It provides capabilities for the lzma and
**the newer xz compression formats. Compressing text files with xz yields a better compression percentage than with**
**the traditional gzip or bzip2 commands.**

**Approximate build time:**
0.1 SBU
**Required disk space:**
24 MB

## 6.16.1. Installation of Xz

Prepare Xz for compilation:

**./configure --prefix=/usr                     \**
**--host=$LFS_TGT                   \**
**--build=$(build-aux/config.guess) \**
**--disable-static                  \**
**--docdir=/usr/share/doc/xz-5.8.3**

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

Remove the libtool archive file because it is harmful for cross compilation:

**rm -v $LFS/usr/lib/liblzma.la**

Details on this package are located in Section 8.8.2, “Contents of Xz.”

---

Linux From Scratch - Version 13.1-systemd

# 6.17. Binutils-2.47 - Pass 2

The Binutils package contains a linker, an assembler, and other tools for handling object files.

**Approximate build time:**
0.4 SBU
**Required disk space:**
560 MB

## 6.17.1. Installation of Binutils

Binutils building system relies on an shipped libtool copy to link against internal static libraries, but the libiberty and
zlib copies shipped in the package do not use libtool. This inconsistency may cause produced binaries mistakenly linked
against libraries from the host distro. Work around this issue:

**sed '6031s/$add_dir//' -i ltmain.sh**

Create a separate build directory again:

**mkdir -v build**
**cd       build**

Prepare Binutils for compilation:

**../configure                   \**
**--prefix=/usr              \**
**--build=$(../config.guess) \**
**--host=$LFS_TGT            \**
**--disable-nls              \**
**--enable-shared            \**
**--enable-gprofng=no        \**
**--disable-werror           \**
**--enable-64-bit-bfd        \**
**--enable-new-dtags         \**
**--enable-default-hash-style=gnu**

**The meaning of the new configure options:**

--enable-shared

Builds libbfd as a shared library.

--enable-64-bit-bfd

Enables 64-bit support (on hosts with smaller word sizes). This may not be needed on 64-bit systems, but it does
no harm.

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

Remove the libtool archive files because they are harmful for cross compilation, and remove unnecessary static libraries:

**rm -v $LFS/usr/lib/lib{bfd,ctf,ctf-nobfd,opcodes,sframe}.{a,la}**

Details on this package are located in Section 8.22.2, “Contents of Binutils.”

---

Linux From Scratch - Version 13.1-systemd

# 6.18. GCC-16.2.0 - Pass 2

The GCC package contains the GNU compiler collection, which includes the C and C++ compilers.

**Approximate build time:**
5.2 SBU
**Required disk space:**
6.4 GB

## 6.18.1. Installation of GCC

As in the first build of GCC, the GMP, MPFR, and MPC packages are required. Unpack the tarballs and move them
into the required directories:

**tar -xf ../mpfr-4.2.2.tar.xz**
**mv -v mpfr-4.2.2 mpfr**
**tar -xf ../gmp-6.3.0.tar.xz**
**mv -v gmp-6.3.0 gmp**
**tar -xf ../mpc-1.4.1.tar.xz**
**mv -v mpc-1.4.1 mpc**

If you are building on x86_64, change the default directory name for 64-bit libraries to “lib”:

**case $(uname -m) in**
**x86_64)**
**sed -e '/m64=/s/lib64/lib/' \**
**-i.orig gcc/config/i386/t-linux64**
**;;**
**esac**

Create a separate build directory again:

**mkdir -v build**
**cd       build**

Before starting to build GCC, remember to unset any environment variables that override the default optimization flags.

Now prepare GCC for compilation:

**../configure                   \**
**--build=$(../config.guess) \**
**--host=$LFS_TGT            \**
**--target=$LFS_TGT          \**
**--prefix=/usr              \**
**--with-build-sysroot=$LFS  \**
**--enable-default-pie       \**
**--enable-default-ssp       \**
**--disable-fixincludes      \**
**--disable-nls              \**
**--disable-multilib         \**
**--disable-libatomic        \**
**--disable-libgomp          \**
**--disable-libquadmath      \**
**--disable-libsanitizer     \**
**--disable-libssp           \**
**--disable-libvtv           \**
**--enable-languages=c,c++   \**
**CXX_FOR_TARGET="$LFS_TGT-gcc -nostdinc++" \**
**LDFLAGS_FOR_TARGET=-L$PWD/$LFS_TGT/libgcc \**
**target_configargs=gcc_cv_target_thread_file=posix**

---

Linux From Scratch - Version 13.1-systemd

**The meaning of the new configure options:**

--target=$LFS_TGT

We are cross-compiling GCC, so it's impossible to build target libraries (libgcc and libstdc++) with the GCC
binaries compiled in this pass—those binaries won't run on the host. The GCC build system will attempt to use
the host's C and C++ compilers as a workaround by default. Building the GCC target libraries with a different
version of GCC is not supported, so using the host's compilers may cause the build to fail. This parameter ensures
the libraries are built by GCC pass 1.

--with-build-sysroot=$LFS

Normally, using --host ensures that a cross-compiler is used for building GCC, and that compiler knows that it has
to look for headers and libraries in $LFS. However, the build system for GCC uses additional tools which are not
aware of this location. This switch is needed so those tools will find the needed files in $LFS, and not on the host.

--disable-fixincludes

By default, during the installation of GCC some system headers would be “fixed” to be used with GCC. This is
not necessary for a modern Linux system, and potentially harmful if a package is reinstalled after installing GCC.
This switch prevents GCC from “fixing” the headers.

--disable-libsanitizer

Disable GCC sanitizer runtime libraries. They are not needed for the temporary installation. In gcc-pass1 it was
implied by --disable-libstdcxx, and now we can explicitly pass it.

CXX="$LFS_TGT-gcc -nostdinc++"

**Specifies to use $LFS_TGT-gcc to compile the C++ code like Section 5.6, “Libstdc++ from GCC-16.2.0” and**
prevent the compiler from using the headers from the previous libstdc++ installation. Mixing those headers and
the C++ headers from the current libstdc++ build can cause the #include_next directives fail to find the C headers.
**In a normal build, this override is automatically passed to the configure script from the top level directory. Here**
we explicitly pass it.

LDFLAGS_FOR_TARGET=...

Allow libstdc++ to use the libgcc being built in this pass, instead of the previous version built in gcc-pass1. The
previous version cannot properly support C++ exception handling because it was built without libc support.

target_configargs=gcc_cv_target_thread_file=posix

Build the target libraries libgcc and libstdc++ with POSIX thread support enabled. The default is following the
configuration of the compiler used for building the target library (in this case, gcc-pass1 which was configured
with none thread support).

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

**As a finishing touch, create a utility symlink. Many programs and scripts run cc instead of gcc, which is used to keep**
programs generic and therefore usable on all kinds of UNIX systems where the GNU C compiler is not always installed.
**Running cc leaves the system administrator free to decide which C compiler to install:**

**ln -sv gcc $LFS/usr/bin/cc**

Details on this package are located in Section 8.32.2, “Contents of GCC.”

---

Linux From Scratch - Version 13.1-systemd