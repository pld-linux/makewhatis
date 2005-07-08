Summary:	makewhatis - FreeBSD C implementation, Linux port
Name:		makewhatis
Version:	2005.07.08
Release:	0.1
License:	BSD
Group:		Applications
Source0:	http://twittner.host.sk/files/makewhatis/%{name}-%{version}.tar.gz
# Source0-md5:	9d0a4c8013cc21fe554b11a9a58845c0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
makewhatis - FreeBSD C implementation, Linux port.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_mandir}/man1/%{name}{.1,-bsd.1}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENCES 

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
