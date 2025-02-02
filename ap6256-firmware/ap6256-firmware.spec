# Maintainer: Dan Johansen <strit@manjaro.org>

%define name ap6256-firmware
%define version 2020.02
%define sourcerelease 10
%define release %{sourcerelease}%{?dist}

Summary: ap6256-firmware
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL2
URL: https://gitlab.manjaro.org/manjaro-arm/packages/community/ap6256-firmware.git
ExclusiveArch: aarch64
BuildRequires: git-core

%global debug_package %{nil}

%description
Firmware files for the ap6256 wifi/bt module

%prep
git clone https://gitlab.manjaro.org/manjaro-arm/packages/community/%{name}.git
cd %{name}
git checkout 056d5f6776e515f90bbbbead1be06857aaef17d0
%setup -c -T

%build

%install
mkdir %{buildroot}/usr/lib/firmware/brcm -p
# Bluetooth firmware
install -Dm644 ${RPM_BUILD_DIR}/%{name}/BCM4345C5.hcd -t %{buildroot}/usr/lib/firmware/brcm/

%files
/usr/lib/firmware/

%post

%preun

%changelog
* Sat Aug 06 2022 Bengt Fredh <bengt@fredhs.net> - 2020.02-10
- Clean up
* Sat Aug 06 2022 Bengt Fredh <bengt@fredhs.net> - 2020.02-6
- Clean up
* Mon Oct 12 2020 Bengt Fredh <bengt@fredhs.net> - 2020.02-5
- First version
