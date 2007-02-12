Summary:	dog - better than cat
Summary(pl.UTF-8):	dog - lepszy niż cat
Name:		dog
Version:	1.7
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	http://jl.photodex.com/dog/%{name}-%{version}.tar.gz
# Source0-md5:	9dd1e04efb7f8535a632bac2eef60a10
URL:		http://jl.photodex.com/dog/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dog writes the contents of each given file, URL, or the standard input
if none are given or when a file named '-' is given, to the standard
output. It currently supports the file, http, and raw URL types. It is
designed as a compatible, but enhanced, replacement of cat(1).

%description -l pl.UTF-8
dog wypisuje zawartość podanego pliku, URL lub standardowego wejścia
(jeżeli nazwa pliku nie została podana albo jest to '-') na
standardowe wyjście. Aktualnie obsługuje URL-e typu file, http oraz
raw. dog został zaprojektowany jako kompatybilny, ale rozszerzony
zamiennik cat(1).

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
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/dog
%{_mandir}/man1/dog.1*
