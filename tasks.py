from invoke import task


@task
def test(ctx):
    """Runs Pytest test suite."""
    ctx.run("poetry run pytest", echo=True)
