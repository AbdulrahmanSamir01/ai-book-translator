# 8.83. About Debugging Symbols

**Most programs and libraries are, by default, compiled with debugging symbols included (with gcc's -g option). This**
means that when debugging a program or library that was compiled with debugging information, the debugger can
provide not only memory addresses, but also the names of the routines and variables.

The inclusion of these debugging symbols enlarges a program or library significantly. Here are two examples of the
amount of space these symbols occupy:

**• A bash binary with debugging symbols: 1200 KB**

**• A bash binary without debugging symbols: 480 KB (60% smaller)**

• Glibc and GCC files (/lib and /usr/lib) with debugging symbols: 87 MB

• Glibc and GCC files without debugging symbols: 16 MB (82% smaller)

Sizes will vary depending on which compiler and C library were used, but a program that has been stripped of debugging
symbols is usually some 50% to 80% smaller than its unstripped counterpart. Because most users will never use a
debugger on their system software, a lot of disk space can be regained by removing these symbols. The next section
shows how to strip all debugging symbols from the programs and libraries.

# 8.84. Stripping

This section is optional. If the intended user is not a programmer and does not plan to do any debugging of the system
software, the system's size can be decreased by some 2 GB by removing the debugging symbols, and some unnecessary
symbol table entries, from binaries and libraries. This causes no real inconvenience for a typical Linux user.

Most people who use the commands mentioned below do not experience any difficulties. However, it is easy to make a
**mistake and render the new system unusable. So before running the strip commands, it is a good idea to make a backup**
of the LFS system in its current state.

**A strip command with the --strip-unneeded option removes all debug symbols from a binary or library. It also removes**
all symbol table entries not needed by the linker (for static libraries) or dynamic linker (for dynamically linked binaries
and shared libraries).

The debugging symbols from selected libraries are compressed with Zstd and preserved in separate files. That debugging
information is needed to run regression tests with valgrind or gdb later, in BLFS.

**Note that strip will overwrite the binary or library file it is processing. This can crash the processes using code or data**
**from the file. If the process running strip is affected, the binary or library being stripped can be destroyed; this can**
make the system completely unusable. To avoid this problem we copy some libraries and binaries into /tmp, strip them
**there, then reinstall them with the install command. (The related entry in Section 8.2.1, “Upgrade Issues” gives the**
**rationale for using the install command here.)**

### Note

The ELF loader's name is ld-linux-x86-64.so.2 on 64-bit systems and ld-linux.so.2 on 32-bit systems. The
construct below selects the correct name for the current architecture, excluding anything ending with g, in
case the commands below have already been run.

---

Linux From Scratch - Version 13.1-systemd

### Important

If there is any package whose version is different from the version specified by the book (either following
a security advisory or satisfying personal preference), it may be necessary to update the library file name in

**save_usrlib or online_usrlib. Failing to do so may render the system completely unusable.**

**save_usrlib="$(cd /usr/lib; ls ld-linux*[^g])**
**libc.so.6**
**libthread_db.so.1**
**libquadmath.so.0.0.0**
**libstdc++.so.6.0.36**
**libitm.so.1.0.0**
**libatomic.so.1.2.0"**

**cd /usr/lib**

**for LIB in $save_usrlib; do**
**objcopy --only-keep-debug --compress-debug-sections=zstd $LIB $LIB.dbg**
**cp $LIB /tmp/$LIB**
**strip --strip-unneeded /tmp/$LIB**
**objcopy --add-gnu-debuglink=$LIB.dbg /tmp/$LIB**
**install -vm755 /tmp/$LIB /usr/lib**
**rm /tmp/$LIB**
**done**

**online_usrbin="bash find strip"**
**online_usrlib="libbfd-2.47.20260726.so**
**libsframe.so.3.0.0**
**libhistory.so.8.3**
**libncursesw.so.6.6**
**libm.so.6**
**libreadline.so.8.3**
**libz.so.1.3.2**
**libzstd.so.1.5.7**
**$(cd /usr/lib; find libnss*.so* -type f)"**

**for BIN in $online_usrbin; do**
**cp /usr/bin/$BIN /tmp/$BIN**
**strip --strip-unneeded /tmp/$BIN**
**install -vm755 /tmp/$BIN /usr/bin**
**rm /tmp/$BIN**
**done**

**for LIB in $online_usrlib; do**
**cp /usr/lib/$LIB /tmp/$LIB**
**strip --strip-unneeded /tmp/$LIB**
**install -vm755 /tmp/$LIB /usr/lib**
**rm /tmp/$LIB**
**done**

**for i in $(find /usr/lib -type f -name \*.so* ! -name \*dbg) \**
**$(find /usr/lib -type f -name \*.a)                 \**
**$(find /usr/{bin,sbin,libexec} -type f); do**
**case "$online_usrbin $online_usrlib $save_usrlib" in**
***$(basename $i)* )**
**;;**
*** ) strip --strip-unneeded $i**
**;;**
**esac**
**done**

