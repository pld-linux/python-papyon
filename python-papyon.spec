#
# Conditional build:
%bcond_with	tests	# perform "make test". needs live-id

%define 	module	papyon
Summary:	An implementation of the MSN Messenger Protocol
Summary(pl.UTF-8):	Implementacja protokołu komunikatora MSN
Name:		python-%{module}
Version:	0.5.6
Release:	3
License:	GPL v2+
Group:		Development/Languages/Python
Source0:	https://www.freedesktop.org/software/papyon/releases/papyon-%{version}.tar.gz
# Source0-md5:	7b9a723e5ba6ee82a9c391676144ad29
Patch0:		%{name}-farstream.patch
URL:		https://www.freedesktop.org/wiki/Software/papyon/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-Crypto
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pyOpenSSL
BuildRequires:	python-pygobject
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-Crypto >= 2.0.0
Requires:	python-farstream
Requires:	python-libs >= 1:2.5
Requires:	python-pyOpenSSL >= 0.6
Requires:	python-pygobject >= 2.10.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
papyon is a library, written in Python, for accessing the MSN instant
messaging service.

%description -l pl.UTF-8
papyon to napisana w Pythona biblioteka pozwalająca na dostęp do
usługi komunikatora MSN.

%prep
%setup -q -n %{module}-%{version}
%patch -P0 -p1

%build
%py_build

%{?with_tests:%{__python} test.py}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

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
