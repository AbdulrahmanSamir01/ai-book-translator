A. Acronyms and Terms ..................................................................................................................................... 288
B. Acknowledgments ........................................................................................................................................... 291
C. Dependencies ................................................................................................................................................... 294
D. LFS Licenses ................................................................................................................................................... 309

D.1. Creative Commons License ................................................................................................................... 309
D.2. The MIT License ................................................................................................................................... 313
Index ........................................................................................................................................................................... 314

vii

---

Linux From Scratch - Version 13.1-systemd

# Preface

# Foreword

My journey to learn and better understand Linux began back in 1998. I had just installed my first Linux distribution
and had quickly become intrigued with the whole concept and philosophy behind Linux.

There are always many ways to accomplish a single task. The same can be said about Linux distributions. A great many
have existed over the years. Some still exist, some have morphed into something else, yet others have been relegated
to our memories. They all do things differently to suit the needs of their target audience. Because so many different
ways to accomplish the same end goal exist, I began to realize I no longer had to be limited by any one implementation.
Prior to discovering Linux, we simply put up with issues in other Operating Systems as you had no choice. It was what
it was, whether you liked it or not. With Linux, the concept of choice began to emerge. If you didn't like something,
you were free, even encouraged, to change it.

I tried a number of distributions and could not decide on any one. They were great systems in their own right. It wasn't
a matter of right and wrong anymore. It had become a matter of personal taste. With all that choice available, it became
apparent that there would not be a single system that would be perfect for me. So I set out to create my own Linux
system that would fully conform to my personal preferences.

To truly make it my own system, I resolved to compile everything from source code instead of using pre-compiled
binary packages. This “perfect” Linux system would have the strengths of various systems without their perceived
weaknesses. At first, the idea was rather daunting. I remained committed to the idea that such a system could be built.

After sorting through issues such as circular dependencies and compile-time errors, I finally built a custom-built Linux
system. It was fully operational and perfectly usable like any of the other Linux systems out there at the time. But it
was my own creation. It was very satisfying to have put together such a system myself. The only thing better would
have been to create each piece of software myself. This was the next best thing.

As I shared my goals and experiences with other members of the Linux community, it became apparent that there was
a sustained interest in these ideas. It quickly became plain that such custom-built Linux systems serve not only to meet
user specific requirements, but also serve as an ideal learning opportunity for programmers and system administrators
to enhance their (existing) Linux skills. Out of this broadened interest, the Linux From Scratch Project was born.

This Linux From Scratch book is the central core around that project. It provides the background and instructions
necessary for you to design and build your own system. While this book provides a template that will result in a correctly
working system, you are free to alter the instructions to suit yourself, which is, in part, an important part of this project.
You remain in control; we just lend a helping hand to get you started on your own journey.

I sincerely hope you will have a great time working on your own Linux From Scratch system and enjoy the numerous
benefits of having a system that is truly your own.

--
Gerard Beekmans
gerard@linuxfromscratch.org

# Audience

There are many reasons why you would want to read this book. One of the questions many people raise is, “why go
through all the hassle of manually building a Linux system from scratch when you can just download and install an
existing one?”

viii

---

Linux From Scratch - Version 13.1-systemd

One important reason for this project's existence is to help you learn how a Linux system works from the inside out.
Building an LFS system helps demonstrate what makes Linux tick, and how things work together and depend on each
other. One of the best things this learning experience can provide is the ability to customize a Linux system to suit
your own unique needs.

Another key benefit of LFS is that it gives you control of the system without relying on someone else's Linux
implementation. With LFS, you are in the driver's seat. You dictate every aspect of your system.

LFS allows you to create very compact Linux systems. With other distributions you are often forced to install a great
many programs you neither use nor understand. These programs waste resources. You may argue that with today's hard
drives and CPUs, wasted resources are no longer a consideration. Sometimes, however, you are still constrained by the
system's size, if nothing else. Think about bootable CDs, USB sticks, and embedded systems. Those are areas where
LFS can be beneficial.

Another advantage of a custom built Linux system is security. By compiling the entire system from source code, you
are empowered to audit everything and apply all the security patches you want. You don't have to wait for somebody
else to compile binary packages that fix a security hole. Unless you examine the patch and implement it yourself, you
have no guarantee that the new binary package was built correctly and adequately fixes the problem.

The goal of Linux From Scratch is to build a complete and usable foundation-level system. If you do not wish to build
your own Linux system from scratch, you may nevertheless benefit from the information in this book.

There are too many good reasons to build your own LFS system to list them all here. In the end, education is by far
the most important reason. As you continue your LFS experience, you will discover the power that information and
knowledge can bring.

# LFS Target Architectures

The primary target architectures of LFS are the AMD/Intel x86 (32-bit) and x86_64 (64-bit) CPUs. On the other hand,
the instructions in this book are also known to work, with some modifications, with the Power PC and ARM CPUs.
To build a system that utilizes one of these alternative CPUs, the main prerequisite, in addition to those on the next
page, is an existing Linux system such as an earlier LFS installation, Ubuntu, Red Hat/Fedora, SuSE, or some other
distribution that targets that architecture. (Note that a 32-bit distribution can be installed and used as a host system on
a 64-bit AMD/Intel computer.)

The gain from building on a 64-bit system, as compared to a 32-bit system, is minimal. For example, in a test build of
LFS-9.1 on a Core i7-4790 CPU based system, using 4 cores, the following statistics were measured:

Architecture Build Time     Build Size
32-bit       239.9 minutes  3.6 GB
64-bit       233.2 minutes  4.4 GB

As you can see, on the same hardware, the 64-bit build is only 3% faster (and 22% larger) than the 32-bit build. If
you plan to use LFS as a LAMP server, or a firewall, a 32-bit CPU may be good enough. On the other hand, several
packages in BLFS now need more than 4 GB of RAM to be built and/or to run; if you plan to use LFS as a desktop,
the LFS authors recommend building a 64-bit system.

The default 64-bit build that results from LFS is a “pure” 64-bit system. That is, it supports 64-bit executables only.
Building a “multi-lib” system requires compiling many applications twice, once for a 32-bit system and once for a 64-
bit system. This is not directly supported in LFS because it would interfere with the educational objective of providing
the minimal instructions needed for a basic Linux system. Some of the LFS/BLFS editors maintain a multilib fork of
LFS, accessible at https://www.linuxfromscratch.org/~thomas/multilib/index.html. But that's an advanced topic.

ix

---

Linux From Scratch - Version 13.1-systemd