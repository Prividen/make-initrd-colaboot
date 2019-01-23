%add_findreq_skiplist /usr/share/make-initrd/features/*

Name: make-initrd-colaboot
Version: 0.9
Release: alt1

Summary: CoLaBoot feature for make-initrd
License: GPL
Group: System/Base
Packager: Michael A. Kangin <prividen@altlinux.org>

Url: https://www.altlinux.org/Colaboot
Source0: %name-%version.tar

Requires: make-initrd >= 0.7.6-alt1
Requires: dhcpcd curl

BuildArch: noarch

%description
Make-initrd CoLaBoot (Compressed Layers Boot) feature allow to boot host
with a separate compressed (squashfs) layers, mounted as overlayfs.
Layers can be aquired from network (HTTP/...) or local filesystem (ISO/HDD).

%prep
%setup

%install
mkdir -p %buildroot%_datadir/make-initrd/features/
mkdir -p %buildroot%_sysconfdir/initrd.mk.d/
cp -a colaboot %buildroot%_datadir/make-initrd/features/
cp colaboot.mk.example %buildroot%_sysconfdir/initrd.mk.d/

%files 
%_datadir/make-initrd/features/colaboot
%config %_sysconfdir/initrd.mk.d/colaboot.mk.example
%doc docs/*

%changelog
* Wed Jan 23 2019 Michael A. Kangin <prividen@altlinux.org> 0.9-alt1
- device names for local filesystems can be specified in LABEL/UUID notation;
- permanent RW layers (file container or filesystem on separate device);
- static IP configuration;
- if overlay module unavailable, falling back to copy layers' content to tmpfs;

* Tue Mar 20 2018 Michael A. Kangin <prividen@altlinux.org> 0.5-alt2
- Homepage URL

* Tue Mar 13 2018 Michael A. Kangin <prividen@altlinux.org> 0.5-alt1
- Initial build

