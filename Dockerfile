# Use slim Python base image
FROM python:3.11-slim

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Set Poetry version
ENV POETRY_VERSION=1.7.1

# Install system dependencies & Poetry
RUN apt-get update && apt-get install -y curl build-essential \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && rm -rf /var/lib/apt/lists/*

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy poetry files first to leverage Docker cache
COPY pyproject.toml poetry.lock* ./

# Configure poetry (no virtualenvs inside container)
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi

# Copy all source code
COPY . .

# Optional: Set environment variables from .env if needed
# ENV VAR=value

# Set default command (update this if you use something like uvicorn)
CMD ["python", "src/main.py"]


