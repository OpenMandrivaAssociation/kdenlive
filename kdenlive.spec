%define	snapshot	20071031

Name: 		kdenlive
Version: 	0.6
Release: 	0.%{snapshot}.%mkrel 1
License: 	GPL
Summary: 	A non-linear video editing application for KDE
Group:		Graphical desktop/KDE
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	%{name}-%{version}-%{snapshot}.tar.bz2
Patch0:		%{name}-desktop-icon-fix.patch
BuildRequires:	kdelibs-devel
BuildRequires:	mlt-devel >= 0.2.4
BuildRequires:	mlt++-devel
BuildRequires:	libavc-devel
BuildRequires:	libiec61883-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	desktop-file-utils
Requires:	mlt >= 0.2.4
Requires:	kdebase-progs >= 3.0.0
Requires:	ffmpeg
Requires:	dvgrab
URL:		http://kdenlive.sourceforge.net/

%description
Kdenlive is a non-linear video editor for KDE. It relies on a separate
renderer, piave, to handle it's rendering. Kdenlive supports multitrack
editing.

%prep
%setup -q -n %{name}

%build
%if %{mdkversion} <= 200710 || "%{mdvver}" == "mlcd4"
%define __libtoolize    /bin/true
%endif

make -f admin/Makefile.common cvs

%ifarch %ix86
export CXXFLAGS="%optflags -fno-omit-frame-pointer"
%endif
%configure2_5x \
		--enable-shared \
		--disable-static \
		--disable-embedded \
		--disable-palmtop \
		--disable-rpath \
		--with-gnu-ld \
		--with-pic \
		--with-xinerama

%make

%install
rm -rf %buildroot
%makeinstall

desktop-file-install --vendor='' \
	--dir %buildroot%_datadir/applications/kde \
	--add-category='Video;AudioVideoEditing' \
	%buildroot%_datadir/applications/kde/*.desktop

%find_lang %name

%clean
rm -rf %{buildroot}

%post
%update_menus
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%clean_menus
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -f %name.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README TODO
%doc %{_docdir}/HTML
%_bindir/*
%_datadir/apps/%{name}
%_datadir/config.kcfg
%_datadir/applications/kde/%{name}.desktop
%_datadir/icons/hicolor/*/*/*
%_datadir/mimelnk/application/vnd.kde.kdenlive.desktop
%_datadir/mimelnk/application/vnd.kde.kdenlive.scenelist.desktop
%_libdir/kde3/kfile_westley.la
%_libdir/kde3/kfile_westley.so
%_libdir/kde3/westleythumbcreator.la
%_libdir/kde3/westleythumbcreator.so
%_datadir/services/kfile_westley.desktop
%_datadir/services/westleythumbcreator.desktop

