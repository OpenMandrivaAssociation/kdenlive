Name: 		kdenlive
Version: 	0.7.5
Release: 	%mkrel 1
License: 	GPLv2+
Summary: 	A non-linear video editing application for KDE
Group:		Graphical desktop/KDE
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	http://downloads.sourceforge.net/kdenlive/%name-%version.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	mlt-devel >= 0.4.0
Requires:	mlt >= 0.4.0
Requires:	ffmpeg
Requires:	dvgrab
Suggests:	swh-plugins
URL:		http://kdenlive.sourceforge.net/

%description
Kdenlive is a non-linear video editor for KDE. It relies on a separate
renderer, piave, to handle it's rendering. Kdenlive supports multitrack
editing.

%if %mdkversion < 200900
%post
%update_menus
%{update_desktop_database}
%update_icon_cache hicolor
%update_mime_database
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%{clean_desktop_database}
%clean_icon_cache hicolor
%clean_mime_database
%endif

%files -f %name.lang
%defattr(-, root, root)
%_kde_bindir/*
%_kde_libdir/kde4/*.so
%_kde_datadir/apps/%{name}
%_kde_services/*.desktop
%_kde_datadir/config.kcfg/*
%_kde_datadir/applications/kde4/%{name}.desktop
%_kde_iconsdir/*/*/*/*
%_kde_datadir/mime/packages/*.xml
%_kde_configdir/*.knsrc
%_kde_configdir/kdenlivetranscodingrc
%_mandir/man1/*
# Debian menu file
%exclude %{_datadir}/menu/kdenlive
%exclude %{_datadir}/pixmaps/kdenlive.xpm


#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%find_lang %name

%clean
rm -rf %{buildroot}
