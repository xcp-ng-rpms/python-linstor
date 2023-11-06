Summary: Linstor python api
Name:    python-linstor
Version: 1.19.0
Release: 1%{?dist}
License: LGPLv3
URL:     https://linbit.com/linstor/

BuildArch: noarch

Source0: https://pkg.linbit.com//downloads/linstor/%{name}-%{version}.tar.gz

# The build container for XCP-ng 8.2 doesn't have python3, so python3 available
# means we're building for XCP-ng >= 8.3 and thus we use python3.
%if "%(which python3 2>/dev/null)"
%define python "python3"
BuildRequires: python3-setuptools
%else
%define python "python2"
Patch0: setup.py-python2.patch
BuildRequires: python-setuptools python-enum34
Requires: python-enum34
%endif

%description
This repository contains a Python library to communicate with a linstor controller.

%prep
%autosetup -p1

%build
PYTHON=%{python} %{python} ./setup.py build

%install
PYTHON=%{python} %{python} ./setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%license COPYING

%changelog
* Tue Nov 7 2023 Thierry Escande <thierry.escande@vates.tech> - 1.19.0-1
- Update to python-linstor-1.19.0
