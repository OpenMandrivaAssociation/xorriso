Name:		xorriso
Version:	1.0.8
Release:	%mkrel 1
Summary:	ISO 9660 Rock Ridge Filesystem Manipulator
License:	GPLv3
Source0:	http://www.gnu.org/software/xorriso/%{name}-%{version}.tar.gz
Source1:	http://www.gnu.org/software/xorriso/%{name}-%{version}.tar.gz.sig
URL:		http://www.gnu.org/software/xorriso/xorriso_eng.html
Group:		File tools 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
xorriso copies file objects from POSIX compliant filesystems into Rock Ridge enhanced ISO 9660 filesystems and allows session-wise manipulation of such filesystems.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%defattr(-,root,root) 
%doc AUTHORS COPYING COPYRIGHT README texinfo.tex
%{_bindir}/osirrox
%{_bindir}/xorrecord
%{_bindir}/xorriso
%{_bindir}/xorrisofs
%{_datadir}/info/xorriso.info.xz
%{_datadir}/info/xorrisofs.info.xz
%{_mandir}/man1/xorriso.1.xz
%{_mandir}/man1/xorrisofs.1.xz
