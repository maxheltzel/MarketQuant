from setuptools import setup, find_packages

setup(
    name="marketquant",
    version="0.4.5",
    author="Max Heltzel",
    author_email="maxheltzel6@gmail.com",
    description="A quantitative market analysis tool builder library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/maxheltzel/MarketQuant",
    project_urls={
        "Documentation": "https://market-quant.gitbook.io/home/",
        "Source Code": "https://github.com/maxheltzel/MarketQuant",
        "Issue Tracker": "https://github.com/maxheltzel/MarketQuant/issues",
        "Personal Website": "https://maxheltzel.net"
    },
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "mplfinance",
        "mplcursors",
        "yfinance",
        "numpy",
        "websockets",
        "requests",
        "python-dotenv",
        "scipy",
        "plotly",
        "hurst",
        "joblib",
        "json"

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
    ],
    python_requires=">=3.6",
    license="MPL-2.0",
)
