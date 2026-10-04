# Chapter 7. Entering Chroot and Building Additional

# Temporary Tools

# 7.1. Introduction

This chapter shows how to build the last missing bits of the temporary system: the tools needed to build the various
packages. Now that all circular dependencies have been resolved, a “chroot” environment, completely isolated from
the host operating system (except for the running kernel), can be used for the build.

For proper operation of the isolated environment, some communication with the running kernel must be established.
This is done via the so-called Virtual Kernel File Systems, which will be mounted before entering the chroot
**environment. You may want to verify that they are mounted by issuing the findmnt command.**

Until Section 7.4, “Entering the Chroot Environment”, the commands must be run as root, with the LFS variable set.
After entering chroot, all commands are run as root, fortunately without access to the OS of the computer you built
LFS on. Be careful anyway, as it is easy to destroy the whole LFS system with bad commands.

# 7.2. Changing Ownership

### Note

The commands in the remainder of this book must be performed while logged in as user root and no longer
as user lfs. Also, double check that $LFS is set in root's environment.

Currently, the whole directory hierarchy in $LFS is owned by the user lfs, a user that exists only on the host system.
If the directories and files under $LFS are kept as they are, they will be owned by a user ID without a corresponding
account. This is dangerous because a user account created later could get this same user ID and would own all the files
under $LFS, thus exposing these files to possible malicious manipulation.

To address this issue, change the ownership of the $LFS/* directories to user root by running the following command:

**chown --from lfs -R root:root $LFS/{usr,var,etc,tools}**
**case $(uname -m) in**
**x86_64) chown --from lfs -R root:root $LFS/lib64 ;;**
**esac**

# 7.3. Preparing Virtual Kernel File Systems

Applications running in userspace utilize various file systems created by the kernel to communicate with the kernel
itself. These file systems are virtual: no disk space is used for them. The content of these file systems resides in
memory. These file systems must be mounted in the $LFS directory tree so the applications can find them in the chroot
environment.

Begin by creating the directories on which these virtual file systems will be mounted:

**mkdir -pv $LFS/{dev,proc,sys,run}**

## 7.3.1. Mounting and Populating /dev

During a normal boot of an LFS system, the kernel automatically mounts the devtmpfs file system on the /dev directory;
the kernel creates device nodes on that virtual file system during the boot process, or when a device is first detected
or accessed. The udev daemon may change the ownership or permissions of the device nodes created by the kernel,

---

Linux From Scratch - Version 13.1-systemd

and create new device nodes or symlinks, to ease the work of distro maintainers and system administrators. (See
Section 9.3.2.2, “Device Node Creation” for details.) If the host kernel supports devtmpfs, we can simply mount a

devtmpfs at $LFS/dev and rely on the kernel to populate it.

But some host kernels lack devtmpfs support; these host distros use different methods to create the content of /dev. So
the only host-agnostic way to populate the $LFS/dev directory is by bind mounting the host system's /dev directory. A
bind mount is a special type of mount that makes a directory subtree or a file visible at some other location. Use the
following command to do this.

**mount -v --bind /dev $LFS/dev**

## 7.3.2. Mounting Virtual Kernel File Systems

Now mount the remaining virtual kernel file systems:

**mount -vt devpts devpts -o gid=5,mode=0620 $LFS/dev/pts**
**mount -vt proc proc $LFS/proc**
**mount -vt sysfs sysfs $LFS/sys**
**mount -vt tmpfs tmpfs $LFS/run**

**The meaning of the mount options for devpts:**

gid=5

This ensures that all devpts-created device nodes are owned by group ID 5. This is the ID we will use later on for the

tty group. We use the group ID instead of a name, since the host system might use a different ID for its tty group.

mode=0620

This ensures that all devpts-created device nodes have mode 0620 (user readable and writable, group writable).
Together with the option above, this ensures that devpts will create device nodes that meet the requirements of
**grantpt(), meaning the Glibc pt_chown helper binary (which is not installed by default) is not necessary.**

In some host systems, /dev/shm is a symbolic link to a directory, typically /run/shm. The /run tmpfs was mounted above
so in this case only a directory needs to be created with the correct permissions.

In other host systems /dev/shm is a mount point for a tmpfs. In that case the mount of /dev above will only create /dev/
shm as a directory in the chroot environment. In this situation we must explicitly mount a tmpfs:

**if [ -h $LFS/dev/shm ]; then**
**install -v -d -m 1777 $LFS$(realpath /dev/shm)**
**else**
**mount -vt tmpfs -o nosuid,nodev tmpfs $LFS/dev/shm**
**fi**

# 7.4. Entering the Chroot Environment

Now that all the packages which are required to build the rest of the needed tools are on the system, it is time to enter
the chroot environment and finish installing the temporary tools. This environment will also be used to install the final
system. As user root, run the following command to enter the environment that is, at the moment, populated with
nothing but temporary tools:

**chroot "$LFS" /usr/bin/env -i   \**
**HOME=/root                  \**
**TERM="$TERM"                \**
**PS1='(lfs chroot) \u:\w\$ ' \**
**PATH=/usr/bin:/usr/sbin     \**
**MAKEFLAGS="-j$(nproc)"      \**
**TESTSUITEFLAGS="-j$(nproc)" \**
**/bin/bash --login**

---

Linux From Scratch - Version 13.1-systemd

If you don't want to use all available logical cores, replace $(nproc) with the number of logical cores you want to use
for building packages in this chapter and the following chapters. The test suites of some packages (notably Autoconf,
Libtool, and Tar) in Chapter 8 are not affected by MAKEFLAGS, they use a TESTSUITEFLAGS environment variable instead.
We set that here as well for running these test suites with multiple cores.

**The -i option given to the env command will clear all the variables in the chroot environment. After that, only the HOME,**

TERM, PS1, and PATH variables are set again. The TERM=$TERM construct sets the TERM variable inside chroot to the same
**value as outside chroot. This variable is needed so programs like vim and less can operate properly. If other variables**
are desired, such as CFLAGS or CXXFLAGS, this is a good place to set them.

From this point on, there is no need to use the LFS variable any more because all work will be restricted to the LFS file
**system; the chroot command runs the Bash shell with the root (/) directory set to $LFS.**

Notice that /tools/bin is not in the PATH. This means that the cross toolchain will no longer be used.

**Also note that the bash prompt will say I have no name! This is normal because the /etc/passwd file has not been**
created yet.

### Note

It is important that all the commands throughout the remainder of this chapter and the following chapters
are run from within the chroot environment. If you leave this environment for any reason (rebooting for
example), ensure that the virtual kernel filesystems are mounted as explained in Section 7.3.1, “Mounting and
Populating /dev” and Section 7.3.2, “Mounting Virtual Kernel File Systems” and enter chroot again before
continuing with the installation.