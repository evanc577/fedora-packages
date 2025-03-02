%global common_description Patched automatic updates for rpm-ostree and flatpak

Name:           evanc577-update-services
Version:        1.0.0
Release:        1%{?dist}
Summary:        %{common_description}
License:        MIT
URL:            https://github.com/evanc577/fedora-packages
Source0:        {{{ git_dir_pack }}}
BuildRequires:  systemd-rpm-macros
Supplements:    ublue-os-update-services
BuildArch:      noarch

%description
%{common_description}


%prep
{{{ git_dir_setup_macro }}}


%install
install -Dm 644 src/%{_unitdir}/rpm-ostreed-automatic.service.d/z-override.conf -t %{buildroot}%{_unitdir}/rpm-ostreed-automatic.service.d/
install -Dm 644 src/%{_unitdir}/rpm-ostreed-automatic.timer.d/z-override.conf -t %{buildroot}%{_unitdir}/rpm-ostreed-automatic.timer.d/
install -Dm 644 src/%{_userunitdir}/flatpak-user-update.service.d/z-override.conf -t %{buildroot}%{_userunitdir}/flatpak-user-update.service.d/
install -Dm 755 src/%{_bindir}/wait-for-network -t %{_bindir}/


%files
%{buildroot}%{_unitdir}/rpm-ostreed-automatic.service.d/z-override.conf
%{buildroot}%{_unitdir}/rpm-ostreed-automatic.timer.d/z-override.conf
%{buildroot}%{_userunitdir}/flatpak-user-update.service.d/z-override.conf
%{_bindir}/wait-for-network


%changelog
* Sat Mar 01 2025 Evan Chang <evanc577@gmail.com> - 1.0.0
- Initial version
