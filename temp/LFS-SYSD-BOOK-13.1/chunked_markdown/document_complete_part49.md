# 8.65. GRUB-2.14

The GRUB package contains the GRand Unified Bootloader.

### Note

This page is split up into multiple sections aimed to install for a specific boot method (BIOS, 64-bit UEFI,
and 32-bit UEFI). GRUB cannot be built with all the boot method architectures at once.

You may skip other sections to go to the boot method you need. If in doubt, you may follow all of the sections
at the cost of extra build time. After you have installed support for your boot method, then continue building
the rest of the packages in this chapter. Making your LFS system bootable with GRUB will be discussed in
Section 10.4, “Using GRUB to Set Up the Boot Process.”

### Warning

Unset any environment variables which may affect the build:

**unset {C,CPP,CXX,LD}FLAGS**

Don't try “tuning” this package with custom compilation flags. This package is a bootloader. The low-level
operations in the source code may be broken by aggressive optimization.

**Approximate build time:**
1.0 SBU
**Required disk space:**
245 MB

## 8.65.1. Installation of GRUB for BIOS

First fix a bug introduced in grub-2.14:

**sed 's/--image-base/--nonexist-linker-option/' -i configure**

Prepare GRUB for compilation:

**./configure --prefix=/usr     \**
**--sysconfdir=/etc \**
**--disable-efiemu  \**
**--disable-werror**

**The meaning of the new configure options:**

--disable-werror

This allows the build to complete with warnings introduced by more recent versions of Flex.

--disable-efiemu

This option minimizes what is built by disabling a feature and eliminating some test programs not needed for LFS.

Compile the package:

**make**

The test suite for this packages is not recommended. Most of the tests depend on packages that are not available in the
**limited LFS environment. To run the tests anyway, run make check.**

Install the package:

**make install**

---

Linux From Scratch - Version 13.1-systemd

## 8.65.2. Installation of GRUB for 64-bit UEFI

If you want to boot with 64-bit UEFI, you should build support for it.

First, if you built GRUB from the section above, clean the source tree:

**make clean**

Now configure GRUB for 64-bit UEFI support:

**./configure --prefix=/usr       \**
**--sysconfdir=/etc   \**
**--target=x86_64     \**
**--with-platform=efi \**
**--disable-efiemu    \**
**--disable-werror**

**The meaning of the new configure options:**

--target=x86_64

This defines that the UEFI firmware architecture is x86_64, which GRUB should target.

--with-platform=efi

This specifies that EFI is a platform GRUB should target. In combination with --target=x86_64, GRUB will have
the ability to target the x86_64-efi platform.

Compile the package for 64-bit UEFI support:

**make**

Install support for 64-bit UEFI:

**make install**

## 8.65.3. Installation of GRUB for 32-bit UEFI

If you want to boot with 32-bit UEFI, which is very rare, you should build support for it.

First, if you built GRUB from any of the sections above, clean the source tree:

**make clean**

Now configure GRUB for 32-bit UEFI support:

**./configure --prefix=/usr       \**
**--sysconfdir=/etc   \**
**--target=i386       \**
**--with-platform=efi \**
**--disable-efiemu    \**
**--disable-werror**

**The meaning of the new configure options:**

--target=i386

This defines that the UEFI firmware architecture is i386/32-bit, which GRUB should target. In combination with

--with-platform=efi, GRUB will have the ability to target the i386-efi platform.

Compile the package for 32-bit UEFI support:

**make**

---

Linux From Scratch - Version 13.1-systemd

Install support for 32-bit UEFI:

**make install**

## 8.65.4. Contents of GRUB

**Installed programs:**
grub-bios-setup, grub-editenv, grub-file, grub-fstest, grub-glue-efi, grub-install, grub-
kbdcomp, grub-macbless, grub-menulst2cfg, grub-mkconfig, grub-mkimage, grub-
mklayout, grub-mknetdir, grub-mkpasswd-pbkdf2, grub-mkrelpath, grub-mkrescue,
grub-mkstandalone, grub-ofpathname, grub-probe, grub-reboot, grub-render-label, grub-
script-check, grub-set-default, grub-sparc64-setup, and grub-syslinux2cfg
**Installed directories:**
/usr/lib/grub, /etc/grub.d, /usr/share/grub, and /boot/grub (when grub-install is first run)

