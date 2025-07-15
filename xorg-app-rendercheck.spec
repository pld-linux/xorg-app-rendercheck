Summary:	rendercheck application - simple tests of the X Render extension
Summary(pl.UTF-8):	Aplikacja rendercheck - proste testy rozszerzenia X Render
Name:		xorg-app-rendercheck
Version:	1.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/test/rendercheck-%{version}.tar.xz
# Source0-md5:	4b3b862b4fad00a0ca9183df71b6bb42
URL:		https://xorg.freedesktop.org/
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
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
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README doc/TODO
%attr(755,root,root) %{_bindir}/rendercheck
%{_mandir}/man1/rendercheck.1*
