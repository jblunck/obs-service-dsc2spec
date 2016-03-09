Name: obs-service-dsc2spec
Version: 0.1
Release: 0
Group: Development/Libraries
Summary: OBS service to convert *.dsc to *.spec file
License: GPL-2.0+
URL: https://github.com/jblunck/obs-service-dsc2spec
BuildArch: noarch
Source0: %{name}-%{version}.tar.gz

%description
An OBS service that can create a RPM specfile based on a simple Debian source
package.

%package -n dh-installrpm
Group: Development/Libraries
Summary: Debianhelper to install from debian/* to RPM_BUILD_ROOT

%description -n dh-installrpm
Debianhelper script to install from debian/* to RPM_BUILD_ROOT.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 scripts/dh_installrpm %{buildroot}%{_bindir}

%files -n dh-installrpm
%defattr(-,root,root)
%{_bindir}/dh_installrpm

%changelog
