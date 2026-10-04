# 8.55. Flit-Core-4.0.2

Flit-core is the distribution-building parts of Flit (a packaging tool for simple Python modules).

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
1.3 MB

## 8.55.1. Installation of Flit-Core

Build the package:

**pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD**

Install the package:

**pip3 install --no-index --find-links dist flit_core**

**The meaning of the pip3 configuration options and commands:**

**wheel**

This command builds the wheel archive for this package.

-w dist

Instructs pip to put the created wheel into the dist directory.

--no-cache-dir

Prevents pip from copying the created wheel into the /root/.cache/pip directory.

**install**

This command installs the package.

--no-build-isolation, --no-deps, and --no-index

These options prevent fetching files from the online package repository (PyPI). If packages are installed in the
correct order, pip won't need to fetch any files in the first place; these options add some safety in case of user error.

--find-links dist

Instructs pip to search for wheel archives in the dist directory.

## 8.55.2. Contents of Flit-Core

**Installed directory:**
/usr/lib/python3.14/site-packages/flit_core
and
/usr/lib/python3.14/site-packages/
flit_core-4.0.2.dist-info

---

Linux From Scratch - Version 13.1-systemd

# 8.56. Packaging-26.3

The packaging module is a Python library that provides utilities that implement the interoperability specifications which
have clearly one correct behaviour (PEP440) or benefit greatly from having a single shared implementation (PEP425).
This includes utilities for version handling, specifiers, markers, tags, and requirements.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
3.0 MB

## 8.56.1. Installation of Packaging

Compile packaging with the following command:

**pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD**

Install packaging with the following command:

**pip3 install --no-index --find-links dist packaging**

## 8.56.2. Contents of Packaging

**Installed directories:**
/usr/lib/python3.14/site-packages/packaging
and
/usr/lib/python3.14/site-packages/
packaging-26.3.dist-info

---

Linux From Scratch - Version 13.1-systemd

# 8.57. Wheel-0.48.0

Wheel is a Python library that is the reference implementation of the Python wheel packaging standard.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
768 KB

## 8.57.1. Installation of Wheel

Compile Wheel with the following command:

**pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD**

Install Wheel with the following command:

**pip3 install --no-index --find-links dist wheel**

## 8.57.2. Contents of Wheel

**Installed program:**
wheel
**Installed directories:**
/usr/lib/python3.14/site-packages/wheel
and
/usr/lib/python3.14/site-packages/
wheel-0.48.0.dist-info

**Short Descriptions**

**wheel**
is a utility to unpack, pack, or convert wheel archives

---

Linux From Scratch - Version 13.1-systemd

# 8.58. Setuptools-84.0.0

Setuptools is a tool used to download, build, install, upgrade, and uninstall Python packages.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
19 MB

## 8.58.1. Installation of Setuptools

Build the package:

**pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD**

Install the package:

**pip3 install --no-index --find-links dist setuptools**

## 8.58.2. Contents of Setuptools

**Installed directory:**
/usr/lib/python3.14/site-packages/_distutils_hack,
/usr/lib/python3.14/site-packages/
pkg_resources, /usr/lib/python3.14/site-packages/setuptools, and /usr/lib/python3.14/
site-packages/setuptools-84.0.0.dist-info

---

Linux From Scratch - Version 13.1-systemd

# 8.59. Meson-1.12.0

Meson is an open source build system designed to be both extremely fast and as user friendly as possible.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
50 MB

## 8.59.1. Installation of Meson

Compile Meson with the following command:

**pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD**

The test suite requires some packages outside the scope of LFS.

Install the package:

**pip3 install --no-index --find-links dist meson**
**install -vDm644 data/shell-completions/bash/meson /usr/share/bash-completion/completions/meson**
**install -vDm644 data/shell-completions/zsh/_meson /usr/share/zsh/site-functions/_meson**

**The meaning of the install parameters:**

-w dist

Puts the created wheels into the dist directory.

--find-links dist

Installs wheels from the dist directory.

## 8.59.2. Contents of Meson

**Installed programs:**
meson
**Installed directory:**
/usr/lib/python3.14/site-packages/meson-1.12.0.dist-info and /usr/lib/python3.14/site-
packages/mesonbuild

**Short Descriptions**

**meson**
A high productivity build system

