import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py4Soundex",
    version="0.0.1",
    author="Mgs. M. Luthfi Ramadhan",
    author_email="luthfir96@gmail.com",
    description="Soundex Python Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luthfi118/py4Soundex",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)
