# revision 31235
# category Package
# catalog-ctan /macros/latex/contrib/polytable
# catalog-date 2012-05-31 00:57:47 +0200
# catalog-license lppl
# catalog-version 0.8.2
Name:		texlive-polytable
Version:	0.8.2
Release:	7
Summary:	Tabular-like environments with named columns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/polytable
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polytable.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polytable.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polytable.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements a variant of tabular-like environments
where columns can be given a name and entries can flexibly be
placed between arbitrary columns. Complex alignment-based
layouts, for example for program code, are possible.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/polytable/polytable.sty
%doc %{_texmfdistdir}/doc/latex/polytable/README
%doc %{_texmfdistdir}/doc/latex/polytable/polytable.pdf
#- source
%doc %{_texmfdistdir}/source/latex/polytable/polytable.dtx
%doc %{_texmfdistdir}/source/latex/polytable/polytable.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
