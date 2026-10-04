# 8.23. GMP-6.3.0

The GMP package contains math libraries. These have useful functions for arbitrary precision arithmetic.

**Approximate build time:**
0.3 SBU
**Required disk space:**
54 MB

## 8.23.1. Installation of GMP

### Note

If you are building for 32-bit x86, but you have a CPU which is capable of running 64-bit code and you have
specified CFLAGS in the environment, the configure script will attempt to configure for 64-bits and fail. Avoid
this by invoking the configure command below with

**ABI=32 ./configure ...**

### Note

The default settings of GMP produce libraries optimized for the host processor. If libraries suitable for
processors less capable than the host's CPU are desired, generic libraries can be created by appending the -

**-host=none-linux-gnu option to the configure command.**

First, make an adjustment for compatibility with gcc-15 and later:

**sed -i '/long long t1;/,+1s/()/(...)/' configure**

Prepare GMP for compilation:

**./configure --prefix=/usr    \**
**--enable-cxx     \**
**--disable-static \**
**--docdir=/usr/share/doc/gmp-6.3.0**

**The meaning of the new configure options:**

--enable-cxx

This parameter enables C++ support

--docdir=/usr/share/doc/gmp-6.3.0

This variable specifies the correct place for the documentation.

Compile the package and generate the HTML documentation:

**make**
**make html**

### Important

The test suite for GMP in this section is considered critical. Do not skip it under any circumstances.

Test the results:

**make check**

---

Linux From Scratch - Version 13.1-systemd

### Caution

The code in gmp is highly optimized for the processor where it is built. Occasionally, the code that detects
the processor misidentifies the system capabilities and there will be errors in the tests or other applications
using the gmp libraries with the message Illegal instruction. In this case, gmp should be reconfigured with
the option --host=none-linux-gnu and rebuilt.

Ensure that at least 199 tests in the test suite passed. Check the results by issuing the following command:

**cat $(find -name '*.log') | grep -c ^PASS**

Install the package and its documentation:

**make install**
**make install-html**

## 8.23.2. Contents of GMP

**Installed libraries:**
libgmp.so and libgmpxx.so
**Installed directory:**
/usr/share/doc/gmp-6.3.0

**Short Descriptions**

libgmp
Contains precision math functions

libgmpxx
Contains C++ precision math functions

---

Linux From Scratch - Version 13.1-systemd

# 8.24. MPFR-4.2.2

The MPFR package contains functions for multiple precision math.

**Approximate build time:**
0.2 SBU
**Required disk space:**
44 MB

## 8.24.1. Installation of MPFR

Prepare MPFR for compilation:

**./configure --prefix=/usr        \**
**--disable-static     \**
**--enable-thread-safe \**
**--docdir=/usr/share/doc/mpfr-4.2.2**

Compile the package and generate the HTML documentation:

**make**
**make html**

### Important

The test suite for MPFR in this section is considered critical. Do not skip it under any circumstances.

Test the results and ensure that all 198 tests passed:

**make check**

Install the package and its documentation:

**make install**
**make install-html**

## 8.24.2. Contents of MPFR

**Installed libraries:**
libmpfr.so
**Installed directory:**
/usr/share/doc/mpfr-4.2.2

**Short Descriptions**

libmpfr
Contains multiple-precision math functions

---

Linux From Scratch - Version 13.1-systemd

# 8.25. MPC-1.4.1

The MPC package contains a library for the arithmetic of complex numbers with arbitrarily high precision and correct
rounding of the result.

**Approximate build time:**
0.1 SBU
**Required disk space:**
23 MB

## 8.25.1. Installation of MPC

Prepare MPC for compilation:

**./configure --prefix=/usr    \**
**--disable-static \**
**--docdir=/usr/share/doc/mpc-1.4.1**

Compile the package and generate the HTML documentation:

**make**
**make html**

To test the results, issue:

**make check**

Install the package and its documentation:

**make install**
**make install-html**

