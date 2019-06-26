#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : opencl-headers
Version  : c5a4bbeabb10d8ed3d1c651b93aa31737bc473dd
Release  : 1
URL      : https://github.com/KhronosGroup/OpenCL-Headers/archive/c5a4bbeabb10d8ed3d1c651b93aa31737bc473dd.tar.gz
Source0  : https://github.com/KhronosGroup/OpenCL-Headers/archive/c5a4bbeabb10d8ed3d1c651b93aa31737bc473dd.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: opencl-headers-license = %{version}-%{release}

%description
# OpenCL<sup>TM</sup> API Headers
This repository contains C language headers for the OpenCL API.

%package dev
Summary: dev components for the opencl-headers package.
Group: Development
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
%setup -q -n OpenCL-Headers-c5a4bbeabb10d8ed3d1c651b93aa31737bc473dd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561567420
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags} || :


%install
export SOURCE_DATE_EPOCH=1561567420
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/opencl-headers
cp LICENSE %{buildroot}/usr/share/package-licenses/opencl-headers/LICENSE
:
## install_append content
mkdir -p %{buildroot}/usr/include/CL
install -m644 CL/* %{buildroot}/usr/include/CL
## install_append end

%files
%defattr(-,root,root,-)

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
/usr/include/CL/cl_gl.h
/usr/include/CL/cl_gl_ext.h
/usr/include/CL/cl_platform.h
/usr/include/CL/cl_va_api_media_sharing_intel.h
/usr/include/CL/cl_version.h
/usr/include/CL/opencl.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/opencl-headers/LICENSE