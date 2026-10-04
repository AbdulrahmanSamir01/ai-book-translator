# Part I. Introduction

---

Linux From Scratch - Version 13.1-systemd

# Chapter 1. Introduction

# 1.1. How to Build an LFS System

The LFS system will be built by using an already installed Linux distribution (such as Debian, OpenMandriva, Fedora,
or openSUSE). This existing Linux system (the host) will be used as a starting point to provide necessary programs,
including a compiler, linker, and shell, to build the new system. Select the “development” option during the distribution
installation to include these tools.

### Note

There are many ways to install a Linux distribution and the defaults are usually not optimal for building an
LFS system. For suggestions on setting up a commercial distribution see: https://www.linuxfromscratch.org/
hints/downloads/files/partitioning-for-lfs.txt.

As an alternative to installing a separate distribution on your machine, you may wish to use a LiveCD from a commercial
distribution.

### Note

The host distro must satisfy Host System Requirements.

Chapter 2 of this book describes how to create a new Linux native partition and file system, where the new LFS
system will be compiled and installed. Chapter 3 explains which packages and patches must be downloaded to build
an LFS system, and how to store them on the new file system. Chapter 4 discusses the setup of an appropriate working
environment. Please read Chapter 4 carefully as it explains several important issues you should be aware of before you
begin to work your way through Chapter 5 and beyond.

Chapter 5 explains the installation of the initial tool chain, (binutils, gcc, and glibc) using cross-compilation techniques
to isolate the new tools from the host system.

Chapter 6 shows you how to cross-compile basic utilities using the just built cross-toolchain.

Chapter 7 then enters a "chroot" environment, where we use the new tools to build all the rest of the tools needed to
create the LFS system.

This effort to isolate the new system from the host distribution may seem excessive. A full technical explanation as to
why this is done is provided in Toolchain Technical Notes.

In Chapter 8 the full-blown LFS system is built. Another advantage provided by the chroot environment is that it allows
you to continue using the host system while LFS is being built. While waiting for package compilations to complete,
you can continue using your computer as usual.

To finish the installation, the basic system configuration is set up in Chapter 9, and the kernel and boot loader are
created in Chapter 10. Chapter 11 contains information on continuing the LFS experience beyond this book. After the
steps in this chapter have been implemented, the computer is ready to boot into the new LFS system.

This is the process in a nutshell. Detailed information on each step is presented in the following chapters. Items that
seem complicated now will be clarified, and everything will fall into place as you commence your LFS adventure.

# 1.2. What's new since the last release

Here is a list of the packages updated since the previous release of LFS.

---

Linux From Scratch - Version 13.1-systemd

**Upgraded to:**

•

• Acl-2.4.0

• Attr-2.6.0

• Autoconf-2.73

• Binutils-2.47

• Coreutils-9.11

• E2fsprogs-1.47.4

• Expat-2.8.3

• File-5.48

• Findutils-4.11.0

• Flit-Core-4.0.2

• Gawk-5.4.1

• GCC-16.2.0

• Glibc-2.44

• Groff-1.24.1

• Iana-Etc-20260805

• Inetutils-2.8

• IPRoute2-7.1.0

• Kbd-2.10.0

• Less-704

• Libcap-2.78

• Libelf from Elfutils-0.195

• Libffi-3.8.0

• Libtool-2.6.2

• Linux-7.1.8

• Man-pages-6.18

• Meson-1.12.0

• MPC-1.4.1

• OpenSSL-4.0.1

• Packaging-26.3

• Perl-5.44.0

• Pkgconf-3.0.5

---

Linux From Scratch - Version 13.1-systemd

• Procps-ng-4.0.7

• Python-3.14.7

• Sed-4.10

• Setuptools-84.0.0

• Shadow-4.20.2

• Sqlite-3530400

• Systemd-261.2

• Tcl-8.6.18

• Texinfo-7.3

• Tzdata-2026c

• Util-linux-2.42.2

• Vim-9.2.1025

• Wheel-0.48.0

• Xz-5.8.3

**Added:**

• mpdecimal-4.0.1

• tar-1.35-acl_fix-1.patch

• Python-3.14.6-consolidated_fixes-1.patch

**Removed:**

•

• XML-Parser (Moved to BLFS)

• intltool (Moved to BLFS)

# 1.3. Changelog

This is version 13.1-systemd of the Linux From Scratch book, dated September 1st, 2026. If this book is more than six
months old, a newer and better version is probably already available. To find out, please check one of the mirrors via
https://www.linuxfromscratch.org/mirrors.html.

Below is a list of changes made since the previous release of the book.

**Changelog Entries:**

• 2026-09-01

• [bdubbs] - LFS-13.1 released.

• 2026-08-31

• [bdubbs] - Update to vim-9.2.1025 (Security Update). Fixes #6006.

---

Linux From Scratch - Version 13.1-systemd

• 2026-08-15

• [bdubbs] - Update to expat-2.8.3 (Security Update). Fixes #5996.

• [bdubbs] - Update to iana-etc-20260805. Addresses #5006.

• [bdubbs] - Update to libffi-3.8.0. Fixes #5993.

• [bdubbs] - Update to linux-7.1.8. Fixes #5997.

