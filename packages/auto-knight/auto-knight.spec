%global common_description Automatic dark mode switcher for KDE Plasma 

Name:           auto-knight
Version:        1.0.1
Release:        1%{?dist}
Summary:        %{common_description}
License:        MIT
Source0:        {{{ git_dir_pack }}}
BuildRequires:  systemd-rpm-macros
Requires:       plasma-workspace dbus-tools qt6-qttools
BuildArch:      noarch

%description
%{common_description}


%prep
{{{ git_dir_setup_macro }}}


%install
install -Dm 755 src/%{_bindir}/auto-knight -t %{buildroot}%{_bindir}/
install -Dm 644 src/%{_userunitdir}/auto-knight.service -t %{buildroot}%{_userunitdir}/


%files
%license src/LICENSE
%{_bindir}/auto-knight
%{_userunitdir}/auto-knight.service


%changelog
* Thu Apr 03 2025 Evan Chang <evanc577@gmail.com> - 1.0.1
- Adjust systemd service file
* Mon Mar 17 2025 Evan Chang <evanc577@gmail.com> - 1.0.0
- Initial version
