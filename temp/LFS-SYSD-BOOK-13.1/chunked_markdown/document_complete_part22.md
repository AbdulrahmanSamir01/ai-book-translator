# 5.4. Linux-7.1.8 API Headers

The Linux API Headers (in linux-7.1.8.tar.xz) expose the kernel's API for use by Glibc.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
1.8 GB

## 5.4.1. Installation of Linux API Headers

The Linux kernel needs to expose an Application Programming Interface (API) for the system's C library (Glibc in
LFS) to use. This is done by way of sanitizing various C header files that are shipped in the Linux kernel source tarball.

Make sure there are no stale files embedded in the package:

**make mrproper**

Now extract the user-visible kernel headers from the source. The recommended make target “headers_install” cannot
be used, because it requires rsync, which may not be available. The headers are first placed in ./usr, then copied to
the needed location.

**make headers**
**find usr/include -type f ! -name '*.h' -delete**
**cp -rv usr/include $LFS/usr**

## 5.4.2. Contents of Linux API Headers

**Installed headers:**
/usr/include/asm/*.h, /usr/include/asm-generic/*.h, /usr/include/drm/*.h, /usr/include/
linux/*.h, /usr/include/misc/*.h, /usr/include/mtd/*.h, /usr/include/rdma/*.h, /usr/
include/scsi/*.h, /usr/include/sound/*.h, /usr/include/video/*.h, and /usr/include/xen/*.h
**Installed directories:**
/usr/include/asm, /usr/include/asm-generic, /usr/include/drm, /usr/include/linux, /usr/
include/misc, /usr/include/mtd, /usr/include/rdma, /usr/include/scsi, /usr/include/sound, /
usr/include/video, and /usr/include/xen

**Short Descriptions**

/usr/include/asm/*.h
The Linux API ASM Headers

/usr/include/asm-generic/*.h
The Linux API ASM Generic Headers

/usr/include/drm/*.h
The Linux API DRM Headers

/usr/include/linux/*.h
The Linux API Linux Headers

/usr/include/misc/*.h
The Linux API Miscellaneous Headers

/usr/include/mtd/*.h
The Linux API MTD Headers

/usr/include/rdma/*.h
The Linux API RDMA Headers

/usr/include/scsi/*.h
The Linux API SCSI Headers

/usr/include/sound/*.h
The Linux API Sound Headers

/usr/include/video/*.h
The Linux API Video Headers

/usr/include/xen/*.h
The Linux API Xen Headers

---

Linux From Scratch - Version 13.1-systemd

# 5.5. Glibc-2.44

The Glibc package contains the main C library. This library provides the basic routines for allocating memory, searching
directories, opening and closing files, reading and writing files, string handling, pattern matching, arithmetic, and so on.
**Approximate build time:**
1.3 SBU
**Required disk space:**
900 MB

## 5.5.1. Installation of Glibc

First, create a symbolic link for LSB compliance. Additionally, for x86_64, create a compatibility symbolic link required
for proper operation of the dynamic library loader:

**case $(uname -m) in**
**i?86)   ln -sfv ld-linux.so.2 $LFS/lib/ld-lsb.so.3**
**;;**
**x86_64) ln -sfv ../lib/ld-linux-x86-64.so.2 $LFS/lib64**
**ln -sfv ../lib/ld-linux-x86-64.so.2 $LFS/lib64/ld-lsb-x86-64.so.3**
**;;**
**esac**

### Note

**The above command is correct. The ln command has several syntactic versions, so be sure to check info**
**coreutils ln and ln(1) before reporting what may appear to be an error.**

Some of the Glibc programs use the non-FHS-compliant /var/db directory to store their runtime data. Apply the
following patch to make such programs store their runtime data in the FHS-compliant locations:

**patch -Np1 -i ../glibc-fhs-1.patch**

Fix an issue causing the tanh(3) function to crash on some old x86_64 processors, and to fix installing with multiple
**make jobs:**

**patch -Np1 -i ../glibc-2.44-upstream_fixes-1.patch**

The Glibc documentation recommends building Glibc in a dedicated build directory:

**mkdir -v build**
**cd       build**

**Ensure that the ldconfig and sln utilities are installed into /usr/sbin:**

**echo "rootsbindir=/usr/sbin" > configparms**

Next, prepare Glibc for compilation:

**../configure                             \**
**--prefix=/usr                      \**
**--host=$LFS_TGT                    \**
**--build=$(../scripts/config.guess) \**
**--disable-nscd                     \**
**libc_cv_slibdir=/usr/lib           \**
**--enable-kernel=5.10**

**The meaning of the configure options:**

--host=$LFS_TGT, --build=$(../scripts/config.guess)

The combined effect of these switches is that Glibc's build system configures itself to be cross-compiled, using
the cross-linker and cross-compiler in $LFS/tools.

---

Linux From Scratch - Version 13.1-systemd

--enable-kernel=5.10

This tells Glibc to compile the library with support for 5.10 and later Linux kernels. Workarounds for older kernels
are not enabled.

libc_cv_slibdir=/usr/lib

This ensures that the library is installed in /usr/lib instead of the default /lib64 on 64-bit machines.

--disable-nscd

Do not build the name service cache daemon which is no longer used.

During this stage the following warning might appear:

configure: WARNING:
*** These auxiliary programs are missing or
*** incompatible versions: msgfmt
*** some features will be disabled.
*** Check the INSTALL file for required versions.

**The missing or incompatible msgfmt program is generally harmless. This msgfmt program is part of the Gettext**
package, which the host distribution should provide.

### Note

There have been reports that this package may fail when building as a “parallel make.” If that occurs, rerun
the make command with the -j1 option.

Compile the package:

**make**

Install the package:

### Warning

If LFS is not properly set, and despite the recommendations, you are building as root, the next command will
install the newly built Glibc to your host system, which will almost certainly render it unusable. So double-
check that the environment is correctly set, and that you are not root, before running the following command.

**make DESTDIR=$LFS install**

**The meaning of the make install option:**

DESTDIR=$LFS

The DESTDIR make variable is used by almost all packages to define the location where the package should be
installed. If it is not set, it defaults to the root (/) directory. Here we specify that the package is installed in  $LFS,
which will become the root directory in Section 7.4, “Entering the Chroot Environment.”

**Fix a hard coded path to the executable loader in the ldd script:**

**sed '/RTLDLIST=/s@/usr@@g' -i $LFS/usr/bin/ldd**

Now that our cross toolchain is in place, it is important to ensure that compiling and linking will work as expected.
We do this by performing some sanity checks:

**echo 'int main(){}' | $LFS_TGT-gcc -x c - -v -Wl,--verbose &> dummy.log**
**$LFS_TGT-readelf -l a.out | grep ': /lib'**

---

Linux From Scratch - Version 13.1-systemd

There should be no errors, and the output of the last command will be (allowing for platform-specific differences in
the dynamic linker name):

[Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]

Note that this path should not contain /mnt/lfs (or the value of the LFS variable if you used a different one). The path
is resolved when the compiled program is executed, and that should only happen after we enter the chroot environment
where the kernel would consider $LFS as the root directory (/).

Now make sure that we're set up to use the correct start files:

**grep -E -o "$LFS/lib.*/S?crt[1in].*succeeded" dummy.log**

