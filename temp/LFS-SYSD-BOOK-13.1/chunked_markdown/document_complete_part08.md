• Readline

This package is a set of libraries that offer command-line editing and history capabilities. It is used by Bash.

• Sed

This package allows editing of text without opening it in a text editor. It is also needed by many LFS packages'
configure scripts.

• Shadow

This package contains programs for handling passwords securely.

• Sqlite

This package provides a serverless, zero-configuration, transactional SQL database engine.

• Systemd

xvi

---

Linux From Scratch - Version 13.1-systemd

This package provides an init program and several additional boot and system control capabilities as an alternative
to SysVinit. It is used by many Linux distributions.

• Tar

This package provides archiving and extraction capabilities of virtually all the packages used in LFS.

• Tcl

This package contains the Tool Command Language used in many test suites.

• Texinfo

This package supplies programs for reading, writing, and converting info pages. It is used in the installation
procedures of many LFS packages.

• Util-linux

This package contains miscellaneous utility programs. Among them are utilities for handling file systems,
consoles, partitions, and messages.

• Vim

This package provides an editor. It was chosen because of its compatibility with the classic vi editor and its huge
number of powerful capabilities. An editor is a very personal choice for many users. Any other editor can be
substituted, if you wish.

• Wheel

This package supplies a Python module that is the reference implementation of the Python wheel packaging
standard.

• XZ Utils

This package contains programs for compressing and decompressing files. It provides the highest compression
generally available and is useful for decompressing packages in XZ or LZMA format.

• Zlib

This package contains compression and decompression routines used by some programs.

• Zstd

This package supplies compression and decompression routines used by some programs. It provides high
compression ratios and a very wide range of compression / speed trade-offs.

# Typography

To make things easier to follow, there are a few typographical conventions used throughout this book. This section
contains some examples of the typographical format found throughout Linux From Scratch.

**./configure --prefix=/usr**

This form of text is designed to be typed exactly as seen unless otherwise noted in the surrounding text. It is also used
in the explanation sections to identify which of the commands is being referenced.

In some cases, a logical line is extended to two or more physical lines with a backslash at the end of the line.

**CC="gcc -B/usr/bin/" ../binutils-2.18/configure \**
**--prefix=/tools --disable-nls --disable-werror**

xvii

---

Linux From Scratch - Version 13.1-systemd

Note that the backslash must be followed by an immediate return. Other whitespace characters like spaces or tab
characters will create incorrect results.

install-info: unknown option '--dir-file=/mnt/lfs/usr/info/dir'

This form of text (fixed-width text) shows screen output, usually as the result of commands issued. If you are reading
the book in the HTML format (instead of PDF), the text should be blue.

The fixed-width text is also used to show filenames, such as /etc/ld.so.conf.

### Note

Please configure your browser to display fixed-width text with a good monospace" font-size="9ptd font, with
which you can distinguish the glyphs of Il1 or O0 clearly.

Emphasis

This form of text is used for several purposes in the book. Its main purpose is to emphasize important points or items.

https://www.linuxfromscratch.org/

This format is used for hyperlinks both within the LFS community and to external pages. It includes HOWTOs,
download locations, and websites.

**cat > $LFS/etc/group << "EOF"**
root:x:0:
bin:x:1:
......
**EOF**

This format is used when creating configuration files. The first command tells the system to create the file $LFS/etc/

group from whatever is typed on the following lines until the sequence End Of File (EOF) is encountered. Therefore,
this entire section is generally typed as seen.

<REPLACED TEXT>

This format is used to encapsulate text that is not to be typed as seen or for copy-and-paste operations.

[OPTIONAL TEXT]

This format is used to encapsulate text that is optional.

passwd(5)

This format is used to refer to a specific manual (man) page. The number inside parentheses indicates a specific section
**inside the manuals. For example, passwd has two man pages. Per LFS installation instructions, those two man pages**
will be located at /usr/share/man/man1/passwd.1 and /usr/share/man/man5/passwd.5. When the book uses passwd(5)
**it is specifically referring to /usr/share/man/man5/passwd.5. man passwd will print the first man page it finds that**
**matches “passwd,” which will be /usr/share/man/man1/passwd.1. For this example, you will need to run man 5 passwd**
in order to read the page being specified. Note that most man pages do not have duplicate page names in different
**sections. Therefore, man <program name> is generally sufficient. In the LFS book these references to man pages are also**
hyperlinks, so clicking on such a reference will open the man page rendered in HTML from Arch Linux manual pages.

# Structure

This book is divided into the following parts.

xviii

---

Linux From Scratch - Version 13.1-systemd

## Part I - Introduction

Part I explains a few important notes on how to proceed with the LFS installation. This section also provides meta-
information about the book.

## Part II - Preparing for the Build

Part II describes how to prepare for the building process—making a partition, downloading the packages, and compiling
temporary tools.

## Part III - Building the LFS Cross Toolchain and Temporary Tools

Part III provides instructions for building the tools needed for constructing the final LFS system.

## Part IV - Building the LFS System

Part IV guides the reader through the building of the LFS system—compiling and installing all the packages one by
one, setting up the boot scripts, and installing the kernel. The resulting Linux system is the foundation on which other
software can be built to expand the system as desired. At the end of this book, there is an easy to use reference listing
all of the programs, libraries, and important files that have been installed.

## Part V - Appendices

Part V provides information about the book itself including acronyms and terms, acknowledgments, package
dependencies, a listing of LFS boot scripts, licenses for the distribution of the book, and a comprehensive index of
packages, programs, libraries, and scripts.

# Errata and Security Advisories

The software used to create an LFS system is constantly being updated and enhanced. Security warnings and bug fixes
may become available after the LFS book has been released. To check whether the package versions or instructions in
this release of LFS need any modifications—to repair security vulnerabilities or to fix other bugs—please visit https://
www.linuxfromscratch.org/lfs/errata/13.1-systemd/ before proceeding with your build. You should note any changes
shown and apply them to the relevant sections of the book as you build the LFS system.

In addition, the Linux From Scratch editors maintain a list of security vulnerabilities discovered after a book has been
released. To read the list, please visit https://www.linuxfromscratch.org/advisories/ before proceeding with your build.
You should apply the changes suggested by the advisories to the relevant sections of the book as you build the LFS
system. And, if you will use the LFS system as a real desktop or server system, you should continue to consult the
advisories and fix any security vulnerabilities, even when the LFS system has been completely constructed.

xix

---

Linux From Scratch - Version 13.1-systemd