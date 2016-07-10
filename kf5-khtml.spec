%define		kdeframever	5.24
%define		qtver		5.3.2
%define		kfname		khtml

Summary:	HTML rendering engine
Name:		kf5-%{kfname}
Version:	5.24.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/portingAids/%{kfname}-%{version}.tar.xz
# Source0-md5:	ae5e262e34e8dda40ab928bc6feb478e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5PrintSupport-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kglobalaccel-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kjobwidgets-devel >= %{version}
BuildRequires:	kf5-kjs-devel >= %{version}
BuildRequires:	kf5-knotifications-devel >= %{version}
BuildRequires:	kf5-kparts-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwallet-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-base
BuildRequires:	phonon-qt5-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KHTML is a web rendering engine, based on the KParts technology and
using KJS for JavaScript support.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
/etc/xdg/khtmlrc
%attr(755,root,root) %ghost %{_libdir}/libKF5KHtml.so.5
%attr(755,root,root) %{_libdir}/libKF5KHtml.so.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/khtmladaptorpart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/khtmlimagepart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/khtmlpart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/kjavaappletviewer.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/kmultipart.so
%{_datadir}/kf5/khtml
%{_datadir}/kf5/kjava
#%%dir %{_datadir}/kxmlgui5/khtml
#%%{_datadir}/kxmlgui5/khtml/khtml.rc
#%%{_datadir}/kxmlgui5/khtml/khtml_browser.rc
%{_datadir}/kservices5/khtml.desktop
%{_datadir}/kservices5/khtmladaptorpart.desktop
%{_datadir}/kservices5/khtmlimage.desktop
%{_datadir}/kservices5/kjavaappletviewer.desktop
%{_datadir}/kservices5/kmultipart.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KHtml
%{_includedir}/KF5/khtml_version.h
%{_libdir}/cmake/KF5KHtml
%attr(755,root,root) %{_libdir}/libKF5KHtml.so
%{qt5dir}/mkspecs/modules/qt_KHtml.pri