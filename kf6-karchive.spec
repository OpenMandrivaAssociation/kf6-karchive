%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define major %(echo %{version} |cut -d. -f1-2)

%define libname %mklibname KF6Archive
%define devname %mklibname KF6Archive -d
#define git 20240217

Name: kf6-karchive
Version: 6.16.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/karchive/-/archive/master/karchive-master.tar.bz2#/karchive-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/karchive-%{version}.tar.xz
%endif
Summary: Qt addon providing access to numerous types of archives
URL: https://invent.kde.org/frameworks/karchive
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(LibLZMA)
BuildRequires: cmake(BZip2)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(openssl)
Requires: %{libname} = %{EVRD}

%description
Qt addon providing access to numerous types of archives

%package -n %{libname}
Summary: Qt addon providing access to numerous types of archives
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Qt addon providing access to numerous types of archives

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Qt addon providing access to numerous types of archives

%prep
%autosetup -p1 -n karchive-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/karchive.*

%files -n %{devname}
%{_includedir}/KF6/KArchive
%{_libdir}/cmake/KF6Archive

%files -n %{libname}
%{_libdir}/libKF6Archive.so*
