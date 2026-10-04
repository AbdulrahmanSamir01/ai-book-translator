# 8.20. Ninja-1.13.2

Ninja is a small build system with a focus on speed.

**Approximate build time:**
0.2 SBU
**Required disk space:**
43 MB

## 8.20.1. Installation of Ninja

**When run, ninja normally utilizes the greatest possible number of processes in parallel. By default this is the number**
**of cores on the system, plus two. This may overheat the CPU, or make the system run out of memory. When ninja is**
invoked from the command line, passing the -jN parameter will limit the number of parallel processes. Some packages
**embed the execution of ninja, and do not pass the -j parameter on to it.**

Using the optional procedure below allows a user to limit the number of parallel processes via an environment variable,
**NINJAJOBS. For example, setting:**

export NINJAJOBS=4

**will limit ninja to four parallel processes.**

**If desired, make ninja recognize the environment variable NINJAJOBS by running the stream editor:**

**sed -i '/int Guess/a \**
**int   j = 0;\**
**char* jobs = getenv( "NINJAJOBS" );\**
**if ( jobs != NULL ) j = atoi( jobs );\**
**if ( j > 0 ) return j;\**
**' src/ninja.cc**

Build Ninja with:

**python3 configure.py --bootstrap --verbose**

**The meaning of the build option:**

--bootstrap

This parameter forces Ninja to rebuild itself for the current system.

--verbose

**This parameter makes configure.py show the progress building Ninja.**

The package tests cannot run in the chroot environment. They require cmake. But the basic function of this package is
already tested by rebuilding itself (with the --bootstrap option) anyway.

Install the package:

