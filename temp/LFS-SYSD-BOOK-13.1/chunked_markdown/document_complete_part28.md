# 7.7. Gettext-1.0

The Gettext package contains utilities for internationalization and localization. These allow programs to be compiled
with NLS (Native Language Support), enabling them to output messages in the user's native language.

**Approximate build time:**
1.5 SBU
**Required disk space:**
531 MB

## 7.7.1. Installation of Gettext

For our temporary set of tools, we only need to install three programs from Gettext.

Prepare Gettext for compilation:

**./configure --disable-shared**

**The meaning of the configure option:**

--disable-shared

We do not need to install any of the shared Gettext libraries at this time, therefore there is no need to build them.

Compile the package:

**make**

**Install the msgfmt, msgmerge, and xgettext programs:**

**cp -v gettext-tools/src/{msgfmt,msgmerge,xgettext} /usr/bin**

Details on this package are located in Section 8.36.2, “Contents of Gettext.”

---

Linux From Scratch - Version 13.1-systemd

# 7.8. Bison-3.8.2

The Bison package contains a parser generator.

**Approximate build time:**
0.2 SBU
**Required disk space:**
58 MB

## 7.8.1. Installation of Bison

Prepare Bison for compilation:

**./configure --prefix=/usr \**
**--docdir=/usr/share/doc/bison-3.8.2**

**The meaning of the new configure option:**

--docdir=/usr/share/doc/bison-3.8.2

This tells the build system to install bison documentation into a versioned directory.

Compile the package:

**make**

Install the package:

**make install**

Details on this package are located in Section 8.37.2, “Contents of Bison.”

---

Linux From Scratch - Version 13.1-systemd

# 7.9. Perl-5.44.0

The Perl package contains the Practical Extraction and Report Language.

**Approximate build time:**
0.6 SBU
**Required disk space:**
301 MB

## 7.9.1. Installation of Perl

Prepare Perl for compilation:

**sh Configure -des                                         \**
**-D prefix=/usr                               \**
**-D vendorprefix=/usr                         \**
**-D useshrplib                                \**
**-D privlib=/usr/lib/perl5/5.44/core_perl     \**
**-D archlib=/usr/lib/perl5/5.44/core_perl     \**
**-D sitelib=/usr/lib/perl5/5.44/site_perl     \**
**-D sitearch=/usr/lib/perl5/5.44/site_perl    \**
**-D vendorlib=/usr/lib/perl5/5.44/vendor_perl \**
**-D vendorarch=/usr/lib/perl5/5.44/vendor_perl**

**The meaning of the Configure options:**

-des

This is a combination of three options: -d uses defaults for all items; -e ensures completion of all tasks; -s silences
non-essential output.

-D vendorprefix=/usr

**This ensures perl knows how to tell packages where they should install their Perl modules.**

-D useshrplib

Build libperl needed by some Perl modules as a shared library, instead of a static library.

-D privlib,-D archlib,-D sitelib,...

These settings define where Perl looks for installed modules. The LFS editors chose to put them in a directory
structure based on the MAJOR.MINOR version of Perl (5.44) which allows upgrading Perl to newer patch levels
(the patch level is the last dot separated part in the full version string like 5.44.0) without reinstalling all of the
modules.

Compile the package:

**make**

Install the package:

**make install**

Details on this package are located in Section 8.46.2, “Contents of Perl.”

---

Linux From Scratch - Version 13.1-systemd

# 7.10. Zlib-1.3.2

The Zlib package contains compression and decompression routines used by some programs.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
5.7 MB

## 7.10.1. Installation of Zlib

Prepare Zlib for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

Install the package:

**make install**

Remove a useless static library:

**rm -fv /usr/lib/libz.a**

Details on this package are located in Section 8.6.2, “Contents of Zlib.”

---

Linux From Scratch - Version 13.1-systemd

# 7.11. mpdecimal-4.0.1

The mpdecimal package contains fast C/C++ libraries for correctly-rounded arbitrary precision decimal floating point
arithmetic.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
3.3 MB

