import os
from setuptools import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_version():
    path = os.path.join(BASE_DIR, "VERSION")
    with open(path, "r") as version_file:
        return version_file.read().strip()


def get_license_file():
    return os.path.join(BASE_DIR, "LICENSE")


def get_long_description():
    path = os.path.join(BASE_DIR, "README.md")


def get_requires():
    path = os.path.join(BASE_DIR, "requirements.txt")
    with open(path, "r") as require_file:
        packages = [
            package.strip()
            for package in require_file.read().strip().split("\n")
        ]

        return packages


APP_PROPERTY = {
    "name": "fxp",
    "version": get_version(),
    "author": "Zhdanovich Vital",
    "author_email": "v.urich1993@yandex.by",
    "url": "",
    "packages": find_packages("src", exclude=["tests", "*test*"]),
    "package_dir": {"": "src"},
    "test_suite": "tests",
    "include_package_data": True,
    "license": get_license_file(),
    "description": "Forex parser",
    "long_description": get_long_description(),
    "long_description_content_type": "text/markdown",
    "install_requires": get_requires(),
    "python_requires": ">=3.8",
    "zip_safe": False,
    "classifiers": ["Development Status ::5 - Production/Stable"],
}
setup(**APP_PROPERTY)
