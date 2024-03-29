import setuptools 
with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ ="0.0.1"

REPO_NAME="kidney_disease_classification"
AUTHOR_USER_NAME="dhruvk2002"
SRC_REPO="cnnClassifer"
AUTHOR_EMAIL="gautampavitra17@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Kidney Disease Classification",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
)
