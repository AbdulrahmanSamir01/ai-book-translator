# 8.51. Libffi-3.8.0

The Libffi library provides a portable, high level programming interface to various calling conventions. This allows a
programmer to call any function specified by a call interface description at run time.

FFI stands for Foreign Function Interface. An FFI allows a program written in one language to call a program written
in another language. Specifically, Libffi can provide a bridge between an interpreter like Perl, or Python, and shared
library subroutines written in C, or C++.

**Approximate build time:**
1.7 SBU
**Required disk space:**
12 MB

## 8.51.1. Installation of Libffi

### Note

Like GMP, Libffi builds with optimizations specific to the processor in use. If building for another system,
change the value of the --with-gcc-arch= parameter in the following command to an architecture name fully
**implemented by both the host CPU and the CPU on that system. If this is not done, all applications that link**
to libffi will trigger Illegal Operation Errors. If you cannot figure out a value safe for both the CPUs, replace
the parameter with --without-gcc-arch to produce a generic library.

Prepare Libffi for compilation:

**./configure --prefix=/usr    \**
**--disable-static \**
**--with-gcc-arch=native**

**The meaning of the configure option:**

--with-gcc-arch=native

Ensure GCC optimizes for the current system. If this is not specified, the system is guessed and the code generated
may not be correct. If the generated code will be copied from the native system to a less capable system, use the less
capable system as a parameter. For details about alternative system types, see  the x86 options in the GCC manual.

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

## 8.51.2. Contents of Libffi

**Installed library:**
libffi.so

**Short Descriptions**

libffi
Contains the foreign function interface API functions

---

Linux From Scratch - Version 13.1-systemd

# 8.52. Sqlite-3530400

The Sqlite package is a software library that implements a self-contained, serverless, zero-configuration, transactional
SQL database engine.

**Approximate build time:**
0.4 SBU
**Required disk space:**
128 MB

## 8.52.1. Installation of Sqlite

Unpack the documentation:

**python3 -m zipfile -e ../sqlite-doc-3530400.zip .**

Prepare Sqlite for compilation with:

**./configure --prefix=/usr     \**
**--disable-static  \**
**--enable-fts{4,5} \**
**CPPFLAGS="-D SQLITE_ENABLE_COLUMN_METADATA=1 \**
**-D SQLITE_ENABLE_UNLOCK_NOTIFY=1   \**
**-D SQLITE_ENABLE_DBSTAT_VTAB=1     \**
**-D SQLITE_SECURE_DELETE=1"**

**The meaning of the configure options:**

--enable-fts{4,5}

These switches enable support for version 4 and 5 of the full text search (FTS) extension.

CPPFLAGS="-D SQLITE_ENABLE_COLUMN_METADATA=1 ...

Some applications require these options to be turned on. The only way to do this is to include them in the CFLAGS
or CPPFLAGS. We use the latter so the default value (or any value set by the user) of CFLAGS won't be affected.
For further information on what can be specified see https://www.sqlite.org/compile.html.

Compile the package:

**make LDFLAGS.rpath=""**

The LDFLAGS.rpath="" option prevents hard coding library search paths (rpath) into the shared library. This package
does not need rpath for an installation into the standard location, and rpath may sometimes cause unwanted effects or
even security issues.

This package does not come with a test suite.

Install the package:

**make install**

If desired, install the documentation:

**cp -v -R sqlite-doc-3530400 -T /usr/share/doc/sqlite-3.53.4**

## 8.52.2. Contents of Sqlite

**Installed programs:**
sqlite3
**Installed libraries:**
libsqlite3.so
**Installed directories:**
/usr/share/doc/sqlite-3.53.4

---

Linux From Scratch - Version 13.1-systemd

**Short Descriptions**

**sqlite3**
is a terminal-based front-end to the SQLite library that can evaluate queries interactively and
display the results

libsqlite3.so
contains the SQLite API functions

---

Linux From Scratch - Version 13.1-systemd

# 8.53. mpdecimal-4.0.1

The mpdecimal package contains fast C/C++ libraries for correctly-rounded arbitrary precision decimal floating point
arithmetic.

**Approximate build time:**
0.1 SBU
**Required disk space:**
4.4 MB

## 8.53.1. Installation of mpdecimal

Prepare mpdecimal for compilation:

**./configure --prefix=/usr    \**
**--disable-static \**
**--docdir=/usr/share/doc/mpdecimal-4.0.1**

Compile the package:

**make**

To test the results, issue:

**make check_local**

Install the package:

**make install**

## 8.53.2. Contents of mpdecimal

**Installed libraries:**
libmpdec.so and libmpdec++.so
**Installed directory:**
/usr/share/doc/mpdecimal-4.0.1

**Short Descriptions**

libmpdec
Contains arbitrary precision decimal floating point arithmetic functions for C programs

libmpdec++
Contains arbitrary precision decimal floating point arithmetic functions for C++ programs

