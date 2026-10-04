# This may cause some systemd features malfunction:
[ ] Group scheduling for SCHED_RR/FIFO                    [RT_GROUP_SCHED]
[ ] Configure standard kernel features (expert users) --->            [EXPERT]

Processor type and features --->
[*] Build a relocatable kernel                                   [RELOCATABLE]
[*]   Randomize the address of the kernel image (KASLR)       [RANDOMIZE_BASE]

General architecture-dependent options --->
[*] Stack Protector buffer overflow detection                 [STACKPROTECTOR]
[*]   Strong Stack Protector                           [STACKPROTECTOR_STRONG]

[*] Networking support --->                                                [NET]
Networking options --->
[*] TCP/IP networking                                                 [INET]
[*]   The IPv6 protocol --->                                          [IPV6]

Device Drivers --->
Generic Driver Options --->
[ ] Support for uevent helper                                [UEVENT_HELPER]
[*] Maintain a devtmpfs filesystem to mount at /dev               [DEVTMPFS]
[*]   Automount devtmpfs at /dev, after the kernel mounted the rootfs
...  [DEVTMPFS_MOUNT]
Firmware loader --->
[ ] Enable the firmware sysfs fallback mechanism   [FW_LOADER_USER_HELPER]
Firmware Drivers --->
[*] Export DMI identification via sysfs to userspace                 [DMIID]
[*] Mark VGA/VBE/EFI FB as generic system framebuffer       [SYSFB_SIMPLEFB]
Character devices --->
-*- Enable TTY                                                         [TTY]
[ ]   Allow legacy TIOCSTI usage                            [LEGACY_TIOCSTI]
Graphics support --->
<*>    Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) --->
...  [DRM]
[*]    Display a user-friendly message when a kernel panic occurs
...  [DRM_PANIC]
(kmsg)   Panic screen formatter                           [DRM_PANIC_SCREEN]
Supported DRM clients --->
[*] Enable legacy fbdev support for your modesetting driver
...  [DRM_FBDEV_EMULATION]
Drivers for system framebuffers --->
<*> Simple framebuffer driver                              [DRM_SIMPLEDRM]
Console display driver support --->
[*] Framebuffer Console support                      [FRAMEBUFFER_CONSOLE]

File systems --->
[*] Inotify support for userspace                               [INOTIFY_USER]
Pseudo filesystems --->
[*] Tmpfs virtual memory file system support (former shm fs)         [TMPFS]
[*]   Tmpfs POSIX Access Control Lists                     [TMPFS_POSIX_ACL]

---

Linux From Scratch - Version 13.1-systemd

Enable some additional features if you are building a 64-bit system. If you are using menuconfig, enable them
in the order of CONFIG_PCI_MSI first, then CONFIG_IRQ_REMAP, at last CONFIG_X86_X2APIC because an option only
shows up after its dependencies are selected.

Processor type and features --->
[*] x2APIC interrupt controller architecture support              [X86_X2APIC]

Device Drivers --->
[*] PCI support --->                                                     [PCI]
[*] Message Signaled Interrupts (MSI and MSI-X)                    [PCI_MSI]
[*] IOMMU Hardware Support --->                                [IOMMU_SUPPORT]
[*] Support for Interrupt Remapping                              [IRQ_REMAP]

If you are building a 32-bit system, adjust the configuration so the kernel will be able to use up to 4GB
physical RAM:

Processor type and features --->
[*] High Memory Support                                            [HIGHMEM4G]

If the partition for the LFS system is in a NVME SSD (i. e. the device node for the partition is /dev/nvme*
instead of /dev/sd*), enable NVME support or the LFS system won't boot:

Device Drivers --->
NVME Support --->
<*> NVM Express block device                                  [BLK_DEV_NVME]

If you are booting with UEFI, adjust the kernel so it can have EFI partition and runtime support, on top of
supporting the DOS VFAT filesystem which is needed for the EFI partition:

Processor type and features --->
[*] EFI runtime service support                                          [EFI]
[*]   EFI stub support                                              [EFI_STUB]

