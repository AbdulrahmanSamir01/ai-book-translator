# for xterm
"\eOH": beginning-of-line
"\eOF": end-of-line

# for Konsole
"\e[H": beginning-of-line
"\e[F": end-of-line

# uncomment for history search mode with up/down

# "\e[A": history-search-backward

# "\e[B": history-search-forward

# End /etc/inputrc
**EOF**

# 9.9. Creating the /etc/shells File

The shells file contains a list of login shells on the system. Applications use this file to determine whether a shell is
valid. For each shell a single line should be present, consisting of the shell's path relative to the root of the directory
structure (/).

---

Linux From Scratch - Version 13.1-systemd

**For example, this file is consulted by chsh to determine whether an unprivileged user may change the login shell for**
her own account. If the command name is not listed, the user will be denied the ability to change shells.

It is a requirement for applications such as GDM which does not populate the face browser if it can't find /etc/shells,
or FTP daemons which traditionally disallow access to users with shells not included in this file.

**cat > /etc/shells << "EOF"**

# Begin /etc/shells

/bin/sh
/bin/bash

# End /etc/shells
**EOF**

# 9.10. Systemd Usage and Configuration

## 9.10.1. Basic Configuration

The /etc/systemd/system.conf file contains a set of options to control basic systemd operations. The default file has
all entries commented out with the default settings indicated. This file is where the log level may be changed as well
as some basic logging settings. See the systemd-system.conf(5) manual page for details on each configuration option.

## 9.10.2. Disabling Screen Clearing at Boot Time

The normal behavior for systemd is to clear the screen at the end of the boot sequence. If desired, this behavior may
be changed by running the following command:

**mkdir -pv /etc/systemd/system/getty@tty1.service.d**

**cat > /etc/systemd/system/getty@tty1.service.d/noclear.conf << EOF**
[Service]
TTYVTDisallocate=no
**EOF**

**The boot messages can always be reviewed by using the journalctl -b command as the root user.**

## 9.10.3. Disabling tmpfs for /tmp

By default, /tmp is created as a tmpfs. If this is not desired, it can be overridden by executing the following command:

**systemctl mask tmp.mount**

Alternatively, if a separate partition for /tmp is desired, specify that partition in a /etc/fstab entry.

## 9.10.4. Configuring Automatic File Creation and Deletion

There are several services that create or delete files or directories:

• systemd-tmpfiles-clean.service

• systemd-tmpfiles-setup-dev.service

• systemd-tmpfiles-setup.service

