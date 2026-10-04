# 8.16. Flex-2.6.4

The Flex package contains a utility for generating programs that recognize patterns in text.

**Approximate build time:**
0.1 SBU
**Required disk space:**
33 MB

## 8.16.1. Installation of Flex

Prepare Flex for compilation:

**./configure --prefix=/usr    \**
**--disable-static \**
**--docdir=/usr/share/doc/flex-2.6.4**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

**A few programs do not know about flex yet and try to run its predecessor, lex. To support those programs, create a**
**symbolic link named lex that runs flex in lex emulation mode, and also create the man page of lex as a symlink:**

**ln -sv flex   /usr/bin/lex**
**ln -sv flex.1 /usr/share/man/man1/lex.1**

## 8.16.2. Contents of Flex

**Installed programs:**
flex, flex++ (link to flex), and lex (link to flex)
**Installed libraries:**
libfl.so
**Installed directory:**
/usr/share/doc/flex-2.6.4

**Short Descriptions**

**flex**
A tool for generating programs that recognize patterns in text; it allows for the versatility to specify the rules
for pattern-finding, eradicating the need to develop a specialized program

**flex++**
**An extension of flex, is used for generating C++ code and classes. It is a symbolic link to flex**

**lex**
**A symbolic link that runs flex in lex emulation mode**

libfl
The flex library

---

Linux From Scratch - Version 13.1-systemd

# 8.17. Tcl-8.6.18

The Tcl package contains the Tool Command Language, a robust general-purpose scripting language. The Expect
package is written in Tcl (pronounced "tickle").

**Approximate build time:**
2.9 SBU
**Required disk space:**
92 MB

## 8.17.1. Installation of Tcl

This package and the next two (Expect and DejaGNU) are installed to support running the test suites for Binutils, GCC
and other packages. Installing three packages for testing purposes may seem excessive, but it is very reassuring, if not
essential, to know that the most important tools are working properly.

Prepare Tcl for compilation:

**SRCDIR=$(pwd)**
**cd unix**
**./configure --prefix=/usr           \**
**--mandir=/usr/share/man \**
**--disable-rpath**

**The meaning of the new configure parameters:**

--disable-rpath

This parameter prevents hard coding library search paths (rpath) into the binary executable files and shared
libraries. This package does not need rpath for an installation into the standard location, and rpath may sometimes
cause unwanted effects or even security issues.

Build the package:

**make**

**sed -e "s|$SRCDIR/unix|/usr/lib|" \**
**-e "s|$SRCDIR|/usr/include|"  \**
**-i tclConfig.sh**

**sed -e "s|$SRCDIR/unix/pkgs/tdbc1.1.13|/usr/lib/tdbc1.1.13|" \**
**-e "s|$SRCDIR/pkgs/tdbc1.1.13/generic|/usr/include|"     \**
**-e "s|$SRCDIR/pkgs/tdbc1.1.13/library|/usr/lib/tcl8.6|"  \**
**-e "s|$SRCDIR/pkgs/tdbc1.1.13|/usr/include|"             \**
**-i pkgs/tdbc1.1.13/tdbcConfig.sh**

**sed -e "s|$SRCDIR/unix/pkgs/itcl4.3.7|/usr/lib/itcl4.3.7|" \**
**-e "s|$SRCDIR/pkgs/itcl4.3.7/generic|/usr/include|"    \**
**-e "s|$SRCDIR/pkgs/itcl4.3.7|/usr/include|"            \**
**-i pkgs/itcl4.3.7/itclConfig.sh**

**unset SRCDIR**

The various “sed” instructions after the “make” command remove references to the build directory from the
configuration files and replace them with the install directory. This is not mandatory for the remainder of LFS, but may
be needed if a package built later uses Tcl.

To test the results, issue:

**LC_ALL=C.UTF-8 make test**

---

Linux From Scratch - Version 13.1-systemd

Install the package:

**make install**
**chmod 644 /usr/lib/libtclstub8.6.a**

Make the installed library writable so debugging symbols can be removed later:

**chmod -v u+w /usr/lib/libtcl8.6.so**

Install Tcl's headers. The next package, Expect, requires them.

**make install-private-headers**

Now make a necessary symbolic link:

**ln -sfv tclsh8.6 /usr/bin/tclsh**

Rename a man page that conflicts with a Perl man page:

**mv -v /usr/share/man/man3/{Thread,Tcl_Thread}.3**

Optionally, install the documentation by issuing the following commands:

