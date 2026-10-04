# 2.3. Building LFS in Stages

LFS is designed to be built in one session. That is, the instructions assume that the system will not be shut down during
the process. This does not mean that the system has to be built in one sitting. The issue is that certain procedures must
be repeated after a reboot when resuming LFS at different points.

## 2.3.1. Chapters 1–4

These chapters run commands on the host system. When restarting, be certain of one thing:

• Procedures performed as the root user after Section 2.4 must have the LFS environment variable set FOR THE
ROOT USER.

## 2.3.2. Chapters 5–6

• The /mnt/lfs partition must be mounted.
**• These two chapters must be done as user lfs. A su - lfs command must be issued before performing any task in**
these chapters. If you don't do that, you are at risk of installing packages to the host, and potentially rendering it
unusable.
• The procedures in General Compilation Instructions are critical. If there is any doubt a package has been installed
correctly, ensure the previously expanded tarball has been removed, then re-extract the package, and complete all
the instructions in that section.

## 2.3.3. Chapters 7–10

• The /mnt/lfs partition must be mounted.
• A few operations, from “Preparing Virtual Kernel File Systems” to “Entering the Chroot Environment,” must be
done as the root user, with the LFS environment variable set for the root user.
• When entering chroot, the LFS environment variable must be set for root. The LFS variable is not used after the
chroot environment has been entered.
• The virtual file systems must be mounted. This can be done before or after entering chroot by changing to a
host virtual terminal and, as root, running the commands in Section 7.3.1, “Mounting and Populating /dev” and
Section 7.3.2, “Mounting Virtual Kernel File Systems.”

---

Linux From Scratch - Version 13.1-systemd

# 2.4. Creating a New Partition

Like most other operating systems, LFS is usually installed on a dedicated partition. The recommended approach to
building an LFS system is to use an available empty partition or, if you have enough unpartitioned space, to create one.

A minimal system requires a partition of around 10 gigabytes (GB). This is enough to store all the source tarballs and
compile the packages. However, if the LFS system is intended to be the primary Linux system, additional software will
probably be installed which will require additional space. A 30 GB partition is a reasonable size to provide for growth.
The LFS system itself will not take up this much room. A large portion of this requirement is to provide sufficient free
temporary storage as well as for adding additional capabilities after LFS is complete. Additionally, compiling packages
can require a lot of disk space which will be reclaimed after the package is installed.

Because there is not always enough Random Access Memory (RAM) available for compilation processes, it is a good
idea to use a small disk partition as swap space. This is used by the kernel to store seldom-used data and leave more
memory available for active processes. The swap partition for an LFS system can be the same as the one used by the
host system, in which case it is not necessary to create another one.

**Start a disk partitioning program such as cfdisk or fdisk with a command line option naming the hard disk on which**
the new partition will be created—for example /dev/sda for the primary disk drive. Create a Linux native partition and
a swap partition, if needed. Please refer to cfdisk(8) or fdisk(8) if you do not yet know how to use the programs.

### Note

For experienced users, other partitioning schemes are possible. The new LFS system can be on a software
RAID array or an LVM logical volume. However, some of these options require an initramfs, which is an
advanced topic. These partitioning methodologies are not recommended for first time LFS users.

Remember the designation of the new partition (e.g., sda5). This book will refer to this as the LFS partition. Also
remember the designation of the swap partition. These names will be needed later for the /etc/fstab file.

## 2.4.1. Other Partition Issues

Requests for advice on system partitioning are often posted on the LFS mailing lists. This is a highly subjective topic.
The default for most distributions is to use the entire drive with the exception of one small swap partition. This is not
optimal for LFS for several reasons. It reduces flexibility, makes sharing of data across multiple distributions or LFS
builds more difficult, makes backups more time consuming, and can waste disk space through inefficient allocation
of file system structures.

**2.4.1.1. The Root Partition**

A root LFS partition (not to be confused with the /root directory) of twenty gigabytes is a good compromise for most
systems. It provides enough space to build LFS and most of BLFS, but is small enough so that multiple partitions can
be easily created for experimentation.

**2.4.1.2. The Swap Partition**

Most distributions automatically create a swap partition. Generally the recommended size of the swap partition is about
twice the amount of physical RAM, however this is rarely needed. If disk space is limited, hold the swap partition to
two gigabytes and monitor the amount of disk swapping.