• [bdubbs] - Update to meson-1.12.0. Fixes #5998.

• [bdubbs] - Update to procps-ng-4.0.7. Fixes #6000.

• [bdubbs] - Update to setuptools-84.0.0 (Python module). Fixes #5994.

• [bdubbs] - Update to shadow-4.20.2. Fixes #5995.

• [bdubbs] - Update to vim-9.2.0954. Addresses #4500.

• [bdubbs] - Update to wheel-0.48.0 (Python module). Fixes #5999.

• 2026-08-07

• [bdubbs] - Update to flit_core-4.0.2 (Python module). Fixes #5989.

• [bdubbs] - Update to gcc-16.2.0. Fixes #5992.

• [bdubbs] - Update to linux-7.1.7. Fixes #5988.

• [bdubbs] - Update to packaging-26.3 (Python module). Fixes #5990.

• [bdubbs] - Update to pkgconf-3.0.5. Fixes #5987.

• [bdubbs] - Update to Python-3.14.7 (Security Update). Fixes #5991.

• 2026-08-01

• [bdubbs] - Update to shadow-4.20.0. Fixes #5986.

• [bdubbs] - Update to vim-9.2.0858 (Security Update). Fixes #5982.

• [bdubbs] - Update to systemd-261.2. Fixes #5981.

• [bdubbs] - Update to sqlite-3.53.4. Fixes #5984.

• [bdubbs] - Update to pkgconf-3.0.4. Fixes #5977.

• [bdubbs] - Update to perl-5.44.0. Fixes #5980.

• [bdubbs] - Update to linux-7.1.5. Fixes #5979.

• [bdubbs] - Update to libtool-2.6.2. Fixes #5978.

• [bdubbs] - Update to iana-etc-20260723. Addresses #5006.

• [bdubbs] - Update to glibc-2.44 (Security Update). Fixes #5983.

• [bdubbs] - Update to binutils-2.47. Fixes #5985.

• 2026-07-15

• [bdubbs] - Add mpdecimal-4.0.1. Fixes #5963.

• [bdubbs] - Update to tzdata-2026c. Fixes #5971.

• [bdubbs] - Update to setuptools-83.0.0. Fixes #5969.

• [bdubbs] - Update to pkgconf-3.0.2. Fixes #5962.

• [bdubbs] - Update to meson-1.11.2. Fixes #5975.

---

Linux From Scratch - Version 13.1-systemd

• [bdubbs] - Update to libffi-3.7.1. Fixes #5970.
• [bdubbs] - Update to linux-7.1.3. Fixes #5968.
• [bdubbs] - Update to gawk-5.4.1. Fixes #5973.
• [bdubbs] - Update to findutils-4.11.0. Fixes #5974.
• 2026-07-01
• [bdubbs] - Add tar-1.35-acl_fix-1.patch. Addresses issue arising from acl-2.4.0.
• [bdubbs] - Add Python3-3.14.6 consolidated fixes (Security patch). Fixes #5961.
• [bdubbs] - Update to attr-2.6.0 (Security Update). Fixes #5967.
• [bdubbs] - Update to acl-2.4.0 (Security Update). Fixes #5966.
• [bdubbs] - Update to expat-2.8.2 (Security Update). Fixes #5964.
• [bdubbs] - Update to iana-etc-20260617. Addresses #5006.
• [bdubbs] - Update to iproute2-7.1.0. Fixes #5954.
• [bdubbs] - Update to libffi-3.6.0. Fixes #5958.
• [bdubbs] - Update to linux-7.1.1. Fixes #5953.
• [bdubbs] - Update to sqlite-autoconf-3.53.3. Fixes #5965.
• [bdubbs] - Update to systemd-261. Fixes #5959.
• [bdubbs] - Update to util-linux-2.42.2 (Security Update). Fixes #5955.
• [bdubbs] - Update to vim-9.2.0752 (Security Update). Fixes #5956.
• 2026-06-15
• [bdubbs] - Update to binutils-2.46.1. Fixes #5950.
• [bdubbs] - Update to file-5.48. Fixes #5949.
• [bdubbs] - Update to less-704. Fixes #5948.
• [bdubbs] - Update to linux-7.0.12. Fixes #5945.
• [bdubbs] - Update to openssl-4.0.1. Fixes #5951.
• [bdubbs] - Update to Python3-3.14.6. Fixes #5952.
• [bdubbs] - Update to sqlite-autoconf-3.53.2. Fixes #5946.
• [bdubbs] - Update to vim-9.2.0640 (Security Update). Fixes #5947.
• 2026-06-01
• [bdubbs] - Update to systemd-260.2. Fixes #5944.
• [bdubbs] - Update to kbd-2.10.0. Fixes #5943.
• [bdubbs] - Update to util-linux-2.42.1. Fixes #5939.
• [bdubbs] - Update to less-702. Fixes #5941.
• [bdubbs] - Update to vim-9.2.0567 (Security Update). Fixes #5940.
• [bdubbs] - Update to iana-etc-20260529. Addresses #5006.
• 2026-05-24
• [bdubbs] - Update to linux-7.0.10 (Security Update). Fixes #5942.