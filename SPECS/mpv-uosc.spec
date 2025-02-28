%global gh_user tomasklaen
%global gh_repo uosc
%global common_description Feature-rich minimalist proximity-based UI for MPV player.
%global pkgname uosc-%{version}
%global _missing_build_ids_terminate_build 0
%define debug_package %{nil}

Name:           mpv-uosc
# renovate: datasource=github-releases depName=tomasklaen/uosc
Version:        5.8.0
Release:        2
Summary:        %{common_description}
License:        LGPL-2.1-only
URL:            https://github.com/%{gh_user}/%{gh_repo}
Source0:        https://github.com/%{gh_user}/%{gh_repo}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  golang git-core

%description
%{common_description}

%prep
%setup -n %{pkgname}

%build
tools/build ziggy

%install
install -Dm 644 %{_builddir}/%{pkgname}/src/fonts/* -t %{buildroot}%{_sysconfdir}/mpv/fonts/
install -Dm 644 %{_builddir}/%{pkgname}/src/uosc.conf -t %{buildroot}%{_sysconfdir}/mpv/script-opts/
install -Dm 755 %{_builddir}/%{pkgname}/src/uosc/bin/ziggy-linux -t %{buildroot}%{_sysconfdir}/mpv/scripts/uosc/bin
for dir in {char-conv,elements,intl,lib}; do
    install -Dm 644 %{_builddir}/%{pkgname}/src/uosc/${dir}/** -t %{buildroot}%{_sysconfdir}/mpv/scripts/uosc/${dir}/
done
install -Dm 644 %{_builddir}/%{pkgname}/src/uosc/main.lua -t %{buildroot}%{_sysconfdir}/mpv/scripts/uosc/

%files
%license LICENSE.LGPL
%{_sysconfdir}/mpv/

%changelog
* Thu Feb 27 2025 Evan Chang <evanc577@gmail.com> - 5.8.0
- Version 5.8.0
