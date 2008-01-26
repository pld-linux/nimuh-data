%define	_name	nimuh
Summary:	Nimuh is a game ambiented in Andalusia
Name:		%{_name}-data
Version:	1.0
Release:	0.1
License:	Creative Commons
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/nimuh/%{name}-%{version}.tar.gz
# Source0-md5:	f71e242d6a06d6dd769b7cd141be1453
URL:		http://www.nimuh.com/index.php?lang=en
Requires:	%{_name} = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nimuh is a game ambiented in Andalusia. A game based in "Theseus and
the Minotaur Mazes" that will go through different andalusian
locations.

This package contains Nimuh data files.

%prep
%setup -q

%build
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
%dir %{_datadir}/%{_name}
%{_datadir}/%{_name}/data
