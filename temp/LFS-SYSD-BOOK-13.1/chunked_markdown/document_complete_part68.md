# Appendix B. Acknowledgments

We would like to thank the following people and organizations for their contributions to the Linux From Scratch Project.

• Gerard Beekmans <gerard@linuxfromscratch.org> – LFS Creator

• Bruce Dubbs <bdubbs@linuxfromscratch.org> – LFS Managing Editor

• Jim Gifford <jim@linuxfromscratch.org> – CLFS Project Co-Leader

• Pierre Labastie <pierre@linuxfromscratch.org> – BLFS Editor and ALFS Lead

• DJ Lucas <dj@linuxfromscratch.org> – LFS and BLFS Editor

• Ken Moffat <ken@linuxfromscratch.org> – BLFS Editor

• Countless other people on the various LFS and BLFS mailing lists who helped make this book possible by giving
their suggestions, testing the book, and submitting bug reports, instructions, and their experiences with installing
various packages.

## Translators

• Manuel Canales Esparcia <macana@macana-es.com> – Spanish LFS translation project

• Johan Lenglet <johan@linuxfromscratch.org> – French LFS translation project until 2008

• Jean-Philippe Mengual  <jmengual@linuxfromscratch.org> – French LFS translation project 2008-2016

• Julien Lepiller  <jlepiller@linuxfromscratch.org> – French LFS translation project 2017-present

• Anderson Lizardo <lizardo@linuxfromscratch.org> – Portuguese LFS translation project historical

• Jamenson Espindula <jafesp@gmail.com> – Portuguese LFS translation project 2022-present

• Thomas Reitelbach  <tr@erdfunkstelle.de> – German LFS translation project

## Mirror Maintainers

**North American Mirrors**

• Scott Kveton <scott@osuosl.org> – lfs.oregonstate.edu mirror

• William Astle <lost@l-w.net> – ca.linuxfromscratch.org mirror

• Eujon Sellers <jpolen@rackspace.com> – lfs.introspeed.com mirror

• Justin Knierim <tim@idge.net> – lfs-matrix.net mirror

**South American Mirrors**

• Manuel Canales Esparcia <manuel@linuxfromscratch.org> – lfsmirror.lfs-es.info mirror

• Luis Falcon <Luis Falcon> – torredehanoi.org mirror

**European Mirrors**

• Guido Passet <guido@primerelay.net> – nl.linuxfromscratch.org mirror

• Bastiaan Jacques <baafie@planet.nl> – lfs.pagefault.net mirror

• Sven Cranshoff <sven.cranshoff@lineo.be> – lfs.lineo.be mirror

---

Linux From Scratch - Version 13.1-systemd

• Scarlet Belgium – lfs.scarlet.be mirror

• Sebastian Faulborn <info@aliensoft.org> – lfs.aliensoft.org mirror

• Stuart Fox <stuart@dontuse.ms> – lfs.dontuse.ms mirror

• Ralf Uhlemann <admin@realhost.de> – lfs.oss-mirror.org mirror

• Antonin Sprinzl <Antonin.Sprinzl@tuwien.ac.at> – at.linuxfromscratch.org mirror

• Fredrik Danerklint <fredan-lfs@fredan.org> – se.linuxfromscratch.org mirror

• Franck <franck@linuxpourtous.com> – lfs.linuxpourtous.com mirror

• Philippe Baque <baque@cict.fr> – lfs.cict.fr mirror

• Vitaly Chekasin <gyouja@pilgrims.ru> – lfs.pilgrims.ru mirror

• Benjamin Heil <kontakt@wankoo.org> – lfs.wankoo.org mirror

• Anton Maisak <info@linuxfromscratch.org.ru> – linuxfromscratch.org.ru mirror

**Asian Mirrors**

• Satit Phermsawang <satit@wbac.ac.th> – lfs.phayoune.org mirror

• Shizunet Co.,Ltd. <info@shizu-net.jp> – lfs.mirror.shizu-net.jp mirror

**Australian Mirrors**

• Jason Andrade <jason@dstc.edu.au> – au.linuxfromscratch.org mirror

## Former Project Team Members

• Christine Barczak <theladyskye@linuxfromscratch.org> – LFS Book Editor

• Archaic <archaic@linuxfromscratch.org> – LFS Technical Writer/Editor, HLFS Project Leader, BLFS Editor,
Hints and Patches Project Maintainer

• Matthew Burgess <matthew@linuxfromscratch.org> – LFS Project Leader, LFS Technical Writer/Editor

• Nathan Coulson <nathan@linuxfromscratch.org> – LFS-Bootscripts Maintainer

• Timothy Bauscher

