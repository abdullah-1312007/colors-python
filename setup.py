from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="colorspy",
    version="0.1",
    description="All main RGB color values for easy access",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abdullah-1312007/colors-python",
    author="abdullah-1312007",
    author_email="tcs270804@gmail.com",
    license="MIT",
    packages=["colorspy"],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
