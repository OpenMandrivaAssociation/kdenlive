Name: 		kdenlive
Version: 	0.7
Release: 	%mkrel 1
License: 	GPLv2+
Summary: 	A non-linear video editing application for KDE
Group:		Graphical desktop/KDE
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	http://downloads.sourceforge.net/kdenlive/%name-%version.tar.bz2
Patch0:		%{name}-0.7-desktop-icon-fix.patch
Patch1:		%{name}-0.7-desktop-path-fix.patch
Patch2:		kdenlive-kde4-fix-underlink.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	mlt-devel >= 0.3.1
BuildRequires:	mlt++-devel >= 0.3.1
Requires:	mlt >= 0.3.1
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

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%find_lang %name

%clean
rm -rf %{buildroot}