## 7.11.1. Installation of mpdecimal

Prepare mpdecimal for compilation:

**./configure --prefix=/usr    \**
**--disable-static \**
**--docdir=/usr/share/doc/mpdecimal-4.0.1**

Compile the package:

**make**

Install the package:

**make install**

Details on this package are located in Section 8.53.2, “Contents of mpdecimal.”

---

Linux From Scratch - Version 13.1-systemd

# 7.12. Python-3.14.7

The Python 3 package contains the Python development environment. It is useful for object-oriented programming,
writing scripts, prototyping large programs, and developing entire applications. Python is an interpreted computer
language.

**Approximate build time:**
0.5 SBU
**Required disk space:**
603 MB

## 7.12.1. Installation of Python

### Note

There are two package files whose name starts with the “python” prefix. The one to extract from is Python-

3.14.7.tar.xz (notice the uppercase first letter).

Prepare Python for compilation:

**./configure --prefix=/usr       \**
**--enable-shared     \**
**--without-ensurepip \**
**--without-static-libpython**

**The meaning of the configure option:**

--enable-shared

This switch prevents installation of static libraries.

--without-ensurepip

This switch disables the Python package installer, which is not needed at this stage.

--without-static-libpython

This switch prevents building a large, but unneeded, static library.

Compile the package:

**make**

### Note

Some Python 3 modules can't be built now because the dependencies are not installed yet. For the ssl module,
a message Python requires a OpenSSL 1.1.1 or newer is outputted. The message should be ignored. Just
**make sure the toplevel make command has not failed. The optional modules are not needed now and they**
will be built in Chapter 8.

Install the package:

**make install**

Details on this package are located in Section 8.54.2, “Contents of Python 3.”

---

Linux From Scratch - Version 13.1-systemd

# 7.13. Texinfo-7.3

The Texinfo package contains programs for reading, writing, and converting info pages.

**Approximate build time:**
0.2 SBU
**Required disk space:**
147 MB

## 7.13.1. Installation of Texinfo

Prepare Texinfo for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

Install the package:

**make install**

Details on this package are located in Section 8.73.2, “Contents of Texinfo.”

---

Linux From Scratch - Version 13.1-systemd

# 7.14. Util-linux-2.42.2

The Util-linux package contains miscellaneous utility programs.

**Approximate build time:**
0.2 SBU
**Required disk space:**
211 MB

## 7.14.1. Installation of Util-linux

The FHS recommends using the /var/lib/hwclock directory instead of the usual /etc directory as the location for the

adjtime file. Create this directory with:

**mkdir -pv /var/lib/hwclock**

Prepare Util-linux for compilation:

**./configure --libdir=/usr/lib     \**
**--runstatedir=/run    \**
**--disable-chfn-chsh   \**
**--disable-login       \**
**--disable-nologin     \**
**--disable-su          \**
**--disable-setpriv     \**
**--disable-runuser     \**
**--disable-pylibmount  \**
**--disable-static      \**
**--disable-liblastlog2 \**
**--without-python      \**
**ADJTIME_PATH=/var/lib/hwclock/adjtime \**
**--docdir=/usr/share/doc/util-linux-2.42.2**

**The meaning of the configure options:**

ADJTIME_PATH=/var/lib/hwclock/adjtime

This sets the location of the file recording information about the hardware clock in accordance to the FHS. This
is not strictly needed for this temporary tool, but it prevents creating a file at another location, which would not
be overwritten or removed when building the final util-linux package.

--libdir=/usr/lib

This switch ensures the .so symlinks targeting the shared library file in the same directory (/usr/lib) directly.

--disable-*

These switches prevent warnings about building components that require packages not in LFS or not installed yet.

--without-python

This switch disables using Python. It avoids trying to build unneeded bindings.

runstatedir=/run

**This switch sets the location of the socket used by uuidd and libuuid correctly.**

Compile the package:

**make**

Install the package:

**make install**

Details on this package are located in Section 8.81.2, “Contents of Util-linux.”

---

Linux From Scratch - Version 13.1-systemd