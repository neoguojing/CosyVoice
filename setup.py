#!/usr/bin/env python
import os

import numpy
from setuptools import Extension, find_packages, setup

with open("README.md", encoding="utf-8") as readme_file:
    README = readme_file.read()

cwd = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(cwd, "cosyvoice", "VERSION")) as fin:
    version = fin.read().strip()

setup(
    name="cosyvoice-tts",
    version=version,
    description="🍵 Cosyvoice-TTS: A fast TTS architecture with conditional flow matching",
    long_description=README,
    long_description_content_type="text/markdown",
    author="neo",
    author_email="guojingneo1988@gmail.com",
    url="https://github.com/neoguojing/CosyVoice",
    install_requires=[str(r) for r in open(os.path.join(os.path.dirname(__file__), "requirements.txt"))],
    include_dirs=[numpy.get_include()],
    # packages=find_packages(exclude=["tools", "tools/*", "third_party", "third_party/*","docker","docker/*","examples","examples/*"]),
    packages=find_packages(include=["cosyvoice", "cosyvoice.*"]),
    include_package_data=True,
    # use this to customize global commands available in the terminal after installing the package
    # entry_points={
    #     "console_scripts": [
    #         "cosyvoice-tts=webui:",
    #     ]
    # },
    python_requires=">=3.9.0",
)