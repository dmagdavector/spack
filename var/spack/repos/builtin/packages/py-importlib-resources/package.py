# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyImportlibResources(PythonPackage):
    """Read resources from Python packages"""

    homepage = "https://github.com/python/importlib_resources"
    pypi = "importlib_resources/importlib_resources-1.0.2.tar.gz"

    license("Apache-2.0")

    version("6.4.5", sha256="980862a1d16c9e147a59603677fa2aa5fd82b87f223b6cb870695bcfce830065")
    version("6.4.0", sha256="cdb2b453b8046ca4e3798eb1d84f3cce1446a0e8e7b5ef4efb600f19fc398145")
    version("6.3.2", sha256="963eb79649252b0160c1afcfe5a1d3fe3ad66edd0a8b114beacffb70c0674223")
    version("6.3.0", sha256="166072a97e86917a9025876f34286f549b9caf1d10b35a1b372bffa1600c6569")
    version("6.2.0", sha256="4351403cba8e3a1c03ff15b6bbea1cde4c6de00c705f49ea13909b404b415b9c")
    version("6.1.3", sha256="56fb4525197b78544a3354ea27793952ab93f935bb4bf746b846bb1015020f2b")
    version("6.1.0", sha256="9d48dcccc213325e810fd723e7fbb45ccb39f6cf5c31f00cf2b965f5f10f3cb9")
    version("6.0.1", sha256="4359457e42708462b9626a04657c6208ad799ceb41e5c58c57ffa0e6a098a5d4")
    version("6.0.0", sha256="4cf94875a8368bd89531a756df9a9ebe1f150e0f885030b461237bc7f2d905f2")
    version("5.13.0", sha256="82d5c6cca930697dbbd86c93333bb2c2e72861d4789a11c2662b933e5ad2b528")
    version("5.12.0", sha256="4be82589bf5c1d7999aedf2a45159d10cb3ca4f19b2271f8792bc8e6da7b22f6")
    version("5.9.0", sha256="5481e97fb45af8dcf2f798952625591c58fe599d0735d86b10f54de086a61681")
    version("5.3.0", sha256="f2e58e721b505a79abe67f5868d99f8886aec8594c962c7490d0c22925f518da")
    version("5.2.3", sha256="203d70dda34cfbfbb42324a8d4211196e7d3e858de21a5eb68c6d1cdd99e4e98")
    version("5.2.2", sha256="a65882a4d0fe5fbf702273456ba2ce74fe44892c25e42e057aca526b702a6d4b")
    version("5.1.0", sha256="bfdad047bce441405a49cf8eb48ddce5e56c696e185f59147a8b79e75e9e6380")
    version("1.0.2", sha256="d3279fd0f6f847cced9f7acc19bd3e5df54d34f93a2e7bb5f238f81545787078")

    depends_on("python@3.8:", when="@6.4:", type=("build", "run"))
    depends_on("py-setuptools@61.2:", when="@6.4.1:", type="build")
    depends_on("py-setuptools@56:", when="@5.9.0:", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm@3.4.1:+toml", when="@5:", type="build")

    depends_on("py-zipp@3.1.0:", when="@5.2.2: ^python@:3.9", type=("build", "run"))
    depends_on("py-zipp@0.4:", when="@5.0:5.1", type=("build", "run"))
