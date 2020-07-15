Name:                gnome-software
Version:             3.30.6
Release:             6
Summary:             GNOME software Store
License:             GPLv2+
URL:                 https://wiki.gnome.org/Apps/Software
Source0:             https://download.gnome.org/sources/gnome-software/3.30/gnome-software-%{version}.tar.xz
Patch0001:           gnome-software-3-30-error-message-fixes.patch
Patch0002:           0001-packagekit-Fix-progress-marshalling-for-upgrade_down.patch
BuildRequires:       gettext libxslt docbook-style-xsl desktop-file-utils
BuildRequires:       fwupd-devel >= 1.0.7 glib2-devel >= 2.56.0 gnome-desktop3-devel
BuildRequires:       gsettings-desktop-schemas-devel >= 3.12.0
BuildRequires:       gspell-devel gtk3-devel >= 3.22.4 gtk-doc json-glib-devel >= 1.2.0
BuildRequires:       libappstream-glib-devel >= 0.7.14-3 libsoup-devel meson
BuildRequires:       PackageKit-glib-devel >= 1.1.1 polkit-devel libsecret-devel
BuildRequires:       flatpak-devel >= 0.9.4 ostree-devel rpm-ostree-devel
BuildRequires:       libgudev1-devel valgrind-devel liboauth-devel snapd-glib-devel >= 1.42
Requires:            appstream-data epiphany-runtime
Requires:            flatpak >= 0.9.4 flatpak-libs >= 0.9.4 fwupd >= 1.0.7 glib2 >= 2.56.0
Requires:            gnome-desktop3 >= 3.18.0 gnome-menus gsettings-desktop-schemas >= 3.12.0
Requires:            gtk3 >= 3.22.4 json-glib >= 1.2.0 iso-codes libappstream-glib >= 0.7.14-3
Requires:            librsvg2 libsoup >= 2.52.0 PackageKit >= 1.1.1 snapd-login-service
Provides:            gnome-software-snap = %{version}-%{release}
Obsoletes:           gnome-software-snap < %{version}-%{release}

%description
AppStore like management of Application fir your GNOME Desktop.

%package             devel
Summary:             Development files for the GNOME software store
Requires:            gnome-software = %{version}-%{release}
%description devel
This subpackage contains the header files for developing GNOME software store plugins.

%package             help
Summary:             Help documentation for the GNOME software store.
%description help
Help documentation for the GNOME software store.

%package             editor
Summary:             Editor for designing banners for GNOME Software
Requires:            gnome-software = %{version}-%{release}

%description         editor
Editor is used to design banners for GNOME Software.

%prep
%autosetup -n gnome-software-%{version} -p1

%build
%meson -Dsnap=true -Dgudev=true -Dpackagekit=true -Dexternal_appstream=false -Drpm_ostree=true \
       -Dtests=false -Dubuntuone=false -Dubuntu_reviews=false
%meson_build

%install
%meson_install
desktop-file-edit %{buildroot}%{_datadir}/applications/org.gnome.Software.desktop \
    --set-key=X-AppInstall-Package --set-value=gnome-software
install -d %{buildroot}%{_datadir}/gnome-software/backgrounds

%find_lang %name --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f gnome-software.lang
%doc AUTHORS README.md COPYING
%{_bindir}/gnome-software
%{_datadir}/applications/gnome-software-local-file.desktop
%{_datadir}/applications/org.gnome.Software.desktop
%dir %{_datadir}/gnome-software
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/gnome-software/backgrounds/
%{_datadir}/gnome-software/{*.png,featured-*.svg,featured-*.jpg}
%{_datadir}/metainfo/*.xml
%dir %{_libdir}/gs-plugins-12
%{_libdir}/gs-plugins-12/*.so
%{_sysconfdir}/xdg/autostart/gnome-software-service.desktop
%{_datadir}/app-info/xmls/org.gnome.Software.Featured.xml
%{_datadir}/dbus-1/services/org.freedesktop.PackageKit.service
%{_datadir}/dbus-1/services/org.gnome.Software.service
%{_datadir}/gnome-shell/search-providers/org.gnome.Software-search-provider.ini
%{_datadir}/glib-2.0/schemas/org.gnome.software.gschema.xml
%{_libexecdir}/{gnome-software-cmd,gnome-software-restarter}
%{_libdir}/gs-plugins-12/libgs_plugin_snap.so
%{_datadir}/metainfo/org.gnome.Software.Plugin.Snap.metainfo.xml

%files devel
%{_libdir}/pkgconfig/gnome-software.pc
%dir %{_includedir}/gnome-software
%{_includedir}/gnome-software/*.h
%{_datadir}/gtk-doc/html/gnome-software

%files help
%{_mandir}/man1/gnome-software-editor.1*
%{_mandir}/man1/gnome-software.1.gz

%files editor
%{_bindir}/gnome-software-editor
%{_datadir}/applications/org.gnome.Software.Editor.desktop

%changelog
* Fri Apr 24 2020 wangyue<wangyue92@huawei.com> - 3.30.6-6
- package init