---

Linux From Scratch - Version 13.1-systemd

**unset BIN LIB save_usrlib online_usrbin online_usrlib**

A large number of files will be flagged as errors because their file format is not recognized. These warnings can be
safely ignored. They indicate that those files are scripts, not binaries.

# 8.85. Cleaning Up

Finally, clean up some extra files left over from running tests:

**rm -rf /tmp/{*,.*}**

There are also several files in the /usr/lib and /usr/libexec directories with a file name extension of .la. These are "libtool
archive" files. On a modern Linux system the libtool .la files are only useful for libltdl. No libraries in LFS are expected
to be loaded by libltdl, and it's known that some .la files can break BLFS package builds. Remove those files now:

**find /usr/lib /usr/libexec -name \*.la -delete**

For more information about libtool archive files, see the BLFS section "About Libtool Archive (.la) files".

The compiler built in Chapter 6 and Chapter 7 is still partially installed and not needed anymore. Remove it with:

**find /usr -depth -name $(uname -m)-lfs-linux-gnu\* | xargs rm -rf**

Finally, remove the temporary 'tester' user account created at the beginning of the previous chapter.

**userdel -r tester**

---

Linux From Scratch - Version 13.1-systemd

# Chapter 9. System Configuration

# 9.1. Introduction

This chapter discusses configuration files and systemd services. First, the general configuration files needed to set up
networking are presented.

• Section 9.2, “General Network Configuration.”

• Section 9.2.3, “Configuring the system hostname.”

• Section 9.2.4, “Customizing the /etc/hosts File.”

Second, issues that affect the proper setup of devices are discussed.

• Section 9.3, “Overview of Device and Module Handling.”

• Section 9.4, “Managing Devices.”

Third, configuring the system clock and keyboard layout is shown.

• Section 9.5, “Configuring the System Clock.”

• Section 9.6, “Configuring the Linux Console.”

Fourth, a brief introduction to the scripts and configuration files used when the user logs into the system is presented.

• Section 9.7, “Configuring the System Locale.”

• Section 9.8, “Creating the /etc/inputrc File.”

And finally, configuring the behavior of systemd is discussed.

• Section 9.10, “Systemd Usage and Configuration.”

# 9.2. General Network Configuration

This section only applies if a network card is to be configured.

## 9.2.1. Network Interface Configuration Files

**Starting with version 209, systemd ships a network configuration daemon called systemd-networkd which can be used**
**for basic network configuration. Additionally, since version 213, DNS name resolution can be handled by systemd-**
**resolved in place of a static /etc/resolv.conf file. Both services are enabled by default.**

### Note

**If you will not use systemd-networkd for network configuration (for example, when the system is not**
connected to network, or you want to use another utility like NetworkManager for network configuration),
disable a service to prevent an error message during boot:

**systemctl disable systemd-networkd-wait-online**

**Configuration files for systemd-networkd (and systemd-resolved) can be placed in /usr/lib/systemd/network or /**

etc/systemd/network. Files in /etc/systemd/network have a higher priority than the ones in /usr/lib/systemd/network.
There are three types of configuration files: .link, .netdev and .network files. For detailed descriptions and example
contents of these configuration files, consult the systemd.link(5), systemd.netdev(5), and systemd.network(5) manual
pages.

---

Linux From Scratch - Version 13.1-systemd

**9.2.1.1. Network Device Naming**

Udev normally assigns network card interface names based on physical system characteristics such as enp2s1. If you
**are not sure what your interface name is, you can always run ip link after you have booted your system.**

### Note

The interface names depend on the implementation and configuration of the udev daemon running on the
**system. The udev daemon for LFS (systemd-udevd, installed in Section 8.77, “Systemd-261.2”) will not run**
unless the LFS system is booted. So it's unreliable to determine the interface names being used in LFS system
by running those commands on the host distro, even though you are in the chroot environment.

For most systems, there is only one network interface for each type of connection. For example, the classic interface
name for a wired connection is eth0. A wireless connection will usually have the name wifi0 or wlan0.

If you prefer to use the classic or customized network interface names, there are three alternative ways to do that:

• Mask udev's .link file for the default policy:

**ln -s /dev/null /etc/systemd/network/99-default.link**

• Create a manual naming scheme, for example by naming the interfaces something like internet0, dmz0, or lan0.
To do that, create .link files in /etc/systemd/network/ that select an explicit name or a better naming scheme for
your network interfaces. For example:

**cat > /etc/systemd/network/10-ether0.link << "EOF"**
[Match]