---

Linux From Scratch - Version 13.1-systemd

# 8.54. Python-3.14.7

The Python 3 package contains the Python development environment. It is useful for object-oriented programming,
writing scripts, prototyping large programs, and developing entire applications. Python is an interpreted computer
language.

**Approximate build time:**
2.7 SBU
**Required disk space:**
509 MB

## 8.54.1. Installation of Python 3

First, apply a patch for compatibility with OpenSSL 4:

**patch -Np1 -i ../Python-3.14.7-openssl_4-1.patch**

Prepare Python for compilation:

**./configure --prefix=/usr          \**
**--enable-shared        \**
**--with-system-expat    \**
**--enable-optimizations \**
**--without-static-libpython**

**The meaning of the configure options:**

--with-system-expat

This switch enables linking against the system version of Expat.

--enable-optimizations

This switch enables extensive, but time-consuming, optimization steps. The interpreter is built twice; tests
performed on the first build are used to improve the optimized final version.

Compile the package:

**make**

Some tests are known to occasionally hang indefinitely. So to test the results, run the test suite but set a 2-minute time
limit for each test case:

**make test TESTOPTS="--timeout 120"**

For a relatively slow system you may need to increase the time limit and 1 SBU (measured when building Binutils pass
1 with one CPU core) should be enough. Some tests are flaky, so the test suite will automatically re-run failed tests. If
a test failed but then passed when re-run, it should be considered as passed.

Two tests, test_urllib2 and test_urllibnet, are known to fail because name resolution is not configured in the
incomplete LFS environment.

Install the package:

**make install**

**We use the pip3 command to install Python 3 programs and modules for all users as root in several places in this**
book. This conflicts with the Python developers' recommendation: to install packages into a virtual environment, or
**into the home directory of a regular user (by running pip3 as this user). A multi-line warning is triggered whenever**
**pip3 is issued by the root user.**

---

Linux From Scratch - Version 13.1-systemd

**The main reason for the recommendation is to avoid conflicts with the system's package manager (dpkg, for example).**
**LFS does not have a system-wide package manager, so this is not a problem. Also, pip3 will check for a new version**
**of itself whenever it's run. Since domain name resolution is not yet configured in the LFS chroot environment, pip3**
cannot check for a new version of itself, and will produce a warning.

After we boot the LFS system and set up a network connection, a different warning will be issued, telling the user
**to update pip3 from a pre-built wheel on PyPI (whenever a new version is available). But LFS considers pip3 to**
be a part of Python 3, so it should not be updated separately. Also, an update from a pre-built wheel would deviate
**from our objective: to build a Linux system from source code. So the warning about a new version of pip3 should be**
ignored as well. If you wish, you can suppress all these warnings by running the following command, which creates
a configuration file:

**cat > /etc/pip.conf << EOF**
[global]
root-user-action = ignore
disable-pip-version-check = true
**EOF**

### Important

**In LFS and BLFS we normally build and install Python modules with the pip3 command. Please be sure that**
**the pip3 install commands in both books are run as the root user (unless it's for a Python virtual environment).**
**Running pip3 install as a non-root user may seem to work, but it will cause the installed module to be**
inaccessible by other users.

**pip3 install will not reinstall an already installed module automatically. When using the pip3 install**
command to upgrade a module (for example, from meson-0.61.3 to meson-0.62.0), insert the option --upgrade
into the command line. If it's really necessary to downgrade a module, or reinstall the same version for some
reason, insert --force-reinstall --no-deps into the command line.

If desired, install the preformatted documentation:

**install -v -dm755 /usr/share/doc/python-3.14.7/html**

**tar --strip-components=1  \**
**--no-same-owner       \**
**--no-same-permissions \**
**-C /usr/share/doc/python-3.14.7/html \**
**-xvf ../python-3.14.7-docs-html.tar.bz2**

**The meaning of the documentation install commands:**

--no-same-owner and --no-same-permissions

Ensure the installed files have the correct ownership and permissions. Without these options, tar will install the
package files with the upstream creator's values.

## 8.54.2. Contents of Python 3

**Installed programs:**
idle3, pip3, pydoc3, python3, and python3-config
**Installed library:**
libpython3.14.so and libpython3.so
**Installed directories:**
/usr/include/python3.14, /usr/lib/python3, and /usr/share/doc/python-3.14.7

**Short Descriptions**

**idle3**
is a wrapper script that opens a Python aware GUI editor. For this script to run, you must have installed
Tk before Python, so that the Tkinter Python module is built.

---

Linux From Scratch - Version 13.1-systemd

**pip3**
The package installer for Python. You can use pip to install packages from Python Package Index and
other indexes.

**pydoc3**
is the Python documentation tool

**python3**
is the interpreter for Python, an interpreted, interactive, object-oriented programming language

---

Linux From Scratch - Version 13.1-systemd