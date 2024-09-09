from setuptools import setup, find_packages

setup(
    name="MarketQuant",
    version="0.2.1",
    author="Max Heltzel",
    author_email="maxheltzel6@gmail.com",
    description="A quantitative market analysis tool builder library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/maxheltzel/MarketQuant",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "mplfinance",
        "mplcursors",
        "yfinance",
        "numpy"

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MPL-2.0",
)
