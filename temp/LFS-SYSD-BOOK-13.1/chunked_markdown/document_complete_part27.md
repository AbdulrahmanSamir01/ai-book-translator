# 7.5. Creating Directories

It is time to create the full directory structure in the LFS file system.

### Note

Some of the directories mentioned in this section may have already been created earlier with explicit
instructions, or when installing some packages. They are repeated below for completeness.

Create some root-level directories that are not in the limited set required in the previous chapters by issuing the following
command:

**mkdir -pv /{boot,home,mnt,opt,srv}**

---

Linux From Scratch - Version 13.1-systemd

Create the required set of subdirectories below the root-level by issuing the following commands:

**mkdir -pv /etc/{opt,sysconfig}**
**mkdir -pv /lib/firmware**
**mkdir -pv /media/{floppy,cdrom}**
**mkdir -pv /usr/{,local/}{include,src}**
**mkdir -pv /usr/lib/locale**
**mkdir -pv /usr/local/{bin,lib,sbin}**
**mkdir -pv /usr/{,local/}share/{color,dict,doc,info,locale,man}**
**mkdir -pv /usr/{,local/}share/{misc,terminfo,zoneinfo}**
**mkdir -pv /usr/{,local/}share/man/man{1..8}**
**mkdir -pv /var/{cache,local,log,mail,opt,spool}**
**mkdir -pv /var/lib/{color,misc,locate}**

**ln -sfv /run /var/run**
**ln -sfv /run/lock /var/lock**

**install -dv -m 0750 /root**
**install -dv -m 1777 /tmp /var/tmp**

Directories are, by default, created with permission mode 755, but this is not desirable everywhere. In the commands
above, two changes are made—one to the home directory of user root, and another to the directories for temporary files.

The first mode change ensures that not just anybody can enter the /root directory—just like a normal user would do
with his or her own home directory. The second mode change makes sure that any user can write to the /tmp and /

var/tmp directories, but cannot remove another user's files from them. The latter is prohibited by the so-called “sticky
bit,” the highest bit (1) in the 1777 bit mask.

## 7.5.1. FHS Compliance Note

This directory tree is based on the Filesystem Hierarchy Standard (FHS) (available at https://refspecs.linuxfoundation.
org/fhs.shtml). The FHS also specifies the optional existence of additional directories such as /usr/local/games and

/usr/share/games. In LFS, we create only the directories that are really necessary. However, feel free to create more
directories, if you wish.

### Warning

The FHS does not mandate the existence of the directory /usr/lib64, and the LFS editors have decided not
to use it. For the instructions in LFS and BLFS to work correctly, it is imperative that this directory be non-
existent. From time to time you should verify that it does not exist, because it is easy to create it inadvertently,
and this will probably break your system.

# 7.6. Creating Essential Files and Symlinks

Historically, Linux maintained a list of the mounted file systems in the file /etc/mtab. Modern kernels maintain this
list internally and expose it to the user via the /proc filesystem. To satisfy utilities that expect to find /etc/mtab, create
the following symbolic link:

**ln -sv /proc/self/mounts /etc/mtab**

Create a basic /etc/hosts file to be referenced in some test suites, and in one of Perl's configuration files as well:

**cat > /etc/hosts << EOF**
127.0.0.1  localhost $(hostname)
::1        localhost
**EOF**

---

Linux From Scratch - Version 13.1-systemd

In order for user root to be able to login and for the name “root” to be recognized, there must be relevant entries in
the /etc/passwd and /etc/group files.

Create the /etc/passwd file by running the following command:

