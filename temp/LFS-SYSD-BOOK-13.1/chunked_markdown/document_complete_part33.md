# 8.6. Zlib-1.3.2

The Zlib package contains compression and decompression routines used by some programs.

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
5.4 MB

## 8.6.1. Installation of Zlib

Prepare Zlib for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

Remove a useless static library:

**rm -fv /usr/lib/libz.a**

## 8.6.2. Contents of Zlib

**Installed libraries:**
libz.so

**Short Descriptions**

libz
Contains compression and decompression functions used by some programs

---

Linux From Scratch - Version 13.1-systemd

# 8.7. Bzip2-1.0.8

**The Bzip2 package contains programs for compressing and decompressing files. Compressing text files with bzip2**
**yields a much better compression percentage than with the traditional gzip.**

**Approximate build time:**
less than 0.1 SBU
**Required disk space:**
7.3 MB

## 8.7.1. Installation of Bzip2

Apply a patch that will install the documentation for this package:

**patch -Np1 -i ../bzip2-1.0.8-install_docs-1.patch**

The following command ensures installation of symbolic links are relative:

**sed -i 's@\(ln -s -f \)$(PREFIX)/bin/@\1@' Makefile**

Ensure the man pages are installed into the correct location:

**sed -i "s@(PREFIX)/man@(PREFIX)/share/man@g" Makefile**

Prepare Bzip2 for compilation with:

**make -f Makefile-libbz2_so**
**make clean**

**The meaning of the make parameter:**

-f Makefile-libbz2_so

This will cause Bzip2 to be built using a different Makefile file, in this case the Makefile-libbz2_so file, which
creates a dynamic libbz2.so library and links the Bzip2 utilities against it.

Compile and test the package:

**make**

Install the programs:

**make PREFIX=/usr install**

Install the shared library:

**cp -av libbz2.so.* /usr/lib**
**ln -sfv libbz2.so.1.0.8 /usr/lib/libbz2.so**

The name of the shared library isn't standardized and it varies among distros. The instruction above has installed libbz2.

so.1.0, but some applications, for example Kbd, expects a different name libbz2.so.1 that some other distros are using.
Create a compatibility symlink for them:

**ln -sfv libbz2.so.1.0.8 /usr/lib/libbz2.so.1**

### Note

The symlink approach is only valid here because the library name difference is a result of different aesthetic
views of the distro maintainers, not real ABI incompatibilities. In general a library name difference most likely
indicates an ABI incompatibility and it would be very likely invalid to “hide” the difference via a symlink.
Read Section 8.2.1, “Upgrade Issues” for details about library names.

---

Linux From Scratch - Version 13.1-systemd

**Install the shared bzip2 binary into the /usr/bin directory, and replace two copies of bzip2 with symlinks:**

**cp -v bzip2-shared /usr/bin/bzip2**
**for i in /usr/bin/{bzcat,bunzip2}; do**
**ln -sfv bzip2 $i**
**done**

Remove a useless static library:

**rm -fv /usr/lib/libbz2.a**

## 8.7.2. Contents of Bzip2

**Installed programs:**
bunzip2 (link to bzip2), bzcat (link to bzip2), bzcmp (link to bzdiff), bzdiff, bzegrep (link
to bzgrep), bzfgrep (link to bzgrep), bzgrep, bzip2, bzip2recover, bzless (link to bzmore),
and bzmore
**Installed libraries:**
libbz2.so
**Installed directory:**
/usr/share/doc/bzip2-1.0.8

**Short Descriptions**

**bunzip2**
Decompresses bzipped files

**bzcat**
Decompresses to standard output

**bzcmp**
**Runs cmp on bzipped files**

**bzdiff**
**Runs diff on bzipped files**

**bzegrep**
**Runs egrep on bzipped files**

**bzfgrep**
**Runs fgrep on bzipped files**

**bzgrep**
**Runs grep on bzipped files**

**bzip2**
Compresses files using the Burrows-Wheeler block sorting text compression algorithm with
Huffman coding; the compression rate is better than that achieved by more conventional
**compressors using “Lempel-Ziv” algorithms, like gzip**

**bzip2recover**
Tries to recover data from damaged bzipped files

**bzless**
**Runs less on bzipped files**

**bzmore**
**Runs more on bzipped files**

