Summary:	ISO 9660 Rock Ridge Filesystem Manipulator
Name:		xorriso
Version:	1.4.2
Release:	ZED'S DEAD
License:	GPLv3+
Group:		Archiving/Cd burning
URL:		https://www.gnu.org/software/xorriso/xorriso_eng.html
Source0:	http://www.gnu.org/software/xorriso/%{name}-%{version}.tar.gz
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(tcl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	readline-devel

%description
xorriso copies file objects from POSIX compliant filesystems into Rock Ridge 
enhanced ISO 9660 filesystems and allows session-wise manipulation of such
filesystems.

%prep
%setup -q
touch NEWS

%build
# (tpg) clang miscompiles it on i586, and 32bit ISO does not boot
%ifarch %{ix86}
export CC=gcc
export CXX=g++
%endif

%configure \
	--enable-libreadline \
	--disable-debug

%make

%install
%makeinstall_std

%files
%doc AUTHORS README texinfo.tex
%{_bindir}/osirrox
%{_bindir}/xorrecord
%{_bindir}/xorriso
%{_bindir}/xorriso-tcltk
%{_bindir}/xorrisofs
%{_datadir}/info/xorr*.info*
%{_mandir}/man1/xorr*.1*
