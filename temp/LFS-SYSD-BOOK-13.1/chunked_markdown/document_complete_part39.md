## 8.30.3. Setting the Root Password

Choose a password for user root and set it by running:

**passwd root**

## 8.30.4. Contents of Shadow

**Installed programs:**
chage, chfn, chgpasswd, chpasswd, chsh, faillog, getsubids, gpasswd, groupadd,
groupdel, groupmod, grpck, grpconv, grpunconv, login, newgidmap, newgrp,
newuidmap, newusers, nologin, passwd, pwck, pwconv, pwunconv, sg (link to newgrp),
su, useradd, userdel, usermod, vigr (link to vipw), and vipw
**Installed libraries:**
libsubid.so
**Installed directories:**
/etc/default and /usr/include/shadow

**Short Descriptions**

**chage**
Used to change the maximum number of days between obligatory password changes

**chfn**
Used to change a user's full name and other information

**chgpasswd**
Used to update group passwords in batch mode

**chpasswd**
Used to update user passwords in batch mode

**chsh**
Used to change a user's default login shell

**faillog**
Is used to examine the log of login failures, to set a maximum number of failures before an account
is blocked, and to reset the failure count

**getsubids**
Is used to list the subordinate id ranges for a user

**gpasswd**
Is used to add and delete members and administrators to groups

**groupadd**
Creates a group with the given name

**groupdel**
Deletes the group with the given name

**groupmod**
Is used to modify the given group's name or GID

---

Linux From Scratch - Version 13.1-systemd

**grpck**
Verifies the integrity of the group files /etc/group and /etc/gshadow

**grpconv**
Creates or updates the shadow group file from the normal group file

**grpunconv**
Updates /etc/group from /etc/gshadow and then deletes the latter

**login**
Is used by the system to let users sign on

**newgidmap**
Is used to set the gid mapping of a user namespace

**newgrp**
Is used to change the current GID during a login session

**newuidmap**
Is used to set the uid mapping of a user namespace

**newusers**
Is used to create or update an entire series of user accounts

**nologin**
Displays a message saying an account is not available; it is designed to be used as the default shell
for disabled accounts

**passwd**
Is used to change the password for a user or group account

**pwck**
Verifies the integrity of the password files /etc/passwd and /etc/shadow

**pwconv**
Creates or updates the shadow password file from the normal password file

**pwunconv**
Updates /etc/passwd from /etc/shadow and then deletes the latter

**sg**
Executes a given command while the user's GID is set to that of the given group

**su**
Runs a shell with substitute user and group IDs

**useradd**
Creates a new user with the given name, or updates the default new-user information

**userdel**
Deletes the specified user account

**usermod**
Is used to modify the given user's login name, user identification (UID), shell, initial group, home
directory, etc.

**vigr**
Edits the /etc/group or /etc/gshadow files

**vipw**
Edits the /etc/passwd or /etc/shadow files

libsubid
library to handle subordinate id ranges for users and groups

---

Linux From Scratch - Version 13.1-systemd

# 8.31. Gawk-5.4.1

The Gawk package contains programs for manipulating text files.

**Approximate build time:**
0.2 SBU
**Required disk space:**
47 MB

## 8.31.1. Installation of Gawk

First, ensure some unneeded files are not installed:

**sed -i 's/extras//' Makefile.in**

Prepare Gawk for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

To test the results, issue:

**chown -R tester .**
**su tester -c "PATH=$PATH make check"**

Install the package:

**rm -f /usr/bin/gawk-5.4.1**
**make install**

**The meaning of the command:**

**rm -f /usr/bin/gawk-5.4.1**

The building system will not recreate the hard link gawk-5.4.1 if it already exists. Remove it to ensure that the
previous hard link installed in Section 6.9, “Gawk-5.4.1” is updated here.

**The installation process already created awk as a symlink to gawk, create its man page as a symlink as well:**

**ln -sv gawk.1 /usr/share/man/man1/awk.1**

If desired, install the documentation:

**install -vDm644 doc/{awkforai.txt,*.{eps,pdf,jpg}} -t /usr/share/doc/gawk-5.4.1**

