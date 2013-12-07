Summary:	ISO 9660 Rock Ridge Filesystem Manipulator
Name:		xorriso
Version:	1.3.0
Release:	3
License:	GPLv3+
Group:		Archiving/Cd burning
URL:		http://www.gnu.org/software/xorriso/xorriso_eng.html
Source0:	http://www.gnu.org/software/xorriso/%{name}-%{version}.tar.gz
Source1:	http://www.gnu.org/software/xorriso/%{name}-%{version}.tar.gz.sig
BuildRequires:	zlib-devel
BuildRequires:	acl-devel
BuildRequires:	bzip2-devel
BuildRequires:	attr-devel
BuildRequires:	pkgconfig(tcl)

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
%doc AUTHORS README texinfo.tex
%{_bindir}/osirrox
%{_bindir}/xorrecord
%{_bindir}/xorriso
%{_bindir}/xorriso-tcltk
%{_bindir}/xorrisofs
%{_datadir}/info/xorr*.info*
%{_mandir}/man1/xorr*.1*


%changelog
* Mon Jul 23 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.2.4-1
+ Revision: 810672
- update to 1.2.4

* Wed Apr 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.2.2-1
+ Revision: 789188
- update to 1.2.2

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update to new version 1.1.4
    - rewrite spec file
    - add buildrequires

* Mon Jul 04 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.1.0.pl01-1
+ Revision: 688628
- new bugfix release

* Mon Jun 20 2011 Funda Wang <fwang@mandriva.org> 1.1.0-1
+ Revision: 686087
- update to new version 1.1.0

* Fri Apr 15 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.0.8-1
+ Revision: 653089
- update to 1.0.8 (important bugfix)
- add man pages for xorrisofs

* Fri Jan 21 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.0.0-1
+ Revision: 631976
- update to 1.0.0

* Mon Dec 13 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.6.6-1mdv2011.0
+ Revision: 620624
- update to 0.6.6

* Wed Oct 27 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.6.4-1mdv2011.0
+ Revision: 589569
- import xorriso

