%define upstream_name	 Archive-Cpio
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 3

Summary:	Manipulations of cpio archives
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PI/PIXEL/%{upstream_name}-%{upstream_version}.tar.gz
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Archive::Cpio provides a few functions to read and write cpio files.

cpio-filter is a script using Archive::Cpio that transforms a cpio archive on
the fly

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Archive/Cpio*
%{_bindir}/*
%{_mandir}/*/*
