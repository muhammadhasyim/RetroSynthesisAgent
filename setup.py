from setuptools import setup, find_packages

setup(
    name="RetroSynAgent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "graphviz>=0.20",
        "networkx>=3.0",
        "pubchempy>=1.0",
        "pyvis>=0.3",
        "loguru>=0.7",
        "openai>=1.0",
        "PyMuPDF>=1.22",
        "scholarly>=1.7",
        "jsonpickle>=3.0",
        "fake-useragent>=1.4",
        "requests>=2.28",
        "python-dotenv>=1.0",
        "beautifulsoup4>=4.12",
    ],
)
