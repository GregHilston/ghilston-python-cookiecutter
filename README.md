# ghilston-python-cookiecutter

## Virtual Environments, Dependency Resolution, Publishing Packages: [`poetry`](https://github.com/python-poetry/poetry)

### Why We Use It

Having used numerous tools in the past to handle dependencies, separate tools to build out a virtual environment and yet more tools to publish a package to say PyPi, I have found Poetry's feature rich approach to be a one stop shop for a new Python project.

### How To Install

This is the only dependency listed that we'll install by hand, as `poetry` will install all other dependencies for us.

The [official website](https://python-poetry.org/docs/) suggests one install Poetry by running:

`$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`


### Plugin For Githooks: [`poetry-githooks`](https://pypi.org/project/poetry-githooks/)

We leverage this plugin to handle githooks for us, to make them portable and easy to install. By default our githook is a pre-commit, which will ensure all our commits have been checked for formatting, linting, security, and our tests.

To install or apply changes to one's `[tool.githooks]` simply run:

`$ poetry run githooks setup`

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

## Task Execution Tool: [`invoke`](https://github.com/pyinvoke/invoke)

### Why We Use It

Having used raw bash scripts and also `Makefile`s, I have found Invoke's Python approach to handling task execution to be a much more natural approach. One can easily highlight improvements over the previously mentioned approaches by looking at how Invoke handles accepting command line arguments, providing help text and even just the fact that since its Python code, one has access to all Python packages.

### References

- [this excellent blog post walking through a project from start to finish](https://interrupt.memfault.com/blog/building-a-cli-for-firmware-projects#why-invoke-and-python)
- [official documentation](http://www.pyinvoke.org/)
- [getting started guide](http://docs.pyinvoke.org/en/0.23.0/getting_started.html)

## Formatting Tools: [`black`](https://github.com/psf/black) and [`isort`](https://github.com/PyCQA/isort)

### Why We Use Them

Black is a wonderful formatting tool that takes a "little to no configuration approach" which wil ensure that most Python code will look the same. In addition to Black, we leverage Isort to sort our imports automatically.

## Linting Tools: [`flake8`](https://github.com/PyCQA/flake8) and [`pylint`](https://github.com/PyCQA/pylint)

### Why We Use Them

We leverage both of these tools as both cover some aspects that the other does not.

## Security Tools: [`bandit`](https://github.com/PyCQA/bandit), [`safety`](https://github.com/pyupio/safety), and [`dodgy`](https://github.com/landscapeio/dodgy)

### Why We Use Them

This suite of tools will check of common security mistakes and even check against a database of known versions of compromised packages.

## Type Checking Tool: [`mypy`](https://github.com/python/mypy)

### Why We Use It

This is one of my favorite packages for Python, it allows us to check the types of our classes, method and functions and get warnings if we're calling code with incorrect types.

## Testing Tool: [`pytest`](https://github.com/pytest-dev/pytest)

### Why We Use It

While there are many alternatives, such as `unittest` and `nose`, I've found `pytest`'s syntax to be easy to use and unobstrusive.

## Documentation Tools: [`sphinx`](https://github.com/sphinx-doc/sphinx) and [read the docs](https://readthedocs.org/)

### Why We use Them

We use this to ensure that all the wonder docstrings we are writing are parsed and create a much more human readable HTML experience.

### Configuration

Navigate to the [website](https://readthedocs.org/), login and go to the dashboard and "Import a Project"

## Logging

I've grabbed a common logging configuration from online to act as our default setup.

If we were to use this cookiecutter for a package, we'd want to disable the `FileHandler`, as this can cause difficulty with users leveraging our package.

## Docker

Our `docker/Dockerfile` is based off of [this wonderful resource](https://github.com/michael0liver/python-poetry-docker-example) which seems to have come from [this discussion](https://github.com/python-poetry/poetry/discussions/1879)

## CICD Tool: [Circle CI](https://circleci.com)

### Configuration

Navigate to the [website](https://circleci.com), log in and click "Set Up Project" next to your existing Github repository.
