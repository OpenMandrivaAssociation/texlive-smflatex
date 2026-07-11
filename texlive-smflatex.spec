%global tl_name smflatex
%global tl_revision 58910

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Classes for Societe mathematique de France publications
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/smflatex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/smflatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/smflatex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/smflatex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Societe mathematique de France provides a set of classes, packages
and BibTeX styles that are used in its publications. They are based on
AMS classes (whose code is sometimes recopied) and mainly 'upward-
compatible'. Their main features are: quite different design; new
environments for typesetting some information in two languages
(altabstract, alttitle, altkeywords); if necessary, use of babel (option
frenchb) and deactivation of some features of frenchb. Includes
smfart.cls, smfbook.cls, smfplain.bst, smfalpha.bst, amongst others.

