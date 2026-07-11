%global tl_name polytable
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8.6
Release:	%{tl_revision}.1
Summary:	Tabular-like environments with named columns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/polytable
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/polytable.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/polytable.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/polytable.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package implements a variant of tabular-like environments where
columns can be given a name and entries can flexibly be placed between
arbitrary columns. Complex alignment-based layouts, for example for
program code, are possible. The package depends on lazylist.

