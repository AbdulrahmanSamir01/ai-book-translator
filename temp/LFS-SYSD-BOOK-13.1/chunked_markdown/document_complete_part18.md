# 4.6. About the Test Suites

Most packages provide a test suite. Running the test suite for a newly built package is a good idea because it can provide
a “sanity check” indicating that everything compiled correctly. A test suite that passes its set of checks usually proves
that the package is functioning as the developer intended. It does not, however, guarantee that the package is totally
bug free.

---

Linux From Scratch - Version 13.1-systemd

Some test suites are more important than others. For example, the test suites for the core toolchain packages—GCC,
binutils, and glibc—are of the utmost importance due to their central role in a properly functioning system. The test
suites for GCC and glibc can take a very long time to complete, especially on slower hardware, but are strongly
recommended.

### Note

Running the test suites in Chapter 5 and Chapter 6 is pointless; since the test programs are compiled with a
cross-compiler, they probably can't run on the build host.

A common issue with running the test suites for binutils and GCC is running out of pseudo terminals (PTYs). This can
result in a large number of failing tests. This may happen for several reasons, but the most likely cause is that the host
system does not have the devpts file system set up correctly. This issue is discussed in greater detail at https://www.
linuxfromscratch.org/lfs/faq.html#no-ptys.

Sometimes package test suites will fail for reasons which the developers are aware of and have deemed non-critical.
Consult the logs located at https://www.linuxfromscratch.org/lfs/build-logs/13.1/ to verify whether or not these failures
are expected. This site is valid for all test suites throughout this book.

---

Linux From Scratch - Version 13.1-systemd

# Part III. Building the LFS Cross

# Toolchain and Temporary Tools

---

Linux From Scratch - Version 13.1-systemd

# Important Preliminary Material

# Introduction

This part is divided into three stages: first, building a cross compiler and its associated libraries; second, using this
cross toolchain to build several utilities in a way that isolates them from the host distribution; and third, entering the
chroot environment (which further improves host isolation) and constructing the remaining tools needed to build the
final system.

### Important

This is where the real work of building a new system begins. Be very careful to follow the instructions
exactly as the book shows them. You should try to understand what each command does, and no matter how
eager you are to finish your build, you should refrain from blindly typing the commands as shown. Read
the documentation when there is something you do not understand. Also, keep track of your typing and of
**the output of commands, by using the tee utility to send the terminal output to a file. This makes debugging**
easier if something goes wrong.

**The next section is a technical introduction to the build process, while the following one presents very important**
general instructions.

# Toolchain Technical Notes

This section explains some of the rationale and technical details behind the overall build method. Don't try to
immediately understand everything in this section. Most of this information will be clearer after performing an actual
build. Come back and re-read this chapter at any time during the build process.

The overall goal of Chapter 5 and Chapter 6 is to produce a temporary area containing a set of tools that are known to
**be good, and that are isolated from the host system. By using the chroot command, the compilations in the remaining**
chapters will be isolated within that environment, ensuring a clean, trouble-free build of the target LFS system. The
build process has been designed to minimize the risks for new readers, and to provide the most educational value at
the same time.

This build process is based on cross-compilation. Cross-compilation is normally used to build a compiler and its
associated toolchain for a machine different from the one that is used for the build. This is not strictly necessary for
LFS, since the machine where the new system will run is the same as the one used for the build. But cross-compilation
has one great advantage: anything that is cross-compiled cannot depend on the host environment.

## About Cross-Compilation

### Note

The LFS book is not (and does not contain) a general tutorial to build a cross- (or native) toolchain. Don't
use the commands in the book for a cross-toolchain for some purpose other than building LFS, unless you
really understand what you are doing.

It's known installing GCC pass 2 will break the cross-toolchain. We don't consider it a bug because GCC pass
2 is the last package to be cross-compiled in the book, and we won't “fix” it until we really need to cross-
compile some package after GCC pass 2 in the future.

---

Linux From Scratch - Version 13.1-systemd

Cross-compilation involves some concepts that deserve a section of their own. Although this section may be omitted
on a first reading, coming back to it later will help you gain a fuller understanding of the process.

Let us first define some terms used in this context.

The build

is the machine where we build programs. Note that this machine is also referred to as the “host.”

The host

is the machine/system where the built programs will run. Note that this use of “host” is not the same as in other
sections.

The target

is only used for compilers. It is the machine the compiler produces code for. It may be different from both the
build and the host.

As an example, let us imagine the following scenario (sometimes referred to as “Canadian Cross”). We have a compiler
on a slow machine only, let's call it machine A, and the compiler ccA. We also have a fast machine (B), but no compiler
for (B), and we want to produce code for a third, slow machine (C). We will build a compiler for machine C in three
stages.

**Stage**
**Build**
**Host**
**Target**
**Action**

A
A
B
Build
cross-
compiler
cc1 using
ccA on
machine
A.

A
B
C
Build
cross-
compiler
cc2 using
cc1 on
machine
A.

B
C
C
Build
compiler
ccC using
cc2 on
machine
B.

Then, all the programs needed by machine C can be compiled using cc2 on the fast machine B. Note that unless B can
run programs produced for C, there is no way to test the newly built programs until machine C itself is running. For
example, to run a test suite on ccC, we may want to add a fourth stage:

**Stage**
**Build**
**Host**
**Target**
**Action**

C
C
C
Rebuild
and test

---

Linux From Scratch - Version 13.1-systemd

**Stage**
**Build**
**Host**
**Target**
**Action**
ccC using
ccC on
machine
C.

In the example above, only cc1 and cc2 are cross-compilers, that is, they produce code for a machine different from the
one they are run on. The other compilers ccA and ccC produce code for the machine they are run on. Such compilers
are called native compilers.

## Implementation of Cross-Compilation for LFS

### Note

All the cross-compiled packages in this book use an autoconf-based building system. The autoconf-based
building system accepts system types in the form cpu-vendor-kernel-os, referred to as the system triplet. Since
the vendor field is often irrelevant, autoconf lets you omit it.

An astute reader may wonder why a “triplet” refers to a four component name. The kernel field and the
os field began as a single “system” field. Such a three-field form is still valid today for some systems, for
example, x86_64-unknown-freebsd. But two systems can share the same kernel and still be too different to use
the same triplet to describe them. For example, Android running on a mobile phone is completely different
from Ubuntu running on an ARM64 server, even though they are both running on the same type of CPU
(ARM64) and using the same kernel (Linux).