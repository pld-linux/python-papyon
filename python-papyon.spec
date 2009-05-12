%define 	module	papyon
Summary:	An implementation of the MSN Messenger Protocol
Name:		python-%{module}
Version:	0.3.3
Release:	0.1
License:	GPL v2+
Group:		Development/Languages/Python
Source0:	%{module}.tar.bz2
# Source0-md5:	8497be52702c8abdaa1028f8325042a4
URL:		http://github.com/Kjir/papyon/tree/master
BuildRequires:	python >= 1:2.5
BuildRequires:	python-pyOpenSSL
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python >= 1:2.5
Requires:	python-pyOpenSSL
Requires:	python-Crypto
Requires:	python-pygobject >= 2.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
papyon is a library, written in Python, for accessing the MSN instant
messaging service.

%prep
%setup -q -n %{module}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README doc/user-api.conf
%{py_sitescriptdir}/papyon
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/papyon-*.egg-info
%endif
