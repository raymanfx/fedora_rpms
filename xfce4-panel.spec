%global xfceversion 4.14

Name:           xfce4-panel
Version:        4.14.0
Release:        1%{?dist}
Summary:        Next generation panel for Xfce

License:        GPLv2+ and LGPLv2+
URL:            http://www.xfce.org/
#VCS git:git://git.xfce.org/xfce/xfce4-panel
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

# clock icon taken from system-config-date, license is GPLv2+
Source1:        xfce4-clock.png
Source2:        xfce4-clock.svg
## Downstream patches
# FIXME: do the patch once SIG has decided about a panel layout
## Patch10:        xfce4-panel-4.8.2-defaults.patch

BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  garcon-devel >= 0.6.0
BuildRequires:  libxml2-devel >= 2.4.0
BuildRequires:  startup-notification-devel
BuildRequires:  exo-devel >= 0.3.93
BuildRequires:  libwnck3-devel >= 3.14
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala

# xfce4-iconbox isn't in Xfce 4.4
Obsoletes:      xfce4-iconbox <= 4.2.3-4.fc6
# xfce4-systray isn't in Xfce 4.4
Obsoletes:      xfce4-systray <= 4.2.3-3.fc6
# xfce4-toys isn't in Xfce 4.4
Obsoletes:      xfce4-toys <= 4.2.3-3.fc6
# xfce4-trigger-launcher isn't in Xfce 4.4
Obsoletes:      xfce4-trigger-launcher <= 4.2.3-3.fc6
# xfce4-showdesktop-plugin isn't in Xfce 4.4
Obsoletes:      xfce4-showdesktop-plugin <= 0.4.0-7.fc6
# xfce4-taskbar-plugin isn't in Xfce 4.4
Obsoletes:      xfce4-taskbar-plugin <= 0.2.2-7.fc6
# xfce4-windowlist-plugin isn't in Xfce 4.4
Obsoletes:      xfce4-windowlist-plugin <= 0.1.0-7.fc6
# xfce4-xmms-plugin isn't in F11
Obsoletes:      xfce4-xmms-plugin <= 0.5.1-3.fc11
# xfce4-volstatus-icon isn't in F15
Obsoletes:      xfce4-volstatus-icon <= 0.1.0-7.fc15
# xfce4-stopwatch-plugin isn't in F15
Obsoletes:      xfce4-stopwatch-plugin <= 0.2.0-3.fc15
# xfce4-xfapplet-plugin isn't in F15
Obsoletes:      xfce4-xfapplet-plugin <= 0.1.0-10.fc15
# xfce4-radio-plugin isn't in f22
Obsoletes:      xfce4-radio-plugin <= 0.5.1-10.fc22
# xfce4-quicklauncher-plugin isn't in f22
Obsoletes:      xfce4-quicklauncher-plugin <= 1.9.4-20.fc22
# xfce4-modemlights-plugin isn't in f22
Obsoletes:      xfce4-modemlights-plugin <= 0.1.3.99-18.fc22
# xfce4-xfswitch-plugin isn't in f22
Obsoletes:      xfce4-xfswitch-plugin <= 0.0.1-13.fc22
# xfce4-wmdock-plugin isn't in f22
Obsoletes:      xfce4-wmdock-plugin <= 0.3.4-12.fc22

%description
This package includes the panel for the Xfce desktop environment.

%package devel
Summary:        Development headers for xfce4-panel
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       libxfce4util-devel >= %{xfceversion}
Requires:       libxfce4ui-devel >= %{xfceversion}

%description devel
This package includes the header files you will need to build
plugins for xfce4-panel.


%prep
%setup -q
#patch10 -p1 -b .default

# Fix icon in 'Add new panel item' dialog
sed -i 's|Icon=office-calendar|Icon=xfce4-clock|g' plugins/clock/clock.desktop.in.in


%build
%configure --enable-gtk-doc --disable-static 

# Remove rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# The LD_LIBRARY_PATH hack is needed for --enable-gtk-doc
# because lt-libxfce4panel-scan is linked against libxfce4panel
export LD_LIBRARY_PATH="`pwd`/libxfce4panel/.libs"

%make_build

%install
%make_install

