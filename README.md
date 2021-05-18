# ghilston-python-cookiecutter

## Virtual Environments, Dependency Resolution, Publishing Packages: Poetry

### Why We Use It

Having used numerous tools in the past to handle dependencies, separate tools to build out a virtual environment and yet more tools to publish a package to say PyPi, I have found Poetry's feature rich approach to be a one stop shop for a new Python project.

### Install

The [official website](https://python-poetry.org/docs/) suggests one install Poetry by running:

`$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

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

## Formatting

## Linting

## Security

## Type Checking

## Logging

## Testing

## Packaging

- have a setup.py
- see if poetry helps with this

## CICD

- integration with Circle CI with badge
