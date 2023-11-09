Summary:	A non-linear video editing application for KDE
Name:		kdenlive
Version:	23.08.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kdenlive.org/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdenlive-%{version}.tar.xz
Patch0:		kdenlive-19.04.1-menuentry.patch
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
BuildRequires:	cmake(Qt5Help)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5WebKit)
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:	cmake(Qt5UiPlugin)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5NetworkAuth)
BuildRequires:	cmake(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(mlt-framework-7)
BuildRequires:	pkgconfig(mlt++-7)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	rttr-devel
BuildRequires:	doxygen >= 1.8.13
BuildRequires:	graphviz
# For qhelpgenerator
BuildRequires:	qt5-assistant
Requires:	ladspa
Requires:	mlt >= 7.0.0
Requires:	ffmpeg
Requires:	dvgrab
Requires:	dvdauthor
Requires:	frei0r-plugins

%description
Kdenlive is a non-linear video editor for KDE. It relies on a separate
renderer, piave, to handle it's rendering. Kdenlive supports multitrack
editing.

%package devel
Summary:	Development files for Kdenlive
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}

%description devel
Development files for Kdenlive

%files -f %{name}.lang
%{_datadir}/knsrcfiles/*
%{_datadir}/qlogging-categories5/kdenlive.categories
%{_bindir}/%{name}*
%{_libdir}/qt5/plugins/kf5/thumbcreator/mltpreview.so
%{_datadir}/metainfo/org.kde.kdenlive.appdata.xml
%{_datadir}/applications/org.kde.kdenlive.desktop
%{_datadir}/config.kcfg/kdenlivesettings.kcfg
%{_iconsdir}/hicolor/*/*/*.*[gz]
%{_datadir}/kdenlive
%{_datadir}/knotifications5/kdenlive.notifyrc
%{_datadir}/mime/packages/*.xml
%{_mandir}/man1/%{name}*.1.*
%doc %{_docdir}/Kdenlive

%files devel
%{_prefix}/lib/cmake/kdenlive/KdenliveQCHTargets.cmake
%{_docdir}/qt5/kdenlive.{qch,tags}

#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
# Limit to 4 CPUs because of memory constraints -- build consistently fails on
# altra (160 CPUs, 32 GB RAM...)
%ninja -j8 -C build

%install
%ninja_install -C build

# We don't use Debian menus
rm -f %{buildroot}%{_kde5_datadir}/menu/kdenlive

%find_lang %{name} --with-html
