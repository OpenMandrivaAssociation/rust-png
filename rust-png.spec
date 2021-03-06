# Generated by rust2rpm 13
# * glium is not packaged
%bcond_with check
%global debug_package %{nil}

%global crate png

Name:           rust-%{crate}
Version:        0.15.3
Release:        2%{?dist}
Summary:        PNG decoding and encoding library in pure Rust

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/png
Source:         %{crates_source}
# Initial patched metadata
# * Bump to deflate 0.8
Patch0:         png-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
PNG decoding and encoding library in pure Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+benchmarks-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+benchmarks-devel %{_description}

This package contains library source intended for building other packages
which use "benchmarks" feature of "%{crate}" crate.

%files       -n %{name}+benchmarks-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+deflate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deflate-devel %{_description}

This package contains library source intended for building other packages
which use "deflate" feature of "%{crate}" crate.

%files       -n %{name}+deflate-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+png-encoding-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+png-encoding-devel %{_description}

This package contains library source intended for building other packages
which use "png-encoding" feature of "%{crate}" crate.

%files       -n %{name}+png-encoding-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Josh Stone <jistone@redhat.com> - 0.15.3-1
- Update to 0.15.3

* Mon Dec 16 2019 Josh Stone <jistone@redhat.com> - 0.15.2-2
- Bump to deflate 0.8

* Fri Dec 06 10:48:53 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.2-1
- Update to 0.15.2

* Tue Nov 19 08:03:21 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.1-1
- Update to 0.15.1

* Sun Sep 01 20:56:57 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.0-1
- Update to 0.15.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 10:36:38 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.1-2
- Regenerate

* Tue Apr 30 09:41:23 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.1-1
- Update to 0.14.1

* Fri Mar 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.0-1
- Initial package
