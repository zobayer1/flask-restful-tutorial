# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

install_dependencies = [
    "click",
    "flask",
    "flask-cors",
]

setup(
    name="myapi",
    url="https://github.com/zobayer1/flask-restful-tutorial",
    license="MIT",
    author="Zobayer Hasan",
    author_email="zobayer1@gmail.com",
    description="RESTful application server development with python flask",
    keywords="python flask restful api server development",
    use_scm_version=True,
    packages=find_packages(exclude=["docs", "tests", "tests.*"]),
    include_package_data=True,
    zip_safe=True,
    platforms=["posix"],
    install_requires=install_dependencies,
    entry_points={
        "console_scripts": [
            "myapi = myapi.manage:cli",
        ],
    },
)
