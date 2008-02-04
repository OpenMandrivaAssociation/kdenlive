%define	snapshot	20080130

Name: 		kdenlive
Version: 	0.6
Release: 	%mkrel 0.%{snapshot}.2
License: 	GPL
Summary: 	A non-linear video editing application for KDE
Group:		Graphical desktop/KDE
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	%{name}-%{version}-%{snapshot}.tar.bz2
Patch0:		%{name}-desktop-icon-fix.patch
Patch1:		%{name}-desktop-path-fix.patch
BuildRequires:	cmake
BuildRequires:	kdelibs-devel
BuildRequires:	mlt-devel >= 0.2.5
BuildRequires:	mlt++-devel >= 0.2.2-9
BuildRequires:	libavc-devel
BuildRequires:	libiec61883-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	desktop-file-utils
Requires:	mlt >= 0.2.5
Requires:	kdebase-progs >= 3.0.0
Requires:	ffmpeg
Requires:	dvgrab
Suggests:	swh-plugins
URL:		http://kdenlive.sourceforge.net/

%description
Kdenlive is a non-linear video editor for KDE. It relies on a separate
renderer, piave, to handle it's rendering. Kdenlive supports multitrack
editing.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .icon
%patch1 -p1 -b .path

%build
cmake . -DCMAKE_CXX_FLAGS="%{optflags}" \
	-DCMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix}
make

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
%_bindir/*
%_datadir/apps/%{name}
%_datadir/config.kcfg
%_datadir/applications/kde/%{name}.desktop
%_datadir/icons/hicolor/*/*/*
%_datadir/mimelnk/application/vnd.kde.kdenlive.desktop
%_datadir/mimelnk/application/vnd.kde.kdenlive.scenelist.desktop

