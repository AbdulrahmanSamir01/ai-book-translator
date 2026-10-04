### Caution

If you've decided to use a separate /boot partition for the LFS system (maybe sharing a /boot partition with
the host distro), the files copied below should go there. The easiest way to do that is to create the entry for /

boot in /etc/fstab first (read the previous section for details), then issue the following command as the root
user in the chroot environment:

**mount /boot**

**The path to the device node is omitted in the command because mount can read it from /etc/fstab.**

The path to the kernel image may vary depending on the platform being used. The filename below can be changed to
suit your taste, but the stem of the filename should be vmlinuz to be compatible with the automatic setup of the boot
process described in the next section. The following command assumes an x86 architecture:

**cp -iv arch/x86/boot/bzImage /boot/vmlinuz-7.1.8-lfs-13.1-systemd**

System.map is a symbol file for the kernel. It maps the function entry points of every function in the kernel API, as well
as the addresses of the kernel data structures for the running kernel. It is used as a resource when investigating kernel
problems. Issue the following command to install the map file:

**cp -iv System.map /boot/System.map-7.1.8**

**The kernel configuration file .config produced by the make menuconfig step above contains all the configuration**
selections for the kernel that was just compiled. It is a good idea to keep this file for future reference:

**cp -iv .config /boot/config-7.1.8**

---

Linux From Scratch - Version 13.1-systemd

Install the documentation for the Linux kernel:

**cp -r Documentation -T /usr/share/doc/linux-7.1.8**

It is important to note that the files in the kernel source directory are not owned by root. Whenever a package is unpacked
as user root (like we did inside chroot), the files have the user and group IDs of whatever they were on the packager's
computer. This is usually not a problem for any other package to be installed because the source tree is removed after
the installation. However, the Linux source tree is often retained for a long time. Because of this, there is a chance
that whatever user ID the packager used will be assigned to somebody on the machine. That person would then have
write access to the kernel source.

### Note

In many cases, the configuration of the kernel will need to be updated for packages that will be installed later
in BLFS. Unlike other packages, it is not necessary to remove the kernel source tree after the newly built
kernel is installed.

**If the kernel source tree is going to be retained, run chown -R 0:0 on the linux-7.1.8 directory to ensure**
all files are owned by user root.

If you are updating the configuration and rebuilding the kernel from a retained kernel source tree, normally
**you should not run the make mrproper command. The command would purge the .config file and all the .**

o files from the previous build. Despite it's easy to restore .config from the copy in /boot, purging all the .o
files is still a waste: for a simple configuration change, often only a few .o files need to be (re)built and the
kernel build system will correctly skip other .o files if they are not purged.

**On the other hand, if you've upgraded GCC, you should run make clean to purge all the .o files from the**
previous build, or the new build may fail.

### Warning

Some kernel documentation recommends creating a symlink from /usr/src/linux pointing to the kernel
source directory. This is specific to kernels prior to the 2.6 series and must not be created on an LFS system
as it can cause problems for packages you may wish to build once your base LFS system is complete.

## 10.3.2. Contents of Linux

**Installed files:**
config-7.1.8, vmlinuz-7.1.8-lfs-13.1-systemd, and System.map-7.1.8
**Installed directories:**
/lib/modules, /usr/share/doc/linux-7.1.8

**Short Descriptions**

config-7.1.8
Contains all the configuration selections for the kernel

vmlinuz-7.1.8-lfs-13.1-systemd
The engine of the Linux system. When turning on the computer, the
kernel is the first part of the operating system that gets loaded. It detects
and initializes all components of the computer's hardware, then makes
these components available as a tree of files to the software and turns
a single CPU into a multitasking machine capable of running scores of
programs seemingly at the same time

System.map-7.1.8
A list of addresses and symbols; it maps the entry points and addresses
of all the functions and data structures in the kernel

---

Linux From Scratch - Version 13.1-systemd

# 10.4. Using GRUB to Set Up the Boot Process

## 10.4.1. Introduction

