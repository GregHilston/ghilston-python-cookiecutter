import os

from invoke import task


ROOT_PATH = os.path.dirname(__file__)
SOURCE_DIRECTORY = "app"
SOURCE_PATH = os.path.join(ROOT_PATH, SOURCE_DIRECTORY)
TEST_DIRECTORY = "test"
TEST_PATH = os.path.join(ROOT_PATH, TEST_DIRECTORY)
LOGS_DIRECTORY = "log"
LOGS_PATH = os.path.join(ROOT_PATH, LOGS_DIRECTORY)


@task
def test(ctx):
    """Runs Pytest test suite"""
    ctx.run("poetry run pytest", echo=True)

@task
def coverage(ctx):
    """Produces test coverage"""
    ctx.run("poetry run pytest --cov=app test/", echo=True)
