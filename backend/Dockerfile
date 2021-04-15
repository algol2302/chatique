# pull official base image
FROM python:3.9.3-slim-buster

# set working directory
WORKDIR /code/

ARG ENVIRONMENT

# set environment variables
ENV ENVIRONMENT=${ENVIRONMENT} \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  # poetry:
  POETRY_VERSION=1.1.5 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  PATH="$PATH:/root/.poetry/bin"

# install system dependencies
RUN apt-get update \
  && apt-get install --no-install-recommends -y netcat gcc curl \
  # Installing `poetry` package manager:
  # https://github.com/python-poetry/poetry
  && curl -sSL 'https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py' | python \
  && poetry --version \
  # Cleaning cache:
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Copy only requirements, to cache them in docker layer
COPY ./poetry.lock ./pyproject.toml /code/

# Project initialization:
RUN poetry install \
  $(if [ "$ENVIRONMENT" = 'prod' ]; then echo '--no-dev'; fi) \
  --no-interaction --no-ansi \
  # Cleaning poetry installation's cache for production:
  && if [ "$ENVIRONMENT" = 'prod' ]; then rm -rf "$POETRY_CACHE_DIR"; fi

# add app
COPY ./app /code
ENV PYTHONPATH=/code/app
