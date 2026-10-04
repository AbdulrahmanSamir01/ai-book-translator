# 6.4. Bash-5.3

The Bash package contains the Bourne-Again Shell.

**Approximate build time:**
0.2 SBU
**Required disk space:**
73 MB

## 6.4.1. Installation of Bash

Prepare Bash for compilation:

**./configure --prefix=/usr                      \**
**--build=$(sh support/config.guess) \**
**--host=$LFS_TGT                    \**
**--without-bash-malloc              \**
**--docdir=/usr/share/doc/bash-5.3**

**The meaning of the configure options:**

--without-bash-malloc

This option turns off the use of Bash's memory allocation (malloc) function which is known to cause segmentation
faults. By turning this option off, Bash will use the malloc functions from Glibc which are more stable.

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

**Make a link for the programs that use sh for a shell:**

**ln -sv bash $LFS/bin/sh**

Details on this package are located in Section 8.39.2, “Contents of Bash.”

---

Linux From Scratch - Version 13.1-systemd

# 6.5. Coreutils-9.11

The Coreutils package contains the basic utility programs needed by every operating system.

**Approximate build time:**
0.3 SBU
**Required disk space:**
193 MB

## 6.5.1. Installation of Coreutils

Prepare Coreutils for compilation:

**./configure --prefix=/usr                     \**
**--host=$LFS_TGT                   \**
**--build=$(build-aux/config.guess) \**
**--enable-install-program=hostname**

**The meaning of the configure options:**

--enable-install-program=hostname

**This enables the hostname binary to be built and installed – it is disabled by default but is required by the Perl**
test suite.

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

Move programs to their final expected locations. Although this is not necessary in this temporary environment, we must
do so because some programs hardcode executable locations:

**mv -v $LFS/usr/bin/chroot              $LFS/usr/sbin**
**mkdir -pv $LFS/usr/share/man/man8**
**mv -v $LFS/usr/share/man/man1/chroot.1 $LFS/usr/share/man/man8/chroot.8**
**sed -i 's/"1"/"8"/'                    $LFS/usr/share/man/man8/chroot.8**

Details on this package are located in Section 8.61.2, “Contents of Coreutils.”

---

Linux From Scratch - Version 13.1-systemd

# 6.6. Diffutils-3.12

The Diffutils package contains programs that show the differences between files or directories.

**Approximate build time:**
0.1 SBU
**Required disk space:**
35 MB

## 6.6.1. Installation of Diffutils

Prepare Diffutils for compilation:

**./configure --prefix=/usr   \**
**--host=$LFS_TGT \**
**gl_cv_func_strcasecmp_works=yes \**
**--build=$(./build-aux/config.guess)**

**The meaning of the configure options:**

gl_cv_func_strcasecmp_works=yes

This option specify the result of a check for the strcasecmp function. The check requires running a compiled C
program, and this is impossible during cross-compilation because in general a cross-compiled program cannot
**run on the host distro. Normally for such a check the configure script would use a fall-back value for cross-**
**compilation, but the fall-back value for this check is absent and the configure script would have no value to use**
**and error out. Upstream have already fixed the issue, but to apply the fix we'd need to run autoconf that the host**
distro may lack. So we just specify the check result (yes as we know the strcasecmp function in Glibc-2.44 works
**fine) instead, then configure will just use the specified value and skip the check.**

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

Details on this package are located in Section 8.62.2, “Contents of Diffutils.”

---

Linux From Scratch - Version 13.1-systemd

# 6.7. File-5.48

The File package contains a utility for determining the type of a given file or files.

**Approximate build time:**
0.1 SBU
**Required disk space:**
46 MB

## 6.7.1. Installation of File

**The file command on the build host needs to be the same version as the one we are building in order to create the**
**signature file. Run the following commands to make a temporary copy of the file command:**

**mkdir build**
**pushd build**
**../configure --disable-bzlib      \**
**--disable-libseccomp \**
**--disable-xzlib      \**
**--disable-zlib**
**make**
**popd**

**The meaning of the new configure option:**

--disable-*

The configuration script attempts to use some packages from the host distribution if the corresponding library files
exist. It may cause compilation failure if a library file exists, but the corresponding header files do not. These
options prevent using these unneeded capabilities from the host.

Prepare File for compilation:

**./configure --prefix=/usr --host=$LFS_TGT --build=$(./config.guess)**

Compile the package:

**make FILE_COMPILE=$(pwd)/build/src/file**

Install the package:

**make DESTDIR=$LFS install**

Remove the libtool archive file because it is harmful for cross compilation:

**rm -v $LFS/usr/lib/libmagic.la**

Details on this package are located in Section 8.11.2, “Contents of File.”

---

Linux From Scratch - Version 13.1-systemd

# 6.8. Findutils-4.11.0

The Findutils package contains programs to find files. Programs are provided to search through all the files in a directory
tree and to create, maintain, and search a database (often faster than the recursive find, but unreliable unless the database
**has been updated recently). Findutils also supplies the xargs program, which can be used to run a specified command**
on each file selected by a search.

**Approximate build time:**
0.2 SBU
**Required disk space:**
51 MB

## 6.8.1. Installation of Findutils

Prepare Findutils for compilation:

**./configure --prefix=/usr                   \**
**--localstatedir=/var/lib/locate \**
**--host=$LFS_TGT                 \**
**--build=$(build-aux/config.guess)**

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

Details on this package are located in Section 8.63.2, “Contents of Findutils.”

---

Linux From Scratch - Version 13.1-systemd

# 6.9. Gawk-5.4.1

The Gawk package contains programs for manipulating text files.

**Approximate build time:**
0.1 SBU
**Required disk space:**
52 MB

## 6.9.1. Installation of Gawk

First, ensure some unneeded files are not installed:

**sed -i 's/extras//' Makefile.in**

Prepare Gawk for compilation:

**./configure --prefix=/usr   \**
**--host=$LFS_TGT \**
**--build=$(build-aux/config.guess)**

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

Details on this package are located in Section 8.31.2, “Contents of Gawk.”

---

Linux From Scratch - Version 13.1-systemd

# 6.10. Grep-3.12

The Grep package contains programs for searching through the contents of files.

**Approximate build time:**
0.1 SBU
**Required disk space:**
32 MB

## 6.10.1. Installation of Grep

Prepare Grep for compilation:

**./configure --prefix=/usr   \**
**--host=$LFS_TGT \**
**--build=$(./build-aux/config.guess)**

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

Details on this package are located in Section 8.38.2, “Contents of Grep.”

---

Linux From Scratch - Version 13.1-systemd

# 6.11. Gzip-1.14

The Gzip package contains programs for compressing and decompressing files.

**Approximate build time:**
0.1 SBU
**Required disk space:**
12 MB

## 6.11.1. Installation of Gzip

Prepare Gzip for compilation:

**./configure --prefix=/usr --host=$LFS_TGT**

Compile the package:

**make**

Install the package:

**make DESTDIR=$LFS install**

Details on this package are located in Section 8.66.2, “Contents of Gzip.”

---

Linux From Scratch - Version 13.1-systemd