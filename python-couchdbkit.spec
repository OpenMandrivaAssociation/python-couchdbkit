%define module_name couchdbkit
%define name python-%module_name
%define version 0.5.4
%define release 2
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


%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.4-1mdv2011.0
+ Revision: 662525
- update to new version 0.5.4

* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.2-1
+ Revision: 636235
- update to new version 0.5.2

* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.1-1mdv2011.0
+ Revision: 603067
- update to new version 0.5.1

* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 0.4.11-2mdv2011.0
+ Revision: 598982
- rebuild for py2.7

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.11-1mdv2011.0
+ Revision: 569666
- update to new version 0.4.11

* Sat Mar 27 2010 Michael Scherer <misc@mandriva.org> 0.4.5-1mdv2010.1
+ Revision: 528264
- update to 0.4.5 ( and adapt to the migration to github )

* Sun Feb 07 2010 Michael Scherer <misc@mandriva.org> 0.4.2-1mdv2010.1
+ Revision: 501615
- fix wrong permission on directory
- do not requires python, not needed anymore since one year
- fix rpmlint warning about missing section
- upgrade to 0.4.2

* Thu Feb 04 2010 Michael Scherer <misc@mandriva.org> 0.4.1-1mdv2010.1
+ Revision: 500605
- update to new version 0.4.1

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.4-1mdv2010.1
+ Revision: 489179
- update to new version 0.4

* Tue Nov 10 2009 Michael Scherer <misc@mandriva.org> 0.2.2-1mdv2010.1
+ Revision: 463891
- fix BuildRequires
- import python-couchdbkit

