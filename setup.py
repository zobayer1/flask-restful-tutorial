# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name="myapi",
    url="https://github.com/zobayer1/flask-restful-tutorial",
    author="Zobayer Hasan",
    author_email="zobayer1@gmail.com",
    description="A RESTful application server template built with Python and Flask.",
    keywords="python flask restful api server development template boilerplate",
    license="MIT",
    packages=find_packages(exclude=["docs", "tests", "tests.*"]),
    use_scm_version=True,
    platforms=["posix"],
    entry_points={
        "console_scripts": [
            "myapi = myapi.manage:cli",
        ],
    },
)