**cat > /etc/passwd << "EOF"**
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/dev/null:/usr/bin/false
daemon:x:6:6:Daemon User:/dev/null:/usr/bin/false
messagebus:x:18:18:D-Bus Message Daemon User:/run/dbus:/usr/bin/false
systemd-journal-gateway:x:73:73:systemd Journal Gateway:/:/usr/bin/false
systemd-journal-remote:x:74:74:systemd Journal Remote:/:/usr/bin/false
systemd-journal-upload:x:75:75:systemd Journal Upload:/:/usr/bin/false
systemd-network:x:76:76:systemd Network Management:/:/usr/bin/false
systemd-resolve:x:77:77:systemd Resolver:/:/usr/bin/false
systemd-timesync:x:78:78:systemd Time Synchronization:/:/usr/bin/false
systemd-coredump:x:79:79:systemd Core Dumper:/:/usr/bin/false
uuidd:x:80:80:UUID Generation Daemon User:/dev/null:/usr/bin/false
systemd-oom:x:81:81:systemd Out Of Memory Daemon:/:/usr/bin/false
nobody:x:65534:65534:Unprivileged User:/dev/null:/usr/bin/false
**EOF**

The actual password for root will be set later.

Create the /etc/group file by running the following command:

**cat > /etc/group << "EOF"**
root:x:0:
bin:x:1:daemon
sys:x:2:
kmem:x:3:
tape:x:4:
tty:x:5:
daemon:x:6:
floppy:x:7:
disk:x:8:
lp:x:9:
dialout:x:10:
audio:x:11:
video:x:12:
utmp:x:13:
clock:x:14:
cdrom:x:15:
adm:x:16:
messagebus:x:18:
systemd-journal:x:23:
input:x:24:
mail:x:34:
kvm:x:61:
systemd-journal-gateway:x:73:
systemd-journal-remote:x:74:
systemd-journal-upload:x:75:
systemd-network:x:76:
systemd-resolve:x:77:
systemd-timesync:x:78:
systemd-coredump:x:79:
uuidd:x:80:
systemd-oom:x:81:
wheel:x:97:
users:x:999:
nogroup:x:65534:
**EOF**

---

Linux From Scratch - Version 13.1-systemd

The created groups are not part of any standard—they are groups decided on in part by the requirements of the Udev
configuration in Chapter 9, and in part by common conventions employed by a number of existing Linux distributions.
In addition, some test suites rely on specific users or groups. The Linux Standard Base (LSB, available at https://
refspecs.linuxfoundation.org/lsb.shtml) only recommends that, besides the group root with a Group ID (GID) of 0, a
group bin with a GID of 1 be present. The GID of 5 is widely used for the tty group, and the number 5 is also used in
systemd for the devpts filesystem. All other group names and GIDs can be chosen freely by the system administrator
since well-written programs do not depend on GID numbers, but rather use the group's name.

The ID 65534 is used by the kernel for NFS and separate user namespaces for unmapped users and groups (those exist
on the NFS server or the parent user namespace, but “do not exist” on the local machine or in the separate namespace).
We assign nobody and nogroup to avoid an unnamed ID. But other distros may treat this ID differently, so any portable
program should not depend on this assignment.

Some tests in Chapter 8 need a regular user. We add this user here and delete this account at the end of that chapter.

**echo "tester:x:101:101::/home/tester:/bin/bash" >> /etc/passwd**
**echo "tester:x:101:" >> /etc/group**
**install -o tester -d /home/tester**

To remove the “I have no name!” prompt, start a new shell. Since the /etc/passwd and /etc/group files have been
created, user name and group name resolution will now work:

**exec /usr/bin/bash --login**

**The login, agetty, and init programs (and others) use a number of log files to record information such as who was**
logged into the system and when. However, these programs will not write to the log files if they do not already exist.
Initialize the log files and give them proper permissions:

**touch /var/log/{btmp,lastlog,faillog,wtmp}**
**chgrp -v utmp /var/log/lastlog**
**chmod -v 664  /var/log/lastlog**
**chmod -v 600  /var/log/btmp**

The /var/log/wtmp file records all logins and logouts. The /var/log/lastlog file records when each user last logged
in. The /var/log/faillog file records failed login attempts. The /var/log/btmp file records the bad login attempts.

### Note

The /run/utmp file records the users that are currently logged in. This file is created dynamically when a user
logs into the system.

### Note

The utmp, wtmp, btmp, and lastlog files use 32-bit integers for timestamps and they'll be fundamentally broken
after year 2038. Many packages have stopped using them and other packages are going to stop using them.
It is probably best to consider them deprecated.

---

Linux From Scratch - Version 13.1-systemd