# fix permissions for installed libs
chmod 755 %{buildroot}%{_libdir}/*.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# remove duplicate docs
rm -f %{buildroot}%{_docdir}/xfce4-panel/README.gtkrc-2.0

# FIXME: We need to own these dirs until all plugins are ported to Xfce 4.8
mkdir -p %{buildroot}%{_libexecdir}/xfce4/panel-plugins
mkdir -p %{buildroot}%{_libdir}/xfce4/panel-plugins
mkdir -p %{buildroot}%{_datadir}/xfce4/panel-plugins

%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/panel-desktop-handler.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/panel-preferences.desktop

# install additional icons
install -pm 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -pm 0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README docs/README.gtkrc-2.0
%config(noreplace) %{_sysconfdir}/xdg/xfce4/panel/default.xml
%{_bindir}/*
%{_libdir}/libxfce4panel-*.so.*
%{_libdir}/xfce4/panel/
%{_libdir}/girepository-1.0/libxfce4panel-2.0.typelib
%{_datadir}/gir-1.0/libxfce4panel-2.0.gir
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfce4/panel/
%{_datadir}/applications/*.desktop
%{_datadir}/vala/vapi/libxfce4panel-2.0.deps
%{_datadir}/vala/vapi/libxfce4panel-2.0.vapi
# FIXME: Remove these when no longer needed
%dir %{_libexecdir}/xfce4/panel-plugins/
%dir %{_libdir}/xfce4/panel-plugins
%dir %{_datadir}/xfce4/panel-plugins

%files devel
%{_libdir}/pkgconfig/*
%{_libdir}/libxfce4panel-*.so
%doc %{_datadir}/gtk-doc/html/libxfce4panel-*/
%{_includedir}/xfce4/libxfce4panel-*/

%changelog
* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.14.0-1
- Update to 4.14.0

* Tue Jul 30 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 4.13.7-2
- rebuild for xfce 4.14pre3

* Mon Jul 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.7-1
- Update to 4.13.7

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.6-2
- Enable gobject introspection

* Mon Jul 01 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.6-1
- Update to 4.13.6

* Sat May 18 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.5-1
- Update to 4.13.5

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.4-1
- Update to 4.13.4

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.13.3-20
- Update to 4.13.3

* Tue Jul 17 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.12.2-4
- Add gcc-c++ as BR
- spec cleanup

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.12.2-1
- Update to 4.12.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 25 2016 Kevin Fenzi <kevin@scrye.com> - 4.12.1-1
- Update to 4.12.1. Fixes bug #1388439

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Kevin Fenzi <kevin@scrye.com> 4.12.0-3
- Obsolete some panel plugins we are dropping with Fedora 22.

* Sat Feb 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.12.0-2
- Build with GTK3 support

* Sat Feb 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.12.0-1
- Update to stable release 4.12.0

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 4.10.1-7
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 02 2013 Kevin Fenzi <kevin@scrye.com> 4.10.1-4
- Rebuild for new libwnck

* Mon Oct 21 2013 Kevin Fenzi <kevin@scrye.com> 4.10.1-3
- Add patch to fix autohide and session menu issue. Fixes bug #1021548

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 05 2013 Kevin Fenzi <kevin@scrye.com> 4.10.1-1
- Update to 4.10.1

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 29 2012 Christoph Wickert <cwickert@fedoraproject.org> - 4.10.0-1
- Update to 4.10.0 final
- Make build verbose
- Add VCS key

* Sat Apr 14 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.2-1
- Update to 4.9.2 (Xfce 4.10pre2)

* Mon Apr 02 2012 Kevin Fenzi <kevin@scrye.com> - 4.9.1-1
- Update to 4.9.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.6-3
- Rebuilt for glibc bug#747377

