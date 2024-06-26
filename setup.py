import io
import os
import re
from setuptools import setup, find_packages


def _read(fname, fail_silently=False):
    """
    Read the content of the given file. The path is evaluated from the
    directory containing this file.
    """
    try:
        filepath = os.path.join(os.path.dirname(__file__), fname)
        with io.open(filepath, "rt", encoding="utf8") as f:
            return f.read()
    except:
        if not fail_silently:
            raise
        return ""


def _get_version():
    # data = _read("some_dir/some_file.py")
    # version = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", data, re.M | re.I).group(1).strip()
    return "0.0.1"


def _get_requirements(fname):
    """
    Create a list of requirements from the output of the pip freeze command
    saved in a text file.
    """
    packages = _read(fname).split("\n")
    packages = (p.strip() for p in packages)
    packages = (p for p in packages if p and not p.startswith("#"))
    return list(packages)


def _get_long_description():
    return _read("README.md")


if __name__ == "__main__":
    setup(
        name="somescript",
        version=_get_version(),
        packages=find_packages(exclude=["test*"]),
        # metadata for upload to PyPI
        author="Ben Vandesteen",
        author_email="benjaminfvandersteen@gmail.com",
        maintainer="Ben Vandesteen",
        # url="",
        description="Some package with a script entrypoint",
        long_description=_get_long_description(),
        # license="",
        # keywords="",
        install_requires=_get_requirements("requirements.txt"),
        tests_require=_get_requirements("requirements-dev.txt"),
        test_suite="pytest",
        entry_points={"console_scripts": ["somecmd=main:main"]},
    )
