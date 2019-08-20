%global xfceversion 4.14

Name:           xfdesktop
Version:        4.14.1
Release:        1%{?dist}
Summary:        Desktop manager for the Xfce Desktop Environment

License:        GPLv2+
URL:            http://www.xfce.org/
#VCS: git:git://git.xfce.org/xfce/xfdesktop
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  gettext
BuildRequires:  exo-devel >= 0.12.0
BuildRequires:  libgudev1-devel >= 145
BuildRequires:  Thunar-devel >= 1.8.0
BuildRequires:  dbus-glib-devel >= 0.84
BuildRequires:  garcon-devel >= 0.1.2
BuildRequires:  libwnck3-devel >= 3.14
BuildRequires:  libnotify-devel >= 0.4.0
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  libSM-devel
BuildRequires:  libICE-devel
Requires:       xfwm4 >= %{xfceversion}
Requires:       xfce4-panel >= %{xfceversion}
Requires:       redhat-menus
Requires:       desktop-backgrounds-compat


%description
This package includes a desktop manager for the Xfce Desktop Environment.


%prep
%setup -q

# change default background for Fedora
sed -i 's/\/backgrounds\/xfce\/xfce-teal.jpg/\/backgrounds\/images\/default.png/g' common/xfdesktop-common.h

%build
%configure

%make_build

%install

%make_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

