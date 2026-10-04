# 8.33. Ncurses-6.6

The Ncurses package contains libraries for terminal-independent handling of character screens.

**Approximate build time:**
0.2 SBU
**Required disk space:**
47 MB

## 8.33.1. Installation of Ncurses

Prepare Ncurses for compilation:

**./configure --prefix=/usr           \**
**--mandir=/usr/share/man \**
**--with-shared           \**
**--without-debug         \**
**--without-normal        \**
**--with-cxx-shared       \**
**--enable-pc-files       \**
**--with-pkg-config-libdir=/usr/lib/pkgconfig**

**The meaning of the new configure options:**

--with-shared

This makes Ncurses build and install shared C libraries.

--without-normal

This prevents Ncurses building and installing static C libraries.

--without-debug

This prevents Ncurses building and installing debug libraries.

--with-cxx-shared

This makes Ncurses build and install shared C++ bindings. It also prevents it building and installing static C+
+ bindings.

--enable-pc-files

This switch generates and installs .pc files for pkg-config.

Compile the package:

**make**

This package has a test suite, but it can only be run after the package has been installed. The tests reside in the test/
directory. See the README file in that directory for further details.

The installation of this package will overwrite libncursesw.so.6.6 in-place. It may crash the shell process which is
using code and data from the library file. Install the package with DESTDIR, and replace the library file correctly using
**the --remove-destination option of cp (the header curses.h is also edited to ensure the wide-character ABI to be used**
as what we've done in Section 6.3, “Ncurses-6.6”):

**make DESTDIR=$PWD/dest install**
**sed -e 's/^#if.*XOPEN.*$/#if 1/' \**
**-i dest/usr/include/curses.h**
**cp --remove-destination -av dest/* /**

---

Linux From Scratch - Version 13.1-systemd

Many applications still expect the linker to be able to find non-wide-character Ncurses libraries. Trick such applications
into linking with wide-character libraries by means of symlinks (note that the .so links are only safe with curses.h
edited to always use the wide-character ABI):

**for lib in ncurses form panel menu ; do**
**ln -sfv lib${lib}w.so /usr/lib/lib${lib}.so**
**ln -sfv ${lib}w.pc    /usr/lib/pkgconfig/${lib}.pc**
**done**

Finally, make sure that old applications that look for -lcurses at build time are still buildable:

**ln -sfv libncursesw.so /usr/lib/libcurses.so**

If desired, install the Ncurses documentation:

**cp -v -R doc -T /usr/share/doc/ncurses-6.6**

### Note

The instructions above don't create non-wide-character Ncurses libraries since no package installed by
compiling from sources would link against them at runtime. However, the only known binary-only
applications that link against non-wide-character Ncurses libraries require version 5. If you must have such
libraries because of some binary-only application or to be compliant with LSB, build the package again with
the following commands:

**make distclean**
**./configure --prefix=/usr    \**
**--with-shared    \**
**--without-normal \**
**--without-debug  \**
**--without-cxx-binding \**
**--with-abi-version=5**
**make sources libs**
**cp -av lib/lib*.so.5* /usr/lib**

## 8.33.2. Contents of Ncurses

**Installed programs:**
captoinfo (link to tic), clear, infocmp, infotocap (link to tic), ncursesw6-config, reset (link
to tset), tabs, tic, toe, tput, and tset
**Installed libraries:**
libcurses.so (symlink), libform.so (symlink), libformw.so, libmenu.so (symlink),
libmenuw.so, libncurses.so (symlink), libncursesw.so, libncurses++w.so, libpanel.so
(symlink), and libpanelw.so,
**Installed directories:**
/usr/share/tabset, /usr/share/terminfo, and /usr/share/doc/ncurses-6.6

**Short Descriptions**

**captoinfo**
Converts a termcap description into a terminfo description

**clear**
Clears the screen, if possible

**infocmp**
Compares or prints out terminfo descriptions

**infotocap**
Converts a terminfo description into a termcap description

**ncursesw6-config**
Provides configuration information for ncurses

**reset**
Reinitializes a terminal to its default values

**tabs**
Clears and sets tab stops on a terminal

---

Linux From Scratch - Version 13.1-systemd

**tic**
The terminfo entry-description compiler that translates a terminfo file from source format
into the binary format needed for the ncurses library routines [A terminfo file contains
information on the capabilities of a certain terminal.]

**toe**
Lists all available terminal types, giving the primary name and description for each

**tput**
Makes the values of terminal-dependent capabilities available to the shell; it can also be used
to reset or initialize a terminal or report its long name

**tset**
Can be used to initialize terminals

libncursesw
Contains functions to display text in many complex ways on a terminal screen; a good
**example of the use of these functions is the menu displayed during the kernel's make**
**menuconfig**

libncurses++w
Contains C++ binding for other libraries in this package

libformw
Contains functions to implement forms

libmenuw
Contains functions to implement menus

libpanelw
Contains functions to implement panels

---

Linux From Scratch - Version 13.1-systemd

# 8.34. Sed-4.10

The Sed package contains a stream editor.

**Approximate build time:**
0.4 SBU
**Required disk space:**
42 MB

## 8.34.1. Installation of Sed

Prepare Sed for compilation:

**./configure --prefix=/usr**

Compile the package and generate the HTML documentation:

**make**
**make html**

To test the results, issue:

**chown -R tester .**
**su tester -c "PATH=$PATH make check"**

Install the package and its documentation:

**make install**
**install -vDm644 doc/sed.html -t /usr/share/doc/sed-4.10**

## 8.34.2. Contents of Sed

**Installed program:**
sed
**Installed directory:**
/usr/share/doc/sed-4.10

**Short Descriptions**

**sed**
Filters and transforms text files in a single pass

---

Linux From Scratch - Version 13.1-systemd

# 8.35. Psmisc-23.7

The Psmisc package contains programs for displaying information about running processes.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
6.8 MB

## 8.35.1. Installation of Psmisc

Prepare Psmisc for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

To run the test suite, run:

**make check**

Install the package:

**make install**

## 8.35.2. Contents of Psmisc

**Installed programs:**
fuser, killall, peekfd, prtstat, pslog, pstree, and pstree.x11 (link to pstree)

**Short Descriptions**

**fuser**
Reports the Process IDs (PIDs) of processes that use the given files or file systems

**killall**
Kills processes by name; it sends a signal to all processes running any of the given commands

**peekfd**
Peek at file descriptors of a running process, given its PID

**prtstat**
Prints information about a process

**pslog**
Reports current logs path of a process

**pstree**
Displays running processes as a tree

**pstree.x11**
**Same as pstree, except that it waits for confirmation before exiting**

---

Linux From Scratch - Version 13.1-systemd

# 8.36. Gettext-1.0

The Gettext package contains utilities for internationalization and localization. These allow programs to be compiled
with NLS (Native Language Support), enabling them to output messages in the user's native language.

**Approximate build time:**
2.1 SBU
**Required disk space:**
448 MB

## 8.36.1. Installation of Gettext

Prepare Gettext for compilation:

**./configure --prefix=/usr    \**
**--disable-static \**
**--docdir=/usr/share/doc/gettext-1.0**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**
**chmod -v 0755 /usr/lib/preloadable_libintl.so**

## 8.36.2. Contents of Gettext

**Installed programs:**
autopoint, envsubst, gettext, gettext.sh, gettextize, msgattrib, msgcat, msgcmp,
msgcomm, msgconv, msgen, msgexec, msgfilter, msgfmt, msggrep, msginit, msgmerge,
msgunfmt, msguniq, ngettext, recode-sr-latin, and xgettext
**Installed libraries:**
libasprintf.so, libgettextlib.so, libgettextpo.so, libgettextsrc.so, libtextstyle.so, and
preloadable_libintl.so
**Installed directories:**
/usr/lib/gettext, /usr/share/doc/gettext-1.0, /usr/share/gettext, and /usr/share/gettext-1.0

**Short Descriptions**

**autopoint**
Copies standard Gettext infrastructure files into a source package

**envsubst**
Substitutes environment variables in shell format strings

**gettext**
Translates a natural language message into the user's language by looking up the
translation in a message catalog

**gettext.sh**
Primarily serves as a shell function library for gettext

**gettextize**
Copies all standard Gettext files into the given top-level directory of a package to begin
internationalizing it

**msgattrib**
Filters the messages of a translation catalog according to their attributes and manipulates
the attributes

**msgcat**
Concatenates and merges the given .po files

**msgcmp**
Compares two .po files to check that both contain the same set of msgid strings

---

Linux From Scratch - Version 13.1-systemd

**msgcomm**
Finds the messages that are common to the given .po files

**msgconv**
Converts a translation catalog to a different character encoding

**msgen**
Creates an English translation catalog

**msgexec**
Applies a command to all translations of a translation catalog

**msgfilter**
Applies a filter to all translations of a translation catalog

**msgfmt**
Generates a binary message catalog from a translation catalog

**msggrep**
Extracts all messages of a translation catalog that match a given pattern or belong to
some given source files

**msginit**
Creates a new .po file, initializing the meta information with values from the user's
environment

**msgmerge**
Combines two raw translations into a single file

**msgunfmt**
Decompiles a binary message catalog into raw translation text

**msguniq**
Unifies duplicate translations in a translation catalog

**ngettext**
Displays native language translations of a textual message whose grammatical form
depends on a number

**recode-sr-latin**
Recodes Serbian text from Cyrillic to Latin script

**xgettext**
Extracts the translatable message lines from the given source files to make the first
translation template

libasprintf
Defines the autosprintf class, which makes C formatted output routines usable in C++
programs, for use with the <string> strings and the <iostream> streams

libgettextlib
Contains common routines used by the various Gettext programs; these are not intended
for general use

libgettextpo
Used to write specialized programs that process .po files; this library is used when the
**standard applications shipped with Gettext (such as msgcomm, msgcmp, msgattrib,**
**and msgen) will not suffice**

libgettextsrc
Provides common routines used by the various Gettext programs; these are not intended
for general use

libtextstyle
Text styling library

preloadable_libintl
A library, intended to be used by LD_PRELOAD, that helps libintl log untranslated
messages

---

Linux From Scratch - Version 13.1-systemd