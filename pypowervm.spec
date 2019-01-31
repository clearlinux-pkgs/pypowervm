#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypowervm
Version  : 1.1.20
Release  : 6
URL      : https://files.pythonhosted.org/packages/20/6e/cdaa57e101476a24655bfb0b83423618d92a6066210cf3bf0e15f60a959b/pypowervm-1.1.20.tar.gz
Source0  : https://files.pythonhosted.org/packages/20/6e/cdaa57e101476a24655bfb0b83423618d92a6066210cf3bf0e15f60a959b/pypowervm-1.1.20.tar.gz
Summary  : Python binding for the PowerVM REST API
Group    : Development/Tools
License  : Apache-2.0
Requires: pypowervm-license = %{version}-%{release}
Requires: pypowervm-python = %{version}-%{release}
Requires: pypowervm-python3 = %{version}-%{release}
Requires: futures
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
BuildRequires : pbr

%description
Python API wrapper for PowerVM

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

%description python3
python3 components for the pypowervm package.


%prep
%setup -q -n pypowervm-1.1.20

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548943756
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypowervm
cp LICENSE %{buildroot}/usr/share/package-licenses/pypowervm/LICENSE
cp debian/copyright %{buildroot}/usr/share/package-licenses/pypowervm/debian_copyright
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypowervm/LICENSE
/usr/share/package-licenses/pypowervm/debian_copyright

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
