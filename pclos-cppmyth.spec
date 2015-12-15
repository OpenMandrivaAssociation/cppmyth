%define cppmyth_major 1
%define libname %mklibname %name %{cppmyth_major}
%define develname %mklibname -d %name


Name:           cppmyth
Version:        1.1.10
Release:        %mkrel 1
Summary:        Client interface for the MythTV backend
Group:          System/Libraries
License:        GPLv2+
URL:            https://github.com/janbar/cppmyth/
Source0:        https://github.com/janbar/%{name}/archive/v%{version}/%{name}-%{version}.tar.xz
Patch0:         aarch64.patch
BuildRequires:  cmake

%description
This project is intended to create a easy client interface for the MythTV
backend. Its development started from January 2014 and today the API supports
the protocol version of MythTV 0.26 to 0.28-pre.

%package -n %libname
Summary:        cppmyth library
Group:          System/Libraries

%description -n %libname
This project is intended to create a easy client interface for the MythTV
backend. Its development started from January 2014 and today the API supports
the protocol version of MythTV 0.26 to 0.28-pre.


%package -n     %{develname}
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{libname} = %{version}-%{release}
Provides:	cppmyth-devel = %{version}-%{release}
Provides:	libcppmyth-devel = %{version}-%{release}

%description -n     %{develname}
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%setup -q
%patch0 -p1


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib}
%make


%install
rm -rf %buildroot
%make_install -C build


%files -n %libname
%doc README
%{_libdir}/*.so.*


%files -n %develname
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sat Aug 22 2015 bb <bb> 1.1.10-1pclos2015
- import into pclos for kodi 15.1