### Note

/usr/lib/grub will have different contents based on what platform(s) you have installed GRUB for. Namely,
there will be different GRUB modules for each platform.

**Short Descriptions**

**grub-bios-setup**
**Is a helper program for grub-install**

**grub-editenv**
Is a tool to edit the environment block

**grub-file**
Checks to see if the given file is of the specified type

**grub-fstest**
Is a tool to debug the file system driver

**grub-glue-efi**
Glues 32-bit and 64-bit binaries into a single file (for Apple machines)

**grub-install**
Installs GRUB on your drive

**grub-kbdcomp**
Is a script that converts an xkb layout into one recognized by GRUB

**grub-macbless**
**Is the Mac-style bless for HFS or HFS+ file systems (bless is peculiar to Apple**
machines; it makes a device bootable)

**grub-menulst2cfg**
Converts a GRUB Legacy menu.lst into a grub.cfg for use with GRUB 2

**grub-mkconfig**
Generates a grub.cfg file

**grub-mkimage**
Makes a bootable image of GRUB

**grub-mklayout**
Generates a GRUB keyboard layout file

**grub-mknetdir**
Prepares a GRUB netboot directory

**grub-mkpasswd-pbkdf2**
Generates an encrypted PBKDF2 password for use in the boot menu

**grub-mkrelpath**
Makes a system pathname relative to its root

**grub-mkrescue**
Makes a bootable image of GRUB suitable for a floppy disk, CDROM/DVD, or a USB
drive

**grub-mkstandalone**
Generates a standalone image

**grub-ofpathname**
Is a helper program that prints the path to a GRUB device

**grub-probe**
Probes device information for a given path or device

**grub-reboot**
Sets the default boot entry for GRUB for the next boot only

**grub-render-label**
Renders Apple .disk_label for Apple Macs

---

Linux From Scratch - Version 13.1-systemd

**grub-script-check**
Checks the GRUB configuration script for syntax errors

**grub-set-default**
Sets the default boot entry for GRUB

**grub-sparc64-setup**
Is a helper program for grub-setup

**grub-syslinux2cfg**
Transforms a syslinux config file into grub.cfg format

---

Linux From Scratch - Version 13.1-systemd

# 8.66. Gzip-1.14

The Gzip package contains programs for compressing and decompressing files.

**Approximate build time:**
0.1 SBU
**Required disk space:**
21 MB

## 8.66.1. Installation of Gzip

Prepare Gzip for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

## 8.66.2. Contents of Gzip

**Installed programs:**
gunzip, gzexe, gzip, uncompress (hard link with gunzip), zcat, zcmp, zdiff, zegrep,
zfgrep, zforce, zgrep, zless, zmore, and znew

**Short Descriptions**

**gunzip**
Decompresses gzipped files

**gzexe**
Creates self-decompressing executable files

**gzip**
Compresses the given files using Lempel-Ziv (LZ77) coding

**uncompress**
Decompresses compressed files

**zcat**
Decompresses the given gzipped files to standard output

**zcmp**
**Runs cmp on gzipped files**

**zdiff**
**Runs diff on gzipped files**

**zegrep**
**Runs egrep on gzipped files**

**zfgrep**
**Runs fgrep on gzipped files**

**zforce**
**Forces a .gz extension on all given files that are gzipped files, so that gzip will not compress them**
again; this can be useful when file names were truncated during a file transfer

**zgrep**
**Runs grep on gzipped files**

**zless**
**Runs less on gzipped files**

**zmore**
**Runs more on gzipped files**

**znew**
**Re-compresses files from compress format to gzip format—.Z to .gz**

---

Linux From Scratch - Version 13.1-systemd