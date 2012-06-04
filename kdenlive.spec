Name: 		kdenlive
Version: 	0.9.2
Release: 	1
License: 	GPLv2+
Summary: 	A non-linear video editing application for KDE
Group:		Graphical desktop/KDE
URL:		http://www.kdenlive.org/
Source0: 	http://download.kde.org/stable/kdenlive/%{version}/src/kdenlive-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	qjson-devel
BuildRequires:	qimageblitz-devel
BuildRequires:	mlt-devel >= 0.7.6
Requires:	mlt >= 0.7.6
Requires:	ffmpeg
Requires:	dvgrab
Suggests:	swh-plugins
Suggests:	recordmydesktop
Suggests:	cdrkit-genisoimage
Suggests:	dvdauthor
Suggests:	oxygen-icon-theme
Suggests:	frei0r

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

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%__rm -f %{buildroot}%{_datadir}/menu/kdenlive 
%__rm -f %{buildroot}%{_datadir}/pixmaps/kdenlive.xpm

%find_lang %name --with-html