---

Linux From Scratch - Version 13.1-systemd

# 8.60. Kmod-34.2

The Kmod package contains libraries and utilities for loading kernel modules

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
6.8 MB

## 8.60.1. Installation of Kmod

Prepare Kmod for compilation:

**mkdir -p build**
**cd       build**

**meson setup --prefix=/usr ..    \**
**--buildtype=release \**
**-D manpages=false**

**The meaning of the configure options:**

-D manpages=false

This option disables generating the man pages which requires an external program.

Compile the package:

**ninja**

The test suite of this package requires raw kernel headers (not the “sanitized” kernel headers installed earlier), which
are beyond the scope of LFS.

Now install the package:

**ninja install**

## 8.60.2. Contents of Kmod

**Installed programs:**
depmod (link to kmod), insmod (link to kmod), kmod, lsmod (link to kmod), modinfo
(link to kmod), modprobe (link to kmod), and rmmod (link to kmod)
**Installed library:**
libkmod.so

**Short Descriptions**

**depmod**
Creates a dependency file based on the symbols it finds in the existing set of modules; this dependency
**file is used by modprobe to automatically load the required modules**

**insmod**
Installs a loadable module in the running kernel

**kmod**
Loads and unloads kernel modules

**lsmod**
Lists currently loaded modules

**modinfo**
Examines an object file associated with a kernel module and displays any information that it can glean

**modprobe**
**Uses a dependency file, created by depmod, to automatically load relevant modules**

**rmmod**
Unloads modules from the running kernel

libkmod
This library is used by other programs to load and unload kernel modules

---

Linux From Scratch - Version 13.1-systemd

# 8.61. Coreutils-9.11

The Coreutils package contains the basic utility programs needed by every operating system.

**Approximate build time:**
1.2 SBU
**Required disk space:**
194 MB

## 8.61.1. Installation of Coreutils

POSIX requires that programs from Coreutils recognize character boundaries correctly even in multibyte locales. The
following patch fixes this non-compliance and other internationalization-related bugs.

**patch -Np1 -i ../coreutils-9.11-i18n-1.patch**

### Note

Many bugs have been found in this patch. When reporting new bugs to the Coreutils maintainers, please check
first to see if those bugs are reproducible without this patch.

Now prepare Coreutils for compilation:

**autoreconf -fv**
**automake -af**
**FORCE_UNSAFE_CONFIGURE=1 ./configure \**
**--prefix=/usr**

**The meaning of the commands and configure options:**

**autoreconf -fv**

The patch for internationalization has modified the build system, so the configuration files must be regenerated.
Normally we would use the -i option to update the standard auxiliary files, but for this package it does not work
because configure.ac specified an old gettext version.

**automake -af**

**The automake auxiliary files were not updated by autoreconf due to the missing -i option. This command updates**
them to prevent a build failure.

FORCE_UNSAFE_CONFIGURE=1

This environment variable allows the package to be built by the root user.

Compile the package:

**make**

Skip down to “Install the package” if not running the test suite.

Now the test suite is ready to be run. First, run the tests that are meant to be run as user root:

**make NON_ROOT_USERNAME=tester check-root**

We're going to run the remainder of the tests as the tester user. Certain tests require that the user be a member of more
than one group. So that these tests are not skipped, add a temporary group and make the user tester a part of it:

**groupadd -g 102 dummy -U tester**

Fix some of the permissions so that the non-root user can compile and run the tests:

**chown -R tester .**

---

Linux From Scratch - Version 13.1-systemd

Now run the tests (using /dev/null for the standard input, or two tests may be broken if building LFS in a graphical
terminal or a session in SSH or GNU Screen because the standard input is connected to a PTY from host distro, and
the device node for such a PTY cannot be accessed from the LFS chroot environment):

**su tester -c "PATH=$PATH make -k RUN_EXPENSIVE_TESTS=yes check" \**
**< /dev/null**

Remove the temporary group:

**groupdel dummy**

Install the package:

**make install**

Move programs to the locations specified by the FHS:

**mv -v /usr/bin/chroot /usr/sbin**
**mv -v /usr/share/man/man1/chroot.1 /usr/share/man/man8/chroot.8**
**sed -i 's/"1"/"8"/' /usr/share/man/man8/chroot.8**