%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	DataGrid_DataSource_MDB2
%define		_status		beta
%define		_pearname	Structures_DataGrid_DataSource_MDB2
Summary:	%{_pearname} - DataSource driver using PEAR::MDB2 and an SQL query
Summary(pl.UTF-8):	%{_pearname} - sterownik DataSource do PEAR::MDB2 i kwerend SQL
Name:		php-pear-%{_pearname}
Version:	0.1.11
Release:	2
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a3cf3471cc5c04d81eaadbeb214a2bc1
URL:		http://pear.php.net/package/Structures_DataGrid_DataSource_MDB2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-MDB2 >= 2.0.3
Requires:	php-pear-PEAR-core >= 1:1.4.9
Requires:	php-pear-Structures_DataGrid >= 0.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a DataSource driver for Structures_DataGrid using PEAR::MDB2
and an SQL query.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza sterownik do PEAR::MDB2 i kwerend SQL dla
Structures_DataGrid.

Ta klasa ma w PEAR status: %{_status}.

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
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/DataGrid/DataSource/MDB2.php
