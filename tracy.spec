Name:    tracy
Version: 0.7.1
Release: 2%{?dist}
Summary: Tracy Profiler
Group:   Applications/Internet
License: BSD
URL:     https://github.com/wolfpld/tracy
Source0: https://github.com/wolfpld/tracy/archive/v%{version}.tar.gz

Patch1:  0001-release.patch

BuildRequires: capstone-devel
BuildRequires: gcc-c++
BuildRequires: glfw-devel
BuildRequires: gtk3-devel
BuildRequires: harfbuzz-devel
BuildRequires: pango-devel
BuildRequires: pkgconfig

%description
Tracy profiler

%prep
%setup -q -n tracy-%{version}
%patch1 -p1

%build
%set_build_flags
%make_build -C profiler/build/unix release

%install
mkdir -p %{buildroot}%{_bindir}
cp ./profiler/build/unix/Tracy-release %{buildroot}%{_bindir}/tracy

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README.md
%license LICENSE
%{_bindir}/tracy

%changelog
* Fri Aug 28 2020 Evan Klitzke <evan@eklitzke.org> - 0.7.1-2
- Use fedora build flags, enable debug package.

* Fri Aug 28 2020 Evan Klitzke <evan@eklitzke.org> - 0.7.1-1
- Initial packaging work.
