from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name="vario",
    version="0.1",
    packages=find_packages(),
    py_modules=["vario.main"],

    # It would be annoying to duplicate requirements.txt here
    # install_requires=parse_requirements('requirements.txt', session='hack'),

    # Package metadata for PyPi
    author="Simon Cooksey, Jonathan Poole",
    author_email="sjc205@kent.ac.uk",
    description="Produce videos of instruments for overlaying in flight videos",
    license="MIT",

    entry_points = {
        'console_scripts': ['vario=vario.main:main']
    }
)