**cd ..**
**tar -xf ../tcl8.6.18-html.tar.gz --strip-components=1**
**mkdir -v -p /usr/share/doc/tcl-8.6.18**
**cp -v -r  ./html/* /usr/share/doc/tcl-8.6.18**

## 8.17.2. Contents of Tcl

**Installed programs:**
tclsh (link to tclsh8.6) and tclsh8.6
**Installed library:**
libtcl8.6.so and libtclstub8.6.a

**Short Descriptions**

**tclsh8.6**
The Tcl command shell

**tclsh**
A link to tclsh8.6

libtcl8.6.so
The Tcl library

libtclstub8.6.a
The Tcl Stub library

---

Linux From Scratch - Version 13.1-systemd

# 8.18. Expect-5.45.4

**The Expect package contains tools for automating, via scripted dialogues, interactive applications such as telnet, ftp,**
**passwd, fsck, rlogin, and tip. Expect is also useful for testing these same applications as well as easing all sorts of**
tasks that are prohibitively difficult with anything else. The DejaGnu framework is written in Expect.

**Approximate build time:**
0.2 SBU
**Required disk space:**
3.9 MB

## 8.18.1. Installation of Expect

Expect needs PTYs to work. Verify that the PTYs are working properly inside the chroot environment by performing
a simple test:

**python3 -c 'from pty import spawn; spawn(["echo", "ok"])'**

This command should output ok. If, instead, the output includes OSError: out of pty devices, then the environment
is not set up for proper PTY operation. You need to exit from the chroot environment, read Section 7.3, “Preparing
Virtual Kernel File Systems” again, and ensure the devpts file system (and other virtual kernel file systems) mounted
correctly. Then reenter the chroot environment following Section 7.4, “Entering the Chroot Environment”. This issue
needs to be resolved before continuing, or the test suites requiring Expect (for example the test suites of Bash, Binutils,
GCC, GDBM, and of course Expect itself) will fail catastrophically, and other subtle breakages may also happen.

Now, make some changes to allow the package with gcc-15.1 or later:

**patch -Np1 -i ../expect-5.45.4-gcc15-1.patch**

Prepare Expect for compilation:

**./configure --prefix=/usr           \**
**--with-tcl=/usr/lib     \**
**--enable-shared         \**
**--disable-rpath         \**
**--mandir=/usr/share/man \**
**--with-tclinclude=/usr/include**

**The meaning of the configure options:**

--with-tcl=/usr/lib

**This parameter is needed to tell configure where the tclConfig.sh script is located.**

--with-tclinclude=/usr/include

This explicitly tells Expect where to find Tcl's internal headers.

Build the package:

**make**

To test the results, issue:

**make test**

Install the package:

**make install**
**ln -svf expect5.45.4/libexpect5.45.4.so /usr/lib**

---

Linux From Scratch - Version 13.1-systemd

## 8.18.2. Contents of Expect

**Installed program:**
expect
**Installed library:**
libexpect5.45.4.so

**Short Descriptions**

**expect**
Communicates with other interactive programs according to a script

libexpect-5.45.4.so
Contains functions that allow Expect to be used as a Tcl extension or to be used directly
from C or C++ (without Tcl)

---

Linux From Scratch - Version 13.1-systemd

# 8.19. DejaGNU-1.6.3

**The DejaGnu package contains a framework for running test suites on GNU tools. It is written in expect, which itself**
uses Tcl (Tool Command Language).

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
7.4 MB

## 8.19.1. Installation of DejaGNU

The upstream recommends building DejaGNU in a dedicated build directory:

**mkdir -v build**
**cd       build**

Prepare DejaGNU for compilation:

**../configure --prefix=/usr**
**makeinfo --html --no-split -o doc/dejagnu.html ../doc/dejagnu.texi**
**makeinfo --plaintext       -o doc/dejagnu.txt  ../doc/dejagnu.texi**

To test the results, issue:

**make check**

Install the package:

**make install**
**install -v -dm755  /usr/share/doc/dejagnu-1.6.3**
**install -v -m644   doc/dejagnu.{html,txt} /usr/share/doc/dejagnu-1.6.3**

## 8.19.2. Contents of DejaGNU

**Installed program:**
dejagnu and runtest

**Short Descriptions**

**dejagnu**
DejaGNU auxiliary command launcher

**runtest**
**A wrapper script that locates the proper expect shell and then runs DejaGNU**

---

Linux From Scratch - Version 13.1-systemd