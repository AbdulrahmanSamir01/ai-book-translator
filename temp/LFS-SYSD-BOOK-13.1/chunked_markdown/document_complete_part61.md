# 9.7. Configuring the System Locale

Some environment variables are necessary for native language support. Setting them properly results in:

• The output of programs being translated into your native language

**• The correct classification of characters into letters, digits and other classes. This is necessary for bash to properly**
accept non-ASCII characters in command lines in non-English locales

• The correct alphabetical sorting order for the country

• The appropriate default paper size

• The correct formatting of monetary, time, and date values

---

Linux From Scratch - Version 13.1-systemd

Replace <ll> below with the two-letter code for your desired language (e.g., en) and <CC> with the two-letter code for
the appropriate country (e.g., GB). <charmap> should be replaced with the canonical charmap for your chosen locale.
Optional modifiers such as @euro may also be present.

The list of all locales supported by Glibc can be obtained by running the following command:

**locale -a**

Charmaps can have a number of aliases, e.g., ISO-8859-1 is also referred to as iso8859-1 and iso88591. Some
applications cannot handle the various synonyms correctly (e.g., require that UTF-8 is written as UTF-8, not utf8), so
it is the safest in most cases to choose the canonical name for a particular locale. To determine the canonical name,
**run the following command, where <locale name> is the output given by locale -a for your preferred locale (en_GB.**

iso88591 in our example).

**LC_ALL=<locale name> locale charmap**

For the en_GB.iso88591 locale, the above command will print:

ISO-8859-1

This results in a final locale setting of en_GB.ISO-8859-1. It is important that the locale found using the heuristic above
is tested prior to it being added to the Bash startup files:

**LC_ALL=<locale name> locale language**
**LC_ALL=<locale name> locale charmap**
**LC_ALL=<locale name> locale int_curr_symbol**
**LC_ALL=<locale name> locale int_prefix**

The above commands should print the language name, the character encoding used by the locale, the local currency,
and the prefix to dial before the telephone number in order to get into the country. If any of the commands above fail
with a message similar to the one shown below, this means that your locale was either not installed in Chapter 8 or is
not supported by the default installation of Glibc.

locale: Cannot set LC_* to default locale: No such file or directory

**If this happens, you should either install the desired locale using the localedef command, or consider choosing a different**
locale. Further instructions assume that there are no such error messages from Glibc.

Other packages can also function incorrectly (but may not necessarily display any error messages) if the locale name
does not meet their expectations. In those cases, investigating how other Linux distributions support your locale might
provide some useful information.

Once the proper locale settings have been determined, create the /etc/locale.conf file:

**cat > /etc/locale.conf << "EOF"**
LANG=<ll>_<CC>.<charmap><@modifiers>
**EOF**

**The shell program /bin/bash (here after referred as “the shell”) uses a collection of startup files to help create the**
environment to run in. Each file has a specific use and may affect login and interactive environments differently. The
files in the /etc directory provide global settings. If equivalent files exist in the home directory, they may override
the global settings.

**An interactive login shell is started after a successful login, using /bin/login, by reading the /etc/passwd file. An**
**interactive non-login shell is started at the command-line (e.g. [prompt]$/bin/bash). A non-interactive shell is usually**
present when a shell script is running. It is non-interactive because it is processing a script and not waiting for user
input between commands.

---

Linux From Scratch - Version 13.1-systemd

The login shells are often unaffected by the settings in /etc/locale.conf. Create the /etc/profile to read the locale
settings from /etc/locale.conf and export them, but set the C.UTF-8 locale instead if running in the Linux console (to
prevent programs from outputting characters that the Linux console is unable to render):

**cat > /etc/profile << "EOF"**

# Begin /etc/profile

for i in $(locale); do
unset ${i%=*}
done

if [[ "$TERM" = linux ]]; then
export LANG=C.UTF-8
else
source /etc/locale.conf

for i in $(locale); do
key=${i%=*}
if [[ -v $key ]]; then
export $key
fi
done
fi

# End /etc/profile
**EOF**

**Note that you can modify /etc/locale.conf with the systemd localectl utility. To use localectl for the example above,**
run:

**localectl set-locale LANG="<ll>_<CC>.<charmap><@modifiers>"**

You can also specify other language specific environment variables such as LANG, LC_CTYPE, LC_NUMERIC or any other
**environment variable from locale output. Just separate them with a space. An example where LANG is set as en_US.UTF-8**
but LC_CTYPE is set as just en_US is:

**localectl set-locale LANG="en_US.UTF-8" LC_CTYPE="en_US"**

### Note

**Please note that the localectl command doesn't work in the chroot environment. It can only be used after the**
LFS system is booted with systemd.

The C (default) and en_US (the recommended one for United States English users) locales are different. C uses the US-
**ASCII 7-bit character set, and treats bytes with the high bit set as invalid characters. That's why, e.g., the ls command**
substitutes them with question marks in that locale. Also, an attempt to send mail with such characters from Mutt or
Pine results in non-RFC-conforming messages being sent (the charset in the outgoing mail is indicated as unknown 8-

bit). It's suggested that you use the C locale only if you are certain that you will never need 8-bit characters.

# 9.8. Creating the /etc/inputrc File

The inputrc file is the configuration file for the readline library, which provides editing capabilities while the user is
entering a line from the terminal. It works by translating keyboard inputs into specific actions. Readline is used by bash
and most other shells as well as many other applications.

Most people do not need user-specific functionality so the command below creates a global /etc/inputrc used by
everyone who logs in. If you later decide you need to override the defaults on a per user basis, you can create a .inputrc
file in the user's home directory with the modified mappings.

---

Linux From Scratch - Version 13.1-systemd

**For more information on how to edit the inputrc file, see info bash under the Readline Init File section. info readline**
is also a good source of information.

Below is a generic global inputrc along with comments to explain what the various options do. Note that comments
cannot be on the same line as commands. Create the file using the following command:

**cat > /etc/inputrc << "EOF"**

# Begin /etc/inputrc

# Modified by Chris Lynn <roryo@roryo.dynup.net>

# Allow the command prompt to wrap to the next line
set horizontal-scroll-mode Off

# Enable 8-bit input
set meta-flag On
set input-meta On

# Turns off 8th bit stripping
set convert-meta Off

# Keep the 8th bit for display
set output-meta On

# none, visible or audible
set bell-style none

# All of the following map the escape sequence of the value

# contained in the 1st argument to the readline specific functions
"\eOd": backward-word
"\eOc": forward-word

# for linux console
"\e[1~": beginning-of-line
"\e[4~": end-of-line
"\e[5~": beginning-of-history
"\e[6~": end-of-history
"\e[3~": delete-char
"\e[2~": quoted-insert