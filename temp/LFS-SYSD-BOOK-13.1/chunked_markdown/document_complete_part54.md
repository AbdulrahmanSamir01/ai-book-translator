# 8.79. Man-DB-2.13.1

The Man-DB package contains programs for finding and viewing man pages.

**Approximate build time:**
0.3 SBU
**Required disk space:**
44 MB

## 8.79.1. Installation of Man-DB

Prepare Man-DB for compilation:

**./configure --prefix=/usr                         \**
**--docdir=/usr/share/doc/man-db-2.13.1 \**
**--sysconfdir=/etc                     \**
**--disable-setuid                      \**
**--enable-cache-owner=bin              \**
**--with-browser=/usr/bin/lynx          \**
**--with-vgrind=/usr/bin/vgrind         \**
**--with-grap=/usr/bin/grap**

**The meaning of the configure options:**

--disable-setuid

**This disables making the man program setuid to user man.**

--enable-cache-owner=bin

This changes ownership of the system-wide cache files to user bin.

--with-...

**These three parameters are used to set some default programs. lynx is a text-based web browser (see BLFS for**
**installation instructions), vgrind converts program sources to Groff input, and grap is useful for typesetting graphs**
**in Groff documents. The vgrind and grap programs are not normally needed for viewing manual pages. They are**
not part of LFS or BLFS, but you should be able to install them yourself after finishing LFS if you wish to do so.

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

## 8.79.2. Non-English Manual Pages in LFS

The following table shows the character set that Man-DB assumes manual pages installed under /usr/share/man/<ll>
will be encoded with. In addition to this, Man-DB correctly determines if manual pages installed in that directory are
UTF-8 encoded.

**Table 8.1. Expected character encoding of legacy 8-bit manual pages**

**Language (code)**
**Encoding**
**Language (code)**
**Encoding**

Danish (da)
ISO-8859-1
Croatian (hr)
ISO-8859-2

German (de)
ISO-8859-1
Hungarian (hu)
ISO-8859-2

---

Linux From Scratch - Version 13.1-systemd

**Language (code)**
**Encoding**
**Language (code)**
**Encoding**

English (en)
ISO-8859-1
Japanese (ja)
EUC-JP

Spanish (es)
ISO-8859-1
Korean (ko)
EUC-KR

Estonian (et)
ISO-8859-1
Lithuanian (lt)
ISO-8859-13

Finnish (fi)
ISO-8859-1
Latvian (lv)
ISO-8859-13

French (fr)
ISO-8859-1
Macedonian (mk)
ISO-8859-5

Irish (ga)
ISO-8859-1
Polish (pl)
ISO-8859-2

Galician (gl)
ISO-8859-1
Romanian (ro)
ISO-8859-2

Indonesian (id)
ISO-8859-1
Greek (el)
ISO-8859-7

Icelandic (is)
ISO-8859-1
Slovak (sk)
ISO-8859-2

Italian (it)
ISO-8859-1
Slovenian (sl)
ISO-8859-2

Norwegian Bokmal
(nb)

ISO-8859-1
Serbian Latin (sr@latin)
ISO-8859-2

Dutch (nl)
ISO-8859-1
Serbian (sr)
ISO-8859-5

Norwegian Nynorsk
(nn)

ISO-8859-1
Turkish (tr)
ISO-8859-9

Norwegian (no)
ISO-8859-1
Ukrainian (uk)
KOI8-U

Portuguese (pt)
ISO-8859-1
Vietnamese (vi)
TCVN5712-1

Swedish (sv)
ISO-8859-1
Simplified Chinese (zh_CN)
GBK

Belarusian (be)
CP1251
Simplified
Chinese,
Singapore
(zh_SG)

GBK

Bulgarian (bg)
CP1251
Traditional Chinese, Hong Kong
(zh_HK)

BIG5HKSCS

Czech (cs)
ISO-8859-2
Traditional Chinese (zh_TW)
BIG5

### Note

Manual pages in languages not in the list are not supported.

## 8.79.3. Contents of Man-DB

**Installed programs:**
accessdb, apropos (link to whatis), catman, lexgrog, man, man-recode, mandb, manpath,
and whatis
**Installed libraries:**
libman.so and libmandb.so (both in /usr/lib/man-db)
**Installed directories:**
/usr/lib/man-db, /usr/libexec/man-db, and /usr/share/doc/man-db-2.13.1

**Short Descriptions**

**accessdb**
**Dumps the whatis database contents in human-readable form**

**apropos**
**Searches the whatis database and displays the short descriptions of system commands that contain**
a given string

---

Linux From Scratch - Version 13.1-systemd

**catman**
Creates or updates the pre-formatted manual pages

**lexgrog**
Displays one-line summary information about a given manual page

**man**
Formats and displays the requested manual page

**man-recode**
Converts manual pages to another encoding

**mandb**
**Creates or updates the whatis database**

