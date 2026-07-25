%define upstream_name    Perl-Critic-Swift
%define upstream_version 1.000003

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    1

Summary:    Additional policies for Perl::Critic
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/dist/Perl-Critic-Swift
Source0:    https://cpan.metacpan.org/authors/id/E/EL/ELLIOTJS/Perl-Critic-Swift-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires: perl(English)
BuildRequires: perl(File::Spec)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Perl::Critic::Policy)
BuildRequires: perl(Perl::Critic::TestUtils)
BuildRequires: perl(Perl::Critic::Utils)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Perl::Critic)
BuildRequires: perl(base)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(version)
BuildRequires: perl(warnings)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The included policies are:

* the Perl::Critic::Policy::CodeLayout::RequireUseUTF8 manpage

  Require that code includes a 'use utf8;' statement. [Severity: 3]

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.0.3-2mdv2011.0
+ Revision: 655613
- rebuild for updated spec-helper

* Thu Sep 02 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 575423
- import perl-Perl-Critic-Swift

