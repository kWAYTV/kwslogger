"""
Setup script for kwslogger package.

This script installs the kwslogger package along with its dependencies.
"""

from setuptools import setup, find_packages

VERSION = '0.2.9'
DESCRIPTION = "My own logging library so i don't need to port it to every single project i make."

setup(
    name="kwslogger",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        "colorama",
        "pystyle",
        "pyfiglet",
        "pytz",
        "yaspin",
        "tqdm",
    ],
    author="kWAY",
    author_email="admin@kwayservices.top",
    description=DESCRIPTION,
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    keywords=["python", "logging", "kwslogger"],
    url="https://github.com/kWAYTV/kwslogger"
)