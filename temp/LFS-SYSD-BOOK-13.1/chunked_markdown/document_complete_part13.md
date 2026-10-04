## 2.4.2. An Example Disk Layout

Below is an example layout for an empty disk drive.

Number  Start (sector)    End (sector)        Size   Code  Name
1            2048           22527       10.0 MiB  EF00  EFI system partition
2           22528           24575     1024.0 KiB  EF02  BIOS boot partition
3           24576         1048575      500.0 MiB  8300  /boot
4         1048576         5242879        2.0 GiB  8200  swap
5         5242880        89128959       40.0 GiB  8300  lfs13.0+
6        89128960       173015039       40.0 GiB  8300  /home

The above example makes a few assumptions:

• The partition table is a GUID Partition Table (GPT).

• Both EFI and BIOS Boot partitions are present, although only one will be used. Which is used depends on
the system firmware. If the system is old, it will not have UEFI capabilities at all. Some later systems can
disable UEFI through the firmware setup by disabling "Secure Boot" and enabling "Legacy Support" or
"CSM" (Compatibility Support Module). If you know in advance which mode you will use, the other partition can
be omitted.

• The EFI partition must be formatted as VFAT.

• The BIOS partition is not formatted.

• The swap partition must be initialized.

• The /boot partition can be formatted as ext2 since it is rarely written (and then only by root) and does not need a
journal.

• The recommendation for all other partitions is to use ext4 formatting.

• Another partition can be added for installing the "host" system for building LFS. A minimal sized partition, 10
GiB, should be sufficient. If you are building the system using a LiveCD, a host partition may not be required.

# 2.5. Creating a File System on the Partition

A partition is just a range of sectors on a disk drive, delimited by boundaries set in a partition table. Before the operating
system can use a partition to store any files, the partition must be formatted to contain a file system, typically consisting
of a label, directory blocks, data blocks, and an indexing scheme to locate a particular file on demand. The file system

---

Linux From Scratch - Version 13.1-systemd

also helps the OS keep track of free space on the partition, reserve the needed sectors when a new file is created or an
existing file is extended, and recycle the free data segments created when files are deleted. It may also provide support
for data redundancy, and for error recovery.

LFS can use any file system recognized by the Linux kernel, but the most common types are ext3 and ext4. The choice
of the right file system can be complex; it depends on the characteristics of the files and the size of the partition. For
example:

ext2

is suitable for small partitions that are updated infrequently such as /boot.
ext3

is an upgrade to ext2 that includes a journal to help recover the partition's status in the case of an unclean shutdown.
It is commonly used as a general purpose file system.
ext4

is the latest version of the ext family of file systems. It provides several new capabilities including nano-second
timestamps, creation and use of very large files (up to 16 TB), and speed improvements.

Other file systems, including FAT32, NTFS, JFS, and XFS are useful for specialized purposes. More information about
these file systems, and many others, can be found at https://en.wikipedia.org/wiki/Comparison_of_file_systems.

LFS assumes that the root file system (/) is of type ext4. To create an ext4 file system on the LFS partition, issue the
following command:

**mkfs -v -t ext4 /dev/<xxx>**

Replace <xxx> with the name of the LFS partition.

If you are using an existing swap partition, there is no need to format it. If a new swap partition was created, it will need
to be initialized with this command:

**mkswap /dev/<yyy>**

Replace <yyy> with the name of the swap partition.

If you have created an EFI System Partition, you have a few options. Motherboards when booting with UEFI look for
EFI applications in partitions formatted with a FAT variant (FAT12, FAT16, FAT32, VFAT, etc). Usually, FAT32 or
VFAT are the recommended options.

If you have chosen FAT32, format the ESP with the following command:

**mkfs.fat -F 32 /dev/<yyy>**

On the other hand, if you have chosen VFAT, you can run the following instead:

**mkfs.vfat /dev/<zzz>**

Replace <zzz> with the name of the EFI System Partition.

# 2.6. Setting the $LFS Variable and the Umask

Throughout this book, the environment variable LFS will be used several times. You should ensure that this variable
is always defined throughout the LFS build process. It should be set to the name of the directory where you will be
building your LFS system - we will use /mnt/lfs as an example, but you may choose any directory name you want. If
you are building LFS on a separate partition, this directory will be the mount point for the partition. Choose a directory
location and set the variable with the following command:

**export LFS=/mnt/lfs**