The system location for the configuration files is /usr/lib/tmpfiles.d/*.conf. The local configuration files are in /

etc/tmpfiles.d. Files in /etc/tmpfiles.d override files with the same name in /usr/lib/tmpfiles.d. See tmpfiles.d(5)
manual page for file format details.

---

Linux From Scratch - Version 13.1-systemd

Note that the syntax for the /usr/lib/tmpfiles.d/*.conf files can be confusing. For example, the default deletion of
files in the /tmp directory is located in /usr/lib/tmpfiles.d/tmp.conf with the line:

q /tmp 1777 root root 10d

The type field, q, indicates the creation of a subvolume with quotas which is really only applicable to btrfs filesystems.
It references type v which in turn references type d (directory). This then creates the specified directory if it is not
present and adjusts the permissions and ownership as specified. Contents of the directory will be subject to time based
cleanup if the age argument is specified.

If the default parameters are not desired, then the file should be copied to /etc/tmpfiles.d and edited as desired. For
example:

**mkdir -p /etc/tmpfiles.d**
**cp /usr/lib/tmpfiles.d/tmp.conf /etc/tmpfiles.d**

## 9.10.5. Overriding Default Services Behavior

The parameters of a unit can be overridden by creating a directory and a configuration file in /etc/systemd/system.
For example:

**mkdir -pv /etc/systemd/system/foobar.service.d**

**cat > /etc/systemd/system/foobar.service.d/foobar.conf << EOF**
[Service]
Restart=always
RestartSec=30
**EOF**

**See systemd.unit(5) manual page for more information. After creating the configuration file, run systemctl daemon-**

**reload and systemctl restart foobar to activate the changes to a service.**

## 9.10.6. Debugging the Boot Sequence

Rather than plain shell scripts used in SysVinit or BSD style init systems, systemd uses a unified format for different
**types of startup files (or units). The command systemctl is used to enable, disable, control state, and obtain status of**
unit files. Here are some examples of frequently used commands:

**• systemctl list-units -t <service> [--all]: lists loaded unit files of type service.**

**• systemctl list-units -t <target> [--all]: lists loaded unit files of type target.**

**• systemctl show -p Wants <multi-user.target>: shows all units that depend on the multi-user target. Targets are**
special unit files that are analogous to runlevels under SysVinit.

**• systemctl status <servicename.service>: shows the status of the servicename service. The .service extension can**
be omitted if there are no other unit files with the same name, such as .socket files (which create a listening socket
that provides similar functionality to inetd/xinetd).

## 9.10.7. Working with the Systemd Journal

Logging on a system booted with systemd is handled with systemd-journald (by default), rather than a typical unix
syslog daemon. You can also add a normal syslog daemon and have both operate side by side if desired. The systemd-
journald program stores journal entries in a binary format rather than a plain text log file. To assist with parsing the file,
**the command journalctl is provided. Here are some examples of frequently used commands:**

**• journalctl -r: shows all contents of the journal in reverse chronological order.**

---

Linux From Scratch - Version 13.1-systemd

**• journalctl -u UNIT: shows the journal entries associated with the specified UNIT file.**

**• journalctl -b[=ID] -r: shows the journal entries since last successful boot (or for boot ID) in reverse chronological**
order.

**• journalctl -f: provides functionality similar to tail -f (follow).**

## 9.10.8. Working with Core Dumps

Core dumps are useful to debug crashed programs, especially when a daemon process crashes. On systemd booted
**systems the core dumping is handled by systemd-coredump. It will log the core dump in the journal and store the**
**core dump itself in /var/lib/systemd/coredump. To retrieve and process core dumps, the coredumpctl tool is provided.**
Here are some examples of frequently used commands:

**• coredumpctl -r: lists all core dumps in reverse chronological order.**

**• coredumpctl -1 info: shows the information from the last core dump.**

**• coredumpctl -1 debug: loads the last core dump into GDB.**

Core dumps may use a lot of disk space. The maximum disk space used by core dumps can be limited by creating a
configuration file in /etc/systemd/coredump.conf.d. For example:

**mkdir -pv /etc/systemd/coredump.conf.d**

**cat > /etc/systemd/coredump.conf.d/maxuse.conf << EOF**
[Coredump]
MaxUse=5G
**EOF**

See the systemd-coredump(8), coredumpctl(1), and coredump.conf.d(5) manual pages for more information.

## 9.10.9. Long Running Processes

Beginning with systemd-230, all user processes are killed when a user session is ended, even if nohup is used, or the
process uses the daemon() or setsid() functions. This is a deliberate change from a historically permissive environment
**to a more restrictive one. The new behavior may cause issues if you depend on long running programs (e.g., screen**
**or tmux) to remain active after ending your user session. There are three ways to enable lingering processes to remain**
after a user session is ended.

• Enable process lingering for only selected users: Normal users have permission to enable process lingering with
**the command loginctl enable-linger for their own user. System administrators can use the same command with**
**a user argument to enable for a user. That user can then use the systemd-run command to start long running**
**processes. For example: systemd-run --scope --user /usr/bin/screen. If you enable lingering for your user, the**
user@.service will remain even after all login sessions are closed, and will automatically start at system boot. This
has the advantage of explicitly allowing and disallowing processes to run after the user session has ended, but
**breaks backwards compatibility with tools like nohup and utilities that use daemon().**

• Enable system-wide process lingering: You can set KillUserProcesses=no in /etc/systemd/logind.conf to enable
process lingering globally for all users. This has the benefit of leaving the old method available to all users at the
expense of explicit control.

• Disable at build-time: You can disable lingering by default while building systemd by adding the switch -D

**default-kill-user-processes=false to the meson command for systemd. This completely disables the ability of**
systemd to kill user processes at session end.

---

Linux From Scratch - Version 13.1-systemd