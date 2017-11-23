# Syncthing for CentOS

## RPM Installation

```
yum install 
```

## RPM Build

#### Install rpmbuild requirements

```
yum install -y spectool git mock
```

### Setup build environment

First we have to add the CentOS Plus repository to get a more recent version of golang.
To do so add these lines right before the `"""` in /etc/mock/epel-7-x86_64.cfg
```
[centosplus]
name=centosplus
baseurl=http://mirror.centos.org/centos/$releasever/centosplus/$basearch/
enabled=1

```

```
cd ~
git clone https://github.com/daftaupe/syncthing-rpms.git
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
ln -s ~/syncthing-rpms/SPECS/syncthing.spec ~/rpmbuild/SPECS/syncthing.spec
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
cd ~/rpmbuild/SOURCES/
spectool -g ../SPECS/syncthing.spec
cd ~/rpmbuild/SPECS/
```
### Build the SRPM
```
mock --resultdir ~/rpmbuild/SRPMS --buildsrpm --spec ~/rpmbuild/SPECS/syncthing.spec --sources ~/rpmbuild/SOURCES/syncthing-source-v0.14.23.tar.gz
# Get the SRPM in ~/rpmbuild/SRPMS
# On Fedora 25 you get syncthing-0.14.23-0.fc25.src.rpm
# On Centos  7 you get syncthing-0.14.23-0.el7.centos.src.rpm
```

### Build the RPM from the SRPM
Either you get directly the SRPM from the release section on Github or you build it as indicated before (in that case be careful about the name of the SRPM you will get).
```
#RPM file will be found in ~/rpmbuild/RPMS
# Centos7-64bits
mock --cleanup-after --resultdir ~/rpmbuild/RPMS -r epel-7-x86_64 ~/rpmbuild/SRPMS/syncthing-0.14.23-0.fc25.src.rpm
# Fedora-25-64bits
mock --cleanup-after --resultdir ~/rpmbuild/SRPMS -r fedora-25-x86_64 ~/rpmbuild/SRPMS/syncthing-0.14.23-0.fc25.src.rpm
# Fedora-25-32bits
mock --cleanup-after --resultdir ~/rpmbuild/SRPMS -r fedora-25-i386 ~/rpmbuild/SRPMS/syncthing-0.14.23-0.fc25.src.rpm
```

### Start  syncthing systemd service

```
useradd syncthing
sudo systemctl start syncthing@syncthing
```

You can now access the GUI through this URL: 
http://127.0.0.1:8384
