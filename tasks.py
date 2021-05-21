"""Invokes tasks"""

import contextlib
import os

from invoke import task


ROOT_PATH = os.path.dirname(__file__)
PROJECT_NAME = "ghilston-python-cookiecutter"
SOURCE_DIRECTORY = PROJECT_NAME.replace('-', '_')
SOURCE_PATH = os.path.join(ROOT_PATH, SOURCE_DIRECTORY)
ENTRYPOINT = "foo.py"
ENTRYPOINT_PATH = os.path.join(ROOT_PATH, ENTRYPOINT)
TEST_DIRECTORY = "tests"
TEST_PATH = os.path.join(ROOT_PATH, TEST_DIRECTORY)
LOGS_DIRECTORY = "log"
LOGS_PATH = os.path.join(ROOT_PATH, LOGS_DIRECTORY)
SPHINX_DOCS_DIRECTORY = "./docs"
# Relative to `./docs` directory
SPHINX_SOURCE_DIRECTORY = "."
SPHINX_OUTPUT_DIRECTORY = "_build"
DOCKER_DIRECTORY = "docker"
CIRCLE_CI_TEST_OUTPUT_DIRECTORY = "test-results"


@contextlib.contextmanager
def chdir(dirname=None):
    """Changes directory

    From: https://github.com/pyinvoke/invoke/issues/225#issuecomment-87240655
    """
    curdir = os.getcwd()
    try:
        if dirname is not None:
            os.chdir(dirname)
        yield
    finally:
        os.chdir(curdir)


@task
def run(ctx):
    """Runs the application"""
    ctx.run(f"poetry run python3 {ENTRYPOINT_PATH}", echo=True)


@task
def format(ctx):
    """Formats Python code"""
    ctx.run(f"poetry run black {SOURCE_DIRECTORY} {TEST_DIRECTORY}", echo=True)
    ctx.run(f"poetry run isort {SOURCE_DIRECTORY} {TEST_DIRECTORY}", echo=True)


@task
def lint(ctx):
    """Lints Python code"""
    ctx.run(f"poetry run flake8 --show-source {SOURCE_DIRECTORY} {TEST_DIRECTORY}", echo=True)
    ctx.run(f"poetry run pylint {SOURCE_DIRECTORY} {TEST_DIRECTORY}", echo=True)


@task
def test(ctx):
    """Runs Pytest test suite"""
    ctx.run("poetry run pytest", echo=True)


@task
def coverage(ctx):
    """Produces test coverage"""
    ctx.run(f"poetry run pytest --cov={SOURCE_DIRECTORY} {TEST_DIRECTORY}", echo=True)


@task
def type_check(ctx):
    """Checks types of our Python source code"""
    ctx.run(f"poetry run mypy {SOURCE_DIRECTORY}", echo=True)


@task
def security(ctx):
    """Performs security checks"""
    ctx.run(f"poetry run bandit -r {SOURCE_DIRECTORY}", echo=True)
    ctx.run(f"poetry run safety check --full-report", echo=True)
    ctx.run(f"dodgy", echo=True)


@task
def clean_docs(ctx):
    """Cleans documentation"""
    # Makefile equivalent is inside the ./docs folder we'd run
    # `$ make clean` which runs `$ sphinx-build -M clean "." "_build"`
    with chdir("./docs"):
        ctx.run(f"poetry run sphinx-build -M clean '{SPHINX_SOURCE_DIRECTORY}' '{SPHINX_OUTPUT_DIR}'", echo=True)


@task
def build_docs(ctx):
    """Generates documentation"""
    # Makefile equivalent is inside the ./docs folder we'd run
    # `$ sphinx-apidoc -o . ..`
    # `$ make html` which runs `$ sphinx-build -M html "." "_build"`
    with chdir("./docs"):
        ctx.run(f"poetry run sphinx-apidoc -o {SPHINX_SOURCE_DIRECTORY} ..", echo=True)
        ctx.run(f"poetry run sphinx-build -M html {SPHINX_SOURCE_DIRECTORY} {SPHINX_OUTPUT_DIRECTORY}", echo=True)
        print(f"To view built docs see {SPHINX_DOCS_DIRECTORY}/{SPHINX_OUTPUT_DIRECTORY}/html/index.html")


@task(pre=[format, lint, type_check, test, security])
def magic(ctx):
    """Performs all our checking steps: format, lint, type_check, test, security."""
    # only uses pre
    pass


@task
def docker_build(ctx):
    """Builds Docker image"""
    ctx.run(f"poetry run docker build --tag {PROJECT_NAME} --file {DOCKER_DIRECTORY}/Dockerfile .")


@task
def docker_run(ctx):
    """Builds Docker container"""
    # can read here for why pty=True is required
    # http://www.pyinvoke.org/faq.html#why-is-my-command-behaving-differently-under-invoke-versus-being-run-by-hand
    ctx.run(f"docker run -it ghilston-python-cookiecutter poetry run invoke run", pty=True)


@task
def circle_ci_test(ctx):
    """Runs Pytest test suite for Circle CI, saving our output as Junit XML style for ease of parsing"""
    ctx.run(f"os.mkdir({CIRCLE_CI_TEST_OUTPUT_DIRECTORY})")
    ctx.run(f"poetry run pytest --junitxml={CIRCLE_CI_TEST_OUTPUT_DIRECTORY}/junit.xml", echo=True)


@task
def circle_ci_security(ctx):
    """Performs security checks for Circle CI, ignoring an out of date Pip binary"""
    ctx.run(f"poetry run bandit -r {SOURCE_DIRECTORY}", echo=True)
    ctx.run(f"poetry run safety check --full-report --ignore 40291", echo=True)
    ctx.run(f"dodgy", echo=True)
