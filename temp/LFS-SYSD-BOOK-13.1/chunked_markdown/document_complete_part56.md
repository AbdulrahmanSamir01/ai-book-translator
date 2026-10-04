**swapon**
Enables devices and files for paging and swapping, and lists the devices and files currently in use

**switch_root**
Switches to another filesystem as the root of the mount tree

**taskset**
Retrieves or sets a process's CPU affinity

**uclampset**
Manipulates the utilization clamping attributes of the system or a process

**ul**
A filter for translating underscores into escape sequences indicating underlining for the terminal
in use

**umount**
Disconnects a file system from the system's file tree

**uname26**
A symbolic link to setarch

**unshare**
Runs a program with some namespaces unshared from parent

**utmpdump**
Displays the content of the given login file in a user-friendly format

**uuidd**
A daemon used by the UUID library to generate time-based UUIDs in a secure and guaranteed-
unique fashion

**uuidgen**
Creates new UUIDs. Each new UUID is a random number likely to be unique among all UUIDs
created, on the local system and on other systems, in the past and in the future, with extremely
high probability (2128 UUIDs are possible)

**uuidparse**
A utility to parse unique identifiers

**wall**
Displays the contents of a file or, by default, its standard input, on the terminals of all currently
logged in users

**wdctl**
Shows hardware watchdog status

**whereis**
Reports the location of the binary, source, and man page files for the given command

**wipefs**
Wipes a filesystem signature from a device

**x86_64**
A symbolic link to setarch

**zramctl**
A program to set up and control zram (compressed ram disk) devices

libblkid
Contains routines for device identification and token extraction

libfdisk
Contains routines for manipulating partition tables

libmount
Contains routines for block device mounting and unmounting

libsmartcols
Contains routines for aiding screen output in tabular form

libuuid
Contains routines for generating unique identifiers for objects that may be accessible beyond the
local system

---

Linux From Scratch - Version 13.1-systemd

# 8.82. E2fsprogs-1.47.4

The E2fsprogs package contains the utilities for handling the ext2 file system. It also supports the ext3 and ext4
journaling file systems.

**Approximate build time:**
2.4 SBU on a spinning disk, 0.4 SBU on an SSD
**Required disk space:**
101 MB

## 8.82.1. Installation of E2fsprogs

The E2fsprogs documentation recommends that the package be built in a subdirectory of the source tree:

**mkdir -v build**
**cd       build**

Prepare E2fsprogs for compilation:

**../configure --prefix=/usr       \**
**--sysconfdir=/etc   \**
**--enable-elf-shlibs \**
**--disable-libblkid  \**
**--disable-libuuid   \**
**--disable-uuidd     \**
**--disable-fsck**

**The meaning of the configure options:**

--enable-elf-shlibs

This creates the shared libraries which some programs in this package use.

--disable-*

**These prevent building and installing the libuuid and libblkid libraries, the uuidd daemon, and the fsck wrapper;**
util-linux installs more recent versions.

Compile the package:

**make**

To run the tests, issue:

**make check**

One test named m_assume_storage_prezeroed is known to fail. Another test named m_rootdir_acl is known to fail if
the file system used for the LFS system is not ext4.

Install the package:

**make install**

Remove useless static libraries:

**rm -fv /usr/lib/{libcom_err,libe2p,libext2fs,libss}.a**

This package installs a gzipped .info file but doesn't update the system-wide dir file. Unzip this file and then update
the system dir file using the following commands:

**gunzip -v /usr/share/info/libext2fs.info.gz**
**install-info --dir-file=/usr/share/info/dir /usr/share/info/libext2fs.info**

---

Linux From Scratch - Version 13.1-systemd

If desired, create and install some additional documentation by issuing the following commands:

**makeinfo -o      doc/com_err.info ../lib/et/com_err.texinfo**
**install -v -m644 doc/com_err.info /usr/share/info**
**install-info --dir-file=/usr/share/info/dir /usr/share/info/com_err.info**

## 8.82.2. Configuring E2fsprogs