**manpath**
Displays the contents of $MANPATH or (if $MANPATH is not set) a suitable search path based on
the settings in man.conf and the user's environment

**whatis**
**Searches the whatis database and displays the short descriptions of system commands that contain**
the given keyword as a separate word

libman
**Contains run-time support for man**

libmandb
**Contains run-time support for man**

---

Linux From Scratch - Version 13.1-systemd

# 8.80. Procps-ng-4.0.7

The Procps-ng package contains programs for monitoring processes.

**Approximate build time:**
0.1 SBU
**Required disk space:**
28 MB

## 8.80.1. Installation of Procps-ng

Prepare Procps-ng for compilation:

**./configure --prefix=/usr                           \**
**--docdir=/usr/share/doc/procps-ng-4.0.7 \**
**--disable-static                        \**
**--disable-kill                          \**
**--enable-watch8bit                      \**
**--with-systemd**

**The meaning of the configure option:**

--disable-kill

**This switch disables building the kill command; it will be installed from the Util-linux package.**

--enable-watch8bit

**This switch enables the ncursesw support for the watch command, so it can handle 8-bit characters.**

Compile the package:

**make**

To run the test suite, run:

**chown -R tester .**
**su tester -c "PATH=$PATH make check"**

One test named ps with output flag bsdtime,cputime,etime,etimes is known to fail if the host kernel is not built
with CONFIG_BSD_PROCESS_ACCT enabled.

Install the package:

**make install**

## 8.80.2. Contents of Procps-ng

**Installed programs:**
free, pgrep, pidof, pkill, pmap, ps, pwdx, slabtop, sysctl, tload, top, uptime, vmstat, w,
and watch
**Installed library:**
libproc-2.so
**Installed directories:**
/usr/include/procps and /usr/share/doc/procps-ng-4.0.7

**Short Descriptions**

**free**
Reports the amount of free and used memory (both physical and swap memory) in the system

**pgrep**
Looks up processes based on their name and other attributes

**pidof**
Reports the PIDs of the given programs

**pkill**
Signals processes based on their name and other attributes

**pmap**
Reports the memory map of the given process

---

Linux From Scratch - Version 13.1-systemd

**ps**
Lists the current running processes

**pwdx**
Reports the current working directory of a process

**slabtop**
Displays detailed kernel slab cache information in real time

**sysctl**
Modifies kernel parameters at run time

**tload**
Prints a graph of the current system load average

**top**
Displays a list of the most CPU intensive processes; it provides an ongoing look at processor activity
in real time

**uptime**
Reports how long the system has been running, how many users are logged on, and the system load
averages

**vmstat**
Reports virtual memory statistics, giving information about processes, memory, paging, block Input/
Output (IO), traps, and CPU activity

**w**
Shows which users are currently logged on, where, and since when

**watch**
Runs a given command repeatedly, displaying the first screen-full of its output; this allows a user to
watch the output change over time

libproc-2
Contains the functions used by most programs in this package

---

Linux From Scratch - Version 13.1-systemd

# 8.81. Util-linux-2.42.2

The Util-linux package contains miscellaneous utility programs. Among them are utilities for handling file systems,
consoles, partitions, and messages.

**Approximate build time:**
0.5 SBU
**Required disk space:**
362 MB

## 8.81.1. Installation of Util-linux

Prepare Util-linux for compilation:

**./configure --bindir=/usr/bin     \**
**--libdir=/usr/lib     \**
**--runstatedir=/run    \**
**--sbindir=/usr/sbin   \**
**--disable-chfn-chsh   \**
**--disable-login       \**
**--disable-nologin     \**
**--disable-su          \**
**--disable-setpriv     \**
**--disable-runuser     \**
**--disable-pylibmount  \**
**--disable-liblastlog2 \**
**--disable-static      \**
**--without-python      \**
**ADJTIME_PATH=/var/lib/hwclock/adjtime \**
**--docdir=/usr/share/doc/util-linux-2.42.2**

The --disable and --without options prevent warnings about building components that either require packages not in
LFS, or are inconsistent with programs installed by other packages.

Compile the package:

**make**

If desired, create a dummy /etc/fstab file to satisfy two tests and run the test suite as a non-root user:

### Warning

Running the test suite as the root user can be harmful to your system. To run it, the CONFIG_SCSI_DEBUG
option for the kernel must be available in the currently running system and must be built as a module. Building
it into the kernel will prevent booting. For complete coverage, other BLFS packages must be installed. If
desired, this test can be run by booting into the completed LFS system and running:

**bash tests/run.sh --srcdir=$PWD --builddir=$PWD**

**touch /etc/fstab**
**chown -R tester .**
**su tester -c "make -k check"**

The lsfd: inotify test will fail if the kernel option CONFIG_NETLINK_DIAG is not enabled.

Install the package:

**make install**

---

Linux From Scratch - Version 13.1-systemd