libbz2
The library implementing lossless, block-sorting data compression, using the Burrows-Wheeler
algorithm

---

Linux From Scratch - Version 13.1-systemd

# 8.8. Xz-5.8.3

The Xz package contains programs for compressing and decompressing files. It provides capabilities for the lzma and
**the newer xz compression formats. Compressing text files with xz yields a better compression percentage than with**
**the traditional gzip or bzip2 commands.**

**Approximate build time:**
0.1 SBU
**Required disk space:**
25 MB

## 8.8.1. Installation of Xz

Prepare Xz for compilation with:

**./configure --prefix=/usr    \**
**--disable-static \**
**--docdir=/usr/share/doc/xz-5.8.3**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

## 8.8.2. Contents of Xz

**Installed programs:**
lzcat (link to xz), lzcmp (link to xzdiff), lzdiff (link to xzdiff), lzegrep (link to xzgrep),
lzfgrep (link to xzgrep), lzgrep (link to xzgrep), lzless (link to xzless), lzma (link to xz),
lzmadec, lzmainfo, lzmore (link to xzmore), unlzma (link to xz), unxz (link to xz), xz,
xzcat (link to xz), xzcmp (link to xzdiff), xzdec, xzdiff, xzegrep (link to xzgrep), xzfgrep
(link to xzgrep), xzgrep, xzless, and xzmore
**Installed libraries:**
liblzma.so
**Installed directories:**
/usr/include/lzma and /usr/share/doc/xz-5.8.3

**Short Descriptions**

**lzcat**
Decompresses to standard output

**lzcmp**
**Runs cmp on LZMA compressed files**

**lzdiff**
**Runs diff on LZMA compressed files**

**lzegrep**
**Runs egrep on LZMA compressed files**

**lzfgrep**
**Runs fgrep on LZMA compressed files**

**lzgrep**
**Runs grep on LZMA compressed files**

**lzless**
**Runs less on LZMA compressed files**

**lzma**
Compresses or decompresses files using the LZMA format

**lzmadec**
A small and fast decoder for LZMA compressed files

**lzmainfo**
Shows information stored in the LZMA compressed file header

---

Linux From Scratch - Version 13.1-systemd

**lzmore**
**Runs more on LZMA compressed files**

**unlzma**
Decompresses files using the LZMA format

**unxz**
Decompresses files using the XZ format

**xz**
Compresses or decompresses files using the XZ format

**xzcat**
Decompresses to standard output

**xzcmp**
**Runs cmp on XZ compressed files**

**xzdec**
A small and fast decoder for XZ compressed files

**xzdiff**
**Runs diff on XZ compressed files**

**xzegrep**
**Runs egrep on XZ compressed files**

**xzfgrep**
**Runs fgrep on XZ compressed files**

**xzgrep**
**Runs grep on XZ compressed files**

**xzless**
**Runs less on XZ compressed files**

**xzmore**
**Runs more on XZ compressed files**

liblzma
The library implementing lossless, block-sorting data compression, using the Lempel-Ziv-Markov chain
algorithm

---

Linux From Scratch - Version 13.1-systemd

# 8.9. Lz4-1.10.0

Lz4 is a lossless compression algorithm, providing compression speed greater than 500 MB/s per core. It features an
extremely fast decoder, with speed in multiple GB/s per core. Lz4 can work with Zstandard to allow both algorithms
to compress data faster.

**Approximate build time:**
0.1 SBU
**Required disk space:**
4.2 MB

## 8.9.1. Installation of Lz4

Compile the package:

**make BUILD_STATIC=no PREFIX=/usr**

To test the results, issue:

**make -j1 check**

Install the package:

**make BUILD_STATIC=no PREFIX=/usr install**

## 8.9.2. Contents of Lz4

**Installed programs:**
lz4, lz4c (link to lz4), lz4cat (link to lz4), and unlz4 (link to lz4)
**Installed library:**
liblz4.so

**Short Descriptions**

**lz4**
Compresses or decompresses files using the LZ4 format

**lz4c**
Compresses files using the LZ4 format

**lz4cat**
Lists the contents of a file compressed using the LZ4 format

**unlz4**
Decompresses files using the LZ4 format

liblz4
The library implementing lossless data compression, using the LZ4 algorithm

---

Linux From Scratch - Version 13.1-systemd