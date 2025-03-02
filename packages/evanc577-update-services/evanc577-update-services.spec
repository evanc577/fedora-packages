Name:           evanc577-update-services
Version:        1.0.0
Release:        1%{?dist}
Summary:        Patched automatic updates for rpm-ostree and flatpak

License:
URL:            https://github.com/evanc577/fedora-packages
Source0:

Requires:       {{{ git_dir_pack }}}

%description


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%check


%files
%license
%doc


%changelog
%autochangelog

