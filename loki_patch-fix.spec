%define	name	loki_patch-fix
%define	version 0.1
%define rel	2
%define	release	%mkrel %rel

Name:		%{name} 
Summary:	A program that fixes broken loki patches
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://goldenfiles.sourceforge.net/index.php?page=lokipatchfix
Group:		Games/Other
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
mkdir -p $RPM_BUILD_ROOT%{_menudir}/
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/loki_patch-fix-GUI" \
icon="loki_update.png" needs="X11" section="More Applications/Games/Other" \
title="Oki" \
longtitle="Oki"
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc TODO README version
%{_bindir}/*
%{_menudir}/*

