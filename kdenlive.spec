Summary:	A non-linear video editing application for KDE
Name:		kdenlive
Version:	15.04.3
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kdenlive.org/
Source0:	http://download.kde.org/stable/applications/%{version}/src/kdenlive-%{version}.tar.xz
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
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(mlt-framework) >= 0.9.6
BuildRequires:	pkgconfig(shared-mime-info)
Requires:	mlt >= 0.9.6
Requires:	ffmpeg
Requires:	dvgrab


%description
Kdenlive is a non-linear video editor for KDE. It relies on a separate
renderer, piave, to handle it's rendering. Kdenlive supports multitrack
editing.

%files -f %{name}.lang
%{_sysconfdir}/xdg/kdenlive_*.knsrc
%{_bindir}/%{name}*
%{_libdir}/qt5/plugins/mltpreview.so
%{_datadir}/appdata/kdenlive.appdata.xml
%{_datadir}/applications/org.kde.kdenlive.desktop
%{_datadir}/config.kcfg/kdenlivesettings.kcfg
%{_iconsdir}/hicolor/*/*/*.*[gz]
%{_datadir}/kdenlive
%{_datadir}/knotifications5/kdenlive.notifyrc
%{_datadir}/kservices5/mltpreview.desktop
%{_datadir}/kxmlgui5/kdenlive/kdenliveui.rc
%{_datadir}/mime/packages/*.xml
%{_datadir}/pixmaps/kdenlive.xpm
%{_mandir}/man1/%{name}*.1.*

#--------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# We don't use Debian menus
rm -f %{buildroot}%{_kde5_datadir}/menu/kdenlive

%find_lang %{name} --with-html


