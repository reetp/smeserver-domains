%define name smeserver-domains
%define version 1.3
%define release 1
Summary: SMEserver rpm for rsync
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
* Sat Apr 22 2016 John Crisp <jcrisp@safeandsoundit.co.uk>
- First import to smecontribs

* Tue Oct 31 17:00:00 2006 Stephen Noble <support@dungog.net>
- warning added to setup remote MailServer before delegating to them
- [1.2-2]

* Sun Aug 20 18:00:00 2006 Stephen Noble <stephen@dungog.net>
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

/bin/chmod 644 /etc/crontab
/etc/e-smith/events/actions/initialize-default-databases

echo ''
echo 'Remote server syntax changed for secure transfers from dungog-rsync-1.2-4'
echo 'you now need to enter the user as well as the server'
echo 'this removes the requirement of having the same user on both servers'
echo 'but you may need to update your existing rules'
echo ''


%postun
#uninstalls
if [ $1 = 0 ] ; then
 /sbin/e-smith/expand-template /etc/crontab
 /bin/rm -rf /usr/bin/dungogrsync-?????
fi

#&upgrades


%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
