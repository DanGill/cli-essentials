import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scprint",
    version="1.1.0b0",
    author="Daniel Gill",
    author_email="DanG_@outlook.com",
    description="Simple Colored Print",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanGill/scprint",
    py_modules=["scprint", "colors"],
    packages=setuptools.find_packages(),
    keywords="simple color colour colored coloured print",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='~=3.3',
    license="MIT",
)
