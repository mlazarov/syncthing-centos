%define debug_package %{nil}
Name:		syncthing
Version:	0.14.28
Release:	0%{?dist}
Summary:	Open, trustworthy and decentralized sync

Group:		Applications/System
License:	MPLv2
URL:		https://github.com/syncthing/syncthing
Source0:	https://github.com/syncthing/syncthing/releases/download/v%{version}/syncthing-source-v%{version}.tar.gz

BuildRequires:  git golang systemd

%description
Syncthing replaces proprietary sync and cloud services with something open,
trustworthy and decentralized. Your data is your data alone and you deserve
to choose where it is stored, if it is shared with some third party and how
it's transmitted over the Internet.

%prep
%setup -q -n %{name}

%build
export GOPATH="$(pwd)"
mkdir -p src/github.com/syncthing
ln -s "$(pwd)" src/github.com/syncthing/syncthing
cd src/github.com/syncthing/syncthing
./build.sh noupgrade

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_userunitdir}

cp syncthing %{buildroot}%{_bindir}
cp etc/linux-systemd/system/syncthing\@.service  %{buildroot}%{_unitdir}
cp etc/linux-systemd/system/syncthing-resume.service  %{buildroot}%{_unitdir}
cp etc/linux-systemd/user/syncthing.service %{buildroot}%{_userunitdir}


%files
%{_bindir}/syncthing
%{_unitdir}/syncthing@.service
%{_unitdir}/syncthing-resume.service
%{_userunitdir}/syncthing.service

%changelog
* Mon Jun 12 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com>
- Update to v0.14.28

* Mon Jun 12 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com>
- Update to v0.14.27

* Mon Jun 12 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com>
- Bump syncthing version 0.14.25 -> 0.14.26

* Sun Mar 26 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com>
- Bump syncthing version 0.14.24 -> 0.14.25

* Sun Mar 26 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com>
- Bump syncthing version 0.14.23 -> 0.14.24

* Fri Feb 10 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com>
- Adapted from Javier Wilson spec file to build from source tarball

* Thu Feb  9 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com>
- Bump syncthing version 0.14.7 -> 0.14.23

* Thu Sep 22 2016 Logan Owen <logan@s1network.com>
- Bump syncthing version 0.13.1 -> 0.14.7

* Mon Feb 08 2016 Martin Lazarov <martin@lazarov.bg>
- Initial spec version
