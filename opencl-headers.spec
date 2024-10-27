#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v13
# autospec commit: 2659038
#
Name     : opencl-headers
Version  : 2024.05.08
Release  : 10
URL      : https://github.com/KhronosGroup/OpenCL-Headers/archive/v2024.05.08/OpenCL-Headers-2024.05.08.tar.gz
Source0  : https://github.com/KhronosGroup/OpenCL-Headers/archive/v2024.05.08/OpenCL-Headers-2024.05.08.tar.gz
Summary  : Khronos OpenCL Headers
Group    : Development/Tools
License  : Apache-2.0
Requires: opencl-headers-data = %{version}-%{release}
Requires: opencl-headers-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# OpenCL<sup>TM</sup> API Headers
This repository contains C language headers for the OpenCL API.

%package data
Summary: data components for the opencl-headers package.
Group: Data

%description data
data components for the opencl-headers package.


%package dev
Summary: dev components for the opencl-headers package.
Group: Development
Requires: opencl-headers-data = %{version}-%{release}
Provides: opencl-headers-devel = %{version}-%{release}
Requires: opencl-headers = %{version}-%{release}

%description dev
dev components for the opencl-headers package.


%package license
Summary: license components for the opencl-headers package.
Group: Default

%description license
license components for the opencl-headers package.


%prep
%setup -q -n OpenCL-Headers-2024.05.08
cd %{_builddir}/OpenCL-Headers-2024.05.08

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720126867
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1720126867
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/opencl-headers
cp %{_builddir}/OpenCL-Headers-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/opencl-headers/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*

%files dev
%defattr(-,root,root,-)
/usr/include/CL/cl.h
/usr/include/CL/cl_d3d10.h
/usr/include/CL/cl_d3d11.h
/usr/include/CL/cl_dx9_media_sharing.h
/usr/include/CL/cl_dx9_media_sharing_intel.h
/usr/include/CL/cl_egl.h
/usr/include/CL/cl_ext.h
/usr/include/CL/cl_ext_intel.h
/usr/include/CL/cl_function_types.h
/usr/include/CL/cl_gl.h
/usr/include/CL/cl_gl_ext.h
/usr/include/CL/cl_half.h
/usr/include/CL/cl_icd.h
/usr/include/CL/cl_layer.h
/usr/include/CL/cl_platform.h
/usr/include/CL/cl_va_api_media_sharing_intel.h
/usr/include/CL/cl_version.h
/usr/include/CL/opencl.h
/usr/lib64/pkgconfig/OpenCL-Headers.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/opencl-headers/2b8b815229aa8a61e483fb4ba0588b8b6c491890
