Summary:	A non-linear video editing application for KDE
Name:		kdenlive
Version:	15.04.2
Release:	1
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
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*.so
%{_kde_datadir}/apps/%{name}
%{_kde_services}/*.desktop
%{_kde_datadir}/config.kcfg/*
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_datadir}/mime/packages/*.xml
%{_kde_configdir}/*
%{_mandir}/man1/*

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


