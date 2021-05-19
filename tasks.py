import os

from invoke import task


ROOT_PATH = os.path.dirname(__file__)
SOURCE_DIRECTORY = "app"
SOURCE_PATH = os.path.join(ROOT_PATH, SOURCE_DIRECTORY)
TEST_DIRECTORY = "tests"
TEST_PATH = os.path.join(ROOT_PATH, TEST_DIRECTORY)
LOGS_DIRECTORY = "log"
LOGS_PATH = os.path.join(ROOT_PATH, LOGS_DIRECTORY)


@task
def format(ctx):
    """Formats Python code"""
    ctx.run(f"poetry run black --line-length 100 {SOURCE_DIRECTORY} {TEST_DIRECTORY}", echo=True)
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
    ctx.run("poetry run pytest --cov=app test/", echo=True)


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
