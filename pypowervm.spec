#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypowervm
Version  : 1.1.17
Release  : 2
URL      : https://files.pythonhosted.org/packages/ea/f7/752fb0b7a7bffe2eeecb7157192163f09b605f44628ce3cb3cd32ceef7d5/pypowervm-1.1.17.tar.gz
Source0  : https://files.pythonhosted.org/packages/ea/f7/752fb0b7a7bffe2eeecb7157192163f09b605f44628ce3cb3cd32ceef7d5/pypowervm-1.1.17.tar.gz
Summary  : Python binding for the PowerVM REST API
Group    : Development/Tools
License  : Apache-2.0
Requires: pypowervm-python3
Requires: pypowervm-license
Requires: pypowervm-python
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

%package doc
Summary: doc components for the pypowervm package.
Group: Documentation

%description doc
doc components for the pypowervm package.


%package license
Summary: license components for the pypowervm package.
Group: Default

%description license
license components for the pypowervm package.


%package python
Summary: python components for the pypowervm package.
Group: Default
Requires: pypowervm-python3

%description python
python components for the pypowervm package.


%package python3
Summary: python3 components for the pypowervm package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pypowervm package.


%prep
%setup -q -n pypowervm-1.1.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536417769
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pypowervm
cp LICENSE %{buildroot}/usr/share/doc/pypowervm/LICENSE
cp debian/copyright %{buildroot}/usr/share/doc/pypowervm/debian_copyright
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/pypowervm/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/pypowervm/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
