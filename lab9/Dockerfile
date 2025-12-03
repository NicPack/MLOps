FROM python:3.13.1-slim-bookworm AS build

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl libsnappy-dev make gcc g++ libc6-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    export PATH="/root/.local/bin:$PATH" && \
    uv --version

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

FROM python:3.13.1-slim-bookworm AS runtime

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libsnappy-dev \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build /root/.local/bin/uv /usr/local/bin/uv 

COPY --from=build /app/.venv /app/.venv

ENV PATH="/app/.venv/bin:$PATH"

COPY . .

EXPOSE 8000

CMD [ "uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port","8000"]