**install -vm755 ninja /usr/bin/**
**install -vDm644 misc/bash-completion /usr/share/bash-completion/completions/ninja**
**install -vDm644 misc/zsh-completion  /usr/share/zsh/site-functions/_ninja**

## 8.20.2. Contents of Ninja

**Installed programs:**
ninja

**Short Descriptions**

**ninja**
is the Ninja build system

---

Linux From Scratch - Version 13.1-systemd

# 8.21. Pkgconf-3.0.5

The pkgconf package is a successor to pkg-config and contains a tool for passing the include path and/or library paths
to build tools during the configure and make phases of package installations.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
47 MB

## 8.21.1. Installation of Pkgconf

First, work around a circular dependency on meson:

**tar -xf ../meson-1.12.0.tar.gz**

Prepare Pkgconf for compilation:

**mkdir build**
**cd    build**

**python3 ../meson-1.12.0/meson.py setup --prefix=/usr --buildtype=release ..**

Compile the package:

**ninja**

To test the results, issue:

**ninja test**

Install the package:

**ninja install**
**mv /usr/share/doc/pkgconf{,-3.0.5}**

To maintain compatibility with the original Pkg-config create two symlinks:

**ln -sv pkgconf   /usr/bin/pkg-config**
**ln -sv pkgconf.1 /usr/share/man/man1/pkg-config.1**

## 8.21.2. Contents of Pkgconf

**Installed programs:**
pkgconf, pkg-config (link to pkgconf), and bomtool
**Installed library:**
libpkgconf.so
**Installed directory:**
/usr/share/doc/pkgconf-3.0.5

**Short Descriptions**

**pkgconf**
Returns meta information for the specified library or package

**bomtool**
Generates a Software Bill Of Materials from pkg-config .pc files

libpkgconf.so
Contains most of pkgconf's functionality, while allowing other tools like IDEs and compilers to
use its frameworks

---

Linux From Scratch - Version 13.1-systemd

# 8.22. Binutils-2.47

The Binutils package contains a linker, an assembler, and other tools for handling object files.

**Approximate build time:**
1.7 SBU
**Required disk space:**
817 MB

## 8.22.1. Installation of Binutils

The Binutils documentation recommends building Binutils in a dedicated build directory:

**mkdir -v build**
**cd       build**

Prepare Binutils for compilation:

**../configure --prefix=/usr       \**
**--sysconfdir=/etc   \**
**--enable-ld=default \**
**--enable-plugins    \**
**--enable-shared     \**
**--disable-werror    \**
**--enable-64-bit-bfd \**
**--enable-new-dtags  \**
**--with-system-zlib  \**
**--with-lib-path=/usr/lib \**
**--enable-default-hash-style=gnu**

**The meaning of the new configure parameters:**

--enable-ld=default

Build the original bfd linker and install it as both ld (the default linker) and ld.bfd.

--enable-plugins

Enable plugin support for the linker.

--with-system-zlib

Use the installed zlib library instead of building the included version.

--with-lib-path=/usr/lib

**Specify the path for the linker (ld) to search. By default it searches several directories that do not exist on LFS**
besides /usr/lib, especially the /usr/lib64 directory that we deliberately avoid. In the case where /usr/lib64 has
**been mistakenly created and populated with some libraries, making ld not search the path can highlight the issue**
earlier with a failure to find those libraries at build time instead of run time.

Compile the package:

**make tooldir=/usr**

**The meaning of the make parameter:**

tooldir=/usr

Normally, the tooldir (the directory where the executables will ultimately be located) is set to $(exec_prefix)/

$(target_alias). For example, x86_64 machines would expand that to /usr/x86_64-pc-linux-gnu. Because this
is a custom system, this target-specific directory in /usr is not required. $(exec_prefix)/$(target_alias) would
be used if the system were used to cross-compile (for example, compiling a package on an Intel machine that
generates code that can be executed on PowerPC machines).

---

Linux From Scratch - Version 13.1-systemd

### Important

The test suite for Binutils in this section is considered critical. Do not skip it under any circumstances.

Test the results:

**make -k check**

For a list of failed tests, run:

**grep '^FAIL:' $(find -name '*.log')**

One test related to gprofng is known to fail.

Install the package:

**make tooldir=/usr install**

Remove useless static libraries and other files:

**rm -rfv /usr/lib/lib{bfd,ctf,ctf-nobfd,gprofng,opcodes,sframe}.a \**
**/usr/share/doc/gprofng/**

## 8.22.2. Contents of Binutils

**Installed programs:**
addr2line, ar, as, c++filt, dwp, elfedit, gprof, gprofng, ld, ld.bfd, nm, objcopy, objdump,
ranlib, readelf, size, strings, and strip
**Installed libraries:**
libbfd.so, libctf.so, libctf-nobfd.so, libgprofng.so, libopcodes.so, and libsframe.so
**Installed directory:**
/usr/lib/ldscripts

**Short Descriptions**

**addr2line**
Translates program addresses to file names and line numbers; given an address and the name of
an executable, it uses the debugging information in the executable to determine which source file
and line number are associated with the address

**ar**
Creates, modifies, and extracts from archives

**as**
**An assembler that assembles the output of gcc into object files**

**c++filt**
Used by the linker to de-mangle C++ and Java symbols and to keep overloaded functions from
clashing

**dwp**
The DWARF packaging utility

**elfedit**
Updates the ELF headers of ELF files

**gprof**
Displays call graph profile data

**gprofng**
Gathers and analyzes performance data

**ld**
A linker that combines a number of object and archive files into a single file, relocating their data
and tying up symbol references

**ld.bfd**
**A hard link to ld**

**nm**
Lists the symbols occurring in a given object file

**objcopy**
Translates one type of object file into another

---

Linux From Scratch - Version 13.1-systemd

**objdump**
Displays information about the given object file, with options controlling the particular information
to display; the information shown is useful to programmers who are working on the compilation
tools

**ranlib**
Generates an index of the contents of an archive and stores it in the archive; the index lists all of
the symbols defined by archive members that are relocatable object files

**readelf**
Displays information about ELF type binaries

**size**
Lists the section sizes and the total size for the given object files

**strings**
Outputs, for each given file, the sequences of printable characters that are of at least the specified
length (defaulting to four); for object files, it prints, by default, only the strings from the initializing
and loading sections while for other types of files, it scans the entire file

**strip**
Discards symbols from object files

libbfd
The Binary File Descriptor library

libctf
The Compat ANSI-C Type Format debugging support library

libctf-nobfd
A libctf variant which does not use libbfd functionality

libgprofng
**A library containing most routines used by gprofng**

libopcodes
A library for dealing with opcodes—the “readable text” versions of instructions for the processor;
**it is used for building utilities like objdump**

libsframe
A library to support online backtracing using a simple unwinder

---

Linux From Scratch - Version 13.1-systemd