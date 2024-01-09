Summary: Linstor python api
Name:    python-linstor
Version: 1.19.0
Release: 2%{?dist}
License: LGPLv3
URL:     https://linbit.com/linstor/

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools

Requires: python-enum34

Source0: https://pkg.linbit.com/downloads/linstor/%{name}-%{version}.tar.gz
Patch0: setup.py.patch

%description
This repository contains a Python library to communicate with a linstor controller.

%prep
%autosetup -p1

%build
PYTHON=%{__python2} %{__python2} ./setup.py build

%install
PYTHON=%{__python2} %{__python2} ./setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%license COPYING
%doc README.md

%changelog
* Tue Jan 09 2024 Thierry Escande <thierry.escande@vates.tech> - 1.19.0-2
- Fixed a missing dependency on enum34 package

* Tue Nov 07 2023 Thierry Escande <thierry.escande@vates.tech> - 1.19.0-1
- Update to python-linstor-1.19.0