If you want to use the hibernation feature (suspend-to-disk) of Linux, it writes out the contents of RAM to the swap
partition before turning off the machine. In this case the size of the swap partition should be at least as large as the
system's installed RAM.

---

Linux From Scratch - Version 13.1-systemd

Swapping is never good. For mechanical hard drives you can generally tell if a system is swapping by just listening to
disk activity and observing how the system reacts to commands. With an SSD you will not be able to hear swapping,
**but you can tell how much swap space is being used by running the top or free programs. Use of an SSD for a swap**
partition should be avoided if possible. The first reaction to swapping should be to check for an unreasonable command
such as trying to edit a five gigabyte file. If swapping becomes a normal occurrence, the best solution is to purchase
more RAM for your system.

**2.4.1.3. The Grub BIOS Partition**

If the boot disk has been partitioned with a GUID Partition Table (GPT), then a small, typically 1 MB, partition must
be created if the system is being booted with BIOS and it does not already exist. This partition is not formatted, but
must be available for GRUB to use during installation of the boot loader. This partition will normally be labeled 'BIOS
**Boot' if using fdisk or have a code of EF02 if using the gdisk command.**

If the boot disk is partitioned with an MBR Partition Table, or DOS disklabel, then this partition is not needed as space
already exists before the first partition that Grub can use.

### Note

The Grub BIOS partition must be on the drive that the BIOS uses to boot the system. This is not necessarily
the drive that holds the LFS root partition. The disks on a system may use different partition table types. The
necessity of the Grub BIOS partition depends only on the partition table type of the boot disk.

**2.4.1.4. The EFI System Partition**

This partition, also known as the ESP, is needed when booting the system with UEFI. It stores the EFI application that
is ran during bootup. The boot drive can be partitioned with MBR Partition Table, or DOS, but compatibility issues
will tend to arise as a result. Therefore, it is always a good idea in this case to partition the boot drive with a GUID
Partition Table (GPT). If you're only booting LFS from the partition, 20 MB or lower can suffice. The partition should
be bigger than the EFI image size because GRUB dumps a lot of data to the partition before creating the EFI image. To
be safe, 128 MB to 256 MB is recommended but can be dropped much lower with some experimentation. The partition
**label should be 'EFI System' if using fdisk.**

For Grub, the EFI System Partition should be located at /boot/efi.

A lot of UEFI systems have a Compatibility Support Module (CSM) or Legacy Boot option, allowing to boot with
BIOS. It could be a good idea to create a Grub BIOS partition if your system supports CSM in case UEFI booting
does not work as expected.

**2.4.1.5. Convenience Partitions**

There are several other partitions that are not required, but should be considered when designing a disk layout. The
following list is not comprehensive, but is meant as a guide.

• /boot – Highly recommended. Use this partition to store kernels and other booting information. To minimize
potential boot problems with larger disks, make this the first physical partition on your first disk drive. A partition
size of 200 megabytes is adequate.
• /home – Highly recommended. Share your home directory and user customization across multiple distributions or
LFS builds. The size is generally fairly large and depends on available disk space.
• /usr – In LFS, /bin, /lib, and /sbin are symlinks to their counterparts in /usr. So /usr contains all the binaries
needed for the system to run. For LFS a separate partition for /usr is normally not needed. If you create it anyway,
you should make a partition large enough to fit all the programs and libraries in the system. The root partition

---

Linux From Scratch - Version 13.1-systemd

can be very small (maybe just one gigabyte) in this configuration, so it's suitable for a thin client or diskless
workstation (where /usr is mounted from a remote server). However, you should be aware that an initramfs (not
covered by LFS) will be needed to boot a system with a separate /usr partition.

• /opt – This directory is most useful for BLFS, where multiple large packages like KDE or Texlive can be installed
without embedding the files in the /usr hierarchy. If used, 5 to 10 gigabytes is generally adequate.

• /tmp – By default, systemd mounts a tmpfs here. If you want to override that behavior, follow Section 9.10.3,
“Disabling tmpfs for /tmp” when configuring the LFS system.

• /usr/src – This partition is very useful for providing a location to store BLFS source files and share them across
LFS builds. It can also be used as a location for building BLFS packages. A reasonably large partition of 30-50
gigabytes provides plenty of room.

Any separate partition that you want automatically mounted when the system starts must be specified in the /etc/fstab
file. Details about how to specify partitions will be discussed in Section 10.2, “Creating the /etc/fstab File”.