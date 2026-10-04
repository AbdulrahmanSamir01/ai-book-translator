## 8.61.2. Contents of Coreutils

**Installed programs:**
[, b2sum, base32, base64, basename, basenc, cat, chgrp, chmod, chown, chroot, cksum,
comm, cp, csplit, cut, date, dd, df, dir, dircolors, dirname, du, echo, env, expand,
expr, factor, false, fmt, fold, groups, head, hostid, id, install, join, link, ln, logname,
ls, md5sum, mkdir, mkfifo, mknod, mktemp, mv, nice, nl, nohup, nproc, numfmt, od,
paste, pathchk, pinky, pr, printenv, printf, ptx, pwd, readlink, realpath, rm, rmdir, seq,
sha1sum, sha224sum, sha256sum, sha384sum, sha512sum, shred, shuf, sleep, sort, split,
stat, stdbuf, stty, sum, sync, tac, tail, tee, test, timeout, touch, tr, true, truncate, tsort, tty,
uname, unexpand, uniq, unlink, users, vdir, wc, who, whoami, and yes
**Installed library:**
libstdbuf.so (in /usr/libexec/coreutils)
**Installed directory:**
/usr/libexec/coreutils

**Short Descriptions**

**[**
**Is an actual command, /usr/bin/[; it is a synonym for the test command**

**base32**
Encodes and decodes data according to the base32 specification (RFC 4648)

**base64**
Encodes and decodes data according to the base64 specification (RFC 4648)

**b2sum**
Prints or checks BLAKE2 (512-bit) checksums

**basename**
Strips any path and a given suffix from a file name

**basenc**
Encodes or decodes data using various algorithms

**cat**
Concatenates files to standard output

**chgrp**
Changes the group ownership of files and directories

**chmod**
Changes the permissions of each file to the given mode; the mode can be either a symbolic
representation of the changes to be made, or an octal number representing the new permissions

**chown**
Changes the user and/or group ownership of files and directories

**chroot**
Runs a command with the specified directory as the / directory

**cksum**
Prints the Cyclic Redundancy Check (CRC) checksum and the byte counts of each specified file

---

Linux From Scratch - Version 13.1-systemd

**comm**
Compares two sorted files, outputting in three columns the lines that are unique and the lines that are
common

**cp**
Copies files

**csplit**
Splits a given file into several new files, separating them according to given patterns or line numbers,
and outputting the byte count of each new file

**cut**
Prints sections of lines, selecting the parts according to given fields or positions

**date**
Displays the current date and time in the given format, or sets the system date and time

**dd**
Copies a file using the given block size and count, while optionally performing conversions on it

**df**
Reports the amount of disk space available (and used) on all mounted file systems, or only on the file
systems holding the selected files

**dir**
**Lists the contents of each given directory (the same as the ls command)**

**dircolors**
**Outputs commands to set the LS_COLOR environment variable to change the color scheme used by ls**

**dirname**
Extracts the directory portion(s) of the given name(s)

**du**
Reports the amount of disk space used by the current directory, by each of the given directories
(including all subdirectories) or by each of the given files

**echo**
Displays the given strings

**env**
Runs a command in a modified environment

**expand**
Converts tabs to spaces

**expr**
Evaluates expressions

**factor**
Prints the prime factors of the specified integers

**false**
Does nothing, unsuccessfully; it always exits with a status code indicating failure

**fmt**
Reformats the paragraphs in the given files

**fold**
Wraps the lines in the given files

**groups**
Reports a user's group memberships

**head**
Prints the first ten lines (or the given number of lines) of each given file

**hostid**
Reports the numeric identifier (in hexadecimal) of the host

**id**
Reports the effective user ID, group ID, and group memberships of the current user or specified user

**install**
Copies files while setting their permission modes and, if possible, their owner and group

**join**
Joins the lines that have identical join fields from two separate files

**link**
Creates a hard link (with the given name) to a file

**ln**
Makes hard links or soft (symbolic) links between files

**logname**
Reports the current user's login name

**ls**
Lists the contents of each given directory

**md5sum**
Reports or checks Message Digest 5 (MD5) checksums

**mkdir**
Creates directories with the given names

**mkfifo**
Creates First-In, First-Outs (FIFOs), "named pipes" in UNIX parlance, with the given names

**mknod**
Creates device nodes with the given names; a device node is a character special file, a block special
file, or a FIFO

---

Linux From Scratch - Version 13.1-systemd

**mktemp**
Creates temporary files in a secure manner; it is used in scripts

**mv**
Moves or renames files or directories

**nice**
Runs a program with modified scheduling priority

**nl**
Numbers the lines from the given files

**nohup**
Runs a command immune to hangups, with its output redirected to a log file

**nproc**
Prints the number of processing units available to a process

**numfmt**
Converts numbers to or from human-readable strings

**od**
Dumps files in octal and other formats

**paste**
Merges the given files, joining sequentially corresponding lines side by side, separated by tab characters

**pathchk**
Checks if file names are valid or portable

**pinky**
Is a lightweight finger client; it reports some information about the given users

**pr**
Paginates and columnates files for printing

**printenv**
Prints the environment

**printf**
Prints the given arguments according to the given format, much like the C printf function

**ptx**
Produces a permuted index from the contents of the given files, with each keyword in its context

**pwd**
Reports the name of the current working directory

**readlink**
Reports the value of the given symbolic link

**realpath**
Prints the resolved path

**rm**
Removes files or directories

**rmdir**
Removes directories if they are empty

**seq**
Prints a sequence of numbers within a given range and with a given increment

**sha1sum**
Prints or checks 160-bit Secure Hash Algorithm 1 (SHA1) checksums

**sha224sum**
Prints or checks 224-bit Secure Hash Algorithm checksums

**sha256sum**
Prints or checks 256-bit Secure Hash Algorithm checksums

**sha384sum**
Prints or checks 384-bit Secure Hash Algorithm checksums

**sha512sum**
Prints or checks 512-bit Secure Hash Algorithm checksums

**shred**
Overwrites the given files repeatedly with complex patterns, making it difficult to recover the data

**shuf**
Shuffles lines of text

**sleep**
Pauses for the given amount of time

**sort**
Sorts the lines from the given files

**split**
Splits the given file into pieces, by size or by number of lines

**stat**
Displays file or filesystem status

**stdbuf**
Runs commands with altered buffering operations for its standard streams

**stty**
Sets or reports terminal line settings

**sum**
Prints checksum and block counts for each given file

**sync**
Flushes file system buffers; it forces changed blocks to disk and updates the super block

---

Linux From Scratch - Version 13.1-systemd

**tac**
Concatenates the given files in reverse

**tail**
Prints the last ten lines (or the given number of lines) of each given file

**tee**
Reads from standard input while writing both to standard output and to the given files

**test**
Compares values and checks file types

**timeout**
Runs a command with a time limit

**touch**
Changes file timestamps, setting the access and modification times of the given files to the current time;
files that do not exist are created with zero length