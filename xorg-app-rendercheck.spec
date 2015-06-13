Summary:	rendercheck application - simple tests of the X Render extension
Summary(pl.UTF-8):	Aplikacja rendercheck - proste testy rozszerzenia X Render
Name:		xorg-app-rendercheck
Version:	1.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/rendercheck-%{version}.tar.bz2
# Source0-md5:	61d02044a2b1b1afb20334308bdca2d0
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
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
%doc AUTHORS ChangeLog COPYING NEWS README doc/TODO
%attr(755,root,root) %{_bindir}/rendercheck
%{_mandir}/man1/rendercheck.1*
