%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	NZ
%define		_status		alpha
%define		_pearname	Validate_NZ

Summary:	%{_pearname} - Validation class for New Zeland
Summary(pl):	%{_pearname} - Klasa sprawdzaj�ca poprawno�� dla Nowej Zelandii
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	1
Epoch:		0
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	09636973b4820a59695232f003063ad8
URL:		http://pear.php.net/package/Validate_NZ/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
Pakiet do sprawdzanie poprawno�ci danych dla Nowej Zelandii takich
jak:
 - numery IRD
 - kody region�w
 - numery telefonu
 - kody pocztowe
 - numery konta bankowego
 - tablice rejestracyjne pojazd�w

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
