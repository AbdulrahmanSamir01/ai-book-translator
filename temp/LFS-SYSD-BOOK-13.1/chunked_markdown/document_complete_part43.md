# 8.43. Expat-2.8.3

The Expat package contains a stream oriented C library for parsing XML.

**Approximate build time:**
0.1 SBU
**Required disk space:**
12 MB

## 8.43.1. Installation of Expat

Prepare Expat for compilation:

**./configure --prefix=/usr    \**
**--disable-static \**
**--docdir=/usr/share/doc/expat-2.8.3**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

If desired, install the documentation:

**install -v -m644 doc/*.{html,css} /usr/share/doc/expat-2.8.3**

## 8.43.2. Contents of Expat

**Installed program:**
xmlwf
**Installed libraries:**
libexpat.so
**Installed directory:**
/usr/share/doc/expat-2.8.3

**Short Descriptions**

**xmlwf**
Is a non-validating utility to check whether or not XML documents are well formed

libexpat
Contains API functions for parsing XML

---

Linux From Scratch - Version 13.1-systemd

# 8.44. Inetutils-2.8

The Inetutils package contains programs for basic networking.

**Approximate build time:**
0.3 SBU
**Required disk space:**
38 MB

## 8.44.1. Installation of Inetutils

First, make the package build with gcc-14.1 or later:

**sed -i 's/def HAVE_TERMCAP_TGETENT/ 1/' telnet/telnet.c**

Prepare Inetutils for compilation:

**./configure --prefix=/usr        \**
**--bindir=/usr/bin    \**
**--localstatedir=/var \**
**--disable-logger     \**
**--disable-whois      \**
**--disable-rcp        \**
**--disable-rexec      \**
**--disable-rlogin     \**
**--disable-rsh        \**
**--disable-servers**

**The meaning of the configure options:**

--disable-logger

**This option prevents Inetutils from installing the logger program, which is used by scripts to pass messages to the**
System Log Daemon. Do not install it because Util-linux installs a more recent version.

--disable-whois

**This option disables the building of the Inetutils whois client, which is out of date. Instructions for a better whois**
client are in the BLFS book.

--disable-r*

These parameters disable building obsolete programs that should not be used due to security issues. The functions
provided by these programs can be provided by the openssh package in the BLFS book.

--disable-servers

This disables the installation of the various network servers included as part of the Inetutils package. These servers
are deemed not appropriate in a basic LFS system. Some are insecure by nature and are only considered safe on
trusted networks. Note that better replacements are available for many of these servers.

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

Move a program to the proper location:

**mv -v /usr/{,s}bin/ifconfig**

---

Linux From Scratch - Version 13.1-systemd

## 8.44.2. Contents of Inetutils

**Installed programs:**
dnsdomainname, ftp, ifconfig, hostname, ping, ping6, talk, telnet, tftp, and traceroute

**Short Descriptions**

**dnsdomainname**
Show the system's DNS domain name

**ftp**
Is the file transfer protocol program

**hostname**
Reports or sets the name of the host

**ifconfig**
Manages network interfaces

**ping**
Sends echo-request packets and reports how long the replies take

**ping6**
**A version of ping for IPv6 networks**

**talk**
Is used to chat with another user

**telnet**
An interface to the TELNET protocol

**tftp**
A trivial file transfer program

**traceroute**
Traces the route your packets take from the host you are working on to another host on a network,
showing all the intermediate hops (gateways) along the way

---

Linux From Scratch - Version 13.1-systemd

# 8.45. Less-704

The Less package contains a text file viewer.

**Approximate build time:**
0.1 SBU
**Required disk space:**
17 MB

## 8.45.1. Installation of Less

Prepare Less for compilation:

**./configure --prefix=/usr --sysconfdir=/etc**

**The meaning of the configure options:**

--sysconfdir=/etc

This option tells the programs created by the package to look in /etc for the configuration files.

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

## 8.45.2. Contents of Less

**Installed programs:**
less, lessecho, and lesskey

**Short Descriptions**

**less**
A file viewer or pager; it displays the contents of the given file, letting the user scroll, find strings, and
jump to marks

**lessecho**
Needed to expand meta-characters, such as * and ?, in filenames on Unix systems

**lesskey**
**Used to specify the key bindings for less**

---

Linux From Scratch - Version 13.1-systemd

# 8.46. Perl-5.44.0

The Perl package contains the Practical Extraction and Report Language.

**Approximate build time:**
1.3 SBU
**Required disk space:**
261 MB

## 8.46.1. Installation of Perl

This version of Perl builds the Compress::Raw::Zlib and Compress::Raw::BZip2 modules. By default Perl will use an
internal copy of the sources for the build. Issue the following command so that Perl will use the libraries installed on
the system:

**export BUILD_ZLIB=False**
**export BUILD_BZIP2=0**

To have full control over the way Perl is set up, you can remove the “-des” options from the following command and
hand-pick the way this package is built. Alternatively, use the command exactly as shown below to use the defaults
that Perl auto-detects:

**sh Configure -des                                          \**
**-D prefix=/usr                                \**
**-D vendorprefix=/usr                          \**
**-D privlib=/usr/lib/perl5/5.44/core_perl      \**
**-D archlib=/usr/lib/perl5/5.44/core_perl      \**
**-D sitelib=/usr/lib/perl5/5.44/site_perl      \**
**-D sitearch=/usr/lib/perl5/5.44/site_perl     \**
**-D vendorlib=/usr/lib/perl5/5.44/vendor_perl  \**
**-D vendorarch=/usr/lib/perl5/5.44/vendor_perl \**
**-D man1dir=/usr/share/man/man1                \**
**-D man3dir=/usr/share/man/man3                \**
**-D pager="/usr/bin/less -isR"                 \**
**-D useshrplib                                 \**
**-D usethreads**

**The meaning of the new Configure options:**

-D pager="/usr/bin/less -isR"

**This ensures that less is used instead of more.**

-D man1dir=/usr/share/man/man1 -D man3dir=/usr/share/man/man3

**Since Groff is not installed yet, Configure will not create man pages for Perl. These parameters override this**
behavior.

-D usethreads

Build Perl with support for threads.

Compile the package:

**make**

To test the results, issue:

**TEST_JOBS=$(nproc) make test_harness**

Install the package and clean up:

**make install**
**unset BUILD_ZLIB BUILD_BZIP2**

---

Linux From Scratch - Version 13.1-systemd

## 8.46.2. Contents of Perl

**Installed programs:**
corelist, cpan, enc2xs, encguess, h2ph, h2xs, instmodsh, json_pp, libnetcfg, perl,
perl5.44.0 (hard link to perl), perlbug, perldoc, perlivp, perlthanks (hard link to perlbug),
piconv, pl2pm, pod2html, pod2man, pod2text, pod2usage, podchecker, podselect, prove,
ptar, ptardiff, ptargrep, shasum, splain, xsubpp, and zipdetails
**Installed libraries:**
Many which cannot all be listed here
**Installed directory:**
/usr/lib/perl5

**Short Descriptions**

**corelist**
A command line front end to Module::CoreList

**cpan**
Interact with the Comprehensive Perl Archive Network (CPAN) from the command line

**enc2xs**
Builds a Perl extension for the Encode module from either Unicode Character Mappings or Tcl
Encoding Files

**encguess**
Guess the encoding type of one or several files

**h2ph**
Converts .h C header files to .ph Perl header files

**h2xs**
Converts .h C header files to Perl extensions

**instmodsh**
Shell script for examining installed Perl modules; it can create a tarball from an installed module

**json_pp**
Converts data between certain input and output formats

**libnetcfg**
Can be used to configure the libnet Perl module

**perl**
**Combines some of the best features of C, sed, awk and sh into a single Swiss Army language**

**perl5.44.0**
**A hard link to perl**

**perlbug**
Used to generate bug reports about Perl, or the modules that come with it, and mail them

**perldoc**
Displays a piece of documentation in pod format that is embedded in the Perl installation tree or in
a Perl script

**perlivp**
The Perl Installation Verification Procedure; it can be used to verify that Perl and its libraries have
been installed correctly

**perlthanks**
Used to generate thank you messages to mail to the Perl developers

**piconv**
**A Perl version of the character encoding converter iconv**

**pl2pm**
A rough tool for converting Perl4 .pl files to Perl5 .pm modules

**pod2html**
Converts files from pod format to HTML format

**pod2man**
Converts pod data to formatted *roff input

**pod2text**
Converts pod data to formatted ASCII text

**pod2usage**
Prints usage messages from embedded pod docs in files

**podchecker**
Checks the syntax of pod format documentation files

**podselect**
Displays selected sections of pod documentation

**prove**
Command line tool for running tests against the Test::Harness module

**ptar**
**A tar-like program written in Perl**

**ptardiff**
A Perl program that compares an extracted archive with an unextracted one

---

Linux From Scratch - Version 13.1-systemd

**ptargrep**
A Perl program that applies pattern matching to the contents of files in a tar archive

**shasum**
Prints or checks SHA checksums

**splain**
Is used to force verbose warning diagnostics in Perl

**xsubpp**
Converts Perl XS code into C code

**zipdetails**
Displays details about the internal structure of a Zip file

---

Linux From Scratch - Version 13.1-systemd