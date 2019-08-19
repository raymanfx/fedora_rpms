%global         srcname icon-theme
%global         commit a9d7ecce6978bad1e589030a2565da488bc56e63
%global         shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           pop-icon-theme
Version:        0.1
Release:        %{shortcommit}
Summary:        System76 Pop!_OS icon theme

%global         _vpath_srcdir %{srcname}-%{commit}

License:        CC-BY-SA
URL:            https://github.com/pop-os/%{srcname}
Source:         %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz

BuildRequires: meson

BuildArch: noarch

%description
Pop_Icons is the icon theme for Pop!_OS. It uses a semi-flat design with raised 3D motifs to help give depth to icons.

Pop_Icons take inspiration from the Adwaita GNOME Icons.

%global debug_package %{nil}

%prep
%autosetup -c

%build
%meson
%meson_build

%install
%meson_install

%files
%{_prefix}/share/icons/Pop/*