* Sun Oct 23 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.6-2
- Fix directory menu plugin's 'Open in Terminal' option (#748226)
- No longer depend on xfce4-doc (#721288)

* Thu Sep 22 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.6-1
- Update to 4.8.6

* Tue Jun 21 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.5-1
- Update to 4.8.5

* Sun Jun 19 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.4-1
- Update to 4.8.4

* Sun May 08 2011 Christoph Wickert <wickert@kolabsys.com> - 4.8.3-2
- Add xfce4-clock icons for the 'Add new items' dialog (#694902)

* Wed Apr 06 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.3-1
- Update to 4.8.3
- Remove upstreamed add_button_release_event_to_proxy_item.patch

* Fri Mar 25 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.2-3
- Fix switching grouped windows in the taskbar (#680779)

* Tue Mar 08 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.2-2
- Include mixer in default panel config (#636227)
- Obsolete old plugins (#682491)

* Fri Feb 25 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.8.2-1
- Update to 4.8.2

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Kevin Fenzi <kevin@tummy.com> - 4.8.1-1
- Update to 4.8.1

* Sun Jan 16 2011 Kevin Fenzi <kevin@tummy.com> - 4.8.0-1
- Update to 4.8.0

* Sun Jan 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.7-1
- Update to 4.7.7

* Sun Dec 19 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.6-2
- Own %%{_libexecdir}/xfce4/panel-plugins/ for now

* Sun Dec 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.6-1
- Update to 4.7.6

* Sat Dec 04 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.5-1
- Update to 4.7.5

* Mon Nov 08 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.4-1
- Update to 4.7.4

* Sun Sep 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.7.3-1
- Update to 4.7.3
- Update icon-cache scriptlets

* Fri May 21 2010 Kevin Fenzi <kevin@tummy.com> - 4.6.4-1
- Update to 4.6.4

* Sat Feb 13 2010 Kevin Fenzi <kevin@tummy.com> - 4.6.3-2
- Add patch for DSO fix. Fixes bug 564694

* Wed Dec 30 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.3-1
- Update to 4.6.3

* Fri Oct 16 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.2-1
- Update to 4.6.2
- Drop explicit requires on Terminal and mousepad

* Wed Sep 30 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.1-4
- Add xfswitch-plugin to default panel config (#525563)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.1-2
- Bring back the multilib patch to fix #505165

* Sun Apr 19 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.1-1
- Update to 4.6.1

* Sat Feb 28 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.6.0-2
- Fix directory ownership problems
- Require xfce4-doc
- Mark gtk-doc files as %%doc
- Obsolete the xfce4-xmms-plugin

* Thu Feb 26 2009 Kevin Fenzi <kevin@tummy.com> - 4.6.0-1
- Update to 4.6.0
- Remove some unneeded BuildRequires

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.99.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Kevin Fenzi <kevin@tummy.com> - 4.5.99.1-1
- Update to 4.5.99.1

* Tue Jan 13 2009 Kevin Fenzi <kevin@tummy.com> - 4.5.93-1
- Update to 4.5.93

* Sat Dec 27 2008 Kevin Fenzi <kevin@tummy.com> - 4.5.92-1
- Update to 4.5.92

* Mon Oct 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 4.4.3-1
- Update to 4.4.3
- Remove mailwatch-plugin from default panel config again
- BuildRequire intltool
- Update gtk-update-icon-cache scriptlets
- Fix BuildRoot tag

* Thu Oct 02 2008 Christoph Wickert <cwickert@fedoraproject.org> - 4.4.2-5
- Fix FTBFS (#465058)
- Update defaults patch to include mailwatch plugin
- Remove old xfce4-iconbox and xftaskbar dummy files

* Tue Apr 08 2008 Kevin Fenzi <kevin@tummy.com> - 4.4.2-4
- Add defaults patch. See bug 433573

* Sat Feb 23 2008 Kevin Fenzi <kevin@tummy.com> - 4.4.2-3
- Drop dependency on xfce-icon-theme. See bug 433152

* Sun Feb 10 2008 Kevin Fenzi <kevin@tummy.com> - 4.4.2-2
- Rebuild for gcc43

* Sun Dec  2 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.2-1
- Update to 4.4.2 (fixes 382471)
- Drop Provides/Obsoletes for xfce4-modemlights-plugin to come back.

* Mon Aug 27 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.1-4
- Update License tag

* Mon Jul 30 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.1-3
- Own %%{_datadir}/xfce4/

* Wed Jun  6 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.1-2
- Fix multilib issues. Bug #228168

* Wed Apr 11 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.1-1
- Upgrade to 4.4.1

* Tue Apr  3 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.0-2
- Own %%{_libexecdir}/xfce4/
- Do not own %%{_libdir}/xfce4/mcs-plugins

* Sun Jan 21 2007 Kevin Fenzi <kevin@tummy.com> - 4.4.0-1
- Upgrade to 4.4.0

* Sat Nov 11 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.2-2
- Require xfce4-icon-theme. 

* Thu Nov  9 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.2-1
- Update to 4.3.99.2

* Fri Oct  6 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-7
- List full old versions in Obsoletes

* Fri Oct  6 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-6
- Tweak Obsolete versions

* Thu Oct  5 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-5
- Add Requires libxfcegui4-devel to devel package

* Thu Oct  5 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-4
- Add period to description
- Fix defattr
- Add gtk-update-icon-cache in post/postun

* Wed Oct  4 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-3
- Add Requires for mousepad and Terminal
- Bump for devel checkin

* Sun Sep 24 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-2
- Obsolete some more plugins who's functionality has been pulled in. 
- Own the libexecdir/xfce4/panel-plugins for new plugins. 

* Sun Sep  3 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.99.1-1
- Update to 4.3.99.1
- Add Provides/Obsoletes for xfce4-iconbox, xfce4-systray, xfce4-toys, xfce4-trigger-launcher
- Fix typo in devel subpackage summary
- Add post/postun ldconfig calls

* Thu Aug 24 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.90.2-2
- fix .so in main package
- add Requires for libxfce4util-devel
- don't own includedir/xfce4 (libxfce4util-devel should)

* Tue Jul 11 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.90.2
- Upgrade to 4.3.90.2

* Thu Apr 27 2006 Kevin Fenzi <kevin@tummy.com> - 4.3.90.1.fc6
- Upgrade to 4.3.90.1

* Thu Feb 16 2006 Kevin Fenzi <kevin@tummy.com> - 4.2.3-3.fc5
- Rebuild for fc5

* Tue Jan 31 2006 Kevin Fenzi <kevin@tummy.com> - 4.2.3-2.fc5
- added imake and libXt-devel BuildRequires for modular xorg

* Mon Nov  7 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.3-1.fc5
- Update to 4.2.3
- Added dist tag
- Tweaked panel-htmlview patch to add - in translation

* Tue May 17 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.2-1.fc4
- Update to 4.2.2

* Fri Mar 25 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1.1-4.fc4
- lowercase Release

* Thu Mar 24 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1.1-3.FC4
- Added htmlview patch
- Removed unneeded la/a files

* Sat Mar 19 2005 Warren Togami <wtogami@redhat.com> - 4.2.1.1-2
- remove stuff

* Thu Mar 17 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1.1-1
- Updated to 4.2.1.1 version
- Changed Requires/Buildrequires to 4.2.1, as xfce4-panel was the only package updated to 4.2.1.1

* Tue Mar 15 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.1-1
- Updated to 4.2.1 version

* Tue Mar  8 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.0-4
- Fixed case of Xfce

* Sun Mar  6 2005 Kevin Fenzi <kevin@tummy.com> - 4.2.0-3
- Created a new patch to change mozilla -mail to launchmail
- Moved the includes to the devel subpackage

* Thu Feb 03 2005 Than Ngo <than@redhat.com> 4.2.0-2
- new sub package xfce4-panel-devel

* Tue Jan 25 2005 Than Ngo <than@redhat.com> 4.2.0-1
- 4.2.0

* Wed Dec 08 2004 Than Ngo <than@redhat.com> 4.0.6-2 
- add patch to use lauchmail/htmlview #142160

* Mon Jul 19 2004 Than Ngo <than@redhat.com> 4.0.6-1
- update to 4.0.6
- remove some unneeded patch files

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun 01 2004 Than Ngo <than@redhat.com> 4.0.5-4
- add buildrequires on startup-notification-devel, bug #124948
- use %%find_lang macros, bug #124948

* Mon May 31 2004 Than Ngo <than@redhat.com> 4.0.5-3
- own %%{_libdir}i/xfce4, bug #124826

* Mon Apr 26 2004 Than Ngo <than@redhat.com> 4.0.5-2
- Change more defaults for fedora, use startup notification
  by default, remove "-splash" option from mozilla launcher. Thanks to Olivier Fourdan
- Patch to avoid crash at startup under some rare circumstances
- Change defaults for fedora

* Thu Apr 15 2004 Than Ngo <than@redhat.com> 4.0.5-1
- update to 4.0.5

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 27 2004 Than Ngo <than@redhat.com> 4.0.3-2
- fixed dependant libraries check on x86_64

* Fri Jan 09 2004 Than Ngo <than@redhat.com> 4.0.3-1
- 4.0.3 release

* Thu Dec 25 2003 Than Ngo <than@redhat.com> 4.0.2-1
- 4.0.2 release

* Tue Dec 16 2003 Than Ngo <than@redhat.com> 4.0.1-1
- initial build

