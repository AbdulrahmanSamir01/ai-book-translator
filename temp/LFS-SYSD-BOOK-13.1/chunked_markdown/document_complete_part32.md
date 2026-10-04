### Note

Glibc now uses libidn2 when resolving internationalized domain names. This is a run time dependency. If
this capability is needed, the instructions for installing libidn2 are in the BLFS libidn2 page.

---

Linux From Scratch - Version 13.1-systemd

## 8.5.2. Configuring Glibc

**8.5.2.1. Adding nsswitch.conf**

The /etc/nsswitch.conf file needs to be created because the Glibc defaults do not work well in a networked
environment.

Create a new file /etc/nsswitch.conf by running the following:

**cat > /etc/nsswitch.conf << "EOF"**

# Begin /etc/nsswitch.conf

passwd: files systemd
group: files systemd
shadow: files systemd

hosts: mymachines resolve [!UNAVAIL=return] files myhostname dns
networks: files

protocols: files
services: files
ethers: files
rpc: files

# End /etc/nsswitch.conf
**EOF**

**8.5.2.2. Adding Time Zone Data**

Install and set up the time zone data with the following:

**tar -xf ../../tzdata2026c.tar.gz**

**ZONEINFO=/usr/share/zoneinfo**
**mkdir -pv $ZONEINFO/{posix,right}**

**for tz in etcetera southamerica northamerica europe africa antarctica  \**
**asia australasia backward; do**
**zic -L /dev/null   -d $ZONEINFO       ${tz}**
**zic -L /dev/null   -d $ZONEINFO/posix ${tz}**
**zic -L leapseconds -d $ZONEINFO/right ${tz}**
**done**

**cp -v zone.tab zone1970.tab iso3166.tab $ZONEINFO**
**zic -d $ZONEINFO -p America/New_York**
**unset ZONEINFO tz**

**The meaning of the zic commands:**

zic -L /dev/null ...

This creates posix time zones without any leap seconds. It is conventional to put these in both zoneinfo and

zoneinfo/posix. It is necessary to put the POSIX time zones in zoneinfo, otherwise various test suites will report
errors. On an embedded system, where space is tight and you do not intend to ever update the time zones, you could
save 1.9 MB by not using the posix directory, but some applications or test suites might produce some failures.

zic -L leapseconds ...

This creates right time zones, including leap seconds. On an embedded system, where space is tight and you do
not intend to ever update the time zones, or care about the correct time, you could save 1.9MB by omitting the

right directory.

---

Linux From Scratch - Version 13.1-systemd

zic ... -p ...

This creates the posixrules file. We use New York because POSIX requires the daylight saving time rules to be
in accordance with US rules.

One way to determine the local time zone is to run the following script:

**tzselect**

After answering a few questions about the location, the script will output the name of the time zone (e.g., America/
Edmonton). There are also some other possible time zones listed in /usr/share/zoneinfo such as Canada/Eastern or
EST5EDT that are not identified by the script but can be used.

Then create the /etc/localtime file by running:

**ln -sfv /usr/share/zoneinfo/<xxx> /etc/localtime**

Replace <xxx> with the name of the time zone selected (e.g., Canada/Eastern).

**8.5.2.3. Configuring the Dynamic Loader**

By default, the dynamic loader (/lib/ld-linux.so.2) searches through /usr/lib for dynamic libraries that are needed
by programs as they are run. However, if there are libraries in directories other than /usr/lib, these need to be added
to the /etc/ld.so.conf file in order for the dynamic loader to find them. Two directories that are commonly known to
contain additional libraries are /usr/local/lib and /opt/lib, so add those directories to the dynamic loader's search
path.

Create a new file /etc/ld.so.conf by running the following:

**cat > /etc/ld.so.conf << "EOF"**

# Begin /etc/ld.so.conf
/usr/local/lib
/opt/lib

**EOF**

If desired, the dynamic loader can also search a directory and include the contents of files found there. Generally the
files in this include directory are one line specifying the desired library path. To add this capability run the following
commands:

**cat >> /etc/ld.so.conf << "EOF"**