### Warning

Configuring GRUB incorrectly can render your system inoperable without an alternate boot device such as a
CD-ROM or bootable USB drive. This section is not required to boot your LFS system. You may just want
to modify your current boot loader, e.g. Grub-Legacy or GRUB2.

Ensure that an emergency boot disk is ready to “rescue” the computer if the computer becomes unusable (un-bootable).
If you do not already have a boot device, you can create one. In order for the procedure below to work, you need to
**jump ahead to BLFS and install xorriso from the  libisoburn package.**

**cd /tmp**
**grub-mkrescue --output=grub-img.iso**
**xorriso -as cdrecord -v dev=/dev/cdrw blank=as_needed grub-img.iso**

## 10.4.2. Turn off Secure Boot

LFS does not have the essential packages to support Secure Boot. To set up the boot process following the instructions
in this section, Secure Boot must be turned off from the configuration interface of the firmware. Read the documentation
provided by the manufacturer of your system to find out how to turn off Secure Boot support.

## 10.4.3. GRUB Naming Conventions

GRUB uses its own naming structure for drives and partitions in the form of (hdn,m), where n is the hard drive number
and m is the partition number. The hard drive numbers start from zero, but the partition numbers start from one for
normal partitions (from five for extended partitions). Note that this is different from earlier versions where both numbers
started from zero. For example, partition sda1 is (hd0,1) to GRUB and sdb3 is (hd1,3). In contrast to Linux, GRUB
does not consider CD-ROM drives to be hard drives. For example, if using a CD on hdb and a second hard drive on

hdc, that second hard drive would still be (hd1).

## 10.4.4. Setting Up the Configuration

If booting the system via BIOS, GRUB works by writing a stub to the first sector (named the Master Boot Record, or
MBR) of the hard disk. This area is not part of any file system. The BIOS loads and executes the content of MBR, then
the stub loads the main GRUB image from the BIOS Boot Partition. The GRUB image is stored as raw data instead
of a file (there must be no file system on the BIOS Boot Partition), so the stub doesn't need to support any file system
and it can be made small enough to fit in the MBR.

If booting the system via UEFI, GRUB works by storing the main GRUB image as a PE-COFF executable file at a
standard location in the EFI System Partition: EFI/BOOT/BOOTX64.EFI (or EFI/BOOT/BOOTIA32.EFI for i386-efi). The
UEFI firmware loads it from the standard location and executes it, launching GRUB.

Many GRUB functions (including booting the Linux kernel) are not included in the main GRUB image. Instead, they
are stored in a file system as GRUB modules. That file system is usually mounted in a way that the GRUB modules can
**be accessed in /boot/grub on most Linux distributions. To avoid the chicken-and-egg problem, grub-install embeds**
the modules necessary to access this file system into the main GRUB image, so it can find and load other modules.

The location of the boot partition is a choice of the user that affects the configuration. One recommendation is to have
a separate small (suggested size is 200 MB) partition just for boot information. In doing so, not just LFS, but any Linux
distribution, can access the same boot files, and in turn any booted system. If you choose to do this, you will need to

---

Linux From Scratch - Version 13.1-systemd

mount the separate partition, move all files in the current /boot directory (e.g. the Linux kernel you just built in the
previous section) to the new partition. You will then need to unmount the partition and remount it as /boot. If you do
this, be sure to update /etc/fstab.

### Note

If the host distro utilizes a separate partition for /boot and you want the LFS system to use that partition for

/boot as well, just mount the partition at $LFS/boot in the host distro. The Linux kernel supports mounting
one partition at multiple mount points.

Leaving /boot on the current LFS partition will also work, but configuration for multiple systems is more difficult.

For examples and more information on boot partition layouts, looking at Section 2.4, “Creating a New Partition” may
be informative.

Using the above information, determine the appropriate designator for the root partition (or boot partition, if a separate
one is used). For the following example, it is assumed that the root (or separate boot) partition is sda2.

