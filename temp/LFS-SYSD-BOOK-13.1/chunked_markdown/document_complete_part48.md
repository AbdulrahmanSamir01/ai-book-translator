**tr**
Translates, squeezes, and deletes the given characters from standard input

**true**
Does nothing, successfully; it always exits with a status code indicating success

**truncate**
Shrinks or expands a file to the specified size

**tsort**
Performs a topological sort; it writes a completely ordered list according to the partial ordering in a
given file

**tty**
Reports the file name of the terminal connected to standard input

**uname**
Reports system information

**unexpand**
Converts spaces to tabs

**uniq**
Discards all but one of successive identical lines

**unlink**
Removes the given file

**users**
Reports the names of the users currently logged on

**vdir**
**Is the same as ls -l**

**wc**
Reports the number of lines, words, and bytes for each given file, as well as grand totals when more
than one file is given

**who**
Reports who is logged on

**whoami**
Reports the user name associated with the current effective user ID

**yes**
Repeatedly outputs y or a given string, until killed

libstdbuf
**Library used by stdbuf**

---

Linux From Scratch - Version 13.1-systemd

# 8.62. Diffutils-3.12

The Diffutils package contains programs that show the differences between files or directories.

**Approximate build time:**
0.4 SBU
**Required disk space:**
51 MB

## 8.62.1. Installation of Diffutils

Prepare Diffutils for compilation:

**./configure --prefix=/usr**

Compile the package:

**make**

To test the results, issue:

**make check**

Install the package:

**make install**

## 8.62.2. Contents of Diffutils

**Installed programs:**
cmp, diff, diff3, and sdiff

**Short Descriptions**

**cmp**
Compares two files and reports any differences byte by byte

**diff**
Compares two files or directories and reports which lines in the files differ

**diff3**
Compares three files line by line

**sdiff**
Merges two files and interactively outputs the results

---

Linux From Scratch - Version 13.1-systemd

# 8.63. Findutils-4.11.0

The Findutils package contains programs to find files. Programs are provided to search through all the files in a directory
tree and to create, maintain, and search a database (often faster than the recursive find, but unreliable unless the database
**has been updated recently). Findutils also supplies the xargs program, which can be used to run a specified command**
on each file selected by a search.

**Approximate build time:**
0.9 SBU
**Required disk space:**
71 MB

## 8.63.1. Installation of Findutils

Prepare Findutils for compilation:

**./configure --prefix=/usr --localstatedir=/var/lib/locate**

**The meaning of the configure options:**

--localstatedir

**This option moves the locate database to /var/lib/locate, which is the FHS-compliant location.**

Compile the package:

**make**

To test the results, issue:

**chown -R tester .**
**su tester -c "PATH=$PATH make check -k"**

One test named test-regex-el is known to fail.

Install the package:

**make install**

## 8.63.2. Contents of Findutils

**Installed programs:**
find, locate, updatedb, and xargs
**Installed directory:**
/var/lib/locate

**Short Descriptions**

**find**
Searches given directory trees for files matching the specified criteria

**locate**
Searches through a database of file names and reports the names that contain a given string or match
a given pattern

**updatedb**
**Updates the locate database; it scans the entire file system (including other file systems that are currently**
mounted, unless told not to) and puts every file name it finds into the database

**xargs**
Can be used to apply a given command to a list of files

---

Linux From Scratch - Version 13.1-systemd

# 8.64. Groff-1.24.1

The Groff package contains programs for processing and formatting text and images.

**Approximate build time:**
0.6 SBU
**Required disk space:**
128 MB

## 8.64.1. Installation of Groff

Groff expects the environment variable PAGE to contain the default paper size. For users in the United States, PAGE=letter
is appropriate. Elsewhere, PAGE=A4 may be more suitable. While the default paper size is configured during compilation,
it can be overridden later by echoing either “A4” or “letter” to the /etc/papersize file.

Prepare Groff for compilation:

**PAGE=<paper_size> ./configure --prefix=/usr**

Build the package:

**make -j1**

To test the results, issue:

**make check**

One test, neqn-smoke-test.sh, is known to fail.

Install the package:

**make install**

## 8.64.2. Contents of Groff

**Installed programs:**
addftinfo, afmtodit, chem, eqn, eqn2graph, gdiffmk, glilypond, gperl, gpinyin,
grap2graph, grn, grodvi, groff, groffer, grog, grolbp, grolj4, gropdf, grops, grotty,
hpftodit, indxbib, lkbib, lookbib, mmroff, neqn, nroff, pdfmom, pdfroff, pfbtops, pic,
pic2graph, post-grohtml, preconv, pre-grohtml, refer, roff2dvi, roff2html, roff2pdf,
roff2ps, roff2text, roff2x, soelim, tbl, tfmtodit, and troff
**Installed directories:**
/usr/lib/groff and /usr/share/doc/groff-1.24.1, /usr/share/groff

