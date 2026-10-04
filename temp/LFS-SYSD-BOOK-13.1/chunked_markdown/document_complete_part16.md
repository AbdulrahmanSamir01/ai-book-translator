### Note
The Linux From Scratch team generates its own tarball of the man pages using the systemd source. This is
done in order to avoid unnecessary dependencies.

**• Tar (1.35) - 2,263 KB:**
Home page: https://www.gnu.org/software/tar/
Download: https://ftpmirror.gnu.org/tar/tar-1.35.tar.xz
MD5 sum: a2d8042658cfd8ea939e6d911eaf4152

**• Tcl (8.6.18) - 11,540 KB:**
Home page: https://tcl.sourceforge.net/
Download: https://downloads.sourceforge.net/tcl/tcl8.6.18-src.tar.gz
MD5 sum: acfe0c9f7d0c626ecf026e834a888da6

**• Tcl Documentation (8.6.18) - 1,172 KB:**
Download: https://downloads.sourceforge.net/tcl/tcl8.6.18-html.tar.gz
MD5 sum: 54d1ff0f5eee4e81e5cdaa4baa343397

**• Texinfo (7.3) - 6,778 KB:**
Home page: https://www.gnu.org/software/texinfo/
Download: https://ftpmirror.gnu.org/texinfo/texinfo-7.3.tar.xz
MD5 sum: 915a09fcdfc2bf0f5ecf9e556d5698ff

**• Time Zone Data (2026c) - 465 KB:**
Home page: https://www.iana.org/time-zones
Download: https://www.iana.org/time-zones/repository/releases/tzdata2026c.tar.gz
MD5 sum: bff7174205cefab793e3b24271ef2f45

**• Util-linux (2.42.2) - 10,409 KB:**
Home page: https://git.kernel.org/pub/scm/utils/util-linux/util-linux.git/
Download: https://www.kernel.org/pub/linux/utils/util-linux/v2.42/util-linux-2.42.2.tar.xz
MD5 sum: 1d70131b70abda3dec3b37e282a20c96

---

Linux From Scratch - Version 13.1-systemd

**• Vim (9.2.1025) - 19,662 KB:**
Home page: https://www.vim.org
Download: https://github.com/vim/vim/archive/v9.2.1025/vim-9.2.1025.tar.gz
MD5 sum: 060c9c0d7e2bdb5e5d80daad596cae02

### Note
The version of vim changes daily. To get the latest version, go to https://github.com/vim/vim/tags.

**• Wheel (0.48.0) - 65 KB:**
Home page: https://pypi.org/project/wheel/
Download: https://pypi.org/packages/source/w/wheel/wheel-0.48.0.tar.gz
MD5 sum: f668e4885de814378b332eceea04a8a0

**• Xz Utils (5.8.3) - 1,512 KB:**
Home page: https://tukaani.org/xz
Download: https://github.com//tukaani-project/xz/releases/download/v5.8.3/xz-5.8.3.tar.xz
MD5 sum: a02753f34e5546d20213b87f876a0933

**• Zlib (1.3.2) - 1,468 KB:**
Home page: https://zlib.net/
Download: https://zlib.net/fossils/zlib-1.3.2.tar.gz
MD5 sum: a1e6c958597af3c67d162995a342138a

**• Zstd (1.5.7) - 2,378 KB:**
Home page: https://facebook.github.io/zstd/
Download: https://github.com/facebook/zstd/releases/download/v1.5.7/zstd-1.5.7.tar.gz
MD5 sum: 780fc1896922b1bc52a4e90980cdda48

Total size of these packages: about 628 MB

# 3.3. Needed Patches

In addition to the packages, several patches are also required. These patches correct any mistakes in the packages that
should be fixed by the maintainer. The patches also make small modifications to make the packages easier to work
with. The following patches will be needed to build an LFS system:

**• Bzip2 Documentation Patch - 1.6 KB:**
Download: https://www.linuxfromscratch.org/patches/lfs/13.1/bzip2-1.0.8-install_docs-1.patch
MD5 sum: 6a5ac7e89b791aae556de0f745916f7f

**• Coreutils Internationalization Fixes Patch - 67 KB:**
Download: https://www.linuxfromscratch.org/patches/lfs/13.1/coreutils-9.11-i18n-1.patch
MD5 sum: 900d64d9936516b68613271c9ebc0059

**• Expect GCC15 Patch - 12 KB:**
Download: https://www.linuxfromscratch.org/patches/lfs/13.1/expect-5.45.4-gcc15-1.patch
MD5 sum: 0ca4d6bb8d572fbcdb13cb36cd34833e

**• Glibc Upstream Fixes Patch - 172 KB:**
Download: https://www.linuxfromscratch.org/patches/lfs/13.1/glibc-2.44-upstream_fixes-1.patch
MD5 sum: 990574184b25aa3029a2444e81865098

---

Linux From Scratch - Version 13.1-systemd