**/etc/mke2fs.conf contains the default value of various command line options of mke2fs. You may edit the file to make**
the default values suitable for your needs. For example, some utilities (not in LFS or BLFS) cannot recognize a ext4
**file system with metadata_csum_seed feature enabled. If you need such a utility, you may remove the feature from the**
default ext4 feature list with the command:

**sed 's/metadata_csum_seed,//' -i /etc/mke2fs.conf**

Read the man page mke2fs.conf(5) for details.

## 8.82.3. Contents of E2fsprogs

**Installed programs:**
badblocks, chattr, compile_et, debugfs, dumpe2fs, e2freefrag, e2fsck, e2image, e2label,
e2mmpstatus, e2scrub, e2scrub_all, e2undo, e4crypt, e4defrag, filefrag, fsck.ext2,
fsck.ext3, fsck.ext4, logsave, lsattr, mk_cmds, mke2fs, mkfs.ext2, mkfs.ext3, mkfs.ext4,
mklost+found, resize2fs, and tune2fs
**Installed libraries:**
libcom_err.so, libe2p.so, libext2fs.so, and libss.so
**Installed directories:**
/usr/include/e2p, /usr/include/et, /usr/include/ext2fs, /usr/include/ss, /usr/lib/e2fsprogs, /
usr/share/et, and /usr/share/ss

**Short Descriptions**

**badblocks**
Searches a device (usually a disk partition) for bad blocks

**chattr**
Changes the attributes of files on ext{234} file systems

**compile_et**
An error table compiler; it converts a table of error-code names and messages into a C source file
suitable for use with the com_err library

**debugfs**
A file system debugger; it can be used to examine and change the state of ext{234} file systems

**dumpe2fs**
Prints the super block and blocks group information for the file system present on a given device

**e2freefrag**
Reports free space fragmentation information

**e2fsck**
Is used to check and optionally repair ext{234} file systems

**e2image**
Is used to save critical ext{234} file system data to a file

**e2label**
Displays or changes the file system label on the ext{234} file system on a given device

**e2mmpstatus**
Checks MMP (Multiple Mount Protection) status of an ext4 file system

**e2scrub**
Checks the contents of a mounted ext{234} file system

**e2scrub_all**
Checks all mounted ext{234} file systems for errors

**e2undo**
Replays the undo log for an ext{234} file system found on a device. [This can be used to undo a
failed operation by an E2fsprogs program.]

**e4crypt**
Ext4 file system encryption utility

**e4defrag**
Online defragmenter for ext4 file systems

---

Linux From Scratch - Version 13.1-systemd

**filefrag**
Reports on how badly fragmented a particular file might be

**fsck.ext2**
**By default checks ext2 file systems and is a hard link to e2fsck**

**fsck.ext3**
**By default checks ext3 file systems and is a hard link to e2fsck**

**fsck.ext4**
**By default checks ext4 file systems and is a hard link to e2fsck**

**logsave**
Saves the output of a command in a log file

**lsattr**
Lists the attributes of files on a second extended file system

**mk_cmds**
Converts a table of command names and help messages into a C source file suitable for use with
the libss subsystem library

**mke2fs**
Creates an ext{234} file system on the given device

**mkfs.ext2**
**By default creates ext2 file systems and is a hard link to mke2fs**

**mkfs.ext3**
**By default creates ext3 file systems and is a hard link to mke2fs**

**mkfs.ext4**
**By default creates ext4 file systems and is a hard link to mke2fs**

**mklost+found**
Creates a lost+found directory on an ext{234} file system; it pre-allocates disk blocks to this
**directory to lighten the task of e2fsck**

**resize2fs**
Can be used to enlarge or shrink ext{234} file systems

**tune2fs**
Adjusts tunable file system parameters on ext{234} file systems

libcom_err
The common error display routine

libe2p
**Used by dumpe2fs, chattr, and lsattr**

libext2fs
Contains routines to enable user-level programs to manipulate ext{234} file systems

libss
**Used by debugfs**

---

Linux From Scratch - Version 13.1-systemd