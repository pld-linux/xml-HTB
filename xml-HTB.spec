Summary:	tool for automatic generation scripts for HTB
Summary(pl):	narzêdzie do automatycznego generowania skryptów dla HTB
Name:		xml-HTB
Version:	1.3
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/xml-htb/%{name}-%{version}.tar.gz
# Source0-md5:	eb042fa44f0fbd25fcac7c6008be7f07
URL:		http://sourceforge.net/projects/xml-htb
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xml-HTB is a tool for automatic generation of bash scripts that sets
up HTB on Linux. It uses xml configuration files. It's easy to use, It
have a lot of features: multiple depths of classes, configurable leaf,
u32 and fw filters, configure both input a

%description -l pl
xml-HTB jest narzêdziem do automatycznego generowania skryptów, które
ustawiaja HTB. U¿ywa plików konfiguracyjnych xml. Jest prosty w
u¿yciu.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xml-HTB
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xml-HTB/dtd

install src/xml-HTB $RPM_BUILD_ROOT%{_sbindir}
install etc/simple.xml $RPM_BUILD_ROOT%{_sysconfdir}/xml-HTB
install etc/complex.xml $RPM_BUILD_ROOT%{_sysconfdir}/xml-HTB
install etc/dtd/c-xml-HTB.dtd $RPM_BUILD_ROOT%{_sysconfdir}/xml-HTB/dtd


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changelog README
%attr(755,root,root) %{_sbindir}/*
%attr(644,root,root) %{_sysconfdir}/xml-HTB/*.xml
%attr(644,root,root) %{_sysconfdir}/xml-HTB/dtd/c-xml-HTB.dtd
