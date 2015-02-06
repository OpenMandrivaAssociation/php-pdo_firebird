%define modname pdo_firebird
%define soname pdo_firebird.so
%define inifile 78_%{modname}.ini

%define major 5
%define libname %mklibname php5_common %{major}

Summary:	Firebird/InterBase driver for PDO
Name:		php-%{modname}
Version:	5.4.4
Release:	2
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
cp -dpR %{_usrsrc}/php-devel/extensions/pdo_firebird/* .

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


%changelog
* Wed Jun 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0:5.4.4-1mdv2012.0
+ Revision: 806393
- 5.4.4

* Thu May 03 2012 Oden Eriksson <oeriksson@mandriva.com> 0:5.4.1-1
+ Revision: 795392
- 5.4.1

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.9-1
+ Revision: 761194
- 5.3.9

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.8-1
+ Revision: 696384
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.7-1
+ Revision: 695344
- rebuilt for php-5.3.7

* Sun Jun 19 2011 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.7-0.0.RC1.1
+ Revision: 685985
- rebuilt for php-5.3.7RC1

* Thu Apr 28 2011 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.6-1
+ Revision: 659828
- stupid bs / rpm5 or whatever.
- rebuilt for php-5.3.6

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.5-1mdv2011.0
+ Revision: 629759
- 5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.4-1mdv2011.0
+ Revision: 628065
- 5.3.4

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.4-0.0.RC1.1mdv2011.0
+ Revision: 600986
- use the correct version

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.3-2mdv2011.0
+ Revision: 600517
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.3-1mdv2011.0
+ Revision: 588737
- 5.3.3

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.2-1mdv2010.1
+ Revision: 514606
- rebuilt for php-5.3.2

* Tue Feb 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.2-0.0.RC2.2mdv2010.1
+ Revision: 506611
- rebuild
- rebuilt against php-5.3.2RC2

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.2-0.0.RC1.1mdv2010.1
+ Revision: 485333
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.1-1mdv2010.1
+ Revision: 468102
- rebuilt against php-5.3.1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.1-0.0.RC1.1mdv2010.0
+ Revision: 451513
- 5.3.1RC1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.0-2mdv2010.0
+ Revision: 451332
- rebuild

* Mon Jul 20 2009 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.0-1mdv2010.0
+ Revision: 398149
- 5.3.0

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 0:5.3.0-0.0.RC2.2mdv2010.0
+ Revision: 397567
- Rebuild

* Mon May 18 2009 Oden Eriksson <oeriksson@mandriva.com> 0:5.3.0-0.0.RC2.1mdv2010.0
+ Revision: 377013
- rebuilt for php-5.3.0RC2

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0:5.2.9-1mdv2009.1
+ Revision: 346388
- 5.2.9

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 0:5.2.9-0.0.RC2.1mdv2009.1
+ Revision: 342256
- import php-pdo_firebird


* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.org> 0:5.2.9-0.0.RC2.1mdv2009.1
- initial Mandriva package
