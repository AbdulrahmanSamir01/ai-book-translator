# 8.75. MarkupSafe-3.0.3

MarkupSafe is a Python module that implements an XML/HTML/XHTML Markup safe string.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
696 KB

## 8.75.1. Installation of MarkupSafe

Compile MarkupSafe with the following command:

**pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD**

This package does not come with a test suite.

Install the package:

**pip3 install --no-index --find-links dist Markupsafe**

## 8.75.2. Contents of MarkupSafe

**Installed directory:**
/usr/lib/python3.14/site-packages/MarkupSafe-3.0.3.dist-info

---

Linux From Scratch - Version 13.1-systemd

# 8.76. Jinja2-3.1.6

Jinja2 is a Python module that implements a simple pythonic template language.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
2.7 MB

## 8.76.1. Installation of Jinja2

Build the package:

**pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD**

Install the package:

**pip3 install --no-index --find-links dist Jinja2**

## 8.76.2. Contents of Jinja2

**Installed directory:**
/usr/lib/python3.14/site-packages/Jinja2-3.1.6.dist-info

---

Linux From Scratch - Version 13.1-systemd

# 8.77. Systemd-261.2

The systemd package contains programs for controlling the startup, running, and shutdown of the system.

**Approximate build time:**
1.2 SBU
**Required disk space:**
396 MB

## 8.77.1. Installation of systemd

Remove two unneeded groups, render and sgx, from the default udev rules:

**sed -e 's/GROUP="render"/GROUP="video"/' \**
**-e 's/GROUP="sgx", //'               \**
**-i rules.d/50-udev-default.rules.in**

Prepare systemd for compilation:

**mkdir -p build**
**cd       build**

**meson setup ..                \**
**--prefix=/usr           \**
**--buildtype=release     \**
**-D default-dnssec=no    \**
**-D firstboot=false      \**
**-D install-tests=false  \**
**-D ldconfig=false       \**
**-D sysusers=false       \**
**-D rpmmacrosdir=no      \**
**-D homed=disabled       \**
**-D man=disabled         \**
**-D mode=release         \**
**-D pamconfdir=no        \**
**-D dev-kvm-mode=0660    \**
**-D nobody-group=nogroup \**
**-D sysupdate=disabled   \**
**-D ukify=disabled       \**
**-D docdir=/usr/share/doc/systemd-261.2**

**The meaning of the meson options:**

--buildtype=release

This switch overrides the default buildtype (“debug”), which produces unoptimized binaries.

-D default-dnssec=no

This switch turns off the experimental DNSSEC support.

-D firstboot=false

This switch prevents installation of systemd services responsible for setting up the system for the first time. These
are not useful in LFS, because everything is done manually.

-D install-tests=false

This switch prevents installation of the compiled tests.

-D ldconfig=false

**This switch prevents installation of a systemd unit that runs ldconfig at boot; this is not useful for source**
**distributions such as LFS, and makes the boot time longer. Remove this option to enable running ldconfig at boot.**

---

Linux From Scratch - Version 13.1-systemd

-D sysusers=false

This switch prevents installation of systemd services responsible for setting up the /etc/group and /etc/passwd
files. Both files were created in the previous chapter. This daemon is not useful on an LFS system since user
accounts are manually created.

-D rpmmacrosdir=no

This switch disables installation of RPM Macros for use with systemd, because LFS does not support RPM.

-D homed=disabled

Remove a daemon which has dependencies that do not fit within the scope of LFS.

-D man=disabled

Prevent the generation of man pages to avoid extra dependencies. We will install pre-generated man pages for
systemd from a tarball.

-D mode=release

Disable some features considered experimental by upstream.

-D pamconfdir=no

Prevent the installation of a PAM configuration file not functional on LFS.

-D dev-kvm-mode=0660

The default udev rule would allow all users to access /dev/kvm. The editors consider it dangerous. This option
overrides it.

-D nobody-group=nogroup

Tell the package the group name with GID 65534 is nogroup.

-D sysupdate=disabled

