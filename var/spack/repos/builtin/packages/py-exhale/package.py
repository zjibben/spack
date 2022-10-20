# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyExhale(PythonPackage):
    """Automatic C++ library api documentation generation: breathe doxygen in
    and exhale it out."""

    homepage = "https://github.com/svenevs/exhale"
    pypi = "exhale/exhale-0.3.6.tar.gz"

    version("0.3.6", sha256="ab41be313e1236bd4386e4696fb35f37ce8103c2059cf8d1f083da5411bb74d7")

    depends_on("py-setuptools@42:", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-breathe@4.32.0:", type="build")
    depends_on("py-beautifulsoup4", type=("build", "run"))
    depends_on("py-lxml", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
