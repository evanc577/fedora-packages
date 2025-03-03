%global gh_user mierak
%global gh_repo rmpc
%global common_description A configurable, terminal based Media Player Client with album art support via various terminal image protocols
%global pkgname rmpc-%{version}
%define debug_package %{nil}

Name:           rmpc
# renovate: datasource=github-releases depName=mierak/rmpc versioning=semver-coerced
Version:        0.8.0
Release:        2%{?dist}
Summary:        %{common_description}
License:        BSD-3-Clause
URL:            https://mierak.github.io/rmpc/
Source0:        https://github.com/%{gh_user}/%{gh_repo}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo
Requires:       mpd

%description
%{common_description}

%prep
%setup -q -n %{pkgname}

%build
cargo b --release

%install
install -Dm 755 %{_builddir}/%{pkgname}/target/release/%{name} -t %{buildroot}%{_bindir}

%files
%license LICENSE
%{_bindir}/rmpc

%changelog
* Sun Mar 02 2025 Evan Chang <evanc577@gmail.com> - 0.8.0
- Version 0.8.0