**• Glibc FHS Patch - 2.8 KB:**
Download: https://www.linuxfromscratch.org/patches/lfs/13.1/glibc-fhs-1.patch
MD5 sum: 9a5997c3452909b1769918c759eff8a2

**• Kbd Backspace/Delete Fix Patch - 12 KB:**
Download: https://www.linuxfromscratch.org/patches/lfs/13.1/kbd-2.10.0-backspace-1.patch
MD5 sum: f75cca16a38da6caa7d52151f7136895

**• Python Openssl4 Patch - 38 KB:**
Download: https://www.linuxfromscratch.org/patches/lfs/13.1/Python-3.14.7-openssl_4-1.patch
MD5 sum: 597d7737df1b4ea4e184c193da523050

**• Tar Upstream Patch - 4.3 KB:**
Download: https://www.linuxfromscratch.org/patches/lfs/13.1/tar-1.35-acl_fix-1.patch
MD5 sum: dbab49e317105539611866dac5dd54f6

Total size of these patches: about 309.7 KB

In addition to the above required patches, there exist a number of optional patches created by the LFS community. These
optional patches solve minor problems or enable functionality that is not enabled by default. Feel free to peruse the
patches database located at https://www.linuxfromscratch.org/patches/downloads/ and acquire any additional patches
to suit your system needs.

---

Linux From Scratch - Version 13.1-systemd

# Chapter 4. Final Preparations

# 4.1. Introduction

In this chapter, we will perform a few additional tasks to prepare for building the temporary system. We will create a set
of directories in $LFS (in which we will install the temporary tools), add an unprivileged user, and create an appropriate
build environment for that user. We will also explain the units of time (“SBUs”) we use to measure how long it takes
to build LFS packages, and provide some information about package test suites.

# 4.2. Creating a Limited Directory Layout in the LFS Filesystem

In this section, we begin populating the LFS filesystem with the pieces that will constitute the final Linux system.
The first step is to create a limited directory hierarchy, so that the programs compiled in Chapter 6 (as well as glibc
and libstdc++ in Chapter 5) can be installed in their final location. We do this so those temporary programs will be
overwritten when the final versions are built in Chapter 8.

Create the required directory layout by issuing the following commands as root:

**mkdir -pv $LFS/{etc,var} $LFS/usr/{bin,lib,sbin}**

**for i in bin lib sbin; do**
**ln -sv usr/$i $LFS/$i**
**done**

**case $(uname -m) in**
**x86_64) mkdir -pv $LFS/lib64 ;;**
**esac**

Programs in Chapter 6 will be compiled with a cross-compiler (more details can be found in section Toolchain Technical
Notes). This cross-compiler will be installed in a special directory, to separate it from the other programs. Still acting
as root, create that directory with this command:

**mkdir -pv $LFS/tools**

### Note

The LFS editors have deliberately decided not to use a /usr/lib64 directory. Several steps are taken to be
sure the toolchain will not use it. If for any reason this directory appears (either because you made an error
in following the instructions, or because you installed a binary package that created it after finishing LFS), it
may break your system. You should always be sure this directory does not exist.

# 4.3. Adding the LFS User

When logged in as user root, making a single mistake can damage or destroy a system. Therefore, the packages in the
next two chapters are built as an unprivileged user. You could use your own user name, but to make it easier to set up
a clean working environment, we will create a new user called lfs as a member of a new group (also named lfs) and
run commands as lfs during the installation process. As root, issue the following commands to add the new user:

**groupadd lfs**
**useradd -s /bin/bash -g lfs -m -k /dev/null lfs**

**This is what the command line options mean:**

-s /bin/bash

**This makes bash the default shell for user lfs.**

---

Linux From Scratch - Version 13.1-systemd

-g lfs

This option adds user lfs to group lfs.

-m

This creates a home directory for lfs.

-k /dev/null

This parameter prevents possible copying of files from a skeleton directory (the default is /etc/skel) by changing
the input location to the special null device.

lfs

This is the name of the new user.

If you want to log in as lfs or switch to lfs from a non-root user (as opposed to switching to user lfs when logged in
as root, which does not require the lfs user to have a password), you need to set a password for lfs. Issue the following
command as the root user to set the password:

**passwd lfs**

Grant lfs full access to all the directories under $LFS by making lfs the owner:

**chown -v lfs $LFS/{usr{,/*},var,etc,tools}**
**case $(uname -m) in**
**x86_64) chown -v lfs $LFS/lib64 ;;**
**esac**

### Note

**In some host systems, the following su command does not complete properly and suspends the login for the**

**lfs user to the background. If the prompt "lfs:~$" does not appear immediately, entering the fg command**
will fix the issue.

Next, start a shell running as user lfs. This can be done by logging in as lfs on a virtual console, or with the following
substitute/switch user command:

**su - lfs**

**The “-” instructs su to start a login shell as opposed to a non-login shell. The difference between these two types of**
**shells is described in detail in bash(1) and info bash.**