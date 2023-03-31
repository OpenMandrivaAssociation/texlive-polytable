Name:		texlive-polytable
Version:	55837
Release:	2
Summary:	Tabular-like environments with named columns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/polytable
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polytable.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polytable.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polytable.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
