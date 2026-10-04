# Change the MAC address as appropriate for your network device
MACAddress=12:34:45:78:90:AB

[Link]
Name=ether0
**EOF**

See systemd.link(5) for more information.

• In /boot/grub/grub.cfg, pass the option net.ifnames=0 on the kernel command line.

**9.2.1.2. Static IP Configuration**

The command below creates a basic configuration file for a Static IP setup (using both systemd-networkd and systemd-
resolved):

**cat > /etc/systemd/network/10-eth-static.network << "EOF"**
[Match]
Name=<network-device-name>

[Network]
Address=192.168.0.2/24
Gateway=192.168.0.1
DNS=192.168.0.1
Domains=<Your Domain Name>
**EOF**

Multiple DNS entries can be added if you have more than one DNS server. Do not include DNS or Domains entries
if you intend to use a static /etc/resolv.conf file.

---

Linux From Scratch - Version 13.1-systemd

**9.2.1.3. DHCP Configuration**

The command below creates a basic configuration file for an IPv4 DHCP setup:

**cat > /etc/systemd/network/10-eth-dhcp.network << "EOF"**
[Match]
Name=<network-device-name>

[Network]
DHCP=ipv4

[DHCPv4]
UseDomains=true
**EOF**

## 9.2.2. Creating the /etc/resolv.conf File

If the system is going to be connected to the Internet, it will need some means of Domain Name Service (DNS) name
resolution to resolve Internet domain names to IP addresses, and vice versa. This is best achieved by placing the IP
address of the DNS server, available from the ISP or network administrator, into /etc/resolv.conf.

**9.2.2.1. systemd-resolved Configuration**

### Note

If using methods incompatible with systemd-resolved to configure your network interfaces (ex: ppp, etc.), or
if using any type of local resolver (ex: bind, dnsmasq, unbound, etc.), or any other software that generates an

**/etc/resolv.conf (ex: a resolvconf program other than the one provided by systemd), the systemd-resolved**
service should not be used.

To disable systemd-resolved, issue the following command:

**systemctl disable systemd-resolved**

**When using systemd-resolved for DNS configuration, it creates the file /run/systemd/resolve/stub-resolv.conf.**
**And, if /etc/resolv.conf does not exist, it will be created by systemd-resolved as a symlink to /run/systemd/resolve/**

stub-resolv.conf. So it's unnecessary to create a /etc/resolv.conf manually.

### Note

**If you want to use systemd-resolved for the LFS system but you need to access the Internet in the**
chroot environment (for example, for building a BLFS package of which the build process requires an
Internet connection), create the /etc/resolv.conf file following the static configuration below for the
chroot environment so the name resolution will work in the chroot environment. When you exit the chroot
**environment, remove it so systemd-resolved will create the symlink on boot.**

---

Linux From Scratch - Version 13.1-systemd

**9.2.2.2. Static resolv.conf Configuration**

If a static /etc/resolv.conf is desired, create it by running the following command:

**cat > /etc/resolv.conf << "EOF"**

# Begin /etc/resolv.conf

domain <Your Domain Name>
nameserver <IP address of your primary nameserver>
nameserver <IP address of your secondary nameserver>

# End /etc/resolv.conf
**EOF**

The domain statement can be omitted or replaced with a search statement. See the man page for resolv.conf for more
details.

Replace <IP address of the nameserver> with the IP address of the DNS server most appropriate for your setup. There
will often be more than one entry (requirements demand secondary servers for fallback capability). If you only need
or want one DNS server, remove the second nameserver line from the file. The IP address may also be a router on the
local network. Another option is to use the Google Public DNS service using the IP addresses below as nameservers.

### Note

The Google Public IPv4 DNS addresses are 8.8.8.8 and 8.8.4.4 for IPv4, and 2001:4860:4860::8888 and

2001:4860:4860::8844 for IPv6.

## 9.2.3. Configuring the system hostname

During the boot process, the file /etc/hostname is used for establishing the system's hostname.

Create the /etc/hostname file and enter a hostname by running:

**echo "<lfs>" > /etc/hostname**

<lfs> needs to be replaced with the name given to the computer. Do not enter the Fully Qualified Domain Name
(FQDN) here. That information is put in the /etc/hosts file.

## 9.2.4. Customizing the /etc/hosts File

Decide on a fully-qualified domain name (FQDN), and possible aliases for use in the /etc/hosts file. If using static IP
addresses, you'll also need to decide on an IP address. The syntax for a hosts file entry is:

IP_address myhost.example.org aliases

Unless the computer is to be visible to the Internet (i.e., there is a registered domain and a valid block of assigned
IP addresses—most users do not have this), make sure that the IP address is in the private network IP address range.
Valid ranges are:

Private Network Address Range      Normal Prefix
10.0.0.1 - 10.255.255.254           8
172.x.0.1 - 172.x.255.254           16
192.168.y.1 - 192.168.y.254         24

x can be any number in the range 16-31. y can be any number in the range 0-255.

---

Linux From Scratch - Version 13.1-systemd

A valid private IP address could be 192.168.1.1.

If the computer is to be visible to the Internet, a valid FQDN can be the domain name itself, or a string resulted by
concatenating a prefix (often the hostname) and the domain name with a “.” character. And, you need to contact the
domain provider to resolve the FQDN to your public IP address.

Even if the computer is not visible to the Internet, a FQDN is still needed for certain programs, such as MTAs, to operate
properly. A special FQDN, localhost.localdomain, can be used for this purpose.

Create the /etc/hosts file using the following command:

**cat > /etc/hosts << "EOF"**

# Begin /etc/hosts

<192.168.0.2> <FQDN> [alias1] [alias2] ...
::1       ip6-localhost ip6-loopback
ff02::1   ip6-allnodes
ff02::2   ip6-allrouters

# End /etc/hosts
**EOF**

The <192.168.0.2> and <FQDN> values need to be changed for specific uses or requirements (if assigned an IP address by
a network/system administrator and the machine will be connected to an existing network). The optional alias name(s)
can be omitted, and the <192.168.0.2> line can be omitted if you are using a connection configured with DHCP or IPv6
Autoconfiguration, or using localhost.localdomain as the FQDN.

The /etc/hostname does not contain entries for localhost, localhost.localdomain, or the hostname (without a domain)
because they are handled by the myhostname NSS module, read the man page nss-myhostname(8) for details.

The ::1 entry is the IPv6 counterpart of 127.0.0.1 and represents the IPv6 loopback interface.

# 9.3. Overview of Device and Module Handling

In Chapter 8, we installed the udev daemon when systemd was built. Before we go into the details regarding how udev
works, a brief history of previous methods of handling devices is in order.

Linux systems in general traditionally used a static device creation method, whereby a great many device nodes were
created under /dev (sometimes literally thousands of nodes), regardless of whether the corresponding hardware devices
**actually existed. This was typically done via a MAKEDEV script, which contained a number of calls to the mknod**
program with the relevant major and minor device numbers for every possible device that might exist in the world.

Using the udev method, device nodes are only created for those devices which are detected by the kernel. These device
nodes are created each time the system boots; they are stored in a devtmpfs file system (a virtual file system that resides
entirely in system memory). Device nodes do not require much space, so the memory that is used is negligible.