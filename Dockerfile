FROM python:3.10 AS base
ENV LANG C.UTF-8
SHELL ["/bin/bash",  "-o", "pipefail", "-c"]
RUN useradd -ms /bin/bash notroot
USER notroot
ENV PYTHONFAULTHANDLER=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=30 \
  POETRY_VIRTUALENVS_IN_PROJECT=true \
  POETRY_NO_INTERACTION=1 \
  PATH="/home/notroot/app/.venv/bin:/home/notroot/.local/bin:${PATH}"
WORKDIR /home/notroot/app

FROM base AS builder
RUN pip install poetry
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-dev --no-root
COPY ./src ./src

FROM base AS runner
COPY --from=builder /home/notroot/app /home/notroot/app
COPY ./src ./src