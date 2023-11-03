from setuptools import setup, find_packages

VERSION = '0.1.6'
DESCRIPTION = "My own logging library so i don't need to port it to every single project i make."

setup(
    name="kwslogger",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        "requests",
        "colorama",
        "pytz",
    ],
    author="kWAY",
    author_email="admin@kwayservices.top",
    description=DESCRIPTION,
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    keywords=["python", "logging", "kwslogger"],
    url="https://github.com/kWAYTV/kwslogger"
)