-*- Enable the block layer --->                                          [BLOCK]
Partition Types --->
[ /*] Advanced partition selection                      [PARTITION_ADVANCED]
[*]     EFI GUID Partition support                           [EFI_PARTITION]

File systems --->
DOS/FAT/EXFAT/NT Filesystems --->
<*/M> VFAT (Windows-95) fs support                                 [VFAT_FS]
Pseudo filesystems --->
<*/M> EFI Variable filesystem                                    [EFIVAR_FS]
-*- Native language support --->                                         [NLS]
<*/M> Codepage 437 (United States, Canada)                [NLS_CODEPAGE_437]
<*/M> NLS ISO 8859-1  (Latin 1; Western European Languages)  [NLS_ISO8859_1]

If PARTITION_ADVANCED is not selected, EFI_PARTITION will be hidden but implicitly selected. Don't select

PARTITION_ADVANCED just because you need to boot via UEFI.

### Note

While "The IPv6 Protocol" is not strictly required, it is highly recommended by the systemd developers.

There are several other options that may be desired depending on the requirements for the system. For a list of options
needed for BLFS packages, see the BLFS Index of Kernel Settings.

---

Linux From Scratch - Version 13.1-systemd

**The rationale for the above configuration items:**

Randomize the address of the kernel image (KASLR)

Enable ASLR for kernel image, to mitigate some attacks based on fixed addresses of sensitive data or code in
the kernel.

Compile the kernel with warnings as errors

This may cause building failure if the compiler and/or configuration are different from those of the kernel
developers.

Enable kernel headers through /sys/kernel/kheaders.tar.xz

**This will require cpio building the kernel. cpio is not installed by LFS.**

Configure standard kernel features (expert users)

This will make some options show up in the configuration interface but changing those options may be dangerous.
Do not use this unless you know what you are doing.

Strong Stack Protector

Enable SSP for the kernel. We've enabled it for the entire userspace with --enable-default-ssp configuring GCC,
but the kernel does not use GCC default setting for SSP. We enable it explicitly here.

Support for uevent helper

Having this option set may interfere with device management when using Udev.

Maintain a devtmpfs

This will create automated device nodes which are populated by the kernel, even without Udev running. Udev
then runs on top of this, managing permissions and adding symlinks. This configuration item is required for all
users of Udev.

Automount devtmpfs at /dev

This will mount the kernel view of the devices on /dev upon switching to root filesystem just before starting init.

Display a user-friendly message when a kernel panic occurs

This will make the kernel correctly display the message in case a kernel panic happens and a running DRM driver
supports to do so. Without this, it would be more difficult to diagnose a panic: if no DRM driver is running, we'd be
on the VGA console which can only hold 24 lines and the relevant kernel message is often flushed away; if a DRM
driver is running, the display is often completely messed up on panic. As of Linux-6.12, none of the dedicated
drivers for mainstream GPU models really supports this, but it's supported by the “Simple framebuffer driver”
which runs on the VESA (or EFI) framebuffer before the dedicated GPU driver is loaded. If the dedicated GPU
driver is built as a module (instead of a part of the kernel image) and no initramfs is used, this functionality will
work just fine before the root file system is mounted and it's already enough for providing information about most
LFS configuration errors causing a panic (for example, an incorrect root= setting in Section 10.4, “Using GRUB
to Set Up the Boot Process”).

Panic screen formatter

Set this kmsg to make sure the last kernel messages lines are displayed when a kernel panic happens. The default,

user, would make the kernel show only a “user friendly” panic message which is not helpful on diagnostic. The
third choice, qr_code, would make the kernel to compress the last kernel message lines into a QR code and display
it. The QR code can hold more message lines than plain text and it can be decoded with an external device (like
a smart phone). But it requires a Rust compiler that LFS does not provide.

Mark VGA/VBE/EFI FB as generic system framebuffer  and Simple framebuffer driver

These allow to use the VESA framebuffer (or the EFI framebuffer if booting the LFS system via UEFI) as a
DRM device. The VESA framebuffer will be set up by GRUB (or the EFI framebuffer will be set up by the UEFI
firmware), so the DRM panic handler can function before the GPU-specific DRM driver is loaded.

---

Linux From Scratch - Version 13.1-systemd

Enable legacy fbdev support for your modesetting driver  and Framebuffer Console support

These are needed to display the Linux console on a GPU driven by a DRI (Direct Rendering Infrastructure) driver.
As CONFIG_DRM (Direct Rendering Manager) is enabled, we should enable these two options as well or we'll see
a blank screen once the DRI driver is loaded.

Support x2apic

Support running the interrupt controller of 64-bit x86 processors in x2APIC mode. x2APIC may be enabled by
firmware on 64-bit x86 systems, and a kernel without this option enabled will panic on boot if x2APIC is enabled
by firmware. This option has no effect, but also does no harm if x2APIC is disabled by the firmware.

**Alternatively, make oldconfig may be more appropriate in some situations. See the README file for more information.**

If desired, skip kernel configuration by copying the kernel config file, .config, from the host system (assuming it is
available) to the unpacked linux-7.1.8 directory. However, we do not recommend this option. It is often better to
explore all the configuration menus and create the kernel configuration from scratch.

Compile the kernel image and modules:

**make**

If using kernel modules, module configuration in /etc/modprobe.d may be required. Information pertaining to modules
and kernel configuration is located in Section 9.3, “Overview of Device and Module Handling” and in the kernel
documentation in the linux-7.1.8/Documentation directory. Also, modprobe.d(5) may be of interest.

Unless module support has been disabled in the kernel configuration, install the modules with:

**make modules_install**

After kernel compilation is complete, additional steps are required to complete the installation. Some files need to be
copied to the /boot directory.