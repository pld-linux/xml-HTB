# TODO: optflags
Summary:	Tool for automatic generation scripts for HTB
Summary(pl.UTF-8):	Narzędzie do automatycznego generowania skryptów dla HTB
Name:		xml-HTB
Version:	1.3
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/xml-htb/%{name}-%{version}.tar.gz
# Source0-md5:	eb042fa44f0fbd25fcac7c6008be7f07
URL:		http://sourceforge.net/projects/xml-htb/
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xml-HTB is a tool for automatic generation of bash scripts that sets
up HTB on Linux. It uses XML configuration files. It's easy to use, It
have a lot of features: multiple depths of classes, configurable leaf,
u32 and fw filters...

%description -l pl.UTF-8
xml-HTB jest narzędziem do automatycznego generowania skryptów, które
ustawiają HTB. Używa plików konfiguracyjnych w formacie XML. Jest
prosty w użyciu i ma wiele możliwości: różne głębokości klas,
konfigurowalne liście, filtry u32 i fw...

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
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
%dir %{_sysconfdir}/xml-HTB
# XXX: %config not needed?
%{_sysconfdir}/xml-HTB/*.xml
%dir %{_sysconfdir}/xml-HTB/dtd
%{_sysconfdir}/xml-HTB/dtd/c-xml-HTB.dtd
