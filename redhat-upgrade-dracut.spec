%global dracutmoddir %{_prefix}/lib/dracut/modules.d
%global plymouthver 0.8.6

Name:       redhat-upgrade-dracut
Version:    0.8.0
Release:    1%{?dist}
Summary:    The Red Hat Enterprise Linux Upgrade tool initramfs environment

License:    GPLv2+
URL:        https://github.com/dashea/redhat-upgrade-dracut
Source0:    https://github.com/downloads/dashea/redhat-upgrade-dracut/%{name}-%{version}.tar.xz

Summary:        initramfs environment for system upgrades
BuildRequires:  rpm-devel >= 4.10.0
BuildRequires:  plymouth-devel >= %{plymouthver}
BuildRequires:  glib2-devel
Requires:       rpm >= 4.10.0
Requires:       plymouth >= %{plymouthver}
Requires:       systemd >= 195-8
Requires:       dracut >= 025

%package plymouth
BuildRequires:  plymouth-devel
BuildArch:      noarch
Requires:       plymouth-plugin-two-step >= %{plymouthver}
Summary:        plymouth theme for system upgrade progress

%description
These dracut modules provide the framework for upgrades and the tool that
actually runs the upgrade itself.

%description plymouth
The plymouth theme used during system upgrade.


%prep
%setup -q


%build
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT \
             LIBEXECDIR=%{_libexecdir} \
             DRACUTMODDIR=%{dracutmoddir}

%files
%doc README.asciidoc TODO.asciidoc COPYING make-redhat-upgrade-repo
%{_libexecdir}/system-upgrade-redhat
%{dracutmoddir}/85system-upgrade-redhat
%{dracutmoddir}/90system-upgrade

%files plymouth
%{_datadir}/plymouth/themes/redhat-upgrade-tool


%changelog
* Fri Nov  8 2013 David Shea <dshea@redhat.com> - 0.8.0-1
- Rename to redhat-upgrade-dracut
  Resolves: rhbz#1027492

* Wed Oct 23 2013 David Shea <dshea@redhat.com> - 0.8.0-0
- Initial rhelup-dracut package for RHEL 7.0
  Resolves: rhbz#1012667
