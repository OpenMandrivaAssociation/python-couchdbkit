%define module_name couchdbkit
%define name python-%module_name
%define version 0.4.5
%define release %mkrel 1
%define git_rev 43e9ffa

Name:		%{name}
Summary:    Framework for your Python application to access and manage Couchdb	
Version:	%{version}
Release:	%{release}

License:	BSD
Group:	    Development/Python
URL:		http://%module_name.org
# (misc) downloaded on http://github.com/benoitc/couchdbkit/downloads
Source:     benoitc-couchdbkit-%git_rev.tar.gz 
BuildRequires:  python-devel python-setuptools 
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-buildroot


%description
Framework for your Python application to access and manage Couchdb.

%prep
%setup -q -n benoitc-couchdbkit-%git_rev

%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc examples doc 
%{py_puresitedir}/%module_name
%{py_puresitedir}/*.egg-info