**Do not install the systemd-sysupdate tool. It's designed for automatically upgrading binary distros, so it's useless**
for a basic Linux system built from source. And it will report errors on boot if it's enabled but not properly
configured.

-D ukify=disabled

**Do not install the systemd-ukify script. At runtime this script requires the pefile Python module that neither LFS**
nor BLFS provides.

Compile the package:

**ninja**

One test creates a mount point in /tmp that we cannot clean up so easily after running the test suite, and some tests need
a basic /etc/os-release file. To test the results, create this file and run the test suite in a separate mount namespace
(so the mount point is only visible for the test suite and it gets cleaned up automatically after the test suite finishes):

**echo 'NAME="Linux From Scratch"' > /etc/os-release**
**unshare -m ninja test**

Three tests are known to fail in the LFS chroot environment but pass in a full installation: core - systemd:test-

namespace, test - systemd:test-chase, and tmpfiles - systemd:test-systemd-tmpfiles. Some additional tests may
fail because they depend on various kernel configuration options. The test named test - systemd:test-copy may time
**out due to I/O congestion with a large parallel job number, but will pass if running alone with meson test test-copy.**

Install the package:

**ninja install**

---

Linux From Scratch - Version 13.1-systemd

Install the man pages:

**tar -xf ../../systemd-man-pages-261.2.tar.xz \**
**--no-same-owner --strip-components=1     \**
**-C /usr/share/man**

**Create the /etc/machine-id file needed by systemd-journald:**

**systemd-machine-id-setup**

Set up the basic target structure:

**systemctl preset-all**

## 8.77.2. Contents of systemd

**Installed programs:**
bootctl, busctl, coredumpctl, halt (symlink to systemctl), hostnamectl, init, journalctl,
kernel-install, localectl, loginctl, machinectl, mount.ddi (symlink to systemd-dissect),
networkctl, oomctl, portablectl, poweroff (symlink to systemctl), reboot (symlink to
systemctl), resolvconf (symlink to resolvectl), resolvectl, run0 (symlink to systemd-run),
runlevel (symlink to systemctl), shutdown (symlink to systemctl), systemctl, systemd-
ac-power, systemd-analyze, systemd-ask-password, systemd-cat, systemd-cgls, systemd-
cgtop, systemd-confext (symlink to systemd-sysext), systemd-creds, systemd-delta,
systemd-detect-virt, systemd-dissect, systemd-escape, systemd-hwdb, systemd-id128,
systemd-inhibit, systemd-machine-id-setup, systemd-mount, systemd-notify, systemd-
nspawn, systemd-path, systemd-pty-forward, systemd-repart, systemd-resolve (symlink
to resolvectl), systemd-run, systemd-socket-activate, systemd-stdio-bridge, systemd-
sysext, systemd-tmpfiles, systemd-tty-ask-password-agent, systemd-vpick, systemd-
umount (symlink to systemd-mount), timedatectl, udevadm, userdbctl, and varlinkctl
**Installed libraries:**
libnss_myhostname.so.2,
libnss_mymachines.so.2,
libnss_resolve.so.2,
libnss_systemd.so.2, libsystemd.so, libsystemd-shared-261.2.so (in /usr/lib/systemd),
and libudev.so
**Installed directories:**
/etc/binfmt.d, /etc/init.d, /etc/kernel, /etc/modules-load.d, /etc/sysctl.d, /etc/systemd, /
etc/tmpfiles.d, /etc/udev, /etc/xdg/systemd, /usr/include/systemd, /usr/lib/binfmt.d, /
usr/lib/credstore, /usr/lib/environment.d, /usr/lib/kernel, /usr/lib/modprobe.d, /usr/lib/
modules-load.d, /usr/lib/systemd, /usr/lib/udev, /usr/lib/sysctl.d, /usr/lib/systemd, /usr/
lib/tmpfiles.d, /usr/share/doc/systemd-261.2, /usr/share/factory, /usr/share/systemd, /var/
lib/systemd, and /var/log/journal