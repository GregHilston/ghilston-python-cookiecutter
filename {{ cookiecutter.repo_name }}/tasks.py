"""Invokes tasks"""

import contextlib
import os

from invoke import task


ROOT_PATH = os.path.dirname(__file__)
PACKAGE_NAME = "sample"
SOURCE_PATH = os.path.join(ROOT_PATH, PACKAGE_NAME)
ENTRYPOINT = "example_project_script.py"
ENTRYPOINT_PATH = os.path.join(ROOT_PATH, ENTRYPOINT)
TEST_DIRECTORY = "tests"
TEST_PATH = os.path.join(ROOT_PATH, TEST_DIRECTORY)
LOGS_DIRECTORY = "log"
LOGS_PATH = os.path.join(ROOT_PATH, LOGS_DIRECTORY)
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
    ctx.run(f"poetry run black . {PACKAGE_NAME} {TEST_DIRECTORY}", echo=True)
    ctx.run(f"poetry run isort . {PACKAGE_NAME} {TEST_DIRECTORY}", echo=True)


@task
def lint(ctx):
    """Lints Python code"""
    ctx.run(f"poetry run flake8 --show-source {ENTRYPOINT_PATH} {PACKAGE_NAME}", echo=True)
    ctx.run(f"poetry run pylint {ENTRYPOINT_PATH} {PACKAGE_NAME}", echo=True)


@task
def test(ctx):
    """Runs Pytest test suite"""
    ctx.run(f"poetry run pytest . {PACKAGE_NAME}", echo=True)


@task
def coverage(ctx):
    """Produces test coverage"""
    ctx.run(f"poetry run pytest --cov=. --cov={PACKAGE_NAME} --cov={TEST_DIRECTORY}", echo=True)


@task
def type_check(ctx):
    """Checks types of our Python source code"""
    ctx.run("poetry run mypy --exclude setup.py", echo=True)


@task
def security(ctx):
    """Performs security checks"""
    ctx.run(f"poetry run bandit -r . {PACKAGE_NAME}", echo=True)
    ctx.run("poetry run safety check --full-report", echo=True)
    ctx.run("dodgy", echo=True)


@task(pre=[format, lint, type_check, test, security])
def magic(ctx):
    """Performs all our checking steps: format, lint, type_check, test, security."""
    pass


@task
def docker_build(ctx):
    """Builds Docker image"""
    # Requires Docker buildkit to be enabled with our environment variable, can read more about that here:
    # https://github.com/moby/buildkit/blob/master/frontend/dockerfile/docs/syntax.md
    ctx.run(
        f"poetry run export DOCKER_BUILDKIT=1 docker build --tag {PACKAGE_NAME} --file {DOCKER_DIRECTORY}/Dockerfile ."
    )


@task
def docker_run(ctx):
    """Builds Docker container"""
    # can read here for why pty=True is required
    # http://www.pyinvoke.org/faq.html#why-is-my-command-behaving-differently-under-invoke-versus-being-run-by-hand
    ctx.run(f"docker run -it {PACKAGE_NAME} /docker-entrypoint.sh python {ENTRYPOINT}", pty=True)


@task
def circle_ci_test(ctx):
    """Runs Pytest test suite for Circle CI, saving our output as Junit XML style for ease of parsing"""
    ctx.run(f"mkdir {CIRCLE_CI_TEST_OUTPUT_DIRECTORY}")
    ctx.run(f"poetry run pytest --junitxml={CIRCLE_CI_TEST_OUTPUT_DIRECTORY}/junit.xml", echo=True)


@task
def circle_ci_security(ctx):
    """Performs security checks for Circle CI, ignoring an out of date Pip binary"""
    ctx.run(f"poetry run bandit -r {PACKAGE_NAME}", echo=True)
    ctx.run("poetry run safety check --full-report --ignore 40291", echo=True)
    ctx.run("dodgy", echo=True)
