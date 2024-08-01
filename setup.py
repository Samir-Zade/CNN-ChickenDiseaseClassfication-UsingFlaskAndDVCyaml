import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classfication"
AUTHOR_USER_NAME = "Samir-Zade"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "samirzadeofficial@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="CNN based project for chicken disease classfication",
    long_description="text/markdown",
    url="https://github.com/Samir-Zade/Chicken-Disease-Classfication.git",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)