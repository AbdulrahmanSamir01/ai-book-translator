## 9.3.4. Useful Reading

Additional helpful documentation is available at the following sites:

• A Userspace Implementation of devfs http://www.kroah.com/linux/talks/ols_2003_udev_paper/Reprint-Kroah-
Hartman-OLS2003.pdf

• The sysfs Filesystem https://www.kernel.org/pub/linux/kernel/people/mochel/doc/papers/ols-2005/mochel.pdf

# 9.4. Managing Devices

## 9.4.1. Dealing with Duplicate Devices

As explained in Section 9.3, “Overview of Device and Module Handling,” the order in which devices with the same
function appear in /dev is essentially random. E.g., if you have a USB web camera and a TV tuner, sometimes /dev/

video0 refers to the camera and /dev/video1 refers to the tuner, and sometimes after a reboot the order changes. For
all classes of hardware except sound cards and network cards, this is fixable by creating udev rules to create persistent
symlinks. The case of network cards is covered separately in Section 9.2, “General Network Configuration,” and sound
card configuration can be found in BLFS.

For each of your devices that is likely to have this problem (even if the problem doesn't exist in your current Linux
distribution), find the corresponding directory under /sys/class or /sys/block. For video devices, this may be /sys/

class/video4linux/videoX. Figure out the attributes that identify the device uniquely (usually, vendor and product IDs
and/or serial numbers work):

**udevadm info -a -p /sys/class/video4linux/video0**

---

Linux From Scratch - Version 13.1-systemd

Then write rules that create the symlinks, e.g.:

**cat > /etc/udev/rules.d/83-duplicate_devs.rules << "EOF"**

# Persistent symlinks for webcam and tuner
KERNEL=="video*", ATTRS{idProduct}=="1910", ATTRS{idVendor}=="0d81", SYMLINK+="webcam"
KERNEL=="video*", ATTRS{device}=="0x036f",  ATTRS{vendor}=="0x109e", SYMLINK+="tvtuner"

**EOF**

The result is that /dev/video0 and /dev/video1 devices still refer randomly to the tuner and the web camera (and thus
should never be used directly), but there are symlinks /dev/tvtuner and /dev/webcam that always point to the correct
device.

# 9.5. Configuring the System Clock

**This section discusses how to configure the systemd-timedated system service, which configures the system clock**
and timezone.

**If you cannot remember whether or not the hardware clock is set to UTC, find out by running the hwclock --localtime**

**--show command. This will display what the current time is according to the hardware clock. If this time matches**
**whatever your watch says, then the hardware clock is set to local time. If the output from hwclock is not local time,**
chances are it is set to UTC time. Verify this by adding or subtracting the proper amount of hours for the timezone
**to the time shown by hwclock. For example, if you are currently in the MST timezone, which is also known as GMT**
-0700, add seven hours to the local time.

**systemd-timedated reads /etc/adjtime, and depending on the contents of the file, sets the clock to either UTC or**
local time.

Create the /etc/adjtime file with the following contents if your hardware clock is set to local time:

**cat > /etc/adjtime << "EOF"**
0.0 0 0.0
LOCAL
**EOF**

**If /etc/adjtime isn't present at first boot, systemd-timedated will assume that hardware clock is set to UTC and adjust**
the file according to that.

**You can also use the timedatectl utility to tell systemd-timedated if your hardware clock is set to UTC or local time:**

**timedatectl set-local-rtc 1**

**timedatectl can also be used to change system time and time zone.**

To change your current system time, issue:

**timedatectl set-time YYYY-MM-DD HH:MM:SS**

The hardware clock will also be updated accordingly.

To change your current time zone, issue:

**timedatectl set-timezone TIMEZONE**

You can get a list of available time zones by running:

**timedatectl list-timezones**

---

Linux From Scratch - Version 13.1-systemd

### Note

**Please note that the timedatectl command doesn't work in the chroot environment. It can only be used after**
the LFS system is booted with systemd.

## 9.5.1. Network Time Synchronization

**Starting with version 213, systemd ships a daemon called systemd-timesyncd which can be used to synchronize the**
system time with remote NTP servers.

The daemon is not intended as a replacement for the well established NTP daemon, but as a client only implementation
of the SNTP protocol which can be used for less advanced tasks and on resource limited systems.

**Starting with systemd version 216, the systemd-timesyncd daemon is enabled by default. If you want to disable it,**
issue the following command:

**systemctl disable systemd-timesyncd**

**The /etc/systemd/timesyncd.conf file can be used to change the NTP servers that systemd-timesyncd synchronizes**
with.

**Please note that when system clock is set to Local Time, systemd-timesyncd won't update hardware clock.**

# 9.6. Configuring the Linux Console

**This section discusses how to configure the systemd-vconsole-setup system service, which configures the virtual**
console font and console keymap.

**The systemd-vconsole-setup service reads the /etc/vconsole.conf file for configuration information. Decide which**
keymap and screen font will be used. Various language-specific HOWTOs can also help with this, see https://tldp.org/
**HOWTO/HOWTO-INDEX/other-lang.html. Examine the output of localectl list-keymaps for a list of valid console**
keymaps. Look in the /usr/share/consolefonts directory for valid screen fonts.

The /etc/vconsole.conf file should contain lines of the form: VARIABLE=value. The following variables are recognized:

KEYMAP

This variable specifies the key mapping table for the keyboard. If unset, it defaults to us.

KEYMAP_TOGGLE

This variable can be used to configure a second toggle keymap and is unset by default.

FONT

This variable specifies the font used by the virtual console.

FONT_MAP

This variable specifies the console map to be used.

FONT_UNIMAP

This variable specifies the Unicode font map.

We'll use C.UTF-8 as the locale for interactive sessions in the Linux console in Section 9.7, “Configuring the
System Locale.” The console fonts shipped by the Kbd package containing the glyphs for all characters from the
program messages in the C.UTF-8 locale are LatArCyrHeb*.psfu.gz, LatGrkCyr*.psfu.gz, Lat2-Terminus16.psfu.gz,

---

Linux From Scratch - Version 13.1-systemd

and pancyrillic.f16.psfu.gz in /usr/share/consolefonts (the other shipped console fonts lack glyphs of some
characters like the Unicode left/right quotation marks and the Unicode English dash). So set one of them, for example

Lat2-Terminus16.psfu.gz as the default console font:

**echo FONT=Lat2-Terminus16 > /etc/vconsole.conf**

An example for a German keyboard and console is given below:

**cat > /etc/vconsole.conf << "EOF"**
KEYMAP=de-latin1
FONT=Lat2-Terminus16
**EOF**

**You can change KEYMAP value at runtime by using the localectl utility:**

**localectl set-keymap MAP**

### Note

**Please note that the localectl command doesn't work in the chroot environment. It can only be used after the**
LFS system is booted with systemd.

**You can also use localectl utility with the corresponding parameters to change X11 keyboard layout, model, variant**
and options:

**localectl set-x11-keymap LAYOUT [MODEL] [VARIANT] [OPTIONS]**

**To list possible values for localectl set-x11-keymap parameters, run localectl with parameters listed below:**

list-x11-keymap-models

Shows known X11 keyboard mapping models.

list-x11-keymap-layouts

Shows known X11 keyboard mapping layouts.

list-x11-keymap-variants

Shows known X11 keyboard mapping variants.

list-x11-keymap-options

Shows known X11 keyboard mapping options.

### Note

Using any of the parameters listed above requires the XKeyboard-Config package from BLFS.