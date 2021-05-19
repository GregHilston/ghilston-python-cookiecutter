# ghilston-python-cookiecutter

## Virtual Environments, Dependency Resolution, Publishing Packages: Poetry

### Why We Use It

Having used numerous tools in the past to handle dependencies, separate tools to build out a virtual environment and yet more tools to publish a package to say PyPi, I have found Poetry's feature rich approach to be a one stop shop for a new Python project.

### Install

The [official website](https://python-poetry.org/docs/) suggests one install Poetry by running:

`$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

### Removing A Package

- When one removes a package from Poetry using `$ poetry remove [package-name]` the package is removed from the `pyproject.toml` but it is not uninstalled from the virtuale environment. As described in [this github comment](https://github.com/python-poetry/poetry/issues/648#issuecomment-461149012) one can run `$ poetry shell` followed by `exit` to see where the virtual environment lives, then blow away said virtual environment's directory and then ask Poetry to reinstall all the dependencies using `$ poetry install`. This will resolve in your virtual environment no longer having said removed packaged.

### Upgrading Pip

Using this [Github issue]() as a guide, we can upgrade pip by running

```
$ poetry shell
$ pip install -U pip
```

### References

- [official documentation](https://python-poetry.org/docs/)
- [this talk on why Poetry is an excellent tool](https://www.youtube.com/watch?v=QX_Nhu1zhlg&t=202s)

## Task Execution Tool: Invoke

### Why We Use It

Having used raw bash scripts and also `Makefile`s, I have found Invoke's Python approach to handling task execution to be a much more natural approach. One can easily highlight improvements over the previously mentioned approaches by looking at how Invoke handles accepting command line arguments, providing help text and even just the fact that since its Python code, one has access to all Python packages.

### References

- [this excellent blog post walking through a project from start to finish](https://interrupt.memfault.com/blog/building-a-cli-for-firmware-projects#why-invoke-and-python)
- [official documentation](http://www.pyinvoke.org/)
- [getting started guide](http://docs.pyinvoke.org/en/0.23.0/getting_started.html)

## Formatting Tools: Black and Isort

### Why We Use It

Black is a wonderful formatting tool that takes a "little to no configuration approach" which wil ensure that most Python code will look the same. In addition to Black, we leverage Isort to sort our imports automatically.

## Linting Tools: Flake8 and Pylint

### Why We Use It

TODO

## Security Tools: Bandit, Safety and Dodgy

### Why We Use it 

TODO

## Type Checking Tool: Mypy

### Why We Use it

TODO

## Testing Tool: Pytest

### Why We Use It

TODO

## Logging



## CICD

- integration with Circle CI with badge
