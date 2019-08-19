%global         srcname gtk-theme
%global         commit f75e86a1d79458a1bd1b0a6e786c880a28cd4d40
%global         shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           pop-gtk-theme
Version:        4.1.4
Release:        %{shortcommit}
Summary:        System76 Pop!_OS GTK theme

%global         _vpath_srcdir %{srcname}-%{commit}

License:        GPLv2 or CC-BY-SA
URL:            https://github.com/pop-os/%{srcname}
Source:         %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz

#BuildRequires:  gdk-pixbuf2-devel
#BuildRequires:  glib2-devel
BuildRequires:  inkscape
#BuildRequires:  librsvg2-devel
#BuildRequires:  libtool
#BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  optipng
BuildRequires:  sassc

BuildArch:      noarch

Requires:       gtk-murrine-engine

%description
Pop_Icons is the icon theme for Pop!_OS. It uses a semi-flat design with raised 3D motifs to help give depth to icons.

Pop_Icons take inspiration from the Adwaita GNOME Icons.

%global debug_package %{nil}

%prep
%autosetup -c

%build
make -C %{srcname}-%{commit} %{?_smp_mflags}

%install
%{__mkdir} -p %{buildroot}/%{_datadir}/themes/Pop
%{__mkdir} -p %{buildroot}/%{_datadir}/themes/Pop-light
%{__mkdir} -p %{buildroot}/%{_datadir}/themes/Pop-dark
%{__mkdir} -p %{buildroot}/%{_datadir}/themes/Pop-slim
%{__mkdir} -p %{buildroot}/%{_datadir}/themes/Pop-slim-light
%{__mkdir} -p %{buildroot}/%{_datadir}/themes/Pop-slim-dark
make -C %{srcname}-%{commit} DESTDIR=%{buildroot} install

%files
%{_datadir}/themes/*
