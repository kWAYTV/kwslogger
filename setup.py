from setuptools import setup, find_packages

VERSION = '0.1.3'
DESCRIPTION = 'This is my own logging library!'

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
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    keywords=["python", "logging", "kwslogger"],
    url="https://github.com/kWAYTV/kwslogger"
)
