import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_helpers",
    version="0.0.1",
    author="Maciek",
    author_email="maciek@optidigital.fr",
    description="Python helpers for all projects in python 3",
    long_description=long_description,
    url="https://github.com/optidigital/python_helpers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)