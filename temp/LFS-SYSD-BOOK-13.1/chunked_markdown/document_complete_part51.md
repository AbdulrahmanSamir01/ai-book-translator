# 8.70. Make-4.4.1

The Make package contains a program for controlling the generation of executables and other non-source files of a
package from source files.

**Approximate build time:**
0.6 SBU
**Required disk space:**
13 MB

## 8.70.1. Installation of Make

Prepare Make for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

To test the results, issue:

**chown -R tester .**
**su tester -c "PATH=$PATH make check"**

Install the package:

**make install**

## 8.70.2. Contents of Make

**Installed program:**
make

**Short Descriptions**

**make**
Automatically determines which pieces of a package need to be (re)compiled and then issues the relevant
commands

---

Linux From Scratch - Version 13.1-systemd

# 8.71. Patch-2.8

The Patch package contains a program for modifying or creating files by applying a “patch” file typically created by
**the diff program.**

**Approximate build time:**
0.2 SBU
**Required disk space:**
14 MB

## 8.71.1. Installation of Patch

Prepare Patch for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

## 8.71.2. Contents of Patch

**Installed program:**
patch

**Short Descriptions**

**patch**
**Modifies files according to a patch file (A patch file is normally a difference listing created with the diff**
**program. By applying these differences to the original files, patch creates the patched versions.)**

---

Linux From Scratch - Version 13.1-systemd

# 8.72. Tar-1.35

The Tar package provides the ability to create tar archives as well as perform various other kinds of archive
manipulation. Tar can be used on previously created archives to extract files, to store additional files, or to update or
list files which were already stored.

**Approximate build time:**
0.5 SBU
**Required disk space:**
43 MB

## 8.72.1. Installation of Tar

First fix the package to build with acl-2.4.0:

**patch -Np1 -i ../tar-1.35-acl_fix-1.patch**

Prepare Tar for compilation:

**FORCE_UNSAFE_CONFIGURE=1  \**
**./configure --prefix=/usr**

**The meaning of the configure option:**

FORCE_UNSAFE_CONFIGURE=1

This forces the test for mknod to be run as root. It is generally considered dangerous to run this test as the root
user, but as it is being run on a system that has only been partially built, overriding it is OK.

Compile the package:

**make**

To test the results, issue:

**make check**

One test, capabilities: binary store/restore, is known to fail if it is run because LFS lacks selinux, but will be skipped if
the host kernel does not support extended attributes or security labels on the filesystem used for building LFS.

Install the package:

**make install**
**make -C doc install-html docdir=/usr/share/doc/tar-1.35**

## 8.72.2. Contents of Tar

**Installed programs:**
tar
**Installed directory:**
/usr/share/doc/tar-1.35

**Short Descriptions**

**tar**
Creates, extracts files from, and lists the contents of archives, also known as tarballs

---

Linux From Scratch - Version 13.1-systemd

# 8.73. Texinfo-7.3

The Texinfo package contains programs for reading, writing, and converting info pages.

**Approximate build time:**
0.4 SBU
**Required disk space:**
151 MB

## 8.73.1. Installation of Texinfo

Prepare Texinfo for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

Optionally, install the components belonging in a TeX installation:

**make TEXMF=/usr/share/texmf install-tex**

**The meaning of the make parameter:**

TEXMF=/usr/share/texmf

The TEXMF makefile variable holds the location of the root of the TeX tree if, for example, a TeX package will
be installed later.

The Info documentation system uses a plain text file to hold its list of menu entries. The file is located at /usr/share/

info/dir. Unfortunately, due to occasional problems in the Makefiles of various packages, it can sometimes get out
of sync with the info pages installed on the system. If the /usr/share/info/dir file ever needs to be recreated, the
following optional commands will accomplish the task:

**pushd /usr/share/info**
**rm -v dir**
**for f in ***
**do install-info $f dir 2>/dev/null**
**done**
**popd**

## 8.73.2. Contents of Texinfo

**Installed programs:**
info, install-info, makeinfo (link to texi2any), pdftexi2dvi, pod2texi, texi2any, texi2dvi,
texi2pdf, and texindex
**Installed library:**
MiscXS.so, Parsetexi.so, and XSParagraph.so (all in /usr/lib/texinfo)
**Installed directories:**
/usr/share/texinfo and /usr/lib/texinfo

**Short Descriptions**

**info**
Used to read info pages which are similar to man pages, but often go much deeper than just
**explaining all the available command line options [For example, compare man bison and info**
**bison.]**

---

Linux From Scratch - Version 13.1-systemd

**install-info**
**Used to install info pages; it updates entries in the info index file**

**makeinfo**
Translates the given Texinfo source documents into info pages, plain text, or HTML

**pdftexi2dvi**
Used to format the given Texinfo document into a Portable Document Format (PDF) file

**pod2texi**
Converts Pod to Texinfo format

**texi2any**
Translate Texinfo source documentation to various other formats

**texi2dvi**
Used to format the given Texinfo document into a device-independent file that can be printed

**texi2pdf**
Used to format the given Texinfo document into a Portable Document Format (PDF) file

**texindex**
Used to sort Texinfo index files

---

Linux From Scratch - Version 13.1-systemd

# 8.74. Vim-9.2.1025

