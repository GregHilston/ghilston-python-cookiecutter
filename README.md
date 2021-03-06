# ghilston-python-cookiecutter

## How To Clone This Repository

One should install [Cookie Cutter](https://cookiecutter.readthedocs.io/en/1.7.3/index.html) and then either clone this repository locally and create a copy of this repo by running:

`$ python3 -m cookiecutter ghilston-python-cookiecutter`

or copy this repo straight from Github by running: 

`$ python3 -m cookiecutter https://github.com/GregHilston/ghilston-python-cookiecutter`

And fill out the interactive form.

## Virtual Environments, Dependency Resolution, Publishing Packages: [`poetry`](https://github.com/python-poetry/poetry)

### Why We Use It

Having used numerous tools in the past to handle dependencies, separate tools to build out a virtual environment and yet more tools to publish a package to say PyPi, I have found Poetry's feature rich approach to be a one-stop shop for a new Python project.

### How To Install Our Dependencies

Poetry is the only dependency listed that we'll install by hand, as `poetry` will install all other dependencies for us.

The [official website](https://python-poetry.org/docs/) suggests one install Poetry by running:

`$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

Once we have poetry installed, we can use it to install our other dependencies by running `$ poetry install`.

### Removing A Package

- When one removes a package from Poetry using `$ poetry remove [package-name]` the package is removed from the `pyproject.toml` but it is not uninstalled from the virtual environment. As described in [this github comment](https://github.com/python-poetry/poetry/issues/648#issuecomment-461149012) one can run `$ poetry shell` followed by `exit` to see where the virtual environment lives, then blow away said virtual environment's directory and then ask Poetry to reinstall all the dependencies using `$ poetry install`. This will resolve in your virtual environment no longer having said removed packaged.

### Upgrading Pip

Using this [Github issue](https://github.com/python-poetry/poetry/issues/1651) as a guide, we can upgrade pip by running

```
$ poetry shell
$ pip install -U pip
```

### References

- [official documentation](https://python-poetry.org/docs/)
- [this talk on why Poetry is an excellent tool](https://www.youtube.com/watch?v=QX_Nhu1zhlg&t=202s)

## Git Hooks

We leverage this [Poetry plugin for githook](https://pypi.org/project/poetry-githooks/) to handle githooks for us, to make them portable and easy to install. By default our githook is a pre-commit, which will ensure all our commits have been checked for formatting, linting, security, and our tests. This is defined in our `pyproject.toml`.

To install or apply changes to one's `[tool.githooks]` simply run:

`$ poetry run githooks setup`

If one didn't want to use Poetry, they could use the [pre-commit](https://pre-commit.com/) Python package and define their pre-commits in a `.pre-commit-config.yaml` file.

## Task Execution Tool: [`invoke`](https://github.com/pyinvoke/invoke)

### Why We Use It

Having used raw bash scripts and also `Makefile`s, I have found Pyinvoke's Python approach to handling task execution to be a much more natural approach. One can easily highlight improvements over the previously mentioned approaches by looking at how Invoke handles accepting command line arguments, providing help text and even just the fact that since its Python code, one has access to all Python packages.

### How To Use It

We generally use this with Poetry, to run commands within our virtual environment. For example, `$ poetry run invoke magic`.

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

## Logging

I've grabbed a common logging configuration from online to act as our default setup.

If we were to use this cookiecutter for a package, we'd want to disable the `FileHandler`, as this can cause difficulty with users leveraging our package.

I may try out the [loguru](https://github.com/Delgan/loguru) library out in the future.

## Docker

Our `docker/Dockerfile` is based off of [this wonderful resource](https://github.com/michael0liver/python-poetry-docker-example) which seems to have come from [this discussion](https://github.com/python-poetry/poetry/discussions/1879)

Our Dockerfile has many layers, each used for specific scenarios. 

## CICD Tool: [Circle CI](https://circleci.com)

_Note: We don't use Circle CI for this `ghilston-python-cookiecutter`, rather we have it configured for the nested project that cookie cutter will clone for us.

### Why We Use It

I previously used [Travis CI](https://travis-ci.org/) until they made some decisions I wasn't a fan of. I've had nothing but a pleasant experience having switched to [Circle CI](https://circleci.com/). I am interested in trying [Github Actions](https://github.com/features/actions), but haven't gotten around to it. Plus this would tie us to Github.

### Configuration

Navigate to the [website](https://circleci.com), log in and click "Set Up Project" next to your existing Github repository.
