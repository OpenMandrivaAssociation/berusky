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
BuildRequires:	SDL-devel
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
%__rm -rf %{buildroot}
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

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png



%changelog
* Tue May 01 2012 Andrey Bondrov <abondrov@mandriva.org> 1.4-1mdv2011.0
+ Revision: 794778
- imported package berusky


* Tue May 01 2012 Andrey Bondrov <abondrov@mandriva.org> 1.4-1mdv2010.2
- Import from Mageia
- Update patch0
- Fix Exec path in desktop file
- New version 1.4

* Tue Jan 31 2012 kamil <kamil> 1.3-3.mga2
+ Revision: 203637
- fix paths and make them generic for games
- include mga-fix-working-paths.patch
  o fix paths in berusky.ini
  o fix path of the .ini file

* Mon Jan 30 2012 fwang <fwang> 1.3-2.mga2
+ Revision: 203418
- br gettext-devel
- do not pull gtk2 during build
- use sourcenum
- drop unneeded BR for gtk
- fix desktop file (remove ext from icon)
- SDL req does not exist, and does not to be speficied

* Mon Jan 30 2012 kamil <kamil> 1.3-1.mga2
+ Revision: 203356
- new version 1.3
- drop berusky-level-load.patch (merged upstream)

* Mon Jan 30 2012 kamil <kamil> 1.2-5.mga2
+ Revision: 203314
- adapt .spec for Mageia
- imported package berusky


* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.2-3
- Rebuild for new libpng

* Wed Jun 22 2011 Martin Stransky <stransky@redhat.com> 1.2-2
- Fixed rhbz#689106 - seg. fault after start

* Sun Mar 6 2011 Martin Stransky <stransky@redhat.com> 1.2-1
- updated to 1.2

* Thu Nov 19 2009 Martin Stransky <stransky@redhat.com> 1.1-13
- fixed dirs (#473628)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 2 2008 Martin Stransky <stransky@redhat.com> 1.1-10
- added patch from #458477 - Berusky aborts at end
  of intermediate level 18

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.1-9
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1-8
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Martin Stransky <stransky@redhat.com> 1.1-7
- rebuild

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.1-6
- Rebuild for selinux ppc32 issue.

* Thu Jun 26 2007 Martin Stransky <stransky@redhat.com> 1.1-5
- added a menu entry and an icon

* Wed May 23 2007 Martin Stransky <stransky@redhat.com> 1.1-4
- removed spec files from binary rpm package

* Tue May 8 2007 Martin Stransky <stransky@redhat.com> 1.1-3
- moved documentation from doc/berusky-1.1/berusky to doc/berusky-1.1

* Tue May 8 2007 Martin Stransky <stransky@redhat.com> 1.1-2
- fixed build in mock

* Mon Apr 23 2007 Martin Stransky <stransky@redhat.com> 1.1-1
- fixes from #237416

* Fri Apr 20 2007 Martin Stransky <stransky@redhat.com> 1.0-1
- initial build