The following sections go over how to boot with BIOS and UEFI. The GRUB installations for BIOS, 64-bit UEFI, and
32-bit UEFI can coexist and share the same configuration. The images and data live at different locations, so you can
create both the BIOS Boot Partition and the EFI System Partition, and install GRUB for all the supported firmware
**types (i.e. running three grub-install commands). If you are unsure about your firmware type, or you plan to move the**
hard drive to a different computer, this is something you can do as a blanket strategy.

### Note

If you're doing UEFI boot but have created the Grub BIOS partition, it may be a good idea to run the command
for BIOS in case UEFI booting does not work as expected.

### Note

If you only need to install GRUB for one boot method, you don't have to run commands for both methods.
You can just run the command for the boot method you need.

**10.4.4.1. Booting With BIOS**

For booting with BIOS, make sure the boot partition is mounted (if using a separate one) and the BIOS Boot partition
exists. After that, install the GRUB files into /boot/grub and set up the boot track:

### Warning

The following command will overwrite the current boot loader. Do not run the command if this is not desired,
for example, if using a third party boot manager to manage the MBR.

**grub-install /dev/sda --target=i386-pc**

**10.4.4.2. Booting With UEFI**

For booting with UEFI, make sure the boot partition is mounted (if using a separate one) and the EFI System Partition
is mounted at /boot/efi. After that, install the GRUB files into /boot/grub and the main GRUB image at /boot/efi/

EFI/BOOT/BOOTX64.EFI:

---

Linux From Scratch - Version 13.1-systemd

### Warning

The following command will overwrite the /boot/efi/EFI/BOOT/BOOTX64.EFI file. If it already exists, it's
likely that it's the entry of another boot loader (for example the GRUB installation from the host distro, or
the Windows Boot Manager). Backup the file so it can be restored later or loaded as a secondary boot loader
by the new GRUB installation from LFS.

**grub-install --target=x86_64-efi --removable**

The command above assumes that you have 64-bit UEFI firmware. If you want to make the system bootable on 32-bit
UEFI firmware, run the command with x86_64-efi replaced by i386-efi.

**The --removable option makes grub-install use the standard location, EFI/BOOT/BOOTX64.EFI (or EFI/BOOT/BOOTIA32.**

EFI for i386-efi), instead of the location GRUB prefers (EFI/GRUB/GRUBX64.EFI or EFI/GRUB/GRUBIA32.EFI). Using a
non-standard location would result in the location in a EFI variable be recorded, but LFS lacks the BLFS package
efibootmgr, which is needed by GRUB to record the location into the EFI variable.

### Note

Some UEFI firmware implementations, while rare, skip the standard EFI path. Such systems most of the time
are old, like Lenovo ThinkPads or HP desktops/laptops. When the boot entry is missing in the firmware setup,
you will need to install the BLFS package efibootmgr to create a boot entry for UEFI. If it's easier, the package
can be installed via the distribution's package manager, if applicable, and used on the host instead of on the
LFS system. This can prevent the need for downloading more tarballs onto the LFS system for now.

First install the package, then mount the EFI variable file system if it isn't already mounted:

**mountpoint /sys/firmware/efi/efivars ||**
**mount -v -t efivarfs efivarfs /sys/firmware/efi/efivars**

Now create a boot entry for the EFI:

**efibootmgr -c -d /dev/sd<x> \**
**-p <y> -L "LFS" -l '\EFI\BOOT\BOOT<X64>.EFI'**

The /dev/sd<x> drive should be the device node for the disk where the ESP exists. The <y> partition number
should match the number of the ESP. If the ESP is on /dev/sda2, then the partition number would be 2. If
you are using 32-bit UEFI, replace <X64> with IA32.

**Some (broken) firmware may require additional parameters for efibootmgr, like --full-dev-path or -e 1 -**

E. Read the man page efibootmgr(8) for details.

Now unmount the EFI variable file system:

**umount -v /sys/firmware/efi/efivars**

---

Linux From Scratch - Version 13.1-systemd