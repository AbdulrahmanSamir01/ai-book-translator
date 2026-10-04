# 8.67. IPRoute2-7.1.0

The IPRoute2 package contains programs for basic and advanced IPV4-based networking.

**Approximate build time:**
0.1 SBU
**Required disk space:**
18 MB

## 8.67.1. Installation of IPRoute2

**The arpd program included in this package will not be built since it depends on Berkeley DB, which is not installed**
**in LFS. However, a directory and a man page for arpd will still be installed. Prevent this by running the commands**
shown below.

**sed -i /ARPD/d Makefile**
**rm -fv man/man8/arpd.8**

Compile the package:

**make NETNS_RUN_DIR=/run/netns**

This package does not have a working test suite.

Install the package:

**make SBINDIR=/usr/sbin install**

If desired, install the documentation:

**install -vDm644 COPYING README* -t /usr/share/doc/iproute2-7.1.0**

## 8.67.2. Contents of IPRoute2

**Installed programs:**
bridge, ctstat (link to lnstat), genl, ifstat, ip, lnstat, nstat, routel, rtacct, rtmon, rtpr, rtstat
(link to lnstat), ss, and tc
**Installed directories:**
/etc/iproute2, /usr/lib/tc, and /usr/share/doc/iproute2-7.1.0

**Short Descriptions**

**bridge**
Configures network bridges

**ctstat**
Connection status utility

**genl**
Generic netlink utility front end

**ifstat**
Shows interface statistics, including the number of packets transmitted and received, by interface

**ip**
The main executable. It has several different functions, including these:
**ip link <device> allows users to look at the state of devices and to make changes**
**ip addr allows users to look at addresses and their properties, add new addresses, and delete old ones**
**ip neighbor allows users to look at neighbor bindings and their properties, add new neighbor entries, and**
delete old ones
**ip rule allows users to look at the routing policies and change them**
**ip route allows users to look at the routing table and change routing table rules**
**ip tunnel allows users to look at the IP tunnels and their properties, and change them**
**ip maddr allows users to look at the multicast addresses and their properties, and change them**
**ip mroute allows users to set, change, or delete the multicast routing**

---

Linux From Scratch - Version 13.1-systemd

**ip monitor allows users to continuously monitor the state of devices, addresses and routes**

**lnstat**
Provides Linux network statistics; it is a generalized and more feature-complete replacement for the old
**rtstat program**

**nstat**
Displays network statistics

**routel**
**A component of ip route, for listing the routing tables**

**rtacct**
Displays the contents of /proc/net/rt_acct

**rtmon**
Route monitoring utility

**rtpr**
**Converts the output of ip -o into a readable form**

**rtstat**
Route status utility

**ss**
**Similar to the netstat command; shows active connections**

**tc**
Traffic control for Quality of Service (QoS) and Class of Service (CoS) implementations
**tc qdisc allows users to set up the queueing discipline**
**tc class allows users to set up classes based on the queueing discipline scheduling**
**tc filter allows users to set up the QoS/CoS packet filtering**
**tc monitor can be used to view changes made to Traffic Control in the kernel.**

---

Linux From Scratch - Version 13.1-systemd

# 8.68. Kbd-2.10.0

The Kbd package contains key-table files, console fonts, and keyboard utilities.

**Approximate build time:**
0.1 SBU
**Required disk space:**
45 MB

## 8.68.1. Installation of Kbd

The behavior of the backspace and delete keys is not consistent across the keymaps in the Kbd package. The following
patch fixes this issue for i386 keymaps:

**patch -Np1 -i ../kbd-2.10.0-backspace-1.patch**

After patching, the backspace key generates the character with code 127, and the delete key generates a well-known
escape sequence.

**Remove the redundant resizecons program (it requires the defunct svgalib to provide the video mode files - for normal**
**use setfont sizes the console appropriately) together with its manpage.**

**sed -i '/RESIZECONS_PROGS=/s/yes/no/' configure**
**sed -i 's/resizecons.8 //' docs/man/man8/Makefile.in**

