# 5.6. Libstdc++ from GCC-16.2.0

Libstdc++ is the standard C++ library. It is needed to compile C++ code (part of GCC is written in C++), but we had
to defer its installation when we built gcc-pass1 because Libstdc++ depends on Glibc, which was not yet available in
the target directory.

**Approximate build time:**
0.3 SBU
**Required disk space:**
1.5 GB

## 5.6.1. Installation of Target Libstdc++

### Note

Libstdc++ is part of the GCC sources. You should first unpack the GCC tarball and change to the gcc-16.

2.0 directory.

Create a separate build directory for Libstdc++ and enter it:

**mkdir -v build**
**cd       build**

Prepare Libstdc++ for compilation:

**../libstdc++-v3/configure      \**
**--host=$LFS_TGT            \**
**--build=$(../config.guess) \**
**CXX=$LFS_TGT-gcc           \**
**--prefix=/usr              \**
**--disable-multilib         \**
**--disable-nls              \**
**--disable-libstdcxx-pch    \**
**--with-gxx-include-dir=/tools/$LFS_TGT/include/c++/16.2.0**

**The meaning of the configure options:**

--host=...

Specifies that the cross-compiler we have just built should be used instead of the one in /usr/bin.

CXX=$LFS_TGT-gcc

**Specifies to use $LFS_TGT-gcc to compile the C++ code. The default, $LFS_TGT-g++, would automatically**
specify linking against libstdc++ when invoking the linker, but in our case libstdc++ is not installed yet so
**some checks in the configure script would misbehave with $LFS_TGT-g++. In a normal build, this override is**
**automatically passed to the configure script from the top level directory. Here we explicitly pass it.**

--disable-libstdcxx-pch

This switch prevents the installation of precompiled include files, which are not needed at this stage.

--with-gxx-include-dir=/tools/$LFS_TGT/include/c++/16.2.0

This specifies the installation directory for include files. Because Libstdc++ is the standard C++ library for LFS,
**this directory should match the location where the C++ compiler ($LFS_TGT-g++) would search for the standard**
**C++ include files. In a normal build, this information is automatically passed to the Libstdc++ configure options**
from the top level directory. In our case, this information must be explicitly given. The C++ compiler will prepend
the sysroot path $LFS (specified when building GCC-pass1) to the include file search path, so it will actually
**search in $LFS/tools/$LFS_TGT/include/c++/16.2.0. The combination of the DESTDIR variable (in the make install**
command below) and this switch causes the headers to be installed there.

---

Linux From Scratch - Version 13.1-systemd

Compile Libstdc++ by running:

**make**

Install the library:

**make DESTDIR=$LFS install**

Remove the libtool archive files because they are harmful for cross-compilation:

**rm -v $LFS/usr/lib/lib{stdc++{,exp,fs},supc++}.la**

Details on this package are located in Section 8.32.2, “Contents of GCC.”

---

Linux From Scratch - Version 13.1-systemd

# Chapter 6. Cross Compiling Temporary Tools

# 6.1. Introduction

This chapter shows how to cross-compile basic utilities using the just built cross-toolchain. Those utilities are installed
into their final location, but cannot be used yet. Basic tasks still rely on the host's tools. Nevertheless, the installed
libraries are used when linking.

Using the utilities will be possible in the next chapter after entering the “chroot” environment. But all the packages built
in the present chapter need to be built before we do that. Therefore we cannot be independent of the host system yet.

Once again, let us recall that improper setting of LFS together with building as root, may render your computer unusable.
This whole chapter must be done as user lfs, with the environment as described in Section 4.4, “Setting Up the
Environment.”

---

Linux From Scratch - Version 13.1-systemd

# 6.2. M4-1.4.21

The M4 package contains a macro processor.

**Approximate build time:**
0.1 SBU
**Required disk space:**
39 MB

## 6.2.1. Installation of M4

Ensure packages that use gnulib detect some newer functions found in glibc-2.44.

**cat > $LFS/usr/share/config.site << EOF**
**ac_cv_func_posix_spawn_file_actions_addchdir=yes**
**ac_cv_func_posix_spawn_file_actions_addfchdir=yes**
**EOF**

Prepare M4 for compilation:

**./configure --prefix=/usr   \**
**--host=$LFS_TGT \**
**--build=$(build-aux/config.guess)**

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

Details on this package are located in Section 8.14.2, “Contents of M4.”

---

Linux From Scratch - Version 13.1-systemd

# 6.3. Ncurses-6.6

The Ncurses package contains libraries for terminal-independent handling of character screens.

**Approximate build time:**
0.4 SBU
**Required disk space:**
54 MB

## 6.3.1. Installation of Ncurses

**First, run the following commands to build the tic program on the build host. We install it in $LFS/tools, so that it is**
found in the PATH when needed:

**mkdir build**
**pushd build**
**../configure --prefix=$LFS/tools AWK=gawk**
**make -C include**
**make -C progs tic**
**install progs/tic $LFS/tools/bin**
**popd**

Prepare Ncurses for compilation:

**./configure --prefix=/usr                \**
**--host=$LFS_TGT              \**
**--build=$(./config.guess)    \**
**--mandir=/usr/share/man      \**
**--with-manpage-format=normal \**
**--with-shared                \**
**--without-normal             \**
**--with-cxx-shared            \**
**--without-debug              \**
**--without-ada                \**
**--disable-stripping          \**
**AWK=gawk**

**The meaning of the new configure options:**

--with-manpage-format=normal

This prevents Ncurses from installing compressed manual pages, which may happen if the host distribution itself
has compressed manual pages.

--with-shared

This makes Ncurses build and install shared C libraries.

--without-normal

This prevents Ncurses from building and installing static C libraries.

--without-debug

This prevents Ncurses from building and installing debug libraries.

--with-cxx-shared

This makes Ncurses build and install shared C++ bindings. It also prevents it building and installing static C+
+ bindings.

--without-ada

This ensures that Ncurses does not build support for the Ada compiler, which may be present on the host but will
**not be available once we enter the chroot environment.**

---

Linux From Scratch - Version 13.1-systemd

--disable-stripping

**This switch prevents the building system from using the strip program from the host. Using host tools on cross-**
compiled programs can cause failure.

AWK=gawk

**This switch prevents the building system from using the mawk program from the host. Some versions of mawk**
can cause this package to fail to build.

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**
**ln -sv libncursesw.so $LFS/usr/lib/libncurses.so**
**sed -e 's/^#if.*XOPEN.*$/#if 1/' \**
**-i $LFS/usr/include/curses.h**

**The meaning of the install options:**

**ln -sv libncursesw.so $LFS/usr/lib/libncurses.so**

The libncurses.so library is needed by a few packages we will build soon. We create this symlink to use

libncursesw.so as a replacement.

**sed -e 's/^#if.*XOPEN.*$/#if 1/' ...**

The header file curses.h contains the definition of various Ncurses data structures. With different preprocessor
macro definitions two different sets of the data structure definition may be used: the 8-bit definition is compatible
with libncurses.so and the wide-character definition is compatible with libncursesw.so. Since we are using

libncursesw.so as a replacement of libncurses.so, edit the header file so it will always use the wide-character
data structure definition compatible with libncursesw.so.

Details on this package are located in Section 8.33.2, “Contents of Ncurses.”

---

Linux From Scratch - Version 13.1-systemd