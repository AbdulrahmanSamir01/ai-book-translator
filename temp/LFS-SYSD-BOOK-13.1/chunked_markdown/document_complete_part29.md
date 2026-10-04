# 7.15. Cleaning up and Saving the Temporary System

## 7.15.1. Cleaning

First, remove the currently installed documentation files to prevent them from ending up in the final system, and to
save about 35 MB:

**rm -rf /usr/share/{info,man,doc}/***

Second, on a modern Linux system, the libtool .la files are only useful for libltdl. No libraries in LFS are loaded by
libltdl, and it's known that some .la files can cause BLFS package failures. Remove those files now:

**find /usr/{lib,libexec} -name \*.la -delete**

The current system size is now about 3 GB, however the /tools directory is no longer needed. It uses about 1 GB of
disk space. Delete it now:

**rm -rf /tools**

## 7.15.2. Backup

At this point the essential programs and libraries have been created and your current LFS system is in a good state.
Your system can now be backed up for later reuse. In case of fatal failures in the subsequent chapters, it often turns out
that removing everything and starting over (more carefully) is the best way to recover. Unfortunately, all the temporary
files will be removed, too. To avoid spending extra time to redo something which has been done successfully, creating
a backup of the current LFS system may prove useful.

### Note

All the remaining steps in this section are optional. Nevertheless, as soon as you begin installing packages
in Chapter 8, the temporary files will be overwritten. So it may be a good idea to do a backup of the current
system as described below.

The following steps are performed from outside the chroot environment. That means you have to leave the chroot
environment first before continuing. The reason for that is to get access to file system locations outside of the chroot
environment to store/read the backup archive, which ought not be placed within the $LFS hierarchy.

If you have decided to make a backup, leave the chroot environment:

**exit**

### Important

All of the following instructions are executed by root on your host system. Take extra care about the
commands you're going to run as mistakes made here can modify your host system. Be aware that the
environment variable LFS is set for user lfs by default but may not be set for root.

Whenever commands are to be executed by root, make sure you have set LFS.

This has been discussed in Section 2.6, “Setting the $LFS Variable and the Umask.”

Before making a backup, unmount the virtual file systems:

**mountpoint -q $LFS/dev/shm && umount $LFS/dev/shm**
**umount $LFS/dev/pts**
**umount $LFS/{sys,proc,run,dev}**

---

Linux From Scratch - Version 13.1-systemd

Make sure you have at least 1 GB free disk space (the source tarballs will be included in the backup archive) on the
file system containing the directory where you create the backup archive.

Note that the instructions below specify the home directory of the host system's root user, which is typically found
on the root file system. Replace $HOME by a directory of your choice if you do not want to have the backup stored in

root's home directory.

Create the backup archive by running the following command:

### Note

Because the backup archive is compressed, it takes a relatively long time (over 10 minutes) even on a
reasonably fast system.

**cd $LFS**
**tar -cJpf $HOME/lfs-temp-tools-13.1-systemd.tar.xz .**

### Note

If continuing to chapter 8, don't forget to reenter the chroot environment as explained in the “Important” box
below.

## 7.15.3. Restore

In case some mistakes have been made and you need to start over, you can use this backup to restore the system and
save some recovery time. Since the sources are located under $LFS, they are included in the backup archive as well,
so they do not need to be downloaded again. After checking that $LFS is set properly, you can restore the backup by
executing the following commands:

### Warning

**The following commands are extremely dangerous. If you run rm -rf ./* as the root user and you do not**
change to the $LFS directory or the LFS environment variable is not set for the root user, it will destroy your
entire host system. YOU ARE WARNED.

cd $LFS
rm -rf ./*
tar -xpf $HOME/lfs-temp-tools-13.1-systemd.tar.xz

Again, double check that the environment has been set up properly and continue building the rest of the system.

### Important

If you left the chroot environment to create a backup or restart building using a restore, remember to check
**that the virtual file systems are still mounted (findmnt | grep $LFS should show at least $LFS/dev, $LFS/**

proc, and $LFS/sys as mounted). If they are not mounted, remount them now as described in Section 7.3,
“Preparing Virtual Kernel File Systems” and re-enter the chroot environment (see Section 7.4, “Entering the
Chroot Environment”) before continuing.

---

Linux From Scratch - Version 13.1-systemd

# Part IV. Building the LFS System

---

Linux From Scratch - Version 13.1-systemd

# Chapter 8. Installing Basic System Software

# 8.1. Introduction

In this chapter, we start constructing the LFS system in earnest.

The installation of this software is straightforward. Although in many cases the installation instructions could be made
shorter and more generic, we have opted to provide the full instructions for every package to minimize the possibilities
for mistakes. The key to learning what makes a Linux system work is to know what each package is used for and why
you (or the system) may need it.

We do not recommend using customized optimizations. They can make a program run slightly faster, but they may
also cause compilation difficulties, and problems when running the program. If a package refuses to compile with a
customized optimization, try to compile it without optimization and see if that fixes the problem. Even if the package
does compile when using a customized optimization, there is the risk it may have been compiled incorrectly because
of the complex interactions between the code and the build tools. Also note that the -march and -mtune options using
values not specified in the book have not been tested. This may cause problems with the toolchain packages (Binutils,
GCC and Glibc). The small potential gains achieved by customizing compiler optimizations are often outweighed by
the risks. First-time builders of LFS are encouraged to build without custom optimizations.

On the other hand, we keep the optimizations enabled by the default configuration of the packages. In addition, we
sometimes explicitly enable an optimized configuration provided by a package but not enabled by default. The package
maintainers have already tested these configurations and consider them safe, so it's not likely they would break the
build. Generally the default configuration already enables -O2 or -O3, so the resulting system will still run very fast
without any customized optimization, and be stable at the same time.

Before the installation instructions, each installation page provides information about the package, including a concise
description of what it contains, approximately how long it will take to build, and how much disk space is required
during this building process. Following the installation instructions, there is a list of programs and libraries (along with
brief descriptions) that the package installs.

### Note

The SBU values and required disk space include test suite data for all applicable packages in Chapter 8. SBU
values have been calculated using four CPU cores (-j4) for all operations unless specified otherwise.

## 8.1.1. About Libraries

In general, the LFS editors discourage building and installing static libraries. Most static libraries have been made
obsolete in a modern Linux system. In addition, linking a static library into a program can be detrimental. If an update
to the library is needed to remove a security problem, every program that uses the static library will need to be relinked
with the new library. Since the use of static libraries is not always obvious, the relevant programs (and the procedures
needed to do the linking) may not even be known.

The procedures in this chapter remove or disable installation of most static libraries. Usually this is done by passing a

**--disable-static option to configure. In other cases, alternate means are needed. In a few cases, especially Glibc and**
GCC, the use of static libraries remains an essential feature of the package building process.

For a more complete discussion of libraries, see  Libraries: Static or shared? in the BLFS book.

---

Linux From Scratch - Version 13.1-systemd