## 8.31.2. Contents of Gawk

**Installed programs:**
awk (link to gawk), gawk, and gawk-5.4.1
**Installed libraries:**
filefuncs.so, fnmatch.so, fork.so, inplace.so, intdiv.so, ordchr.so, readdir.so, readfile.so,
revoutput.so, revtwoway.so, rwarray.so, and time.so (all in /usr/lib/gawk)
**Installed directories:**
/usr/lib/gawk, /usr/libexec/awk, /usr/share/awk, and /usr/share/doc/gawk-5.4.1

**Short Descriptions**

**awk**
**A link to gawk**

**gawk**
**A program for manipulating text files; it is the GNU implementation of awk**

**gawk-5.4.1**
**A hard link to gawk**

---

Linux From Scratch - Version 13.1-systemd

# 8.32. GCC-16.2.0

The GCC package contains the GNU compiler collection, which includes the C and C++ compilers.

**Approximate build time:**
53 SBU (with tests)
**Required disk space:**
7.3 GB

## 8.32.1. Installation of GCC

If building on x86_64, change the default directory name for 64-bit libraries to “lib”:

**case $(uname -m) in**
**x86_64)**
**sed -e '/m64=/s/lib64/lib/' \**
**-i.orig gcc/config/i386/t-linux64**
**;;**
**esac**

The GCC documentation recommends building GCC in a dedicated build directory:

**mkdir -v build**
**cd       build**

Prepare GCC for compilation:

**../configure --prefix=/usr            \**
**LD=ld                    \**
**--enable-languages=c,c++ \**
**--enable-default-pie     \**
**--enable-default-ssp     \**
**--enable-host-pie        \**
**--enable-targets=all     \**
**--disable-multilib       \**
**--disable-bootstrap      \**
**--disable-fixincludes    \**
**--with-system-zlib**

We only enable C and C++ here to save the build time as no packages in LFS and BLFS require GCC to compile other
languages. Append algol68 for Algol 68, fortran for Fortran, go for Go, objc for Objective C, obj-c++ for Objective
C++, and/or m2 for Modula 2 into the value of --enable-languages option if you want to compile programs in one or
more of those languages with GCC.

GCC also supports the Ada, COBOL, and D languages. But that would require some dependencies which are not
available in the base LFS system and would exceed the scope of this book. Read the upstream documentation for details.

**The meaning of the new configure parameters:**

LD=ld

This parameter makes the configure script use the ld program installed by the Binutils package built earlier in this
chapter, rather than the cross-built version which would otherwise be used.

--disable-bootstrap

By default, the build system of GCC will bootstrap it in 3 stages unless it's built as a cross-compiler or it is being
cross-compiled. The bootstrap process is needed for robustness, especially when upgrading GCC to a new version.
In LFS we are using a different method to bootstrap GCC (as we introduced in Toolchain Technical Notes), so
here we don't need the bootstrap process provided by the build system and we disable it to significantly reduce the
build time. Remove this option when you upgrade GCC on a complete LFS system (instead of building LFS).

---

Linux From Scratch - Version 13.1-systemd

--with-system-zlib

This switch tells GCC to link to the system installed copy of the Zlib library, rather than its own internal copy.

--enable-targets=all

This switch tells GCC to enable 64-bit code generation support even if we are building it for a 32-bit system. It's
needed to build GRUB for 64-bit UEFI. This switch has no effect if building for 64-bit.

### Note

PIE (position-independent executables) are binary programs that can be loaded anywhere in memory. Without
PIE, the security feature named ASLR (Address Space Layout Randomization) can be applied for the shared
libraries, but not for the executables themselves. Enabling PIE allows ASLR for the executables in addition
to the shared libraries, and mitigates some attacks based on fixed addresses of sensitive code or data in the
executables.

SSP (Stack Smashing Protection) is a technique to ensure that the parameter stack is not corrupted. Stack
corruption can, for example, alter the return address of a subroutine, thus transferring control to some
dangerous code (existing in the program or shared libraries, or injected by the attacker somehow).

Compile the package:

**make**