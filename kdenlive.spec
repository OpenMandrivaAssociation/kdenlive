Name: 		kdenlive
Version: 	0.9.2
Release: 	2
License: 	GPLv2+
Summary: 	A non-linear video editing application for KDE
Group:		Graphical desktop/KDE
URL:		http://www.kdenlive.org/
Source0: 	http://download.kde.org/stable/kdenlive/%{version}/src/kdenlive-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	qjson-devel
BuildRequires:	qimageblitz-devel
BuildRequires:	mlt-devel >= 0.8.0
Requires:	mlt >= 0.8.0
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

%find_lang %{name} --with-html

%changelog
* Fri Jun 08 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.9.2-2
+ Revision: 803406
- Build for ffmpeg 0.11.x, mlt 0.8.x

* Mon Jun 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.9.2-1
+ Revision: 802323
- version update 0.9.2

* Tue Dec 20 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.8.2.1-1
+ Revision: 743881
- New version 0.8.2.1

* Wed Dec 07 2011 Andrey Bondrov <abondrov@mandriva.org> 0.8.2-1
+ Revision: 738655
- Add patch0 to fix build
- New version 0.8.2, add more Suggests

* Wed Apr 27 2011 Funda Wang <fwang@mandriva.org> 0.8-1
+ Revision: 659718
- add br
- update filelist
- new version 0.8

* Wed Sep 15 2010 Funda Wang <fwang@mandriva.org> 0.7.8-1mdv2011.0
+ Revision: 578654
- new version 0.7.8

* Sun Feb 28 2010 Frederik Himpe <fhimpe@mandriva.org> 0.7.7.1-1mdv2010.1
+ Revision: 512757
- update to new version 0.7.7.1

  + Funda Wang <fwang@mandriva.org>
    - update URL

* Wed Feb 17 2010 Funda Wang <fwang@mandriva.org> 0.7.7-1mdv2010.1
+ Revision: 507050
- New version 0.7.7

* Fri Oct 09 2009 Funda Wang <fwang@mandriva.org> 0.7.6-1mdv2010.0
+ Revision: 456248
- New version 0.7.6

* Sat Jul 04 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.5-1mdv2010.0
+ Revision: 392394
- Update to new version 0.7.5
- Don't package Debian menu file and image

* Mon Jun 01 2009 Funda Wang <fwang@mandriva.org> 0.7.4-1mdv2010.0
+ Revision: 381773
- bump mlt BR
- New version 0.7.4

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 0.7.3-1mdv2010.0
+ Revision: 369522
- New version 0.7.3

* Tue Feb 03 2009 Funda Wang <fwang@mandriva.org> 0.7.2.1-1mdv2009.1
+ Revision: 336743
- 0.7.2.1

* Sun Feb 01 2009 Funda Wang <fwang@mandriva.org> 0.7.2-1mdv2009.1
+ Revision: 336243
- New version 0.7.2

* Wed Dec 31 2008 Funda Wang <fwang@mandriva.org> 0.7.1-1mdv2009.1
+ Revision: 321594
- avcodec is not needed
- New version 0.7.1
- rediff desktop patches

* Thu Nov 13 2008 Funda Wang <fwang@mandriva.org> 0.7-2mdv2009.1
+ Revision: 302604
- bump mlt requirement

* Thu Nov 13 2008 Funda Wang <fwang@mandriva.org> 0.7-1mdv2009.1
+ Revision: 302602
- New version 0.7 final

* Tue Nov 11 2008 Funda Wang <fwang@mandriva.org> 0.7-0.2670.1mdv2009.1
+ Revision: 302095
- new snapshot

* Thu Oct 16 2008 Funda Wang <fwang@mandriva.org> 0.7-0.2471.1mdv2009.1
+ Revision: 294129
- New snapshot

* Tue Sep 23 2008 Funda Wang <fwang@mandriva.org> 0.7-0.2404.2mdv2009.0
+ Revision: 287182
- add icons from old svn trunk
- New snapshot

* Wed Sep 10 2008 Stéphane Téletchéa <steletch@mandriva.org> 0.7-0.2392.2mdv2009.0
+ Revision: 283432
- update the the lastest svn revision
- rebuild with corrected mlt and mlt++

* Sun Sep 07 2008 Funda Wang <fwang@mandriva.org> 0.7-0.2392.1mdv2009.0
+ Revision: 282323
- New snapshot 2387

* Sat Aug 30 2008 Funda Wang <fwang@mandriva.org> 0.7-0.2387.1mdv2009.0
+ Revision: 277592
- fix file list
- rediff path patch
- New snapshot

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Adapt specfile to kde layout