---

Linux From Scratch - Version 13.1-systemd

**Having this variable set is beneficial in that commands such as mkdir -v $LFS/tools can be typed literally. The shell**
will automatically replace “$LFS” with “/mnt/lfs” (or whatever value the variable was set to) when it processes the
command line.

Now set the file mode creation mask (umask) to 022 in case the host distro uses a different default:

**umask 022**

Setting the umask to 022 ensures that newly created files and directories are only writable by their owner, but are
readable and searchable (only for directories) by anyone (assuming default modes are used by the open(2) system call,
new files will end up with permission mode 644 and directories with mode 755). An overly-permissive default can
leave security holes in the LFS system, and an overly-restrictive default can cause strange issues building or using the
LFS system.

### Caution

Do not forget to check that LFS is set and the umask is set to 022 whenever you leave and reenter the current
**working environment (such as when doing a su to root or another user). Check that the LFS variable is set**
up properly with:

**echo $LFS**

Make sure the output shows the path to your LFS system's build location, which is /mnt/lfs if the provided
example was followed.

Check that the umask is set up properly with:

**umask**

The output may be 0022 or 022 (the number of leading zeros depends on the host distro).

If any output of these two commands is incorrect, use the command given earlier on this page to set $LFS to
the correct directory name and set umask to 022.

### Note

One way to ensure that the LFS variable and the umask are always set properly is to edit the .bash_profile file
**in both your personal home directory and in /root/.bash_profile and enter the export and umask commands**
above. In addition, the shell specified in the /etc/passwd file for all users that need the LFS variable must be
bash to ensure that the .bash_profile file is incorporated as a part of the login process.

Another consideration is the method that is used to log into the host system. If logging in through a graphical
display manager, the user's .bash_profile is not normally used when a virtual terminal is started. In this case,
add the commands to the .bashrc file for the user and root. In addition, some distributions use an "if" test,
and do not run the remaining .bashrc instructions for a non-interactive bash invocation. Be sure to place the
commands ahead of the test for non-interactive use.

# 2.7. Mounting the New Partition

Now that a file system has been created, the partition must be mounted so the host system can access it. This book
assumes that the file system is mounted at the directory specified by the LFS environment variable described in the
previous section.

---

Linux From Scratch - Version 13.1-systemd

Strictly speaking, one cannot “mount a partition.” One mounts the file system embedded in that partition. But since
a single partition can't contain more than one file system, people often speak of the partition and the associated file
system as if they were one and the same.

Create the mount point and mount the LFS file system with these commands:

**mkdir -pv $LFS**
**mount -v -t ext4 /dev/<xxx> $LFS**

Replace <xxx> with the name of the LFS partition.

If you are using multiple partitions for LFS (e.g., one for / and another for /home), mount them like this:

**mkdir -pv $LFS**
**mount -v -t ext4 /dev/<xxx> $LFS**
**mkdir -v $LFS/home**
**mount -v -t ext4 /dev/<yyy> $LFS/home**

Replace <xxx> and <yyy> with the appropriate partition names.

Set the owner and permission mode of the $LFS directory (i.e. the root directory in the newly created file system for the
**LFS system) to root and 755 in case the host distro has been configured to use a different default for mkfs:**

**chown root:root $LFS**
**chmod 755 $LFS**

Ensure that this new partition is not mounted with permissions that are too restrictive (such as the nosuid or nodev
**options). Run the mount command without any parameters to see what options are set for the mounted LFS partition.**
If nosuid and/or nodev are set, the partition must be remounted.

If you have created and mounted more partitions for the LFS system than the one mounted at $LFS, now you should fix
up their ownership and permission mode and check the mount options for them as well.

### Warning

The above instructions assume that you will not restart your computer throughout the LFS process. If you shut
down your system, you will either need to remount the LFS partition each time you restart the build process,
or modify the host system's /etc/fstab file to automatically remount it when you reboot. For example, you
might add this line to your /etc/fstab file:

/dev/<xxx>  /mnt/lfs ext4   defaults      1     1

If you use additional optional partitions, be sure to add them also.

**If you are using a swap partition, ensure that it is enabled using the swapon command:**

**/sbin/swapon -v /dev/<zzz>**

Replace <zzz> with the name of the swap partition.

Now that the new LFS partition is open for business, it's time to download the packages.

---

Linux From Scratch - Version 13.1-systemd