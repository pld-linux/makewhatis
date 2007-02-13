Summary:	makewhatis - FreeBSD C implementation, Linux port
Summary(pl.UTF-8):	makewhatis - linuksowy port implementacji w C z FreeBSD
Name:		makewhatis
Version:	2005.08.02
Release:	0.1
License:	BSD
Group:		Applications
Source0:	http://twittner.host.sk/files/makewhatis/%{name}-%{version}.tar.gz
# Source0-md5:	5d21f332a2b79a9dcaf55f3f29c6d9e2
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9.4
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
makewhatis - FreeBSD C implementation, Linux port.

%description -l pl.UTF-8
makewhatis - linuksowy port implementacji w C z FreeBSD.

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