* Wed Aug 13 2008 Funda Wang <fwang@mandriva.org> 0.7-0.2376.1mdv2009.0
+ Revision: 271506
- New snapshot 0.7 ( kde4 version )

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - buildrequires ffmpeg-devel

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Feb 04 2008 Giuseppe Ghibò <ghibo@mandriva.com> 0.6-0.20080130.2mdv2008.1
+ Revision: 161904
- Add constraints to BuildRequires (for bug #37099).

* Wed Jan 30 2008 Giuseppe Ghibò <ghibo@mandriva.com> 0.6-0.20080130.1mdv2008.1
+ Revision: 160221
- Release from svn 20080130.

* Thu Jan 10 2008 Adam Williamson <awilliamson@mandriva.org> 0.6-0.20080105.2mdv2008.1
+ Revision: 147668
- change the swh-plugins require to a suggest as it's in contrib (thanks blino)

* Sun Jan 06 2008 Giuseppe Ghibò <ghibo@mandriva.com> 0.6-0.20080105.1mdv2008.1
+ Revision: 146067
- Use new CMAKE_CXX_FLAGS (thanks to Marco Gittler).
- Release svn 20080105.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Giuseppe Ghibò <ghibo@mandriva.com> 0.6-0.20071212.1mdv2008.1
+ Revision: 119110
- svn 20071212
- Use cmake.
- Add Patch1 to have the .desktop file at the right place.

* Mon Nov 19 2007 Adam Williamson <awilliamson@mandriva.org> 0.6-0.20071031.3mdv2008.1
+ Revision: 110563
- requires swh-plugins (#33601)

* Thu Nov 01 2007 Giuseppe Ghibò <ghibo@mandriva.com> 0.6-0.20071031.2mdv2008.1
+ Revision: 104718
- Removed extension from icon name.
- Revert update|clean menus removing.
- * Sun Oct 31 2007 Giuseppe Ghib?\195?\178 <ghibo@mandriva.com> 0.6-0.20071007.1
- svn 20071031.
- don't libtoolize (problems with -rpath which isn't disabled).
- removed update|clean menus since there aren't.

* Thu Aug 16 2007 Funda Wang <fwang@mandriva.org> 0.5-2mdv2008.0
+ Revision: 64117
- fix file list
- Renew tarball

* Sun Aug 12 2007 Funda Wang <fwang@mandriva.org> 0.5-1mdv2008.0
+ Revision: 62192
- fix file list
- BR ffmpeg
- New version 0.5

* Fri Aug 10 2007 Funda Wang <fwang@mandriva.org> 0.4-4mdv2008.0
+ Revision: 61500
- add fdo category(bug#32464)

* Wed Aug 01 2007 Adam Williamson <awilliamson@mandriva.org> 0.4-3mdv2008.0
+ Revision: 57307
- drop old menu file
- drop now bogus dependency on piave
- small clean (drop 2006.0 conditionals)


* Wed Feb 07 2007 Laurent Montel <lmontel@mandriva.com> 0.4-2mdv2007.0
+ Revision: 117212
- Fix requires

* Wed Dec 13 2006 Anssi Hannula <anssi@mandriva.org> 0.4-1mdv2007.1
+ Revision: 96473
- from Jos?\195?\169 Jorge <jjorge@free.fr>
  o 0.4
  o drop no longer needed patch 0
  o action icons added to spec

* Sun Oct 29 2006 Anssi Hannula <anssi@mandriva.org> 0.3-1mdv2007.1
+ Revision: 73615
- 0.3
- clean spec
- drop no longer needed patches 1, 2, 3, 4
- patch0: fix autoconf detection
- add new buildrequires and requires
- use find_lang
- add clean_desktop_database
- Import kdenlive

* Wed Aug 30 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.2.4-4mdv2007.0
- Add Patch 4: Fix automake > 1.7 detection

* Sat Jul 01 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.2.43mdv2007.0
- Use macros for icons

* Sun Jan 22 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.2.4-2mdk
-  Add Patch 3 ( from qa.mandriva.com at vpanel.cjb.net) :
		- Fix ticket 15538
- Fix URL
- Use mkrel

* Mon Feb 21 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.2.4-1mdk
- 0.2.4

* Thu Dec 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.2.3-10mdk
- Fix spec file

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.2.3-9mdk
- Rebuild

* Sun May 23 2004 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 0.2.3-8mdk
- grf, forgot the automake buildrequires

* Sat May 22 2004 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 0.2.3-7mdk
- fix buildrequires
- do rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- fix path to qt (lib64 issue)
- added url
- fixed typo

* Thu Apr 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.2.3-6mdk
- Fix requires

* Thu Apr 01 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.2.3-5mdk
- use %%configure
- use mdkversion

* Mon Feb 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.2.3-4mdk
- Fix piave path

* Sun Feb 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.2.3-3mdk
- Rebuild