The Vim package contains a powerful text editor.

**Approximate build time:**
3.3 SBU
**Required disk space:**
234 MB

### Alternatives to Vim

If you prefer another editor—such as Emacs, Joe, or Nano—please refer to https://www.linuxfromscratch.
org/blfs/view/13.1-systemd/postlfs/editors.html for suggested installation instructions.

## 8.74.1. Installation of Vim

First, change the default location of the vimrc configuration file to /etc:

**echo '#define SYS_VIMRC_FILE "/etc/vimrc"' >> src/feature.h**

Prepare Vim for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

To prepare the tests, ensure that user tester can write to the source tree and exclude one file containing tests requiring
**curl or wget:**

**chown -R tester .**
**sed '/test_plugin_glvs/d' -i src/testdir/Make_all.mak**

Now run the tests as user tester:

**su tester -c "TERM=xterm-256color LANG=en_US.UTF-8 make -j1 test" \**
**&> vim-test.log**

The test suite outputs a lot of binary data to the screen. This can cause issues with the settings of the current terminal
(especially while we are overriding the TERM variable to satisfy some assumptions of the test suite). The problem can
be avoided by redirecting the output to a log file as shown above. A successful test will show FAILED: 0 in the log
file at completion.

Two tests, Test_client_server_stopinsert() and Test_popup_setbuf(), are known to fail on some systems.

Install the package:

**make install**

**Many users reflexively type vi instead of vim. To allow execution of vim when users habitually enter vi, create a**
symlink for both the binary and the man page in the provided languages:

**ln -sv vim /usr/bin/vi**
**for L in  /usr/share/man/{,*/}man1/vim.1; do**
**ln -sv vim.1 $(dirname $L)/vi.1**
**done**

By default, Vim's documentation is installed in /usr/share/vim. The following symlink allows the documentation to be
accessed via /usr/share/doc/vim-9.2.1025, making it consistent with the location of documentation for other packages:

**ln -sv ../vim/vim92/doc /usr/share/doc/vim-9.2.1025**

---

Linux From Scratch - Version 13.1-systemd

If an X Window System is going to be installed on the LFS system, it may be necessary to recompile Vim after installing
X. Vim comes with a GUI version of the editor that requires X and some additional libraries to be installed. For more
information on this process, refer to the Vim documentation and the Vim installation page in the BLFS book at https://
www.linuxfromscratch.org/blfs/view/13.1-systemd/postlfs/vim.html.

## 8.74.2. Configuring Vim

**By default, vim runs in vi-incompatible mode. This may be new to users who have used other editors in the past. The**
“nocompatible” setting is included below to highlight the fact that a new behavior is being used. It also reminds those
who would change to “compatible” mode that it should be the first setting in the configuration file. This is necessary
**because it changes other settings, and overrides must come after this setting. Create a default vim configuration file**
by running the following:

**cat > /etc/vimrc << "EOF"**
" Begin /etc/vimrc

" Ensure defaults are set before customizing settings, not after
source $VIMRUNTIME/defaults.vim
let skip_defaults_vim=1

set nocompatible
set backspace=2
set mouse=
syntax on
if (&term == "xterm") || (&term == "putty")
set background=dark
endif

" End /etc/vimrc
**EOF**

**The set nocompatible setting makes vim behave in a more useful way (the default) than the vi-compatible manner.**
**Remove the “no” to keep the old vi behavior. The set backspace=2 setting allows backspacing over line breaks,**
autoindents, and the start of an insert. The syntax on parameter enables vim's syntax highlighting. The set mouse=
setting enables proper pasting of text with the mouse when working in chroot or over a remote connection. Finally, the
**if statement with the set background=dark setting corrects vim's guess about the background color of some terminal**
emulators. This gives the highlighting a better color scheme for use on the black background of these programs.

Documentation for other available options can be obtained by running the following command:

**vim -c ':options'**

### Note

By default, vim only installs spell-checking files for the English language. To install spell-checking files for
your preferred language, copy the .spl and optionally, the .sug files for your language and character encoding
from runtime/spell into  /usr/share/vim/vim92/spell/.

To use these spell-checking files, some configuration in /etc/vimrc is needed, e.g.:

set spelllang=en,ru
set spell

For more information, see runtime/spell/README.txt.

---

Linux From Scratch - Version 13.1-systemd

## 8.74.3. Contents of Vim

**Installed programs:**
ex (link to vim), rview (link to vim), rvim (link to vim), vi (link to vim), view (link to
vim), vim, vimdiff (link to vim), vimtutor, and xxd
**Installed directory:**
/usr/share/vim

**Short Descriptions**

**ex**
**Starts vim in ex mode**

**rview**
**Is a restricted version of view; no shell commands can be started and view cannot be suspended**

**rvim**
**Is a restricted version of vim; no shell commands can be started and vim cannot be suspended**

**vi**
**Link to vim**

**view**
**Starts vim in read-only mode**

**vim**
Is the editor

**vimdiff**
**Edits two or three versions of a file with vim and shows differences**

**vimtutor**
**Teaches the basic keys and commands of vim**

**xxd**
Creates a hex dump of the given file; it can also perform the inverse operation, so it can be used for
binary patching

---

Linux From Scratch - Version 13.1-systemd