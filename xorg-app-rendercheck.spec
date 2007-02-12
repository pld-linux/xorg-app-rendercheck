Summary:	rendercheck application - simple tests of the X Render extension
Summary(pl.UTF-8):   Aplikacja rendercheck - proste testy rozszerzenia X Render
Name:		xorg-app-rendercheck
Version:	1.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/rendercheck-%{version}.tar.bz2
# Source0-md5:	76ffc65a3b708d380a66823a56b7be15
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXrender-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rendercheck application - a program to test a Render extension
implementation against separate calculations of expected output.

%description -l pl.UTF-8
Aplikacja rendercheck - program do sprawdzania implementacji
rozszerzenia Render względem oddzielnie wyliczonego oczekiwanego
rezultatu.

%prep
%setup -q -n rendercheck-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README doc/TODO
%attr(755,root,root) %{_bindir}/rendercheck
%{_mandir}/man1/rendercheck.1*