**Short Descriptions**

**addftinfo**
**Reads a troff font file and adds some additional font-metric information that is used by the groff**
system

**afmtodit**
**Creates a font file for use with groff and grops**

**chem**
Groff preprocessor for producing chemical structure diagrams

**eqn**
Compiles descriptions of equations embedded within troff input files into commands that are
**understood by troff**

**eqn2graph**
Converts a troff EQN (equation) into a cropped image

**gdiffmk**
Marks differences between groff/nroff/troff files

**glilypond**
Transforms sheet music written in the lilypond language into the groff language

**gperl**
Preprocessor for groff, allowing the insertion of perl code into groff files

---

Linux From Scratch - Version 13.1-systemd

**gpinyin**
Preprocessor for groff, allowing the insertion of Pinyin (Mandarin Chinese spelled with the Roman
alphabet) into groff files.

**grap2graph**
Converts a grap program file into a cropped bitmap image (grap is an old Unix programming
language for creating diagrams)

**grn**
**A groff preprocessor for gremlin files**

**grodvi**
**A driver for groff that produces TeX dvi format output files**

**groff**
**A front end to the groff document formatting system; normally, it runs the troff program and a**
post-processor appropriate for the selected device

**groffer**
Displays groff files and man pages on X and tty terminals

**grog**
**Reads files and guesses which of the groff options -e, -man, -me, -mm, -ms, -p, -s, and -t are required**
**for printing files, and reports the groff command including those options**

**grolbp**
**Is a groff driver for Canon CAPSL printers (LBP-4 and LBP-8 series laser printers)**

**grolj4**
**Is a driver for groff that produces output in PCL5 format suitable for an HP LaserJet 4 printer**

**gropdf**
**Translates the output of GNU troff to PDF**

**grops**
**Translates the output of GNU troff to PostScript**

**grotty**
**Translates the output of GNU troff into a form suitable for typewriter-like devices**

**hpftodit**
**Creates a font file for use with groff -Tlj4 from an HP-tagged font metric file**

**indxbib**
**Creates an inverted index for the bibliographic databases with a specified file for use with refer,**
**lookbib, and lkbib**

**lkbib**
Searches bibliographic databases for references that contain specified keys and reports any
references found

**lookbib**
Prints a prompt on the standard error (unless the standard input is not a terminal), reads a line
containing a set of keywords from the standard input, searches the bibliographic databases in a
specified file for references containing those keywords, prints any references found on the standard
output, and repeats this process until the end of input

**mmroff**
**A simple preprocessor for groff**

**neqn**
Formats equations for American Standard Code for Information Interchange (ASCII) output

**nroff**
**A script that emulates the nroff command using groff**

**pdfmom**
Is a wrapper around groff that facilitates the production of PDF documents from files formatted
with the mom macros.

**pdfroff**
Creates pdf documents using groff

**pfbtops**
Translates a PostScript font in .pfb format to ASCII

**pic**
Compiles descriptions of pictures embedded within troff or TeX input files into commands
**understood by TeX or troff**

**pic2graph**
Converts a PIC diagram into a cropped image

**post-grohtml**
**Translates the output of GNU troff to HTML**

**preconv**
**Converts encoding of input files to something GNU troff understands**

**pre-grohtml**
**Translates the output of GNU troff to HTML**

---

Linux From Scratch - Version 13.1-systemd

**refer**
Copies the contents of a file to the standard output, except that lines between .[ and .] are interpreted
as citations, and lines between .R1 and .R2 are interpreted as commands for how citations are to
be processed

**roff2dvi**
Transforms roff files into DVI format

**roff2html**
Transforms roff files into HTML format

**roff2pdf**
Transforms roff files into PDFs

**roff2ps**
Transforms roff files into ps files

**roff2text**
Transforms roff files into text files

**roff2x**
Transforms roff files into other formats

**soelim**
Reads files and replaces lines of the form .so file by the contents of the mentioned file

**tbl**
Compiles descriptions of tables embedded within troff input files into commands that are
**understood by troff**

**tfmtodit**
**Creates a font file for use with groff -Tdvi**

**troff**
**Is highly compatible with Unix troff; it should usually be invoked using the groff command, which**
will also run preprocessors and post-processors in the appropriate order and with the appropriate
options

---

Linux From Scratch - Version 13.1-systemd