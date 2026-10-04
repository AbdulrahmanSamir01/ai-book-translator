# 4.4. Setting Up the Environment

**Set up a good working environment by creating two new startup files for the bash shell. While logged in as user lfs,**
issue the following command to create a new .bash_profile:

**cat > ~/.bash_profile << "EOF"**
exec env -i HOME=$HOME TERM=$TERM PS1='\u:\w\$ ' /bin/bash
**EOF**

**When logged on as user lfs, or when switched to the lfs user using an su command with the “-” option, the initial shell**
is a login shell which reads the /etc/profile of the host (probably containing some settings and environment variables)
**and then .bash_profile. The exec env -i.../bin/bash command in the .bash_profile file replaces the running shell with**
a new one with a completely empty environment, except for the HOME, TERM, and PS1 variables. This ensures that no
unwanted and potentially hazardous environment variables from the host system leak into the build environment.

---

Linux From Scratch - Version 13.1-systemd

The new instance of the shell is a non-login shell, which does not read, and execute, the contents of the /etc/profile
or .bash_profile files, but rather reads, and executes, the .bashrc file instead. Create the .bashrc file now:

**cat > ~/.bashrc << "EOF"**
set +h
umask 022
LFS=/mnt/lfs
LC_ALL=POSIX
LFS_TGT=$(uname -m)-lfs-linux-gnu
PATH=/usr/bin
if [ ! -L /bin ]; then PATH=/bin:$PATH; fi
PATH=$LFS/tools/bin:$PATH
CONFIG_SITE=$LFS/usr/share/config.site
export LFS LC_ALL LFS_TGT PATH CONFIG_SITE
**EOF**

**The meaning of the settings in .bashrc**

set +h

**The set +h command turns off bash's hash function. Hashing is ordinarily a useful feature—bash uses a hash**
table to remember the full path to executable files to avoid searching the PATH time and again to find the same
executable. However, the new tools should be used as soon as they are installed. Switching off the hash function
forces the shell to search the PATH whenever a program is to be run. As such, the shell will find the newly compiled
tools in $LFS/tools/bin as soon as they are available without remembering a previous version of the same program
provided by the host distro, in /usr/bin or /bin.

umask 022

Setting the umask as we've already explained in Section 2.6, “Setting the $LFS Variable and the Umask.”

LFS=/mnt/lfs

The LFS variable should be set to the chosen mount point.

LC_ALL=POSIX

The LC_ALL variable controls the localization of certain programs, making their messages follow the conventions
of a specified country. Setting LC_ALL to “POSIX” or “C” (the two are equivalent) ensures that everything will
work as expected in the cross-compilation environment.

LFS_TGT=$(uname -m)-lfs-linux-gnu

The LFS_TGT variable sets a non-default, but compatible machine description for use when building our cross-
compiler and linker and when cross-compiling our temporary toolchain. More information is provided by
Toolchain Technical Notes.

PATH=/usr/bin

Many modern Linux distributions have merged /bin and /usr/bin. When this is the case, the standard PATH variable
should be set to /usr/bin/ for the Chapter 6 environment. When this is not the case, the following line adds /

bin to the path.

if [ ! -L /bin ]; then PATH=/bin:$PATH; fi

If /bin is not a symbolic link, it must be added to the PATH variable.

PATH=$LFS/tools/bin:$PATH

By putting $LFS/tools/bin ahead of the standard PATH, the cross-compiler installed at the beginning of Chapter 5
is picked up by the shell immediately after its installation. This, combined with turning off hashing, limits the risk
that the compiler from the host is used instead of the cross-compiler.

---

Linux From Scratch - Version 13.1-systemd

CONFIG_SITE=$LFS/usr/share/config.site

**In Chapter 5 and Chapter 6, if this variable is not set, configure scripts may attempt to load configuration items**
specific to some distributions from /usr/share/config.site on the host system. Override it to prevent potential
contamination from the host.

export ...

While the preceding commands have set some variables, in order to make them visible within any sub-shells, we
export them.

### Important

Several commercial distributions add an undocumented instantiation of /etc/bash.bashrc to the initialization
**of bash. This file has the potential to modify the lfs user's environment in ways that can affect the building**
of critical LFS packages. To make sure the lfs user's environment is clean, check for the presence of /etc/

bash.bashrc and, if present, move it out of the way. As the root user, run:

**[ ! -e /etc/bash.bashrc ] || mv -v /etc/bash.bashrc /etc/bash.bashrc.NOUSE**

When the lfs user is no longer needed (at the beginning of Chapter 7), you may safely restore /etc/bash.

bashrc (if desired).

Note that the LFS Bash package we will build in Section 8.39, “Bash-5.3” is not configured to load or execute

/etc/bash.bashrc, so this file is useless on a completed LFS system.

For many modern systems with multiple processors (or cores) the compilation time for a package can be reduced by
performing a "parallel make" by telling the make program how many processors are available via a command line
option or an environment variable. For instance, an Intel Core i9-13900K processor has 8 P (performance) cores and 16
E (efficiency) cores, and a P core can simultaneously run two threads so each P core are modeled as two logical cores
by the Linux kernel. As the result there are 32 logical cores in total. One obvious way to use all these logical cores is
**allowing make to spawn up to 32 build jobs. This can be done by passing the -j32 option to make:**

**make -j32**

**Or set the MAKEFLAGS environment variable and its content will be automatically used by make as command line options:**

**export MAKEFLAGS=-j32**

### Important

**Never pass a -j option without a number to make or set such an option in MAKEFLAGS. Doing so will allow**
**make to spawn infinite build jobs and cause system stability problems.**

To use all logical cores available for building packages in Chapter 5 and Chapter 6, set MAKEFLAGS now in .bashrc:

**cat >> ~/.bashrc << "EOF"**
export MAKEFLAGS=-j$(nproc)
**EOF**

Replace $(nproc) with the number of logical cores you want to use if you don't want to use all the logical cores.

**Finally, to ensure the environment is fully prepared for building the temporary tools, force the bash shell to read the**
new user profile:

**source ~/.bash_profile**

---

Linux From Scratch - Version 13.1-systemd

# 4.5. About SBUs

Many people would like to know beforehand approximately how long it takes to compile and install each package.
Because Linux From Scratch can be built on many different systems, it is impossible to provide absolute time estimates.
The biggest package (gcc) will take approximately 5 minutes on the fastest systems, but could take days on slower
systems! Instead of providing actual times, the Standard Build Unit (SBU) measure will be used instead.

The SBU measure works as follows. The first package to be compiled is binutils in Chapter 5. The time it takes to
compile using one core is what we will refer to as the Standard Build Unit or SBU. All other compile times will be
expressed in terms of this unit of time.

For example, consider a package whose compilation time is 4.5 SBUs. This means that if your system took 4 minutes
to compile and install the first pass of binutils, it will take approximately 18 minutes to build the example package.
Fortunately, most build times are shorter than one SBU.

SBUs are not entirely accurate because they depend on many factors, including the host system's version of GCC. They
are provided here to give an estimate of how long it might take to install a package, but the numbers can vary by as
much as dozens of minutes in some cases.

On some newer systems, the motherboard is capable of controlling the system clock speed. This can be controlled
**with a command such as powerprofilesctl. This is not available in LFS, but may be available on the host distro. After**
LFS is complete, it can be added to a system with the procedures at the  BLFS power-profiles-daemon page. Before
measuring the build time of any package it is advisable to use a system power profile set for maximum performance
(and maximum power consumption). Otherwise the measured SBU value may be inaccurate because the system may
react differently when building binutils-pass1 or other packages. Be aware that a significant inaccuracy can still show
up even if the same profile is used for both packages because the system may respond slower if the system is idle when
starting the build procedure. Setting the power profile to “performance” will minimize this problem. And obviously
doing so will also make the system build LFS faster.

**If powerprofilesctl is available, issue the powerprofilesctl set performance command to select the performance**
**profile. Some distros provides the tuned-adm command for managing the profiles instead of powerprofilesctl, on these**
**distros issue the tuned-adm profile throughput-performance command to select the throughput-performance profile.**

### Note

When multiple processors are used in this way, the SBU units in the book will vary even more than they
normally would. In some cases, the make step will simply fail. Analyzing the output of the build process will
also be more difficult because the lines from different processes will be interleaved. If you run into a problem
with a build step, revert to a single processor build to properly analyze the error messages.

The times presented here for all packages (except binutils-pass1 which is based on one core) are based upon
using four cores (-j4). The times in Chapter 8 also include the time to run the regression tests for the package
unless specified otherwise.