The output of the last command should be:

/mnt/lfs/lib/../lib/Scrt1.o succeeded
/mnt/lfs/lib/../lib/crti.o succeeded
/mnt/lfs/lib/../lib/crtn.o succeeded

Verify that the compiler is searching for the correct header files:

**grep -B3 "^ $LFS/usr/include" dummy.log**

This command should return the following output:

#include <...> search starts here:
/mnt/lfs/tools/lib/gcc/x86_64-lfs-linux-gnu/16.2.0/include
/mnt/lfs/tools/lib/gcc/x86_64-lfs-linux-gnu/16.2.0/include-fixed
/mnt/lfs/usr/include

Again, the directory named after your target triplet may be different than the above, depending on your system
architecture.

Next, verify that the new linker is being used with the correct search paths:

**grep 'SEARCH.*/usr/lib' dummy.log |sed 's|; |\n|g'**

References to paths that have components with '-linux-gnu' should be ignored, but otherwise the output of the last
command should be:

SEARCH_DIR("=/mnt/lfs/tools/x86_64-lfs-linux-gnu/lib64")
SEARCH_DIR("=/usr/local/lib64")
SEARCH_DIR("=/lib64")
SEARCH_DIR("=/usr/lib64")
SEARCH_DIR("=/mnt/lfs/tools/x86_64-lfs-linux-gnu/lib")
SEARCH_DIR("=/usr/local/lib")
SEARCH_DIR("=/lib")
SEARCH_DIR("=/usr/lib");

A 32-bit system may use a few other directories, but anyway the important facet here is all the paths should begin with
an equal sign (=), which would be replaced with the sysroot directory that we've configured for the linker.

Next make sure that we're using the correct libc:

**grep "/lib.*/libc.so.6 " dummy.log**

The output of the last command should be:

attempt to open /mnt/lfs/usr/lib/libc.so.6 succeeded

Make sure GCC is using the correct dynamic linker:

**grep found dummy.log**

---

Linux From Scratch - Version 13.1-systemd

The output of the last command should be (allowing for platform-specific differences in dynamic linker name):

found ld-linux-x86-64.so.2 at /mnt/lfs/usr/lib/ld-linux-x86-64.so.2

If the output does not appear as shown above or is not received at all, then something is seriously wrong. Investigate
and retrace the steps to find out where the problem is and correct it. Any issues should be resolved before continuing
with the process.

Once everything is working correctly, clean up the test files:

**rm -v a.out dummy.log**

### Note

Building the packages in the next chapter will serve as an additional check that the toolchain has been built
properly. If some package, especially Binutils-pass2 or GCC-pass2, fails to build, it is an indication that
something has gone wrong with the preceding Binutils, GCC, or Glibc installations.

Details on this package are located in Section 8.5.3, “Contents of Glibc.”

---

Linux From Scratch - Version 13.1-systemd