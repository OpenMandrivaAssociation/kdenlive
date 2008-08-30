%define svnrel 2387

Name: 		kdenlive
Version: 	0.7
Release: 	%mkrel 0.%{svnrel}.1
License: 	GPLv2+
Summary: 	A non-linear video editing application for KDE
Group:		Graphical desktop/KDE
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	%{name}-kde4-r%{svnrel}.tar.bz2
Patch0:		%{name}-0.7-desktop-icon-fix.patch
Patch1:		%{name}-0.7-desktop-path-fix.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	mlt-devel >= 0.3.0
BuildRequires:	mlt++-devel >= 0.3.0
Requires:	mlt >= 0.3.0
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
%_kde_datadir/apps/%{name}
%_kde_datadir/config.kcfg/*
%_kde_datadir/applications/kde4/%{name}.desktop
%_kde_iconsdir/*/*/*/*
%_kde_datadir/mime/packages/kdenlive.xml


#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-kde4
%patch0 -p0
%patch1 -p0

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%find_lang %name

%clean
rm -rf %{buildroot}
