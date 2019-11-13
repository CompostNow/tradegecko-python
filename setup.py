import io
from setuptools import setup, find_packages

author = "Drew Kowalik, Chris Clark"
author_email = "team@epantry.com"
maintainer = "Viktor Kerkez"
maintainer_email = "alefnula@gmail.com"
url = "https://github.com/alefnula/tradegecko-python"

# Get version
version_module = {}
exec(io.open("tradegecko/version.py", "r").read(), version_module)
version = version_module["version"]


setup(
    name="tradegecko-python",
    version=f"{version}",
    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,
    url=url,
    description="Python wrapper for TradeGecko REST API",
    long_description=io.open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    platforms=["Windows", "POSIX", "MacOS"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    license="MIT",
    packages=find_packages(),
    install_requires=io.open("requirements.txt").read().splitlines(),
    keywords=["tradegecko"],
    include_package_data=True,
)
