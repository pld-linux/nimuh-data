Summary:	Nimuh - a game ambiented in Andalusia (data package)
Summary(pl.UTF-8):	Nimuh - gra umiejscowiona w Andaluzji (pliki z danymi)
Name:		nimuh-data
Version:	1.02
Release:	0.2
License:	Creative Commons Attribution-Noncommercial-Share Alike v2.5 Spain
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/nimuh/%{name}-%{version}.tar.gz
# Source0-md5:	ae5d0bc6e49a8b989ce6d0b3421bf948
URL:		http://www.nimuh.com/index.php?lang=en
Requires:	nimuh = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nimuh is a game ambiented in Andalusia. A game based in "Theseus and
the Minotaur Mazes" that will go through different andalusian
locations.

This package contains Nimuh data files.

%description -l pl.UTF-8
Nimuh jest grą umiejscowioną w Andaluzji. Jest oparta na grze "Theseus
and the Minotaur Mazes" (Tezeusz i labirynty Minotaura), ale tu gracz
przemierza różne miejsca w Andaluzji.

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
%dir %{_datadir}/nimuh
%{_datadir}/nimuh/data
