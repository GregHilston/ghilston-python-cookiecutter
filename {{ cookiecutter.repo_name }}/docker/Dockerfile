# from https://github.com/python-poetry/poetry/discussions/1879#discussioncomment-216865

# `python-base` sets up all our shared environment variables
FROM python:3.9.9-slim-buster as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


# builder-base is used to build dependencies
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential

# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
ENV POETRY_VERSION=1.1.12
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# We copy our Python requirements here to cache them
# and install only runtime deps using poetry
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./
RUN --mount=type=cache,target=/home/.cache/pypoetry/cache \
    --mount=type=cache,target=/home/.cache/pypoetry/artifacts
RUN poetry install --no-dev


# 'development' stage installs all dev deps and can be used to develop code.
# For example using docker-compose to mount local volume under /app
FROM python-base as development

# Copying poetry and venv into image
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# Copying in our entrypoint
COPY ./docker/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# venv already has runtime deps installed we get a quicker install
WORKDIR $PYSETUP_PATH
RUN poetry install

WORKDIR /app
COPY . .

ENTRYPOINT /docker-entrypoint.sh $0 $@
CMD ["poetry", "run", "invoke", "run"]


# 'lint' stage runs black and isort
# running in check mode means build will fail if any linting errors occur
FROM development AS lint
RUN poetry run invoke lint
CMD ["tail", "-f", "/dev/null"]


# 'test' stage runs our unit tests with pytest and
# coverage.  Build will fail if test coverage is under 95%
FROM development AS test
RUN poetry run invoke test
CMD ["tail", "-f", "/dev/null"]


# 'production' stage uses the clean 'python-base' stage and copies
# in only our runtime deps that were installed in the 'builder-base'
FROM python-base as production

COPY --from=builder-base $VENV_PATH $VENV_PATH

COPY ./docker/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

COPY ./{{ cookiecutter.repo_name }} /app/{{ cookiecutter.repo_name }}
COPY ./foo.py /app/foo.py
WORKDIR /app

ENTRYPOINT /docker-entrypoint.sh $0 $@