## 8.25.2. Contents of MPC

**Installed libraries:**
libmpc.so
**Installed directory:**
/usr/share/doc/mpc-1.4.1

**Short Descriptions**

libmpc
Contains complex math functions

---

Linux From Scratch - Version 13.1-systemd

# 8.26. Attr-2.6.0

The Attr package contains utilities to administer the extended attributes of filesystem objects.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
4.5 MB

## 8.26.1. Installation of Attr

Prepare Attr for compilation:

**./configure --prefix=/usr     \**
**--disable-static  \**
**--sysconfdir=/etc \**
**--docdir=/usr/share/doc/attr-2.6.0**

Compile the package:

**make**

The tests must be run on a filesystem that supports extended attributes such as the ext2, ext3, or ext4 filesystems. To
test the results, issue:

**make check**

Install the package:

**make install**

## 8.26.2. Contents of Attr

**Installed programs:**
attr, getfattr, and setfattr
**Installed library:**
libattr.so
**Installed directories:**
/usr/include/attr and /usr/share/doc/attr-2.6.0

**Short Descriptions**

**attr**
Extends attributes on filesystem objects

**getfattr**
Gets the extended attributes of filesystem objects

**setfattr**
Sets the extended attributes of filesystem objects

libattr
Contains the library functions for manipulating extended attributes

---

Linux From Scratch - Version 13.1-systemd

# 8.27. Acl-2.4.0

The Acl package contains utilities to administer Access Control Lists, which are used to define fine-grained
discretionary access rights for files and directories.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
7.1 MB

## 8.27.1. Installation of Acl

Prepare Acl for compilation:

**./configure --prefix=/usr    \**
**--disable-static \**
**--docdir=/usr/share/doc/acl-2.4.0**

Compile the package:

**make**

The Acl tests must be run on a filesystem that supports access controls. To test the results, issue:

**make check**

One test named test/cp.run is known to fail because Coreutils is not built with the Acl support yet.

Install the package:

**make install**

## 8.27.2. Contents of Acl

**Installed programs:**
chacl, getfacl, and setfacl
**Installed library:**
libacl.so
**Installed directories:**
/usr/include/acl and /usr/share/doc/acl-2.4.0

**Short Descriptions**

**chacl**
Changes the access control list of a file or directory

**getfacl**
Gets file access control lists

**setfacl**
Sets file access control lists

libacl
Contains the library functions for manipulating Access Control Lists

---

Linux From Scratch - Version 13.1-systemd

# 8.28. Libcap-2.78

The Libcap package implements the userspace interface to the POSIX 1003.1e capabilities available in Linux kernels.
These capabilities partition the all-powerful root privilege into a set of distinct privileges.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
3.1 MB

## 8.28.1. Installation of Libcap

### Note

If updating this package on an existing system and the go compiler is installed, prevent a build error by
**using export GOLANG=no before running the commands below. Be sure to unset GOLANG after installation**
is complete.

Prevent static libraries from being installed:

**sed -i '/install -m.*STA/d' libcap/Makefile**

Compile the package:

**make prefix=/usr lib=lib**

**The meaning of the make option:**

lib=lib

This parameter sets the library directory to /usr/lib rather than /usr/lib64 on x86_64. It has no effect on x86.

To test the results, issue:

**make test**

Install the package:

**make prefix=/usr lib=lib install**

## 8.28.2. Contents of Libcap

**Installed programs:**
capsh, getcap, getpcaps, and setcap
**Installed library:**
libcap.so and libpsx.so

**Short Descriptions**

**capsh**
A shell wrapper to explore and constrain capability support

**getcap**
Examines file capabilities

**getpcaps**
Displays the capabilities of the queried process(es)

**setcap**
Sets file capabilities

libcap
Contains the library functions for manipulating POSIX 1003.1e capabilities

libpsx
Contains functions to support POSIX semantics for syscalls associated with the pthread library

---

Linux From Scratch - Version 13.1-systemd