%define	name	loki_patch-fix
%define	version 0.1
%define rel	4
%define	release	%mkrel %rel

Name:		%{name} 
Summary:	A program that fixes broken loki patches
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://goldenfiles.sourceforge.net/index.php?page=lokipatchfix
Group:		Games/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
Requires:	loki_update zenity
BuildArch:	noarch

%description
loki_patch-fix is a program that fixes old patches for loki games
that now segfault upon startup. It does this by replacing the old
loki_patch executeable with a new one automatically. Running this
file on any of the non-working loki patches should make them work
without any problem.

%prep
%setup -q

%build
./build -wo fixedpatch README LICENSE TODO version -v

%install
rm -rf $RPM_BUILD_ROOT
install -m755 ./Loki_patch-fix/loki_patch-fix -D $RPM_BUILD_ROOT%{_bindir}/loki_patch-fix
install -m755 ./Loki_patch-fix/loki_patch-fix-GUI $RPM_BUILD_ROOT%{_bindir}/loki_patch-fix-GUI
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications//
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/loki_patch-fix-GUI
Icon=loki_update
Categories=Game;
Name=Oki
Comment=Oki
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc TODO README version
%{_bindir}/*
%{_datadir}/applications/mandriva-*.desktop



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-4mdv2011.0
+ Revision: 620254
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1-3mdv2010.0
+ Revision: 429865
- rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.1-2mdv2009.0
+ Revision: 218422
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 0.1-2mdv2008.1
+ Revision: 133064
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import loki_patch-fix


* Fri May 12 2006 Eskild Hustvedt <eskild@mandriva.org> 0.1-1mdk
- Yearly rebuild

* Mon Apr 25 2005  Eskild Hustvedt <eskild@mandriva.org> 0.1-1mdk
- Initial Mandriva Linux package
