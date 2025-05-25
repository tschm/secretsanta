from setuptools import setup, find_packages

setup(
    name="pysanta",
    version="0.1.0",
    packages=find_packages(),
    description="A package for Secret Santa functionality",
    author="Secret Santa Team",
    author_email="thomas.schmelzer@gmail.com",
    python_requires=">=3.6",
    install_requires=[
        "marimo>=0.13.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