• Robert Briggs

• Ian Chilton

• Jeroen Coumans <jeroen@linuxfromscratch.org> – Website Developer, FAQ Maintainer

• Manuel Canales Esparcia <manuel@linuxfromscratch.org> – LFS/BLFS/HLFS XML and XSL Maintainer

• Alex Groenewoud – LFS Technical Writer

• Marc Heerdink

• Jeremy Huntwork <jhuntwork@linuxfromscratch.org> – LFS Technical Writer, LFS LiveCD Maintainer

• Bryan Kadzban <bryan@linuxfromscratch.org> – LFS Technical Writer

• Mark Hymers

• Seth W. Klein – FAQ maintainer

• Nicholas Leippe <nicholas@linuxfromscratch.org> – Wiki Maintainer

---

Linux From Scratch - Version 13.1-systemd

• Anderson Lizardo <lizardo@linuxfromscratch.org> – Website Backend-Scripts Maintainer

• Anderson Lizardo <dj@lucasit.com> – LFS Technical Writer

• Randy McMurchy <randy@linuxfromscratch.org> – BLFS Project Leader, LFS Editor

• Dan Nicholson <dnicholson@linuxfromscratch.org> – LFS and BLFS Editor

• Alexander E. Patrakov <alexander@linuxfromscratch.org> – LFS Technical Writer, LFS Internationalization
Editor, LFS Live CD Maintainer

• Simon Perreault

• Scot Mc Pherson <scot@linuxfromscratch.org> – LFS NNTP Gateway Maintainer

• Douglas R. Reno <renodr@linuxfromscratch.org> – Systemd Editor

• Ryan Oliver <ryan@linuxfromscratch.org> – CLFS Project Co-Leader

• Greg Schafer <gschafer@zip.com.au> – LFS Technical Writer and Architect of the Next Generation 64-bit-
enabling Build Method

• Jesse Tie-Ten-Quee – LFS Technical Writer

• James Robertson <jwrober@linuxfromscratch.org> – Bugzilla Maintainer

• Tushar Teredesai <tushar@linuxfromscratch.org> – BLFS Book Editor, Hints and Patches Project Leader

• Jeremy Utley <jeremy@linuxfromscratch.org> – LFS Technical Writer, Bugzilla Maintainer, LFS-Bootscripts
Maintainer

• Zack Winkles <zwinkles@gmail.com> – LFS Technical Writer

---

Linux From Scratch - Version 13.1-systemd

# Appendix C. Dependencies

Every package built in LFS relies on one or more other packages in order to build and install properly. Some packages
even participate in circular dependencies, that is, the first package depends on the second which in turn depends on the
first. Because of these dependencies, the order in which packages are built in LFS is very important. The purpose of
this page is to document the dependencies of each package built in LFS.

For each package that is built, there are three, and sometimes up to five types of dependencies listed below. The first
lists what other packages need to be available in order to compile and install the package in question. The second lists
the packages that must be available when any programs or libraries from the package are used at runtime. The third
lists what packages, in addition to those on the first list, need to be available in order to run the test suites. The fourth
list of dependencies are packages that require this package to be built and installed in its final location before they are
built and installed.

The last list of dependencies are optional packages that are not addressed in LFS, but could be useful to the user.
These packages may have additional mandatory or optional dependencies of their own. For these dependencies, the
recommended practice is to install them after completion of the LFS book and then go back and rebuild the LFS package.
In several cases, re-installation is addressed in BLFS.

## Acl

**Installation depends on:**
Bash, Binutils, Coreutils, GCC, Gettext, Grep, M4, Make, Perl, Sed, and Texinfo
**Required at runtime:**
Glibc
**Test suite depends on:**
Automake, Diffutils, Findutils, and Libtool
**Must be installed before:**
Coreutils, Sed, Tar, and Vim
**Optional dependencies:**
None

## Attr

**Installation depends on:**
Bash, Binutils, Coreutils, GCC, Gettext, Glibc, Grep, M4, Make, Perl, Sed, and Texinfo
**Required at runtime:**
Glibc
**Test suite depends on:**
Automake, Diffutils, Findutils, and Libtool
**Must be installed before:**
Acl, Libcap, and Patch
**Optional dependencies:**
None

## Autoconf

**Installation depends on:**
Bash, Coreutils, Grep, M4, Make, Perl, Sed, and Texinfo
**Required at runtime:**
Bash, Coreutils, Grep, M4, Make, Sed, and Texinfo
**Test suite depends on:**
Automake, Diffutils, Findutils, GCC, and Libtool
**Must be installed before:**
Automake and Coreutils
**Optional dependencies:**
Emacs