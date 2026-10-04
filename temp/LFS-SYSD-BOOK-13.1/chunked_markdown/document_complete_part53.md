**Short Descriptions**

**bootctl**
Is used to control EFI firmware boot settings on a system

**busctl**
Is used to introspect and monitor the D-Bus bus

**coredumpctl**
Is used to retrieve coredumps from the systemd journal

**halt**
**Normally invokes shutdown with the -h option, except when already**
in run-level 0, when it tells the kernel to halt the system; it notes in the
file /var/log/wtmp that the system is being brought down

**hostnamectl**
Is used to query and change the system hostname and related settings

**init**
Is the first process to be started after the kernel has initialized the
**hardware; init takes over the boot process and starts the processes**
specified by its configuration files; in this case, it starts systemd

---

Linux From Scratch - Version 13.1-systemd

**journalctl**
Is used to query the contents of the systemd journal

**kernel-install**
Is used to add and remove kernel and initramfs images to and from /
boot; in LFS, this is done manually

**localectl**
Is used to query and change the system locale and keyboard layout
settings

**loginctl**
Is used to introspect and control the state of the systemd Login Manager

**machinectl**
Is used to introspect and control the state of the systemd Virtual
Machine and Container Registration Manager

**networkctl**
Is used to introspect and configure the state of the network links
configured by systemd-networkd

**oomctl**
Controls the systemd Out Of Memory daemon

**portablectl**
Is used to attach or detach portable services from the local system

**poweroff**
Instructs the kernel to halt the system and switch off the computer (see
**halt)**

**reboot**
**Instructs the kernel to reboot the system (see halt)**

**resolvconf**
**Registers DNS server and domain configuration with systemd-**
**resolved**

**resolvectl**
Sends control commands to the network name resolution manager, or
resolves domain names, IPv4 and IPv6 addresses, DNS records, and
services

**run0**
Temporarily elevates or acquires different privileges, similar to sudo

**runlevel**
Outputs the previous and the current run-level, as noted in the last run-
level record in /run/utmp

**shutdown**
Brings the system down in a safe and secure manner, signaling all
processes and notifying all logged-in users

**systemctl**
Is used to introspect and control the state of the systemd system and
service manager

**systemd-ac-power**
Reports whether the system is connected to an external power source.

**systemd-analyze**
Is used to analyze system startup performance, as well as identify
troublesome systemd units

**systemd-ask-password**
Is used to query a system password or passphrase from the user, using
a message specified on the Linux command line

**systemd-cat**
Is used to connect the STDOUT and STDERR outputs of a process with
the systemd journal

**systemd-cgls**
Recursively shows the contents of the selected Linux control group
hierarchy in a tree

**systemd-cgtop**
Shows the top control groups of the local Linux control group hierarchy,
ordered by their CPU, memory and disk I/O loads

**systemd-creds**
Displays and processes credentials

**systemd-delta**
Is used to identify and compare configuration files in /etc that override
the defaults in /usr

---

Linux From Scratch - Version 13.1-systemd

**systemd-detect-virt**
Detects whether the system is being run in a virtual environment, and
adjusts udev accordingly

**systemd-dissect**
Is used to inspect OS disk images

**systemd-escape**
Is used to escape strings for inclusion in systemd unit names

**systemd-hwdb**
Is used to manage the hardware database (hwdb)

**systemd-id128**
Generates and prints id128 (UUID) strings

**systemd-inhibit**
Is used to execute a program with a shutdown, sleep or idle inhibitor
lock taken, preventing an action such as a system shutdown until the
process is completed

**systemd-machine-id-setup**
Is used by system installer tools to initialize the machine ID stored in /

etc/machine-id at install time with a randomly generated ID

**systemd-mount**
Is used to temporarily mount or automount disks

**systemd-notify**
Is used by daemon scripts to notify the init system of status changes

**systemd-nspawn**
Is used to run a command, or an entire OS, in a light-weight namespace
container

**systemd-path**
Is used to query system and user paths

**systemd-pty-forward**
Is used to run a command with a custom terminal background color or
title

