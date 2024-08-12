Name:       mpris-qt$${QT_MAJOR_VERSION}

Summary:    Qt and QML MPRIS interface and adaptor
Version:    1.0.6
Release:    1
License:    LGPLv2
URL:        https://git.sailfishos.org/mer-core/qtmpris
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt$${QT_MAJOR_VERSION}Core)
BuildRequires:  pkgconfig(Qt$${QT_MAJOR_VERSION}DBus)
BuildRequires:  pkgconfig(Qt$${QT_MAJOR_VERSION}Qml)

%description
%{summary}.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%package qml-plugin
Summary:    QML plugin for %{name}
Requires:   %{name} = %{version}-%{release}

%description qml-plugin
QML plugin for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5 VERSION=`echo %{version} | sed 's/+.*//'`

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

%qmake5_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_datarootdir}/qt$${QT_MAJOR_VERSION}/mkspecs/features/%{name}.prf
%{_includedir}/qt$${QT_MAJOR_VERSION}/MprisQt/Mpris
%{_includedir}/qt$${QT_MAJOR_VERSION}/MprisQt/MprisPlayer
%{_includedir}/qt$${QT_MAJOR_VERSION}/MprisQt/MprisController
%{_includedir}/qt$${QT_MAJOR_VERSION}/MprisQt/MprisManager
%{_includedir}/qt$${QT_MAJOR_VERSION}/MprisQt/mprisqt.h
%{_includedir}/qt$${QT_MAJOR_VERSION}/MprisQt/mpris.h
%{_includedir}/qt$${QT_MAJOR_VERSION}/MprisQt/mprisplayer.h
%{_includedir}/qt$${QT_MAJOR_VERSION}/MprisQt/mpriscontroller.h
%{_includedir}/qt$${QT_MAJOR_VERSION}/MprisQt/mprismanager.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc


%files qml-plugin
%defattr(-,root,root,-)
%{_libdir}/qt$${QT_MAJOR_VERSION}/qml/org/nemomobile/mpris/libmpris-qt$${QT_MAJOR_VERSION}-qml-plugin.so
%{_libdir}/qt$${QT_MAJOR_VERSION}/qml/org/nemomobile/mpris/plugins.qmltypes
%{_libdir}/qt$${QT_MAJOR_VERSION}/qml/org/nemomobile/mpris/qmldir
