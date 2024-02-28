#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	A non-linear video editing application for KDE
Name:		plasma6-kdenlive
Version:	24.02.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kdenlive.org/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/multimedia/kdenlive/-/archive/%{gitbranch}/kdenlive-%{gitbranchd}.tar.bz2#/kdenlive-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdenlive-%{version}.tar.xz
%endif
Patch0:		kdenlive-19.04.1-menuentry.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6Plotting)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6FileMetaData)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Purpose)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6UiPlugin)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6NetworkAuth)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:  qt6-qtmultimedia-gstreamer
BuildRequires:  qml(QtNetwork)
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
BuildRequires:	cmake(Qt6ToolsTools)
Requires:	ladspa
Requires:	mlt >= 7.0.0
Requires:	mlt-qt6 >= 7.0.0
Requires:	ffmpeg
Requires:	dvgrab
Requires:	dvdauthor
Requires:	frei0r-plugins
Recommends:	mediainfo

%description
Kdenlive is a non-linear video editor for KDE. It relies on a separate
renderer, piave, to handle it's rendering. Kdenlive supports multitrack
editing.

%files -f kdenlive.lang
%{_datadir}/knsrcfiles/*
%{_datadir}/qlogging-categories6/kdenlive.categories
%{_bindir}/kdenlive*
%{_libdir}/qt6/plugins/kf6/thumbcreator/mltpreview.so
%{_datadir}/metainfo/org.kde.kdenlive.appdata.xml
%{_datadir}/applications/org.kde.kdenlive.desktop
%{_datadir}/config.kcfg/kdenlivesettings.kcfg
%{_iconsdir}/hicolor/*/*/*.*[gz]
%{_datadir}/kdenlive
%{_datadir}/knotifications6/kdenlive.notifyrc
%{_datadir}/mime/packages/*.xml
%{_mandir}/man1/kdenlive*.1.*
%doc %{_docdir}/Kdenlive

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n kdenlive-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
# Limit to 4 CPUs because of memory constraints -- build consistently fails on
# altra (160 CPUs, 32 GB RAM...)
%ninja -j8 -C build

%install
%ninja_install -C build

# We don't use Debian menus
rm -f %{buildroot}%{_datadir}/menu/kdenlive

%find_lang kdenlive --with-html
