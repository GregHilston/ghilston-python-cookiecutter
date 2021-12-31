# {{ cookiecutter.repo_name }}

## Cookie Cutter

This project is based off of [this cookie cutter](https://github.com/GregHilston/ghilston-python-cookiecutter)

## Getting Started

### Installing Poetry Dependencies

Assuming you have Poetry installed, simply run `$ poetry install`

### Installing Git Hooks

Our `pyproject.toml` defines a pre-commit Git Hook, which can be used to clean up and inspect your Python code. To install this first make this directory a Git repository:

`$ git init`

Then run `$ poetry run githooks setup`