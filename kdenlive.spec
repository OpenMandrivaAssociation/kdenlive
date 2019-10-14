%define _disable_lto 1

Summary:	A non-linear video editing application for KDE
Name:		kdenlive
Version:	19.08.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kdenlive.org/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/kdenlive-%{version}.tar.xz
Patch0:		kdenlive-19.04.1-menuentry.patch
Patch1:		kdenlive-19.08.2-qt-5.14.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5Plotting)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5FileMetaData)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Purpose)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5WebKit)
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(mlt-framework) >= 6.10.0
BuildRequires:	pkgconfig(shared-mime-info)
Requires:	ladspa
Requires:	mlt >= 6.10.0
Requires:	ffmpeg
Requires:	dvgrab
Requires:	dvdauthor
Requires:	frei0r-plugins

%description
Kdenlive is a non-linear video editor for KDE. It relies on a separate
renderer, piave, to handle it's rendering. Kdenlive supports multitrack
editing.

%files -f %{name}.lang
%{_sysconfdir}/xdg/kdenlive_*.knsrc
%{_datadir}/qlogging-categories5/kdenlive.categories
%{_bindir}/%{name}*
%{_libdir}/qt5/plugins/mltpreview.so
%{_datadir}/metainfo/org.kde.kdenlive.appdata.xml
%{_datadir}/applications/org.kde.kdenlive.desktop
%{_datadir}/config.kcfg/kdenlivesettings.kcfg
%{_iconsdir}/hicolor/*/*/*.*[gz]
%{_datadir}/kdenlive
%{_datadir}/knotifications5/kdenlive.notifyrc
%{_datadir}/kservices5/mltpreview.desktop
%{_datadir}/kxmlgui5/kdenlive/kdenliveui.rc
%{_datadir}/mime/packages/*.xml
%{_mandir}/man1/%{name}*.1.*
%doc %{_docdir}/Kdenlive

#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# We don't use Debian menus
rm -f %{buildroot}%{_kde5_datadir}/menu/kdenlive

%find_lang %{name} --with-html
