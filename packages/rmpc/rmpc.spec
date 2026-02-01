%global gh_user mierak
%global gh_repo rmpc
%global common_description A configurable, terminal based Media Player Client with album art support via various terminal image protocols
%global pkgname rmpc-%{version}
%define debug_package %{nil}

Name:           rmpc
# renovate: datasource=github-releases depName=mierak/rmpc versioning=semver-coerced
Version:        0.11.0
Release:        1%{?dist}
Summary:        %{common_description}
License:        BSD-3-Clause
URL:            https://mierak.github.io/rmpc/
Source0:        https://github.com/%{gh_user}/%{gh_repo}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo
Requires:       mpd
Recommends:     cava

%description
%{common_description}

%prep
%setup -q -n %{pkgname}

%build
cargo b --release

%install
install -Dm 755 %{_builddir}/%{pkgname}/target/release/%{name} -t %{buildroot}%{_bindir}
install -Dm 644 %{_builddir}/%{pkgname}/target/man/rmpc.1 -t %{buildroot}/%{_mandir}/man1/
install -Dm 644 %{_builddir}/%{pkgname}/target/completions/rmpc.bash -t %{buildroot}/%{bash_completions_dir}
install -Dm 644 %{_builddir}/%{pkgname}/target/completions/rmpc.fish -t %{buildroot}/%{fish_completions_dir}
install -Dm 644 %{_builddir}/%{pkgname}/target/completions/_rmpc -t %{buildroot}/%{zsh_completions_dir}

%files
%license LICENSE
%{_bindir}/rmpc
%{_mandir}/man1/rmpc.1*
%{bash_completions_dir}/rmpc.bash
%{fish_completions_dir}/rmpc.fish
%{zsh_completions_dir}/_rmpc

%changelog
* Thu Mar 06 2025 Evan Chang <evanc577@gmail.com> - 0.8.0-3
- Install manpage and completions

* Sun Mar 02 2025 Evan Chang <evanc577@gmail.com> - 0.8.0
- Version 0.8.0
