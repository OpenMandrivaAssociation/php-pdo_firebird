%define modname pdo_firebird
%define dirname pdo_firebird
%define soname pdo_firebird.so
%define inifile 78_%{modname}.ini

%define major 5
%define libname %mklibname php5_common %{major}

Summary:	Firebird/InterBase driver for PDO
Name:		php-%{modname}
Version:	5.3.3
Release:	%mkrel 2
Group:		Development/PHP
URL:		http://www.php.net
License:	PHP License
Source0:	%{modname}.ini
Requires:	php-pdo >= 0:%{version}
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	firebird-devel
Requires:	%{libname} >= 3:%{version}
Epoch:		0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PDO_MYSQL is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to MySQL 3.x and 4.x databases.
 
PDO_MYSQL will take advantage of native prepared statement support present in
MySQL 4.1 and higher. If you're using an older version of the mysql client
libraries, PDO will emulate them for you.

%prep

%setup -c -T
cp -dpR %{_usrsrc}/php-devel/extensions/%{dirname}/* .

%build
%serverbuild

phpize
%configure2_5x \
    --with-libdir=%{_lib} \
    --with-pdo-firebird=%{_libdir}/firebird

%make
mv modules/*.so .

%install
rm -rf %{buildroot} 

install -D -m0755 %{soname} %{buildroot}%{_libdir}/php/extensions/%{soname}
install -D -m0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/php.d/%{inifile}

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CREDITS package*.xml tests
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}

