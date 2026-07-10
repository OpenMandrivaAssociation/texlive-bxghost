%global tl_name bxghost
%global tl_revision 78793

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5.1
Release:	%{tl_revision}.1
Summary:	Ghost insertion for proper xkanjiskip
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/japanese/BX/bxghost
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxghost.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxghost.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides two commands to help authors for documents in
Japanese to insert proper xkanjiskips. It supports LuaTeX, XeTeX, pTeX,
upTeX, and ApTeX (pTeX-ng).

