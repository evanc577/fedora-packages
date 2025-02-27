%global gh_user po5
%global gh_repo thumbfast
%global common_description High-performance on-the-fly thumbnailer script for mpv
%global pkgname %{gh_repo}-%{digest}
%define debug_package %{nil}

# renovate: datasource=git-refs packageName=https://github.com/po5/thumbfast depName=thumbfast ref=master
%define digest 9deb0733c4e36938cf90e42ddfb7a19a8b2f4641

Name:           mpv-thumbfast
Version:        0.0.1
Release:        %autorelease
Summary:        %{common_description}
License:        LGPL
URL:            https://github.com/%{gh_user}/%{gh_repo}
Source0:        https://github.com/%{gh_user}/%{gh_repo}/archive/%{digest}.zip

%description
%{common_description}

%prep
echo %{pkgname}
%setup -n %{pkgname}

%install
install -Dm 644 %{_builddir}/%{pkgname}/thumbfast.conf -t %{buildroot}%{_sysconfdir}/mpv/script-opts/
install -Dm 644 %{_builddir}/%{pkgname}/thumbfast.lua -t %{buildroot}%{_sysconfdir}/mpv/scripts/
install -Dm 644 %{_builddir}/%{pkgname}/LICENSE* -t %{buildroot}%{_prefix}/share/licenses/%{name}/

%files
%{_sysconfdir}/mpv/
%{_prefix}/share/licenses/%{name}/

%changelog
* Thu Feb 27 2025 Evan Chang <evanc577@gmail.com> - 0.0.1
- Initial version
