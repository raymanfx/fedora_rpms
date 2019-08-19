%define spec_release 1
#
#
#
Summary: AMDGPU Pro OpenCL components
Name: amdgpu-pro-opencl
Version: 19.20
Release: %{spec_release}%{?dist}
License: Redistributable
Source0: https://drivers.amd.com/drivers/linux/amdgpu-pro-%{version}-812932-ubuntu-18.04.tar.xz
Requires: glibc >= 2.17
Requires: libgcc >= 4.2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: dpkg

ExclusiveArch: x86_64

%description
AMDGPU Pro OpenCL components, extracted from the official AMD Ubuntu driver
release package.

This package provides the OpenCL binary driver as well as the ICD loader.

%global debug_package %{nil}

%prep
%setup -n amdgpu-pro-%{version}-812932-ubuntu-18.04

%build
dpkg-deb -x libdrm-amdgpu-amdgpu1_2.4.97-812932_amd64.deb .
dpkg-deb -x libdrm-amdgpu-common_1.0.0-812932_all.deb .
dpkg-deb -x opencl-amdgpu-pro-icd_19.20-812932_amd64.deb .
dpkg-deb -x opencl-orca-amdgpu-pro-icd_19.20-812932_amd64.deb .

mkdir -p etc/ld.so.conf.d
cat > etc/ld.so.conf.d/amdgpu-pro.conf <<EOF
/opt/amdgpu/lib/x86_64-linux-gnu
EOF

%install
%{__mkdir} -p %{buildroot}/etc/ld.so.conf.d
%{__mkdir} -p %{buildroot}/etc/OpenCL/vendors
%{__mkdir} -p %{buildroot}/opt/amdgpu/lib/x86_64-linux-gnu/
%{__mkdir} -p %{buildroot}/opt/amdgpu/share/libdrm/
%{__install} -m 0644 etc/ld.so.conf.d/amdgpu-pro.conf %{buildroot}/etc/ld.so.conf.d/
%{__install} -m 0644 etc/OpenCL/vendors/* %{buildroot}/%{_sysconfdir}/OpenCL/vendors/
%{__install} -m 0644 opt/amdgpu/lib/x86_64-linux-gnu/libdrm_amdgpu.so.1.0.0 %{buildroot}/opt/amdgpu/lib/x86_64-linux-gnu/
%{__install} -m 0644 opt/amdgpu/share/libdrm/amdgpu.ids %{buildroot}/opt/amdgpu/share/libdrm/
%{__install} -m 0644 opt/amdgpu-pro/lib/x86_64-linux-gnu/* %{buildroot}/opt/amdgpu/lib/x86_64-linux-gnu/

%post
ln -sf /opt/amdgpu/lib/x86_64-linux-gnu/libdrm_amdgpu.so.1.0.0 /opt/amdgpu/lib/x86_64-linux-gnu/libdrm_amdgpu.so.1
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
#defattr(-,root,root)
%{_sysconfdir}/ld.so.conf.d/amdgpu-pro.conf
%{_sysconfdir}/OpenCL/vendors/*
%dir /opt/amdgpu/lib/x86_64-linux-gnu
/opt/amdgpu/lib/x86_64-linux-gnu/*
%dir /opt/amdgpu/share/libdrm/
/opt/amdgpu/share/libdrm/amdgpu.ids

%changelog
* Thu Jun 13 2019 - J. corwin Coburn <corwin@redhat.com> - 6.2.1.102-1
HASH(0x222cad8) 