%define module_name couchdbkit
%define name python-%module_name
%define version 0.2.2
%define release %mkrel 1

Name:		%{name}
Summary:    Framework for your Python application to access and manage Couchdb	
Version:	%{version}
Release:	%{release}

License:	BSD
Group:	    Development/Python
URL:		http://%module_name.org
Source:     http://bitbucket.org/benoitc/%module_name/get/%{version}.tar.bz2	
Requires:	python
BuildRequires:  python-devel 
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-buildroot


%description
Framework for your Python application to access and manage Couchdb.

%prep

%setup -q -n %module_name
%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root)
%doc examples doc 
%{py_puresitedir}/%module_name
%{py_puresitedir}/*.egg-info
# that's quite weird to have files there
%{py_puresitedir}/tests

