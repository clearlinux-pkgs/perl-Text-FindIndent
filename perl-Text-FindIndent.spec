#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-FindIndent
Version  : 0.11
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Text-FindIndent-0.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Text-FindIndent-0.11.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-findindent-perl/libtext-findindent-perl_0.11-1.debian.tar.xz
Summary  : 'Heuristically determine the indent style'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-FindIndent-license = %{version}-%{release}
Requires: perl-Text-FindIndent-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install::DSL)

%description
No detailed description available

%package dev
Summary: dev components for the perl-Text-FindIndent package.
Group: Development
Provides: perl-Text-FindIndent-devel = %{version}-%{release}
Requires: perl-Text-FindIndent = %{version}-%{release}

%description dev
dev components for the perl-Text-FindIndent package.


%package license
Summary: license components for the perl-Text-FindIndent package.
Group: Default

%description license
license components for the perl-Text-FindIndent package.


%package perl
Summary: perl components for the perl-Text-FindIndent package.
Group: Default
Requires: perl-Text-FindIndent = %{version}-%{release}

%description perl
perl components for the perl-Text-FindIndent package.


%prep
%setup -q -n Text-FindIndent-0.11
cd %{_builddir}
tar xf %{_sourcedir}/libtext-findindent-perl_0.11-1.debian.tar.xz
cd %{_builddir}/Text-FindIndent-0.11
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Text-FindIndent-0.11/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-FindIndent
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Text-FindIndent/f2d009e75f375d5d2d8c4f2aa8019b5fa054c515
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::FindIndent.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-FindIndent/f2d009e75f375d5d2d8c4f2aa8019b5fa054c515

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/Text/FindIndent.pm
