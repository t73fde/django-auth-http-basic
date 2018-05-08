# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


heredir = os.path.abspath(".")
README = open(os.path.join(heredir, "README.md")).read()
with open(os.path.join(heredir, "requirements.txt")) as req_file:
    install_requires = [line.strip() for line in req_file.readlines()]

setup(
    name='django-auth-http-basic',
    version='20180508.0',
    description="Django authentication based based on HTTP basic authentication",
    long_description=README,
    url="https://github.com/t73fde/django-auth-http-basic",
    author=u'Detlef Stern',
    author_email='mail-python.org@yodod.de',
    license="APL2",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: System :: Systems Administration :: Authentication/Directory",
    ],
    keywords="authentication django http basic auth",
    packages=find_packages(),
    install_requires=install_requires,
)
