Summary:	dog - better than cat
Summary(pl):	dog - lepszy ni¿ cat
Name:		dog
Version:	1.7
Release:	1
Group:		Applications/Text
License:	GPL
URL:		http://jl.photodex.com/dog/
Source0:	http://jl.photodex.com/dog/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dog writes the contents of each given file, URL, or the standard input
if none are given or when a file named '-' is given, to the standard
output. It currently supports the file, http, and raw URL types. It is
designed as a compatible, but enhanced, replacement of cat(1).

%description -l pl
dog wypisuje zawarto¶æ podanego pliku, URL lub standardowego wej¶cia
(je¿eli nazwa pliku nie zosta³a podana albo jest to '-') na
standardowe wyj¶cie. Aktualnie obs³uguje pliki, http oraz URL typu
RAW. dog zosta³ zaprojektowany jako kompatybilny, ale roszerzony
zamiennik cat(1)

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install dog $RPM_BUILD_ROOT%{_bindir}/dog
install dog.1 $RPM_BUILD_ROOT%{_mandir}/man1/dog.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dog
%{_mandir}/man1/dog.1.gz
%doc AUTHORS README COPYING
