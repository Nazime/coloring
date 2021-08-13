import codecs
import os

from setuptools import find_packages, setup

# Functions/ global variables
HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


# Metadata
NAME = "coloring"
VERSION = "0.1.5"
LICENSE = "MIT"
DESCRIPTION = "Coloring is an other python library used to colorize texts in terminal using ANSI escape with a pythonic API."
LONG_DESCRIPTION = read("README.md")
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"
URL = "https://github.com/nazime/" + NAME
PROJECT_URLS = {
    "Documentation": "https://" + NAME + ".readthedocs.org/",
    "Bug Tracker": URL + "/issues",
    "Source Code": URL,
}
AUTHOR = "Nazime LAKEHAL"
AUTHOR_EMAIL = "nazime.lkh@gmail.com"
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
KEYWORDS = []
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]

# Packages information
PACKAGES = find_packages(where="src")
PACKAGE_DIR = {"": "src"}
INSTALL_REQUIRES = []
EXTRAS_REQUIRE = {
    "docs": ["sphinx", "sphinx_rtd_theme", "sphinxcontrib.napoleon"],
    "tests": [
        "coverage",
        "hypothesis",
        "pytest>=4.3.0",  # 4.3.0 dropped last use of `convert`
    ],
}
EXTRAS_REQUIRE["dev"] = (
    EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["docs"] + ["pre-commit"]
)

EXTRAS_REQUIRE["travis"] = EXTRAS_REQUIRE["dev"] + ["tox", "codecov"]
PYTHON_REQUIRES = ">=3.6"

ZIP_SAFE = False
ENTRY_POINTS = {"console_scripts": ["coloring=coloring.__main__:main"]}
INCLUDE_PACKAGE_DATA = False
PACKAGE_DATA = {NAME: ["data/*"]}

if __name__ == "__main__":
    setup(
        # Metadata
        name=NAME,
        version=VERSION,
        license=LICENSE,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
        url=URL,
        project_urls=PROJECT_URLS,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        # Package information
        packages=PACKAGES,
        package_dir=PACKAGE_DIR,
        install_requires=INSTALL_REQUIRES,
        python_requires=PYTHON_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        zip_safe=ZIP_SAFE,
        include_package_data=INCLUDE_PACKAGE_DATA,
        entry_points=ENTRY_POINTS,
        package_data=PACKAGE_DATA,
    )
