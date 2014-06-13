Summary:	A non-linear video editing application for KDE
Name:		kdenlive
Version:	0.9.6
Release:	9
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kdenlive.org/
Source0:	http://download.kde.org/stable/kdenlive/%{version}/src/kdenlive-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(mlt-framework) >= 0.8.8
BuildRequires:	pkgconfig(qimageblitz)
BuildRequires:	pkgconfig(QJson)
Requires:	mlt >= 0.8.8
Requires:	ffmpeg
Requires:	dvgrab
Suggests:	xine-ui
Suggests:	swh-plugins
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

rm -f %{buildroot}%{_datadir}/menu/kdenlive
rm -f %{buildroot}%{_datadir}/pixmaps/kdenlive.xpm

%find_lang %{name} --with-html


