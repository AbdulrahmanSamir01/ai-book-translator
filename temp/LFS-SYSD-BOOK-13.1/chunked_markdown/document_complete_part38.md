# 8.29. Libxcrypt-4.5.2

The Libxcrypt package contains a modern library for one-way hashing of passwords.
**Approximate build time:**
0.1 SBU
**Required disk space:**
14 MB

## 8.29.1. Installation of Libxcrypt

First, make a fix required by glibc-2.43 and later:

**sed -i '/strchr/s/const//' lib/crypt-{sm3,gost}-yescrypt.c**

Prepare Libxcrypt for compilation:

**./configure --prefix=/usr                \**
**--enable-hashes=strong,glibc \**
**--enable-obsolete-api=no     \**
**--disable-static             \**
**--disable-failure-tokens**

**The meaning of the new configure options:**

--enable-hashes=strong,glibc

Build strong hash algorithms recommended for security use cases, and the hash algorithms provided by traditional
Glibc libcrypt for compatibility.

--enable-obsolete-api=no

Disable obsolete API functions. They are not needed for a modern Linux system built from source.

--disable-failure-tokens

Disable failure token feature. It's needed for compatibility with the traditional hash libraries of some platforms,
but a Linux system based on Glibc does not need it.

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

### Note

The instructions above disabled obsolete API functions since no package installed by compiling from sources
would link against them at runtime. However, the only known binary-only applications that link against these
functions require ABI version 1. If you must have such functions because of some binary-only application or
to be compliant with LSB, build the package again with the following commands:

**make distclean**
**./configure --prefix=/usr                \**
**--enable-hashes=strong,glibc \**
**--enable-obsolete-api=glibc  \**
**--disable-static             \**
**--disable-failure-tokens**
**make**
**cp -av --remove-destination .libs/libcrypt.so.1* /usr/lib**

---

Linux From Scratch - Version 13.1-systemd

## 8.29.2. Contents of Libxcrypt

**Installed libraries:**
libcrypt.so

**Short Descriptions**

libcrypt
Contains functions to hash passwords

---

Linux From Scratch - Version 13.1-systemd

# 8.30. Shadow-4.20.2

The Shadow package contains programs for handling passwords in a secure way.

**Approximate build time:**
0.1 SBU
**Required disk space:**
112 MB

## 8.30.1. Installation of Shadow

### Important

If you've installed Linux-PAM, you should follow the BLFS instructions instead of this page to build, rebuild,
upgrade shadow.

### Note

If you would like to enforce the use of strong passwords, install and configure Linux-PAM first. Then install
and configure shadow with the PAM support. Finally install libpwquality and configure PAM to use it.

Prevent the installation of manual pages that were already installed in Section 8.3, “Man-pages-6.18”:

**find man -name Makefile.in -exec sed -i 's/getspnam\.3 / /' {} \;**
**find man -name Makefile.in -exec sed -i 's/passwd\.5 / /'   {} \;**

Instead of using the default SHA512 method, use the more secure YESCRYPT method of password encryption. It is
also necessary to change the obsolete /var/spool/mail location for user mailboxes that Shadow uses by default to the

/var/mail location used currently. And, remove /bin and /sbin from the PATH, since they are simply symlinks to their
counterparts in /usr.

### Warning

Including /bin and/or /sbin in the PATH variable may cause some BLFS packages fail to build, so don't do
that in the .bashrc file or anywhere else.

**sed -e 's:#ENCRYPT_METHOD SHA512:ENCRYPT_METHOD YESCRYPT:' \**
**-e 's:/var/spool/mail:/var/mail:'                      \**
**-e '/PATH=/{s@/sbin:@@;s@/bin:@@}'                     \**
**-i etc/login.defs**

Prepare Shadow for compilation:

**touch /usr/bin/passwd**
**./configure --sysconfdir=/etc   \**
**--disable-static    \**
**--with-{b,yes}crypt \**
**--without-libbsd    \**
**--disable-logind    \**
**--with-group-name-max-length=32**

**The meaning of the new configuration options:**

**touch /usr/bin/passwd**

The file /usr/bin/passwd needs to exist because its location is hardcoded in some programs; if it does not already
exist, the installation script will create it in the wrong place.

---

Linux From Scratch - Version 13.1-systemd

--with-{b,yes}crypt

The shell expands this to two switches, --with-bcrypt and --with-yescrypt. They allow shadow to use the Bcrypt
and Yescrypt algorithms implemented by Libxcrypt for hashing passwords. These algorithms are more secure (in
particular, much more resistant to GPU-based attacks) than the traditional SHA algorithms.

--with-group-name-max-length=32

The longest permissible user name is 32 characters. Make the maximum length of a group name the same.

--disable-logind

**This option makes Shadow (specifically, the login and who programs) use the /run/utmp file instead of logind to**
track the active login sessions, as logind isn't available yet in the incomplete LFS system. But as we've discussed
in Section 7.6, “Creating Essential Files and Symlinks”, the /run/utmp file format will be completely broken after
year 2038. The LFS editors will attempt to resolve the issue before that year.

--without-libbsd

Do not use the readpassphrase function from libbsd which is not in LFS. Use the internal copy instead.

Compile the package:

**make**

This package does not come with a test suite.

Install the package:

**make exec_prefix=/usr install**
**make -C man install-man**

## 8.30.2. Configuring Shadow

This package contains utilities to add, modify, and delete users and groups; set and change their passwords; and perform
other administrative tasks. For a full explanation of what password shadowing means, see the doc/HOWTO file within
the unpacked source tree.

Enable shadowed passwords:

**pwconv**

Enable shadowed group passwords as well:

**grpconv**

**Shadow's default configuration for the useradd utility needs some explanation. First, the default action for the useradd**
utility is to create the user and a group with the same name as the user. By default the user ID (UID) and group ID (GID)
**numbers will begin at 1000. This means if you don't pass extra parameters to useradd, each user will be a member of a**
**unique group on the system. If this behavior is undesirable, you'll need to pass either the -g or -N parameter to useradd,**
or else change the setting of USERGROUPS_ENAB in /etc/login.defs. See useradd(8) for more information.

Second, to change the default parameters, the file /etc/default/useradd must be created and tailored to suit your
particular needs. Create it with:

**mkdir -p /etc/default**
**useradd -D --gid 999**

**/etc/default/useradd parameter explanations**

GROUP=999

This parameter sets the beginning of the group numbers used in the /etc/group file. The particular value 999 comes
**from the --gid parameter above. You may set it to any desired value. Note that useradd will never reuse a UID or**

---

Linux From Scratch - Version 13.1-systemd

GID. If the number identified in this parameter is used, it will use the next available number. Note also that if you
**don't have a group with an ID equal to this number on your system, then the first time you use useradd without the**

-g parameter, an error message will be generated—useradd: unknown GID 999, even though the account has been
created correctly. That is why we created the group users with this group ID in Section 7.6, “Creating Essential
Files and Symlinks.”

CREATE_MAIL_SPOOL=yes

**This parameter causes useradd to create a mailbox file for each new user. useradd will assign the group ownership**
of this file to the mail group with 0660 permissions. If you would rather not create these files, issue the following
command:

**sed -i '/MAIL/s/yes/no/' /etc/default/useradd**

Finally, create the empty /etc/subuid and /etc/subgid files:

**touch /etc/sub{u,g}id**

The content of those files will be automatically updated by some utilities provided by Shadow to allocate subordinate
user and group IDs. Read the man pages subuid(5) and subgid(5) for the details about the subordinate IDs.