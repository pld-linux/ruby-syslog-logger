%define	pkgname	syslog-logger
Summary:	An improved Logger replacement that logs to syslog. It is almost drop-in with a few caveats
Name:		ruby-%{pkgname}
Version:	1.6.8
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	5f85ed5fd152e5bafafad0923391296b
URL:		http://github.com/ngmoco/syslog_logger
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An improved Logger replacement that logs to syslog. It is almost
drop-in with a few caveats.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/syslog-formatter.rb
%{ruby_vendorlibdir}/syslog-logger.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
