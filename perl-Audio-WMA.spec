#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Audio
%define	pnam	WMA
Summary:	Audio::WMA - Perl extension for reading WMA/ASF Metadata
Summary(pl.UTF-8):	Audio::WMA - perlowe rozszerzenie do odczytu metadanych WMA/ASF
Name:		perl-Audio-WMA
Version:	1.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Audio/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b7f9e6c21b9d6f74b46b9a579a8c12dc
URL:		http://search.cpan.org/dist/Audio-WMA/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements access to metadata contained in WMA files.

%description -l pl.UTF-8
Ten moduł implementuje dostęp do metadanych zawartych w plikach WMA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Audio/*.pm
%{_mandir}/man3/*
