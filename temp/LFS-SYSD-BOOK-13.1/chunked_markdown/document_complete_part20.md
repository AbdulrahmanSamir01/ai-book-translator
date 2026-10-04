In Chapter 8 (or “stage 3”), all the packages needed for the LFS system are built. Even if a package has already been
installed into the LFS system in a previous chapter, we still rebuild the package. The main reason for rebuilding these
packages is to make them stable: if we reinstall an LFS package on a completed LFS system, the reinstalled content of
the package should be the same as the content of the same package when first installed in Chapter 8. The temporary
packages installed in Chapter 6 or Chapter 7 cannot satisfy this requirement, because some optional features of them
are disabled because of either the missing dependencies or the “cross-compilation mode.” Additionally, a minor reason
for rebuilding the packages is to run the test suites.

## Other Procedural Details

The cross-compiler will be installed in a separate $LFS/tools directory, since it will not be part of the final system.

**Binutils is installed first because the configure runs of both gcc and glibc perform various feature tests on the assembler**
and linker to determine which software features to enable or disable. This is more important than one might realize at
first. An incorrectly configured gcc or glibc can result in a subtly broken toolchain, where the impact of such breakage
might not show up until near the end of the build of an entire distribution. A test suite failure will usually highlight this
error before too much additional work is performed.

Binutils installs its assembler and linker in two locations, $LFS/tools/bin and $LFS/tools/$LFS_TGT/bin. The tools in
one location are hard linked to the other. An important facet of the linker is its library search order. Detailed information
**can be obtained from ld by passing it the --verbose flag. For example, $LFS_TGT-ld --verbose | grep SEARCH will**
illustrate the current search paths and their order. (Note that this example can be run as shown only while logged in as
**user lfs. If you come back to this page later, replace $LFS_TGT-ld with ld).**

---

Linux From Scratch - Version 13.1-systemd

**The next package installed is gcc. An example of what can be seen during its run of configure is:**

checking what assembler to use... /mnt/lfs/tools/i686-lfs-linux-gnu/bin/as
checking what linker to use... /mnt/lfs/tools/i686-lfs-linux-gnu/bin/ld

This is important for the reasons mentioned above. It also demonstrates that gcc's configure script does not search the
**PATH directories to find which tools to use. However, during the actual operation of gcc itself, the same search paths**
**are not necessarily used. To find out which standard linker gcc will use, run: $LFS_TGT-gcc -print-prog-name=ld.**
**(Again, remove the $LFS_TGT- prefix if coming back to this later.)**

**Detailed information can be obtained from gcc by passing it the -v command line option while compiling a program. For**
**example, $LFS_TGT-gcc -v example.c (or without  $LFS_TGT- if coming back later) will show detailed information**
**about the preprocessor, compilation, and assembly stages, including gcc's search paths for included headers and their**
order.

Next up: sanitized Linux API headers. These allow the standard C library (glibc) to interface with features that the
Linux kernel will provide.

Next comes glibc. This is the first package that we cross-compile. We use the --host=$LFS_TGT option to make the build
system to use those tools prefixed with $LFS_TGT-, and the --build=$(../scripts/config.guess) option to enable “the
cross-compilation mode” as we've discussed. The DESTDIR variable is used to force installation into the LFS file system.

As mentioned above, the standard C++ library is compiled next, followed in Chapter 6 by other programs that must
be cross-compiled to break circular dependencies at build time. The steps for those packages are similar to the steps
for glibc.

At the end of Chapter 6 the native LFS compiler is installed. First binutils-pass2 is built, in the same DESTDIR directory
as the other programs, then the second pass of gcc is constructed, omitting some non-critical libraries.

Upon entering the chroot environment in Chapter 7, the temporary installations of programs needed for the proper
operation of the toolchain are performed. From this point onwards, the core toolchain is self-contained and self-hosted.
In Chapter 8, final versions of all the packages needed for a fully functional system are built, tested, and installed.

# General Compilation Instructions

### Caution

During a development cycle of LFS, the instructions in the book are often modified to adapt for a package
update or take the advantage of new features from updated packages. Mixing up the instructions of different
versions of the LFS book can cause subtle breakages. This kind of issue is generally a result from reusing
some script created for a prior LFS release. Such a reuse is strongly discouraged. If you are reusing scripts
for a prior LFS release for any reason, you'll need to be very careful to update the scripts to match current
version of the LFS book.

Here are some things you should know about building each package:

• Several packages are patched before compilation, but only when the patch is needed to circumvent a problem.
A patch is often needed in both the current and the following chapters, but sometimes, when the same package
is built more than once, the patch is not needed right away. Therefore, do not be concerned if instructions for a
downloaded patch seem to be missing. Warning messages about offset or fuzz may also be encountered when
applying a patch. Do not worry about these warnings; the patch was still successfully applied.

---

Linux From Scratch - Version 13.1-systemd

• During the compilation of most packages, some warnings will scroll by on the screen. These are normal and can
safely be ignored. These warnings are usually about deprecated, but not invalid, use of the C or C++ syntax. C
standards change fairly often, and some packages have not yet been updated. This is not a serious problem, but it
does cause the warnings to appear.

• Check one last time that the LFS environment variable is set up properly:

**echo $LFS**

Make sure the output shows the path to the LFS partition's mount point, which is /mnt/lfs, using our example.

• Finally, two important items must be emphasized:

### Important

The build instructions assume that the Host System Requirements, including symbolic links, have been
set properly:

**• bash is the shell in use.**

**• sh is a symbolic link to bash.**

**• /usr/bin/awk is a symbolic link to gawk.**

**• /usr/bin/yacc is a symbolic link to bison, or to a small script that executes bison.**

### Important

Here is a synopsis of the build process.
1. Place all the sources and patches in a directory that will be accessible from the chroot environment,
such as /mnt/lfs/sources/.
2. Change to the /mnt/lfs/sources/ directory.
3. For each package:
**a. Using the tar program, extract the package to be built. In Chapter 5 and Chapter 6, ensure you are**

the lfs user when extracting the package.

**Do not use any method except the tar command to extract the source code. Notably, using the cp**
**-R command to copy the source code tree somewhere else can destroy timestamps in the source**
tree, and cause the build to fail.
b. Change to the directory created when the package was extracted.
c. Follow the instructions for building the package.
d. Change back to the sources directory when the build is complete.
e. Delete the extracted source directory unless instructed otherwise.

---

Linux From Scratch - Version 13.1-systemd