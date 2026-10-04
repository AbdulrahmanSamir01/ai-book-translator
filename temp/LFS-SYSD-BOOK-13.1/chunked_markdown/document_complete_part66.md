## 10.4.5. Creating the GRUB Configuration File

Generate /boot/grub/grub.cfg:

**cat > /boot/grub/grub.cfg << "EOF"**

# Begin /boot/grub/grub.cfg
set default=0
set timeout=5

insmod part_gpt
insmod ext2

set root=(hd0,2)
set gfxpayload=1024x768x32

menuentry "GNU/Linux, Linux 7.1.8-lfs-13.1-systemd" {
linux   /boot/vmlinuz-7.1.8-lfs-13.1-systemd root=/dev/sda2 ro
}
**EOF**

**The insmod commands load the GRUB modules named part_gpt and ext2. Despite the naming, ext2 actually supports**

ext2, ext3, and ext4 filesystems. In a typical configuration, the part_gpt and ext2 modules are already embedded in
**the main GRUB image by grub-install, and the insmod commands for them will do nothing. However, they do no**
harm anyway, and they may be needed with some rare configurations.

**The set gfxpayload=1024x768x32 command sets the resolution and color depth of the VESA framebuffer to be passed**
to the kernel. It's necessary for the kernel SimpleDRM driver to use the VESA framebuffer. You can use a different
resolution or color depth value which better suits for your monitor. This line does nothing when the system is booted
via UEFI, but it does no harm anyway.

### Note

From GRUB's perspective, the kernel files are relative to the partition used. If you used a separate /boot
partition, remove /boot from the above linux line. You will also need to change the set root line to point to
the boot partition.

### Note

The GRUB designator for a partition may change if you added or removed some disks (including
removable disks like USB thumb devices). The change may cause boot failure because grub.cfg refers
to some “old” designators. If you wish to avoid such a problem, you may use the UUID of a partition
**and the UUID of a filesystem instead of a GRUB designator to specify a device. Run lsblk -o**
**UUID,PARTUUID,PATH,MOUNTPOINT to show the UUIDs of your filesystems (in the UUID column)**
and partitions (in the PARTUUID column). Then replace set root=(hdx,y) with search --set=root --fs-

uuid <UUID of the filesystem where the kernel is installed>, and replace root=/dev/sda2 with

root=PARTUUID=<UUID of the partition where LFS is built>.

Note that the UUID of a partition is completely different from the UUID of the filesystem in this
partition. Some online resources may instruct you to use root=UUID=<filesystem UUID> instead of

root=PARTUUID=<partition UUID>, but doing so will require an initramfs, which is beyond the scope of LFS.

The name of the device node for a partition in /dev may also change (very frequently on some systems with
multiple NVME disks). You can also replace paths to device nodes like /dev/sda1 with PARTUUID=<partition

UUID>, in /etc/fstab, to avoid a potential boot failure in case the device node name has changed.

---

Linux From Scratch - Version 13.1-systemd

GRUB is an extremely powerful program and it provides a tremendous number of options for booting from a wide
variety of devices, operating systems, and partition types. There are also many options for customization such as
graphical splash screens, playing sounds, mouse input, etc. The details of these options are beyond the scope of this
introduction.

### Caution

There is a command, grub-mkconfig, that can write a configuration file automatically. It uses a set of scripts
in /etc/grub.d/ and will destroy any customizations that you make. These scripts are designed primarily for
non-source distributions and are not recommended for LFS. If you install a commercial Linux distribution,
there is a good chance that this program will be run. Be sure to back up your grub.cfg file.

---

Linux From Scratch - Version 13.1-systemd

# Chapter 11. The End

# 11.1. The End

Well done! The new LFS system is installed! We wish you much success with your shiny new custom-built Linux
system.

It may be a good idea to create an /etc/lfs-release file. By having this file, it is very easy for you (and for us if you
need to ask for help at some point) to find out which LFS version is installed on the system. Create this file by running:

**echo 13.1-systemd > /etc/lfs-release**

Two files describing the installed system may be used by packages that can be installed on the system later, either in
binary form or by building them.

The first one shows the status of your new system with respect to the Linux Standards Base (LSB). To create this
file, run:

**cat > /etc/lsb-release << "EOF"**
**DISTRIB_ID="Linux From Scratch"**
**DISTRIB_RELEASE="13.1-systemd"**
**DISTRIB_CODENAME="<your name here>"**
**DISTRIB_DESCRIPTION="Linux From Scratch"**
**EOF**

The second one contains roughly the same information, and is used by systemd and some graphical desktop
environments. To create this file, run:

**cat > /etc/os-release << "EOF"**
**NAME="Linux From Scratch"**
**VERSION="13.1-systemd"**
**ID=lfs**
**PRETTY_NAME="Linux From Scratch 13.1-systemd"**
**VERSION_CODENAME="<your name here>"**
**HOME_URL="https://www.linuxfromscratch.org/lfs/"**
**RELEASE_TYPE="stable"**
**EOF**

Be sure to customize the fields 'DISTRIB_CODENAME' and 'VERSION_CODENAME' to make the system uniquely
yours.

# 11.2. Get Counted

Now that you have finished the book, do you want to be counted as an LFS user? Head over to https://www.
linuxfromscratch.org/cgi-bin/lfscounter.php and register as an LFS user by entering your name and the first LFS version
you have used.

Let's reboot into LFS now.

# 11.3. Rebooting the System

Now that all of the software has been installed, it is time to reboot your computer. However, there are still a few things
to check. Here are some suggestions:

---

Linux From Scratch - Version 13.1-systemd

• Install any firmware needed if the kernel driver for your hardware requires some firmware files to function
properly.

• Ensure a password is set for the root user.

• A review of the following configuration files is also appropriate at this point.

• /etc/fstab

• /etc/hosts

• /etc/inputrc

• /etc/profile

• /etc/resolv.conf (optional)

• /etc/vimrc

Now that we have said that, let's move on to booting our shiny new LFS installation for the first time! First exit from
the chroot environment:

**logout**

Then unmount the virtual file systems:

**umount -v $LFS/dev/pts**
**mountpoint -q $LFS/dev/shm && umount -v $LFS/dev/shm**
**umount -v $LFS/dev**
**umount -v $LFS/run**
**umount -v $LFS/proc**
**umount -v $LFS/sys**

If multiple partitions were created, unmount the other partitions before unmounting the main one, like this:

**umount -v $LFS/home**
**umount -v $LFS**

Unmount the LFS file system itself:

**umount -v $LFS**

Now, reboot the system.

Assuming the GRUB boot loader was set up as outlined earlier, the menu is set to boot LFS 13.1-systemd automatically.

When the reboot is complete, the LFS system is ready for use. What you will see is a simple “login: ” prompt. At this
point, you can proceed to the BLFS Book where you can add more software to suit your needs.

**If your reboot is not successful, it is time to troubleshoot. For hints on solving initial booting problems, see https://**
www.linuxfromscratch.org/lfs/troubleshooting.html.

# 11.4. Additional Resources

Thank you for reading this LFS book. We hope that you have found this book helpful and have learned more about
the system creation process.

Now that the LFS system is installed, you may be wondering “What next?” To answer that question, we have compiled
a list of resources for you.

• Maintenance

---

Linux From Scratch - Version 13.1-systemd

Bugs and security notices are reported regularly for all software. Since an LFS system is compiled from source,
it is up to you to keep abreast of such reports. There are several online resources that track such reports, some of
which are shown below:

• LFS Security Advisories

This is a list of security vulnerabilities discovered in the LFS book after it's published.

• Open Source Security Mailing List

This is a mailing list for discussion of security flaws, concepts, and practices in the Open Source community.

• LFS Hints

The LFS Hints are a collection of educational documents submitted by volunteers in the LFS community. The
hints are available at https://www.linuxfromscratch.org/hints/downloads/files/.

• Mailing lists

There are several LFS mailing lists you may subscribe to if you are in need of help, want to stay current with
the latest developments, want to contribute to the project, and more. See Chapter 1 - Mailing Lists for more
information.

• The Linux Documentation Project

The goal of The Linux Documentation Project (TLDP) is to collaborate on all of the issues of Linux
documentation. The TLDP features a large collection of HOWTOs, guides, and man pages. It is located at https://
tldp.org/.