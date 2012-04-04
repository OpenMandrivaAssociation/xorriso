%define rel 1

Summary:	ISO 9660 Rock Ridge Filesystem Manipulator
Name:		xorriso
Version:	1.2.2
%if %{mdvver} <= 201020
Release:	%mkrel %{rel}
%else
Release:	%{rel}
%endif
License:	GPLv3+
Group:		Archiving/Cd burning
URL:		http://www.gnu.org/software/xorriso/xorriso_eng.html
Source0:	http://www.gnu.org/software/xorriso/%{name}-%{version}.tar.gz
Source1:	http://www.gnu.org/software/xorriso/%{name}-%{version}.tar.gz.sig
BuildRequires:	zlib-devel
BuildRequires:	acl-devel
BuildRequires:	bzip2-devel
BuildRequires:	attr-devel

%description
xorriso copies file objects from POSIX compliant filesystems into Rock Ridge 
enhanced ISO 9660 filesystems and allows session-wise manipulation of such
filesystems.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc AUTHORS README texinfo.tex
%{_bindir}/osirrox
%{_bindir}/xorrecord
%{_bindir}/xorriso
%{_bindir}/xorrisofs
%{_datadir}/info/xorr*.info*
%{_mandir}/man1/xorr*.1*
