Name: 		kdenlive
Version: 	0.8.2
Release: 	%mkrel 1
License: 	GPLv2+
Summary: 	A non-linear video editing application for KDE
Group:		Graphical desktop/KDE
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.kdenlive.org/
Source: 	http://downloads.sourceforge.net/kdenlive/%name-%version.tar.gz
Patch0:		kdenlive-0.8-fix-glu.patch
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
%defattr(-, root, root)
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
%patch0 -p1 -b .gl

%build
%cmake_kde4
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build

%__rm -f %{buildroot}%{_datadir}/menu/kdenlive %{buildroot}%{_datadir}/pixmaps/kdenlive.xpm

%find_lang %name --with-html

%clean
%__rm -rf %{buildroot}

