# Prerequisites

Building an LFS system is not a simple task. It requires a certain level of existing knowledge of Unix system
administration in order to resolve problems and correctly execute the commands listed. In particular, as an absolute
minimum, you should already know how to use the command line (shell) to copy or move files and directories, list
directory and file contents, and change the current directory. It is also expected that you know how to use and install
Linux software.

Because the LFS book assumes at least this basic level of skill, the various LFS support forums are unlikely to provide
you with much assistance in these areas. You will find that your questions regarding such basic knowledge will likely
go unanswered (or you will simply be referred to the LFS essential pre-reading list).

Before building an LFS system, we urge you to read these articles:

• Software-Building-HOWTO https://tldp.org/HOWTO/Software-Building-HOWTO.html

This is a comprehensive guide to building and installing “generic” Unix software packages under Linux. Although
it was written some time ago, it still provides a good summary of the basic techniques used to build and install
software.

• Beginner's Guide to Installing from Source https://moi.vonos.net/linux/beginners-installing-from-source/

This guide provides a good summary of the basic skills and techniques needed to build software from source code.

# LFS and Standards

The structure of LFS follows Linux standards as closely as possible. The primary standards are:

• POSIX.1-2008.

• Filesystem Hierarchy Standard (FHS) Version 3.0

• Linux Standard Base (LSB) Version 5.0 (2015)

The LSB has four separate specifications: Core, Desktop, Languages, and Imaging. Some parts of Core and
Desktop specifications are architecture specific. There are also two trial specifications: Gtk3 and Graphics.
LFS attempts to conform to the LSB specifications for the IA32 (32-bit x86) or AMD64 (x86_64) architectures
discussed in the previous section.

### Note

Many people do not agree with these requirements. The main purpose of the LSB is to ensure that
proprietary software can be installed and run on a compliant system. Since LFS is source based, the user
has complete control over what packages are desired; you may choose not to install some packages that
are specified by the LSB.

While it is possible to create a complete system that will pass the LSB certification tests “from scratch,” this can't be
done without many additional packages that are beyond the scope of the LFS book. Installation instructions for some
of these additional packages can be found in BLFS.

**Packages supplied by LFS needed to satisfy the LSB Requirements**

LSB Core:
Bash, Bc, Binutils, Coreutils, Diffutils, File, Findutils, Gawk,
GCC, Gettext, Glibc, Grep, Gzip, M4, Man-DB, Procps,
Psmisc, Sed, Shadow, Systemd, Tar, Util-linux, Zlib

x

---

Linux From Scratch - Version 13.1-systemd

LSB Desktop:
None

LSB Languages:
Perl

LSB Imaging:
None

LSB Gtk3 and LSB Graphics (Trial Use):
None

**Packages supplied by BLFS needed to satisfy the LSB Requirements**

LSB Core:
At, Batch (a part of At), BLFS Bash Startup Files, Cpio, Ed,
Fcrontab, LSB-Tools, NSPR, NSS, Linux-PAM, Pax, Sendmail
(or Postfix or Exim), Time

LSB Desktop:
Alsa, ATK, Cairo, Desktop-file-utils, Freetype, Fontconfig,
Gdk-pixbuf, Glib2, GLU, Icon-naming-utils, Libjpeg-turbo,
Libxml2, Mesa, Pango, Xdg-utils, Xorg

LSB Languages:
Libxml2, Libxslt

LSB Imaging:
CUPS, Cups-filters, Ghostscript, SANE

LSB Gtk3 and LSB Graphics (Trial Use):
GTK+3

**Components not supplied or optionally supplied by LFS or BLFS needed to satisfy the LSB**
**Requirements**

LSB Core:
**install_initd, libcrypt.so.1 (can be provided with optional**
instructions for the LFS Libxcrypt package), libncurses.so.5
(can be provided with optional instructions for the LFS Ncurses
package), libncursesw.so.5 (but libncursesw.so.6 is provided
by the LFS Ncurses package)

LSB Desktop:
libgdk-x11-2.0.so (but libgdk-3.so is provided by the BLFS
GTK+-3 package), libgtk-x11-2.0.so (but libgtk-3.so and

libgtk-4.so are provided by the BLFS GTK+-3 and GTK-4
packages), libpng12.so (but libpng16.so is provided by the
BLFS Libpng package), libQt*.so.4 (but libQt6*.so.6 are
provided by the BLFS Qt6 package), libtiff.so.4 (but

libtiff.so.6 is provided by the BLFS Libtiff package)

LSB Languages:
**/usr/bin/python (LSB requires Python2 but LFS and BLFS**
only provide Python3)

LSB Imaging:
None

LSB Gtk3 and LSB Graphics (Trial Use):
libpng15.so (but libpng16.so is provided by the BLFS Libpng
package)

# Rationale for Packages in the Book

The goal of LFS is to build a complete and usable foundation-level system—including all the packages needed to
replicate itself—and providing a relatively minimal base from which to customize a more complete system based on the
user's choices. This does not mean that LFS is the smallest system possible. Several important packages are included that
are not, strictly speaking, required. The list below documents the reasons each package in the book has been included.

• Acl

xi

---

Linux From Scratch - Version 13.1-systemd

This package contains utilities to administer Access Control Lists, which are used to define fine-grained
discretionary access rights for files and directories.

• Attr

This package contains programs for managing extended attributes on file system objects.

• Autoconf

This package supplies programs for producing shell scripts that can automatically configure source code from a
developer's template. It is often needed to rebuild a package after the build procedure has been updated.

• Automake

This package contains programs for generating Make files from a template. It is often needed to rebuild a package
after the build procedure has been updated.

• Bash

This package satisfies an LSB core requirement to provide a Bourne Shell interface to the system. It was chosen
over other shell packages because of its common usage and extensive capabilities.

• Bc

This package provides an arbitrary precision numeric processing language. It satisfies a requirement for building
the Linux kernel.

• Binutils

This package supplies a linker, an assembler, and other tools for handling object files. The programs in this
package are needed to compile most of the packages in an LFS system.

• Bison

This package contains the GNU version of yacc (Yet Another Compiler Compiler) needed to build several of the
LFS programs.

• Bzip2

This package contains programs for compressing and decompressing files. It is required to decompress many LFS
packages.

• Coreutils

This package contains a number of essential programs for viewing and manipulating files and directories. These
programs are needed for command line file management, and are necessary for the installation procedures of every
package in LFS.

• D-Bus

This package contains programs to implement a message bus system, a simple way for applications to talk to one
another.

• DejaGNU

This package supplies a framework for testing other programs.

• Diffutils

This package contains programs that show the differences between files or directories. These programs can be used
to create patches, and are also used in many packages' build procedures.

xii

---

Linux From Scratch - Version 13.1-systemd

• E2fsprogs

This package supplies utilities for handling the ext2, ext3 and ext4 file systems. These are the most common and
thoroughly tested file systems that Linux supports.

• Expat

This package yields a relatively small XML parsing library. It is required by the XML::Parser Perl module.