desktop-file-validate \
    $RPM_BUILD_ROOT/%{_datadir}/applications/xfce-backdrop-settings.desktop

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README TODO ChangeLog NEWS AUTHORS
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/*
%{_datadir}/backgrounds/xfce
%{_mandir}/man1/*


%changelog
* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.14.1-1
- Update to 4.14.1

* Mon Jul 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.6-1
- Update to 4.13.6

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.5-1
- Update to 4.13.5

* Sat May 18 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.4-1
- Update to 4.13.4

* Sat Mar 09 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.3-1
- Update to 4.13.3

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.2-1
- Update to 4.13.2
- Drop upstreamed patch
- Drop ancient conditionals

* Thu Jul 19 2018 Kevin Fenzi <kevin@scrye.com> - 4.12.4-6
- Rebuild for new Thunar.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Kevin Fenzi <kevin@scrye.com> - 4.12.4-1
- Update to 4.12.4. Fixes bug #1468769

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 21 2015 Kevin Fenzi <kevin@scrye.com> 4.12.3-2
- Add upstream patch to not redraw desktop on every mouse click.
- Fixes bug #1252078

* Mon Jul 20 2015 Kevin Fenzi <kevin@scrye.com> 4.12.3-1
- Update to 4.12.3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Kevin Fenzi <kevin@scrye.com> 4.12.2-1
- Update to 4.12.2

* Sun Mar 22 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.12.1-1
- Update to 4.12.1

* Sat Feb 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.12.0-1
- Update latest stable release 4.12.0
- spec cleanup
- changed default background patch to sed
- removed change backdrop patch (testing)

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 4.10.3-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Thu Jan 08 2015 Kevin Fenzi <kevin@scrye.com> 4.10.3-3
- Add patch with fix for crash in timed desktop backdrop changes. Fixes bug #1174160

* Thu Nov 27 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.10.3-2
- bump release 

* Sun Nov 16 2014 Kevin Fenzi <kevin@scrye.com> 4.10.3-1
- Update to 4.10.3 with various fixes.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 10 2013 Kevin Fenzi <kevin@scrye.com> 4.10.2-1
- Update to 4.10.2. Drop upstreamed patch

* Wed Mar 06 2013 Kevin Fenzi <kevin@scrye.com> 4.10.1-2
- Fix background bug. Fixes bug #918646 (Xfce bug #9892)

* Sat Mar 02 2013 Kevin Fenzi <kevin@scrye.com> 4.10.1-1
- Update to 4.10.1

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 06 2012 Christoph Wickert <cwickert@fedoraproject.org> - 4.10.0-4
- Search new background location in list (bugzilla.xfce.org #8799)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 19 2012 Kevin Fenzi <kevin@scrye.com> - 4.10.0-2
- Drop requirement for xfce4-doc which no longer exists. 

* Sun Apr 29 2012 Christoph Wickert <cwickert@fedoraproject.org> - 4.10.0-1
- Update to 4.10.0 final
- Remove obsolete BuildRequirements
- Make build verbose
- Add VCS key

* Sat Apr 14 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.3-1
- Update to 4.9.3 (Xfce 4.10pre2)

* Tue Apr 03 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.2-1
- Update to 4.9.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 13 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.3-1
- Update to 4.8.3

* Thu May 19 2011 Orion Poplawski <orion@cora.nwra.com> - 4.8.2-2
- Drop BR on libxfce4menu-devel

* Fri Apr 22 2011 Kevin Fenzi <kevin@scrye.com> - 4.8.2-1
- Update to 4.8.2

* Tue Feb 08 2011 Kevin Fenzi <kevin@tummy.com> - 4.8.1-3
- Fix requires and rebuild. 

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Kevin Fenzi <kevin@tummy.com> - 4.8.1-1
- Update to 4.8.1

* Sun Jan 16 2011 Kevin Fenzi <kevin@tummy.com> - 4.8.0-1
- Update to 4.8.0

* Sun Jan 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.5-1
- Update to 4.7.5

* Sun Dec 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.4-1
- Update to 4.7.4
- Drop libnotify fix (upstreamed)

* Sat Dec 04 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.3-1
- Update to 4.7.3
- Fix for libnotify 0.7.0 (bugzilla.xfce.org #6915)

* Sat Nov 13 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.2-1
- Update to 4.7.2

* Wed Sep 29 2010 Jesse Keating <jkeating@fedpraproject.org> - 4.6.2-3
- Rebuilt for gcc bug 634757

* Sun Sep 19 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.2-2
- Fix backdrop-image.patch for F14 artwork (#635399)

* Fri May 21 2010 Kevin Fenzi <kevin@tummy.com> - 4.6.2-1
- Update to 4.6.2

* Sat Apr 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.1-6
- Adjustments for recent Goddard artwork changes

* Sun Feb 14 2010 Kevin Fenzi <kevin@tummy.com> - 4.6.1-5
- Add patch for DSO linking. Fixes bug #564826

* Sun Dec 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.1-4
- Menu fixes

* Sun Nov 01 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.1-3
- Fix dependency for default background image

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 19 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.1-1
- Update to 4.6.1

* Mon Apr 13 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.0-4
- Exclude gnome-default-applications from menu to avoid duplicates (#488558)

* Mon Mar 02 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.0-3
- Fix directory ownership problems
- Require xfce4-doc and redhat-menus
- Tweak and clean up Xfce menu

* Fri Feb 27 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.0-2
- Add libSM-devel to BuildRequires

* Thu Feb 26 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.0-1
- Update to 4.6.0
- Remove unneeded BuildRequires

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.99.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Kevin Fenzi <kevin@tummy.com> - 4.5.99.1-1
- Update to 4.5.99.1

* Tue Jan 13 2009 Kevin Fenzi <kevin@tummy.com> - 4.5.93-1
- Update to 4.5.93

* Sun Dec 28 2008 Kevin Fenzi <kevin@tummy.com> - 4.5.92-1
- Update 4.5.92

* Sun Aug 31 2008 Christoph Wickert <fedora@christoph-wickert.de> - 4.4.2-6
- Update xdg-userdir-compat.patch to use upstream's variable names

* Wed Aug 27 2008 Christoph Wickert <fedora@christoph-wickert.de> - 4.4.2-5
- Use Fedora icon for desktop menu plugin (#445986)
- Respect xdg user directory paths (#457740)
- Fix menu icons
- Fix CRITICAL register message on startup
- Fix for x86_64
- Simplify g_list_free code

* Mon Aug 11 2008 Kevin Fenzi <kevin@tummy.com> - 4.4.2-4
- Add partial memory leak patch (partially fixes #428662)

* Tue Feb 19 2008 Kevin Fenzi <kevin@tummy.com> - 4.4.2-3
- Rebuild for gcc43
- Add patch for gcc43

* Mon Dec 17 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.2-2
- Apply patch to show default backdrop

* Sun Nov 18 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.2-1
- Update to 4.4.2

* Mon Aug 27 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.1-3
- Update License tag
- Update patch to have correct desktop image filename

* Mon Jul  9 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.1-2
- Add patch to fix menu lockups with new gtk2

* Wed Apr 11 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.1-1
- Update to 4.4.1

* Tue Apr  3 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.0-2
- Own %%{_libdir}/xfce4/modules/
- Own %%{_datadir}/xfce4-menueditor/

* Sun Jan 21 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.0-1
- Update to 4.4.0

* Fri Nov 10 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.2-1
- Update to 4.3.99.2

* Thu Oct  5 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-5
- Fix defattr
- Add period to the end of description
- Add gtk-update-icon-cache

* Wed Oct  4 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-4
- Bump release for devel checkin

* Sun Sep 17 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-3
- Don't own datadir/xfce4/panel-plugins as thats owned by xfce4-panel

* Sat Sep  9 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-2
- Add exo, dbus-glib and Thunar-devel BuildRequires

* Sun Sep  3 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-1
- Update to 4.3.99.1

* Wed Jul 12 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.90.2
- Update to 4.3.90.2

* Mon May  8 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.90.1
- Update to 4.3.90.1

* Mon Nov  7 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.3-1.fc5
- Update to 4.2.3
- Added dist tag

* Tue May 17 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.2-1.fc4
- Update to 4.2.2

* Fri Mar 25 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-3.fc4
- lowercase Release

* Wed Mar 23 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-2.FC4
- Removed unneeded a/la files
- Rediffed xfdesktop-image patch against current version and applied

* Tue Mar 15 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-1
- Updated to 4.2.1 version

* Thu Jan 27 2005 Than Ngo <than@redhat.com> 4.2.0-1
- 4.2.0

* Wed Sep 01 2004 Than Ngo <than@redhat.com> 4.0.6-2
- get rid useless static library #131485

* Tue Jul 20 2004 Than Ngo <than@redhat.com> 4.0.6-1
- update to 4.0.6
- fix bug #122743, #124951, #125058

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Apr 20 2004 Than Ngo <than@redhat.com> 4.0.5-2
- Change defaults for fedora, thanks to Olivier Fourdan <fourdan@xfce.org>

* Thu Apr 15 2004 Than Ngo <than@redhat.com> 4.0.5-1
- update to 4.0.5

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 27 2004 Than Ngo <than@redhat.com> 4.0.3-2
- fixed dependant libraries check on x86_64

* Wed Jan 14 2004 Than Ngo <than@redhat.com> 4.0.3-1
- 4.0.3 release

* Thu Dec 25 2003 Than Ngo <than@redhat.com> 4.0.2-1
- 4.0.2 release

* Tue Dec 16 2003 Than Ngo <than@redhat.com> 4.0.1-1
- initial build
