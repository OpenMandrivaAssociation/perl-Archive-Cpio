%define upstream_name	 Archive-Cpio
%define upstream_version 0.09

Summary:	Manipulations of cpio archives
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	9
License:	GPLv2+ or Artistic
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

