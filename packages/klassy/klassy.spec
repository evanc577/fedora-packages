%global gh_user paulmcauley
%global gh_repo klassy
%global common_description Highly customizable theming for the KDE Plasma desktop
%global pkgname klassy-%{version}

Name:           klassy
# renovate: datasource=github-releases depName=paulmcauley/klassy versioning=semver-coerced
Version:        6.5.3
Release:        1%{?dist}
Summary:        %{common_description}
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/%{gh_user}/%{gh_repo}
Source0:        https://github.com/%{gh_user}/%{gh_repo}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  git-core
BuildRequires:  gettext

BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5FrameworkIntegration)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6FrameworkIntegration)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

Requires:       plasma-desktop

%description
%{common_description}


%prep
%setup -q -n %{pkgname}


%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%cmake_build


%install
%cmake_install


%files
%doc README.md AUTHORS
%license LICENSES/*.txt
%{_bindir}/klassy-settings
%{_datadir}/applications/kcm_klassydecoration.desktop
%{_datadir}/applications/klassy-settings.desktop
%{_datadir}/applications/klassystyleconfig.desktop
%{_datadir}/color-schemes/Klassy*
%{_datadir}/icons/hicolor/scalable/apps/klassy-settings.svgz
%{_datadir}/icons/klassy*
%{_datadir}/kstyle/themes/klassy.themerc
%{_datadir}/plasma/desktoptheme/klassy
%{_datadir}/plasma/layout-templates/org.kde.klassy*
%{_datadir}/plasma/look-and-feel/org.kde.klassy*
%{_libdir}/cmake/Klassy/KlassyConfig.cmake
%{_libdir}/cmake/Klassy/KlassyConfigVersion.cmake
%{_libdir}/libklassycommon5.so*
%{_libdir}/libklassycommon6.so*
%{_libdir}/qt5/plugins/styles/klassy5.so
%{_libdir}/qt6/plugins/kstyle_config/klassystyleconfig.so
%{_libdir}/qt6/plugins/org.kde.kdecoration3.kcm/kcm_klassydecoration.so
%{_libdir}/qt6/plugins/org.kde.kdecoration3.kcm/klassydecoration/presets/*.klpw
%{_libdir}/qt6/plugins/org.kde.kdecoration3/org.kde.klassy.so
%{_libdir}/qt6/plugins/styles/klassy6.so


%changelog
* Fri Oct 31 2025 Evan Chang <evanc577@gmail.com - 6.4.breeze6.4.0
- Version 6.4.breeze6.4.0
