%{?scl:%scl_package perl-Config-Perl-V}

%global base_version 0.31

Name:           %{?scl_prefix}perl-Config-Perl-V
Version:        0.32
Release:        452%{?dist}
Summary:        Structured data retrieval of perl -V output
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Config-Perl-V
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/Config-Perl-V-%{base_version}.tgz
# Correct example
Patch0:         Config-Perl-V-0.24-Remove-invalid-shellbang.patch
# Unbundled from perl 5.29.10
Patch1:         Config-Perl-V-0.31-Upgrade-to-0.32.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Optional run-time:
BuildRequires:  %{?scl_prefix}perl(Digest::MD5)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Test::More)
%if !%{defined perl_bootstrap}
# Building core modules must not require non-core modules when bootstrapping
BuildRequires:  %{?scl_prefix}perl(Test::NoWarnings)
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Digest::MD5)
Conflicts:      %{?scl_prefix}perl < 4:5.22.0-347

%description
The command "perl -V" will return you an excerpt from the %%Config::Config
hash combined with the output of "perl -V" that is not stored inside the hash,
but only available to the perl binary itself. This package provides Perl
module that will return you the output of "perl -V" in a structure.

%prep
%setup -q -n Config-Perl-V-%{base_version}
%patch0 -p1
%patch1 -p1
chmod -x examples/*

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# Building core modules must not require non-core modules when bootstrapping
%{?scl:scl enable %{scl} '}make test PERL_CORE=%{defined perl_bootstrap}%{?scl:'}

%files
%doc Changelog CONTRIBUTING.md examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jan 07 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-452
- Re-rebuild of bootstrapped packages

* Fri Dec 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-451
- SCL

* Fri Sep 27 2019 Petr Pisar <ppisar@redhat.com> - 0.32-441
- Indeed upgrade to 0.32

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-438
- Increase release to favour standalone package

* Fri May 03 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-1
- Upgrade to 0.32 as provided in perl-5.29.10

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Petr Pisar <ppisar@redhat.com> - 0.31-1
- 0.31 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Petr Pisar <ppisar@redhat.com> - 0.30-1
- 0.30 bump

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-416
- Increase release to favour standalone package

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 16 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-1
- 0.29 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-394
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-393
- Perl 5.26 rebuild

* Fri May 12 2017 Petr Pisar <ppisar@redhat.com> - 0.28-2
- Building core modules must not require non-core modules when bootstrapping

* Thu May 11 2017 Petr Pisar <ppisar@redhat.com> - 0.28-1
- Upgrade to 0.28 as provided in perl-5.25.12

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 12 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-1
- 0.27 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-2
- Perl 5.24 rebuild

* Wed May 11 2016 Petr Pisar <ppisar@redhat.com> - 0.26-1
- 0.26 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Petr Pisar <ppisar@redhat.com> - 0.25-1
- 0.25 bump

* Wed Jul 01 2015 Petr Pisar <ppisar@redhat.com> 0.24-348
- Specfile autogenerated by cpanspec 1.78.
