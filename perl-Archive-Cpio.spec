%define upstream_name	 Archive-Cpio
%define upstream_version 0.10

Summary:	Manipulations of cpio archives
Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Archive-Cpio
Source0:	https://cpan.metacpan.org/authors/id/P/PI/PIXEL/Archive-Cpio-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test)
BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP

%description
Archive::Cpio provides a few functions to read and write cpio files.

cpio-filter is a script using Archive::Cpio that transforms a cpio archive on
the fly

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes
%{perl_vendorlib}/Archive/Cpio*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

