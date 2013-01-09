%define upstream_name	 Archive-Cpio
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Manipulations of cpio archives
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PI/PIXEL/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP

%description
Archive::Cpio provides a few functions to read and write cpio files.

cpio-filter is a script using Archive::Cpio that transforms a cpio archive on
the fly

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%{makeinstall_std}

%files 
%doc Changes
%{perl_vendorlib}/Archive/Cpio*
%{_bindir}/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.90.0-3mdv2012.0
+ Revision: 765052
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.90.0-2
+ Revision: 763476
- rebuilt for perl-5.14.x

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1
+ Revision: 682110
- update to new version 0.09

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-2
+ Revision: 667026
- mass rebuild

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1
+ Revision: 634259
- new version

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.1
+ Revision: 401787
- rebuild using %%perl_convert_version
- fixed license field

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.07-4mdv2009.1
+ Revision: 351669
- rebuild

* Thu Jul 24 2008 Olivier Blin <blino@mandriva.org> 0.07-3mdv2009.0
+ Revision: 245449
- fix man synopsis

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.07-2mdv2009.0
+ Revision: 223499
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Dec 19 2007 Pixel <pixel@mandriva.com> 0.07-1mdv2008.1
+ Revision: 133825
- 0.07:
- allow ->read($filehandle) and ->write($filehandle) (rt.cpan.org #31686)
- fix ->size on Archive::Cpio::File (rt.cpan.org #31684) (thanks to teek)

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.06-2mdv2008.0
+ Revision: 67582
- rebuild

* Wed Apr 25 2007 Pixel <pixel@mandriva.com> 0.06-1mdv2008.0
+ Revision: 18185
- new release, 0.06
- handle ODC (octal) format (Mike Sliczniak)


* Thu Mar 15 2007 Pixel <pixel@mandriva.com> 0.05-1mdv2007.1
+ Revision: 144367
- new release, 0.05
- add ->add_data, ->get_file
- rename ->list into ->get_files

* Thu Mar 15 2007 Pixel <pixel@mandriva.com> 0.04-1mdv2007.1
+ Revision: 144301
- bug fix release, 0.04
- fix using STDIN which can't seek back

* Thu Mar 15 2007 Pixel <pixel@mandriva.com> 0.03-1mdv2007.1
+ Revision: 144104
- new release, 0.03
- switch to an OO API to handle different archive formats
- handle old binary format (only little-endian for now)
- add option --in-place to cpio-filter

* Thu Mar 01 2007 Pixel <pixel@mandriva.com> 0.02-1mdv2007.1
+ Revision: 130364
- fix padding at end of generated cpio

* Wed Feb 28 2007 Pixel <pixel@mandriva.com> 0.01-1mdv2007.1
+ Revision: 127273
- initial release
- Create perl-Archive-Cpio

