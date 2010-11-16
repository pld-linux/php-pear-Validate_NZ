%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Validate_NZ
Summary:	%{_pearname} - Validation class for New Zeland
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Nowej Zelandii
Name:		php-pear-%{_pearname}
Version:	0.1.3
Release:	1
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b706b28613ba7709ab9d49762e4e06b3
URL:		http://pear.php.net/package/Validate_NZ/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for NZ such as:
 - IRD numbers
 - Regional codes
 - Telephone number
 - Postal code
 - Bank AC
 - Vehical License Plates

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzanie poprawności danych dla Nowej Zelandii takich
jak:
 - numery IRD
 - kody regionów
 - numery telefonu
 - kody pocztowe
 - numery konta bankowego
 - tablice rejestracyjne pojazdów

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/LICENSE
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/NZ.php

%files tests
%defattr(644,root,root,755)
%dir %{php_pear_dir}/tests/Validate_NZ
%dir %{php_pear_dir}/tests/Validate_NZ/tests
%{php_pear_dir}/tests/Validate_NZ/tests/Validate_NZ.phpt
