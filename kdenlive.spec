Name: 		kdenlive
Version: 	0.4
Release: 	%mkrel 3
License: 	GPL
Summary: 	A non-linear video editing application for KDE
Group:		Graphical desktop/KDE
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	%name-%version.tar.bz2
BuildRequires:	kdelibs-devel
BuildRequires:	mlt-devel
BuildRequires:	mlt++-devel
BuildRequires:	libavc-devel
BuildRequires:	libiec61883-devel
Requires:	mlt >= 0.2.2
Requires:	kdebase-progs >= 3.0.0
URL:		http://kdenlive.sourceforge.net/

%description
Kdenlive is a non-linear video editor for KDE. It relies on a separate
renderer, piave, to handle it's rendering. Kdenlive supports multitrack
editing.

%prep
%setup -q

%build
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
rm -rf $RPM_BUILD_ROOT
%makeinstall

perl -pi -e 's|^Icon=.*|Icon=%{name}|' %buildroot/%_datadir/applications/kde/kdenlive.desktop

%find_lang %name

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig
%update_menus
%{update_desktop_database}
%update_icon_cache hicolor

%postun
/sbin/ldconfig
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
%_menudir/%{name}
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/actions/%{name}_*
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/piave.png
%_datadir/mimelnk/application/vnd.kde.kdenlive.desktop
%_datadir/mimelnk/application/vnd.kde.kdenlive.scenelist.desktop
