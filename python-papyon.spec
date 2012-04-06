#
# Conditional build:
%bcond_with	tests	# perform "make test". needs live-id

%define 	module	papyon
Summary:	An implementation of the MSN Messenger Protocol
Name:		python-%{module}
Version:	0.5.6
Release:	2
License:	GPL v2+
Group:		Development/Languages/Python
Source0:	http://www.freedesktop.org/software/papyon/releases/papyon-%{version}.tar.gz
# Source0-md5:	7b9a723e5ba6ee82a9c391676144ad29
Patch0:		%{name}-farstream.patch
URL:		http://www.freedesktop.org/wiki/Software/papyon
BuildRequires:	python >= 1:2.5
BuildRequires:	python-Crypto
BuildRequires:	python-devel
BuildRequires:	python-pyOpenSSL
BuildRequires:	python-pygobject
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python >= 1:2.5
Requires:	python-Crypto >= 2.0.0
Requires:	python-farstream
Requires:	python-gstreamer >= 0.10
Requires:	python-pyOpenSSL >= 0.6
Requires:	python-pygobject >= 2.10.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
papyon is a library, written in Python, for accessing the MSN instant
messaging service.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%{__python} setup.py build

%{?with_tests:%{__python} test.py}

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
