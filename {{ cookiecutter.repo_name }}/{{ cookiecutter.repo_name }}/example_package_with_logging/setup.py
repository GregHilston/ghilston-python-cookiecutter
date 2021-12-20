from setuptools import setup, find_packages

from example_package import __version__

version = __version__

setup(
    name="example_package_with_logging",
    description="Example Python package with logging",
    version=version,
    author_email="Gregory.Hilstoh@gmail.com",
    url="https://github.com/GregHilston/ghilston-python-cookiecutter/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/example_package",
    entry_points={
        # Defines functions that a developer may access. Read more here https://stackoverflow.com/a/782984/1983957
        "console_scripts": [
        ]
    }
)
