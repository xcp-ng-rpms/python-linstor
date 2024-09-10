Summary: Linstor python api
Name:    python-linstor
Version: 1.23.0
Release: 1%{?dist}
License: LGPLv3
URL:     https://linbit.com/linstor/

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

Source0: https://pkg.linbit.com/downloads/linstor/%{name}-%{version}.tar.gz

%description
This repository contains a Python library to communicate with a linstor controller.

%prep
%autosetup -p1

%build
PYTHON=%{__python3} %{__python3} ./setup.py build

%install
PYTHON=%{__python3} %{__python3} ./setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%license COPYING
%doc README.md

%changelog
* Tue Sep 10 2024 Ronan Abhamon <ronan.abhamon@vates.tech> - 1.23.0-1
- Update to python-linstor-1.23.0

* Tue Nov 07 2023 Thierry Escande <thierry.escande@vates.tech> - 1.19.0-1
- Update to python-linstor-1.19.0
