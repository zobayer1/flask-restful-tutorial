# -*- coding: utf-8 -*-
from os import path
from setuptools import find_packages, setup

install_dependencies = [
    "click",
    "flask-cors",
    "flask-restful",
    "python-dotenv",
]

try:
    docs_file = path.join(path.abspath(path.dirname(__file__)), "README.md")
    with open(docs_file, encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = __doc__

setup(
    name="myapi",
    url="https://github.com/zobayer1/flask-restful-tutorial",
    license="MIT",
    author="Zobayer Hasan",
    author_email="zobayer1@gmail.com",
    description="RESTful application server development with python flask",
    keywords="python flask restful api server development",
    long_description=long_description,
    use_scm_version=True,
    packages=find_packages(exclude=["docs", "tests"]),
    include_package_data=True,
    zip_safe=True,
    platforms=["posix"],
    install_requires=install_dependencies,
    entry_points={
        "console_scripts": [
            "myapi = myapi.manage:cli",
        ],
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
