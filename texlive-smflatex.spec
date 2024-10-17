Name:		texlive-smflatex
Version:	58910
Release:	2
Summary:	Classes for Societe mathematique de France publications
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/smflatex
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smflatex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smflatex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smflatex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Societe mathematique de France provides a set of classes,
packages and BibTeX styles that are used in its publications.
They are based on AMS classes (whose code is sometimes
recopied) and mainly 'upward-compatible'. Their main features
are: quite different design; new environments for typesetting
some information in two languages (altabstract, alttitle,
altkeywords); if necessary, use of babel (option frenchb) and
deactivation of some features of frenchb. Includes smfart.cls,
smfbook.cls, smfplain.bst, smfalpha.bst, amongst others.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/smflatex
%{_texmfdistdir}/tex/latex/smflatex
%{_texmfdistdir}/bibtex/bst/smflatex
%doc %{_texmfdistdir}/doc/latex/smflatex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
