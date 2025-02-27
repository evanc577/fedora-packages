%global gh_user tomasklaen
%global gh_repo uosc
%global common_description Feature-rich minimalist proximity-based UI for MPV player.

Name:           mpv-uosc
Version:        5.8.0
Release:        1%{?dist}
Summary:        %{common_description}
License:        LGPL
URL:            https://github.com/%{gh_user}/%{gh_repo}
Source0:        https://github.com/%{gh_user}/%{gh_repo}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  golang git-core

%description
%{common_description}

%prep
%autosetup -n %{name}-%{version}

%build
tools/build ziggy

%install
install -Dm 644 "%{_builddir}/src/fonts/*" -t "%{_sysconfdir}/mpv/fonts/"
install -Dm 644 "%{_builddir}/src/uosc.conf" -t "%{_sysconfdir}/mpv/script-opts/"
install -Dm 755 "%{_builddir}/src/uosc/bin/ziggy-linux" -t "%{_sysconfdir}/mpv/scripts/uosc/bin"
for dir in {char-conv,elements,intl,lib}; do
    install -Dm 644 "%{_builddir}/src/uosc/${dir}/*"* -t "%{_sysconfdir}/mpv/scripts/uosc/${dir}/"
done
install -Dm 644 "%{_builddir}/src/uosc/main.lua" -t "%{_sysconfdir}/mpv/scripts/uosc/"
install -Dm 644 "LICENSE"* -t "%{_prefix}/share/licenses/%{name}/"

%files
%{_sysconfdir}/mpv/
%{_prefix}/share/licenses/%{name}/

%changelog
