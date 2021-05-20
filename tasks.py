"""Invokes tasks"""

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
DOCKER_DIRECTORY = "docker"


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
def docs(ctx):
    """Generates documentation"""
    ctx.run(f"poetry run mypy {SOURCE_DIRECTORY}", echo=True)


@task(pre=[format, lint, type_check, security])
def magic(ctx):
    """Foo"""
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
