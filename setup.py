from setuptools import setup, find_packages

from src.py2plantuml import __version__

setup(
    name="py2plantuml",
    version=__version__,
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
