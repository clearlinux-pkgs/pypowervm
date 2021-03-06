#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypowervm
Version  : 1.1.24
Release  : 15
URL      : https://files.pythonhosted.org/packages/16/c1/8e6574bd5e8936fd858bab0b1aa1b825cfc61e0cebf65a248239c7b2c01b/pypowervm-1.1.24.tar.gz
Source0  : https://files.pythonhosted.org/packages/16/c1/8e6574bd5e8936fd858bab0b1aa1b825cfc61e0cebf65a248239c7b2c01b/pypowervm-1.1.24.tar.gz
Summary  : Python binding for the PowerVM REST API
Group    : Development/Tools
License  : Apache-2.0
Requires: pypowervm-license = %{version}-%{release}
Requires: pypowervm-python = %{version}-%{release}
Requires: pypowervm-python3 = %{version}-%{release}
Requires: lxml
Requires: oslo.concurrency
Requires: oslo.context
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.utils
Requires: pbr
Requires: pyasn1
Requires: pyasn1-modules
Requires: pytz
Requires: requests
Requires: six
Requires: taskflow
BuildRequires : buildreq-distutils3
BuildRequires : lxml
BuildRequires : oslo.concurrency
BuildRequires : oslo.context
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : pyasn1
BuildRequires : pyasn1-modules
BuildRequires : pytz
BuildRequires : requests
BuildRequires : six
BuildRequires : taskflow

%description
pypowervm - Python API wrapper for PowerVM
        ==========================================
        
        NOTE
        ----
        Current versions should utilize the local authentication mechanism.  The remote
        authentication mechanism is intended only for development and test purposes for
        the time being.
        
        Overview
        --------
        pypowervm provides a Python-based API wrapper for interaction with IBM
        PowerVM-based systems.
        
        License
        -------
        The library's license can be found in the LICENSE_ file.  It must be
        reviewed prior to use.

%package license
Summary: license components for the pypowervm package.
Group: Default

%description license
license components for the pypowervm package.


%package python
Summary: python components for the pypowervm package.
Group: Default
Requires: pypowervm-python3 = %{version}-%{release}

%description python
python components for the pypowervm package.


%package python3
Summary: python3 components for the pypowervm package.
Group: Default
Requires: python3-core
Provides: pypi(pypowervm)
Requires: pypi(lxml)
Requires: pypi(oslo.concurrency)
Requires: pypi(oslo.context)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.log)
Requires: pypi(oslo.utils)
Requires: pypi(pbr)
Requires: pypi(pyasn1)
Requires: pypi(pyasn1_modules)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(six)
Requires: pypi(taskflow)

%description python3
python3 components for the pypowervm package.


%prep
%setup -q -n pypowervm-1.1.24
cd %{_builddir}/pypowervm-1.1.24

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583704092
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypowervm
cp %{_builddir}/pypowervm-1.1.24/LICENSE %{buildroot}/usr/share/package-licenses/pypowervm/294b43b2cec9919063be1a3b49e8722648424779
cp %{_builddir}/pypowervm-1.1.24/debian/copyright %{buildroot}/usr/share/package-licenses/pypowervm/f6a3d559ca60d7dcfde2aff5090d1aa19ef48dea
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypowervm/294b43b2cec9919063be1a3b49e8722648424779
/usr/share/package-licenses/pypowervm/f6a3d559ca60d7dcfde2aff5090d1aa19ef48dea

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