Prepare Kbd for compilation:

**./configure --prefix=/usr --disable-vlock**

**The meaning of the configure option:**

--disable-vlock

This option prevents the vlock utility from being built because it requires the PAM library, which isn't available
in the chroot environment.

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

### Note

For some languages (e.g., Belarusian) the Kbd package doesn't provide a useful keymap where the stock
“by” keymap assumes the ISO-8859-5 encoding, and the CP1251 keymap is normally used. Users of such
languages have to download working keymaps separately.

If desired, install the documentation:

**cp -R -v docs/doc -T /usr/share/doc/kbd-2.10.0**

---

Linux From Scratch - Version 13.1-systemd

## 8.68.2. Contents of Kbd

**Installed programs:**
chvt, deallocvt, dumpkeys, fgconsole, getkeycodes, kbdinfo, kbd_mode, kbdrate,
loadkeys, loadunimap, mapscrn, openvt, psfaddtable (link to psfxtable), psfgettable (link
to psfxtable), psfstriptable (link to psfxtable), psfxtable, setfont, setkeycodes, setleds,
setmetamode, setvtrgb, showconsolefont, showkey, unicode_start, and unicode_stop
**Installed directories:**
/usr/share/consolefonts, /usr/share/consoletrans, /usr/share/keymaps, /usr/share/doc/
kbd-2.10.0, and /usr/share/unimaps

**Short Descriptions**

**chvt**
Changes the foreground virtual terminal

**deallocvt**
Deallocates unused virtual terminals

**dumpkeys**
Dumps the keyboard translation tables

**fgconsole**
Prints the number of the active virtual terminal

**getkeycodes**
Prints the kernel scancode-to-keycode mapping table

**kbdinfo**
Obtains information about the status of a console

**kbd_mode**
Reports or sets the keyboard mode

**kbdrate**
Sets the keyboard repeat and delay rates

**loadkeys**
Loads the keyboard translation tables

**loadunimap**
Loads the kernel unicode-to-font mapping table

**mapscrn**
An obsolete program that used to load a user-defined output character mapping table into the
**console driver; this is now done by setfont**

**openvt**
Starts a program on a new virtual terminal (VT)

**psfaddtable**
Adds a Unicode character table to a console font

**psfgettable**
Extracts the embedded Unicode character table from a console font

**psfstriptable**
Removes the embedded Unicode character table from a console font

**psfxtable**
Handles Unicode character tables for console fonts

**setfont**
Changes the Enhanced Graphic Adapter (EGA) and Video Graphics Array (VGA) fonts on
the console

**setkeycodes**
Loads kernel scancode-to-keycode mapping table entries; this is useful if there are unusual
keys on the keyboard

**setleds**
Sets the keyboard flags and Light Emitting Diodes (LEDs)

**setmetamode**
Defines the keyboard meta-key handling

**setvtrgb**
Sets the console color map in all virtual terminals

**showconsolefont**
Shows the current EGA/VGA console screen font

**showkey**
Reports the scancodes, keycodes, and ASCII codes of the keys pressed on the keyboard

**unicode_start**
Puts the keyboard and console in UNICODE mode [Don't use this program unless your
keymap file is in the ISO-8859-1 encoding. For other encodings, this utility produces incorrect
results.]

**unicode_stop**
Reverts keyboard and console from UNICODE mode

---

Linux From Scratch - Version 13.1-systemd

# 8.69. Libpipeline-1.5.8

The Libpipeline package contains a library for manipulating pipelines of subprocesses in a flexible and convenient way.

**Approximate build time:**
0.1 SBU
**Required disk space:**
10 MB

## 8.69.1. Installation of Libpipeline

Prepare Libpipeline for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

The tests require the Check library that we've removed from LFS.

Install the package:

**make install**

## 8.69.2. Contents of Libpipeline

**Installed library:**
libpipeline.so

**Short Descriptions**

libpipeline
This library is used to safely construct pipelines between subprocesses

---

Linux From Scratch - Version 13.1-systemd