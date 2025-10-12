#dockerfile

FROM python:3.12.8

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl libsnappy-dev make gcc g++ libc6-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv and add to PATH in the same layer
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    export PATH="/root/.local/bin:$PATH" && \
    uv --version

ENV PATH="/root/.local/bin:$PATH"

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
#RUN uv pip install --system
RUN uv sync --frozen --no-dev

# Copy application code
COPY . . 

EXPOSE 8090

CMD ["uv", "run", "uvicorn", "lab1.app:app", "--host", "0.0.0.0", "--port", "8090"]