# Add an include directory
include /etc/ld.so.conf.d/*.conf

**EOF**
**mkdir -pv /etc/ld.so.conf.d**

---

Linux From Scratch - Version 13.1-systemd

## 8.5.3. Contents of Glibc

**Installed programs:**
gencat, getconf, getent, iconv, iconvconfig, ldconfig, ldd, lddlibc4, ld.so (symlink to ld-
linux-x86-64.so.2 or ld-linux.so.2), locale, localedef, makedb, mtrace, pcprofiledump,
pldd, sln, sotruss, sprof, tzselect, xtrace, zdump, and zic
**Installed libraries:**
ld-linux-x86-64.so.2, ld-linux.so.2, libBrokenLocale.{a,so}, libanl.{a,so}, libc.{a,so},
libc_nonshared.a, libc_malloc_debug.so, libdl.{a,so.2}, libg.a, libm.{a,so}, libmcheck.a,
libmemusage.so,
libmvec.{a,so},
libnsl.so.1,
libnss_compat.so,
libnss_dns.so,
libnss_files.so, libnss_hesiod.so, libpcprofile.so, libpthread.{a,so.0}, libresolv.{a,so},
librt.{a,so.1}, libthread_db.so, and libutil.{a,so.1}
**Installed directories:**
/usr/include/arpa, /usr/include/bits, /usr/include/gnu, /usr/include/net, /usr/include/
netash, /usr/include/netatalk, /usr/include/netax25, /usr/include/neteconet, /usr/include/
netinet, /usr/include/netipx, /usr/include/netiucv, /usr/include/netpacket, /usr/include/
netrom, /usr/include/netrose, /usr/include/nfs, /usr/include/protocols, /usr/include/rpc, /
usr/include/sys, /usr/lib/audit, /usr/lib/gconv, /usr/lib/locale, /usr/libexec/getconf, /usr/
share/i18n, /usr/share/zoneinfo, and /var/lib/nss_db

**Short Descriptions**

**gencat**
Generates message catalogues

**getconf**
Displays the system configuration values for file system specific variables

**getent**
Gets entries from an administrative database

**iconv**
Performs character set conversion

**iconvconfig**
**Creates fastloading iconv module configuration files**

**ldconfig**
Configures the dynamic linker runtime bindings

**ldd**
Reports which shared libraries are required by each given program or shared library

**lddlibc4**
**Assists ldd with object files. It does not exist on newer architectures like x86_64**

**locale**
Prints various information about the current locale

**localedef**
Compiles locale specifications

**makedb**
Creates a simple database from textual input

**mtrace**
Reads and interprets a memory trace file and displays a summary in human-readable format

**pcprofiledump**
Dump information generated by PC profiling

**pldd**
Lists dynamic shared objects used by running processes

**sln**
**A statically linked ln program**

**sotruss**
Traces shared library procedure calls of a specified command

**sprof**
Reads and displays shared object profiling data

**tzselect**
Asks the user about the location of the system and reports the corresponding time zone
description

**xtrace**
Traces the execution of a program by printing the currently executed function

**zdump**
The time zone dumper

**zic**
The time zone compiler

ld-*.so
The helper program for shared library executables

---

Linux From Scratch - Version 13.1-systemd

libBrokenLocale
Used internally by Glibc as a gross hack to get broken programs (e.g., some Motif
applications) running. See comments in glibc-2.44/locale/broken_cur_max.c for more
information

libanl
Dummy library containing no functions. Previously was the asynchronous name lookup
library, whose functions are now in libc

libc
The main C library

libc_malloc_debug
Turns on memory allocation checking when preloaded

libdl
Dummy library containing no functions. Previously was the dynamic linking interface
library, whose functions are now in libc

libg
**Dummy library containing no functions. Previously was a runtime library for g++**

libm
The mathematical library

libmvec
The vector math library, linked in as needed when libm is used

libmcheck
Turns on memory allocation checking when linked to

libmemusage
**Used by memusage to help collect information about the memory usage of a program**

libnsl
The network services library, now deprecated

libnss_*
The Name Service Switch modules, containing functions for resolving host names, user
names, group names, aliases, services, protocols, etc. Loaded by libc according to the
configuration in /etc/nsswitch.conf

libpcprofile
Can be preloaded to PC profile an executable

libpthread
Dummy library containing no functions. Previously contained functions providing most of
the interfaces specified by the POSIX.1c Threads Extensions and the semaphore interfaces
specified by the POSIX.1b Real-time Extensions, now the functions are in libc

libresolv
Contains functions for creating, sending, and interpreting packets to the Internet domain
name servers

librt
Contains functions providing most of the interfaces specified by the POSIX.1b Real-time
Extensions

libthread_db
Contains functions useful for building debuggers for multi-threaded programs

libutil
Dummy library containing no functions. Previously contained code for “standard”
functions used in many different Unix utilities. These functions are now in libc

---

Linux From Scratch - Version 13.1-systemd