from setuptools import setup
import setuptools

with open("README.md", "r") as rmd:
    long_description = rmd.read()

setup(
    name="Brightness-greyscale-contrast",
    version="0.1",
    author="Bmbus",
    description="Algorithm for creating a nice looking contrast on your image (color and greyscale)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PhotoPuting/Brightness-greyscale-contrast/blob/master/setup.py",
    packages=setuptools.find_packages(),
    install_requires=["PIL"],
    python_requires=">=3.7"
)