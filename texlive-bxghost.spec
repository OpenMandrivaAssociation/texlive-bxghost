Name:		texlive-bxghost
Version:	66147
Release:	1
Summary:	Ghost insertion for proper xkanjiskip
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bxghost
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxghost.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxghost.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides two commands to help authors for documents
in Japanese to insert proper xkanjiskips. It supports LuaTeX,
XeTeX, pTeX, upTeX, and ApTeX (pTeX-ng).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bxghost
%doc %{_texmfdistdir}/doc/latex/bxghost

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