**systemd-repart**
Is used to grow and add partitions to a partition table when systemd is
used with an OS image (e.g. a container)

**systemd-resolve**
Is used to resolve domain names, IPV4 and IPv6 addresses, DNS
resource records, and services

**systemd-run**
Is used to create and start a transient .service or a .scope unit and run
the specified command in it; this is useful for validating systemd units

**systemd-socket-activate**
Is used to listen on socket devices and launch a process upon a
successful connection to the socket

**systemd-sysext**
Activates system extension images

**systemd-tmpfiles**
Creates, deletes, and cleans up volatile and temporary files and
directories, based on the configuration file format and location specified
in tmpfiles.d directories

**systemd-umount**
Unmounts mount points

**systemd-tty-ask-password-agent**
Is used to list and/or process pending systemd password requests

**systemd-vpick**
Is used to resolve paths to a ".v/" versioned directory

**timedatectl**
Is used to query and change the system clock and its settings

**udevadm**
Is a generic udev administration tool which controls the udevd daemon,
provides info from the udev hardware database, monitors uevents, waits
for uevents to finish, tests udev configuration, and triggers uevents for
a given device

**userdbctl**
Is used to inspect users, groups, and group memberships

**varlinkctl**
Is used to interact with and invoke Varlink services

---

Linux From Scratch - Version 13.1-systemd

libsystemd
Is the main systemd utility library

libudev
Is a library to access Udev device information

---

Linux From Scratch - Version 13.1-systemd

# 8.78. D-Bus-1.16.2

D-Bus is a message bus system, a simple way for applications to talk to one another. D-Bus supplies both a system
daemon (for events such as "new hardware device added" or "printer queue changed") and a per-user-login-session
daemon (for general IPC needs among user applications). Also, the message bus is built on top of a general one-to-
one message passing framework, which can be used by any two applications to communicate directly (without going
through the message bus daemon).

**Approximate build time:**
0.1 SBU
**Required disk space:**
17 MB

## 8.78.1. Installation of D-Bus

Prepare D-Bus for compilation:

**mkdir build**
**cd    build**

**meson setup --prefix=/usr --buildtype=release --wrap-mode=nofallback ..**

**The meaning of the meson options:**

--wrap-mode=nofallback

This switch prevents meson from attempting to download a copy of the Glib package for the tests.

Compile the package:

**ninja**

To test the results, issue:

**ninja test**

Many tests are disabled because they require additional packages that are not included in LFS. Instructions for running
the comprehensive test suite can be found in the BLFS book.

Install the package:

**ninja install**

Create a symlink so that D-Bus and systemd can use the same machine-id file:

**ln -sfv /etc/machine-id /var/lib/dbus**

## 8.78.2. Contents of D-Bus

**Installed programs:**
dbus-cleanup-sockets, dbus-daemon, dbus-launch, dbus-monitor, dbus-run-session,
dbus-send, dbus-test-tool, dbus-update-activation-environment, and dbus-uuidgen
**Installed libraries:**
libdbus-1.so
**Installed directories:**
/etc/dbus-1, /usr/include/dbus-1.0, /usr/lib/dbus-1.0, /usr/share/dbus-1, /usr/share/doc/
dbus-1.16.2, and /var/lib/dbus

**Short Descriptions**

**dbus-cleanup-sockets**
is used to remove leftover sockets in a directory

**dbus-daemon**
is the D-Bus message bus daemon

---

Linux From Scratch - Version 13.1-systemd

**dbus-launch**
**starts dbus-daemon from a shell script**

**dbus-monitor**
monitors messages passing through a D-Bus message bus

**dbus-run-session**
**starts a session bus instance of dbus-daemon from a shell script**
and starts a specified program in that session

**dbus-send**
sends a message to a D-Bus message bus

**dbus-test-tool**
is a tool to help packages test D-Bus

**dbus-update-activation-environment**
updates environment variables that will be set for D-Bus session
services

**dbus-uuidgen**
Generates a universally unique ID

libdbus-1
Contains API functions used to communicate with the D-Bus
message bus

---

Linux From Scratch - Version 13.1-systemd