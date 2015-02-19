Name:		berusky
Version:	1.4
Release:	2
Summary:	Sokoban clone
License:	GPLv2+
Group:		Games/Puzzles
URL:		http://www.anakreon.cz/
Source0:	http://anakreon.cz/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-1.4-gettext.patch
Patch1:		%{name}-1.4-datapath.patch
Source1:	berusky.png
BuildRequires:	pkgconfig(sdl)
BuildRequires:	gettext-devel
Requires:	%{name}-data

%description
Berusky is a 2D logic game based on an ancient puzzle named Sokoban.

An old idea of moving boxes in a maze has been expanded with new logic
items such as explosives, stones, special gates and so on.
In addition, up to five bugs can cooperate and be controlled by the player.

This package contains a binary for the game.

%prep
%setup -q
%patch0 -p1 -b .gettext
%patch1 -p0
touch config.rpath ABOUT-NLS

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

# Remove docs from a wrong directory
%__rm -rf %{buildroot}%{_prefix}/doc

# Install icon
%__install -D -p %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# Desktop-file
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Berusky
Comment=Rescue the bugs!
Exec=%{_gamesbindir}/%{name}
Terminal=false
Type=Application
StartupNotify=false
Icon=%{name}
Categories=Game;LogicGame;
EOF

# Move berusyk.ini to /etc
%__mkdir_p %{buildroot}%{_sysconfdir}/%{name}
%__mv %{buildroot}%{_datadir}/%{name}/%{name}.ini %{buildroot}%{_sysconfdir}/%{name}

# Remove empty %{_datadir}, and create %{_gamesdatadir} for files from berusky-data
%__rm -fR %{buildroot}%{_datadir}/%{name}
%__mkdir_p %{buildroot}%{_gamesdatadir}/%{name}

# Move binary to /usr/games
%__mv %{buildroot}%{_bindir} %{buildroot}%{_gamesbindir}


%files
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png



