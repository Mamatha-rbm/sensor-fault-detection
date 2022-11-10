from setuptools import find_packages,setup

setup(
    name="sensor",
    version="0.0.1",
    author="ineuorn",
    author_email="chandholumamatha@gmail.com",
    packages=find_packages(),
    install_requires=["pymongo==4.2.0"],
)
