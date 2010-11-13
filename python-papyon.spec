%define 	module	papyon
Summary:	An implementation of the MSN Messenger Protocol
Name:		python-%{module}
Version:	0.5.0
Release:	2
License:	GPL v2+
Group:		Development/Languages/Python
Source0:	http://telepathy.freedesktop.org/releases/papyon/papyon-%{version}.tar.gz
# Source0-md5:	bcd49f11fa9516fb934197e9418ed295
URL:		http://telepathy.freedesktop.org/wiki/Papyon
BuildRequires:	python >= 1:2.5
BuildRequires:	python-Crypto
BuildRequires:	python-devel
BuildRequires:	python-pyOpenSSL
BuildRequires:	python-pygobject
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python >= 1:2.5
Requires:	python-Crypto
Requires:	python-pyOpenSSL
Requires:	python-pygobject >= 2.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
papyon is a library, written in Python, for accessing the MSN instant
messaging service.

%prep
%setup -q -n %{module}-%{version}

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
%{py_sitescriptdir}/papyon-*.egg-info
