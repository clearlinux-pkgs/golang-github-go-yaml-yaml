#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-go-yaml-yaml
Version  : a83829b6f1293c91addabc89d0571c246397bbf4
Release  : 6
URL      : https://github.com/go-yaml/yaml/archive/a83829b6f1293c91addabc89d0571c246397bbf4.tar.gz
Source0  : https://github.com/go-yaml/yaml/archive/a83829b6f1293c91addabc89d0571c246397bbf4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0 MIT
BuildRequires : go
BuildRequires : golang-github-go-check-check

%description
# YAML support for the Go language
Introduction
------------
The yaml package enables Go programs to comfortably encode and decode YAML
values. It was developed within [Canonical](https://www.canonical.com) as
part of the [juju](https://juju.ubuntu.com) project, and is based on a
pure Go port of the well-known [libyaml](http://pyyaml.org/wiki/LibYAML)
C library to parse and generate YAML data quickly and reliably.

%prep
%setup -q -n yaml-a83829b6f1293c91addabc89d0571c246397bbf4

%build

%install
gopath="/usr/lib/golang"
library_path="gopkg.in/yaml.v2"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
gopath="/usr/lib/golang"
export GOPATH="%{buildroot}${gopath}"
go test -v -x gopkg.in/yaml.v2

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/gopkg.in/yaml.v2/apic.go
/usr/lib/golang/src/gopkg.in/yaml.v2/decode.go
/usr/lib/golang/src/gopkg.in/yaml.v2/decode_test.go
/usr/lib/golang/src/gopkg.in/yaml.v2/emitterc.go
/usr/lib/golang/src/gopkg.in/yaml.v2/encode.go
/usr/lib/golang/src/gopkg.in/yaml.v2/encode_test.go
/usr/lib/golang/src/gopkg.in/yaml.v2/parserc.go
/usr/lib/golang/src/gopkg.in/yaml.v2/readerc.go
/usr/lib/golang/src/gopkg.in/yaml.v2/resolve.go
/usr/lib/golang/src/gopkg.in/yaml.v2/scannerc.go
/usr/lib/golang/src/gopkg.in/yaml.v2/sorter.go
/usr/lib/golang/src/gopkg.in/yaml.v2/suite_test.go
/usr/lib/golang/src/gopkg.in/yaml.v2/writerc.go
/usr/lib/golang/src/gopkg.in/yaml.v2/yaml.go
/usr/lib/golang/src/gopkg.in/yaml.v2/yamlh.go
/usr/lib/golang/src/gopkg.in/yaml.v2/yamlprivateh.go
