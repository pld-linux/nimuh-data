%define	_name	nimuh
Summary:	Nimuh is a game ambiented in Andalusia
Summary(pl.UTF-8):	Nimuh jest grą o Andaluzji
Name:		%{_name}-data
Version:	1.02
Release:	0.2
License:	Creative Commons
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/nimuh/%{name}-%{version}.tar.gz
# Source0-md5:	ae5d0bc6e49a8b989ce6d0b3421bf948
URL:		http://www.nimuh.com/index.php?lang=en
Requires:	%{_name} = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nimuh is a game ambiented in Andalusia. A game based in "Theseus and
the Minotaur Mazes" that will go through different andalusian
locations.

This package contains Nimuh data files.

%description -l pl.UTF-8

Ten pakiet zawiera dane do gry Nimuh.

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
