# Chapter 10. Making the LFS System Bootable

# 10.1. Introduction

It is time to make the LFS system bootable. This chapter discusses creating the /etc/fstab file, building a kernel for
the new LFS system, and installing the GRUB boot loader so that the LFS system can be selected for booting at startup.

# 10.2. Creating the /etc/fstab File

The /etc/fstab file is used by some programs to determine where file systems are to be mounted by default, in which
order, and which must be checked (for integrity errors) prior to mounting. Create a new file systems table like this:

**cat > /etc/fstab << "EOF"**

# Begin /etc/fstab

# file system  mount-point  type     options             dump  fsck

#                                                              order

/dev/<xxx>     /            <fff>    defaults            1     1
/dev/<yyy>     swap         swap     pri=1               0     0

# End /etc/fstab
**EOF**

Replace <xxx>, <yyy>, and <fff> with the values appropriate for the system, for example, sda2, sda5, and ext4. For
details on the six fields in this file, see fstab(5).

Filesystems with MS-DOS or Windows origin (i.e. vfat, ntfs, smbfs, cifs, iso9660, udf) need a special option, utf8, in
order for non-ASCII characters in file names to be interpreted properly. For non-UTF-8 locales, the value of iocharset
should be set to be the same as the character set of the locale, adjusted in such a way that the kernel understands it. This
works if the relevant character set definition (found under File systems -> Native Language Support when configuring
the kernel) has been compiled into the kernel or built as a module. However, if the character set of the locale is UTF-8,
the corresponding option iocharset=utf8 would make the file system case sensitive. To fix this, use the special option

utf8 instead of iocharset=utf8, for UTF-8 locales. The “codepage” option is also needed for vfat and smbfs filesystems.
It should be set to the codepage number used under MS-DOS in your country. For example, in order to mount USB
flash drives, a ru_RU.KOI8-R user would need the following in the options portion of its mount line in /etc/fstab:

noauto,user,quiet,showexec,codepage=866,iocharset=koi8r

The corresponding options fragment for ru_RU.UTF-8 users is:

noauto,user,quiet,showexec,codepage=866,utf8

Note that using iocharset is the default for iso8859-1 (which keeps the file system case insensitive), and the utf8 option
tells the kernel to convert the file names using UTF-8 so they can be interpreted in the UTF-8 locale.

When installing GRUB with UEFI, the ESP must be formatted as a FAT file system (EXFAT should not be considered
one). In the Linux kernel the VFAT driver handles all the FAT file systems, so this file will contain vfat regardless.
An example of how you would go about an entry for the ESP would look like this:

**cat >> /etc/fstab << "EOF"**
/dev/<zzz>  /boot/efi  vfat  rw,relatime,codepage=437,iocharset=iso8859-1   0   2
**EOF**

---

Linux From Scratch - Version 13.1-systemd

The iso8859-1 IO charset is used here as we'll enable it as a part of the kernel UEFI configuration in Section 10.3,
“Linux-7.1.8.” Technically the IO charset should match your locale as we've discussed above. However the name of
all the files in the ESP only contains 7-bit ASCII characters, so things will be OK as long as the character set for your
locale treats 7-bit ASCII characters in the same way as ISO-8859-1. For example, UTF-8 is such a character set.

### Note

The EFI filesystem only needs to be mounted when installing GRUB. The system uses this partition before the
kernel is loaded and is not used otherwise. An alternative to adding this entry to the fstab file is to manually
**mount it before running grub-install below in Section 10.4, “Using GRUB to Set Up the Boot Process.”**

It is also possible to specify default codepage and iocharset values for some filesystems during kernel configuration.
The relevant parameters are named “Default NLS Option” (CONFIG_NLS_DEFAULT), “Default Remote NLS Option”
(CONFIG_SMB_NLS_DEFAULT), “Default codepage for FAT” (CONFIG_FAT_DEFAULT_CODEPAGE), and “Default iocharset for
FAT” (CONFIG_FAT_DEFAULT_IOCHARSET). There is no way to specify these settings for the ntfs filesystem at kernel
compilation time.

---

Linux From Scratch - Version 13.1-systemd

# 10.3. Linux-7.1.8

The Linux package contains the Linux kernel.
**Approximate build time:**
0.4 - 32 SBU (typically about 2.5 SBU)
**Required disk space:**
1.7 - 14 GB (typically about 2.3 GB)

## 10.3.1. Installation of the kernel

Building the kernel involves a few steps—configuration, compilation, and installation. Read the README file in the kernel
source tree for alternative methods to the way this book configures the kernel.

### Important

Building the linux kernel for the first time is one of the most challenging tasks in LFS. Getting it right depends
on the specific hardware for the target system and your specific needs. There are almost 12,000 configuration
items that are available for the kernel although only about a third of them are needed for most computers. The
LFS editors recommend that users not familiar with this process follow the procedures below fairly closely.
The objective is to get an initial system to a point where you can log in at the command line when you reboot
later in Section 11.3, “Rebooting the System.” At this point optimization and customization is not a goal.

For general information on kernel configuration see https://www.linuxfromscratch.org/hints/downloads/files/
kernel-configuration.txt. Additional information about configuring and building the kernel can be found at
https://anduin.linuxfromscratch.org/LFS/kernel-nutshell/. These references are a bit dated, but still give a
reasonable overview of the process.

If all else fails, you can ask for help on the lfs-support mailing list. Note that subscribing is required in order
for the list to avoid spam.

Prepare for compilation by running the following command:

**make mrproper**

This ensures that the kernel tree is absolutely clean. The kernel team recommends that this command be issued prior to
each kernel compilation. Do not rely on the source tree being clean after un-tarring.

There are several ways to configure the kernel options. Usually, this is done through a menu-driven interface, for
example:

**make menuconfig**

**The meaning of optional make environment variables:**

LANG=<host_LANG_value> LC_ALL=

This establishes the locale setting to the one used on the host. This may be needed for a proper menuconfig ncurses
interface line drawing on a UTF-8 linux text console.
If used, be sure to replace <host_LANG_value> by the value of the $LANG variable from your host. You can
alternatively use instead the host's value of $LC_ALL or $LC_CTYPE.
**make menuconfig**

**This launches an ncurses menu-driven interface. For other (graphical) interfaces, type make help.**

### Note

**A good starting place for setting up the kernel configuration is to run make defconfig. This will set the base**
configuration to a good state that takes your current system architecture into account.

---

Linux From Scratch - Version 13.1-systemd

Be sure to enable/disable/set the following features or the system might not work correctly or boot at all:

General setup --->
[ ] Compile the kernel with warnings as errors                        [WERROR]
CPU/Task time and stats accounting --->
[*] Pressure stall information tracking                                [PSI]
[ ]   Require boot parameter to enable pressure stall information tracking
...  [PSI_DEFAULT_DISABLED]
< > Enable kernel headers through /sys/kernel/kheaders.tar.xz      [IKHEADERS]
[*] Control Group support --->                                       [CGROUPS]
[*]   Memory controller                                              [MEMCG]
[ /*] CPU controller --->                                     [CGROUP_SCHED]