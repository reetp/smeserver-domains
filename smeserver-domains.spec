%define name smeserver-domains
%define version 1.4
%define release 1
Summary: SMEserver rpm for domain pseudonyms
Name: %{name}
Version: %{version}
Release: %{release}
License: GNU GPL version 2
URL: http://www.contribs.org
Distribution: SME Server
Group: SMEServer/addon
Source: %{name}-%{version}.tar.gz
Packager: Stephen Noble <stephen@dungog.net>
BuildRoot: /var/tmp/%{name}-%{version}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires: e-smith-release >= 8
AutoReqProv: no

%description
SMEserver rpm for more advanced domain controls

%changelog
* Thu Apr 28 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0-1.4-1.sme
- First import to smecontribs

* Tue Oct 31 2006 Stephen Noble <support@dungog.net>
- warning added to setup remote MailServer before delegating to them
- [1.2-2]

* Sun Aug 20 2006 Stephen Noble <stephen@dungog.net>
- initial release
- [1.2-1]


%prep
%setup

%build
perl createlinks


%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc " >> %{name}-%{version}-filelist

%clean
cd ..
rm -rf %{name}-%{version}

%pre
%preun
%post
#new installs
if [ $1 = 1 ] ; then
 /bin/touch /home/e-smith/db/dungog
fi


%postun
#uninstalls

#&upgrades


%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
