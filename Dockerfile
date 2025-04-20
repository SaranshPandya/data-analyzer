# ---- Base Python Image ----
FROM python:3.11-slim

# ---- System Dependencies ----
RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*

# ---- Install Poetry ----
ENV POETRY_VERSION=1.7.1
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# ---- Set Workdir ----
WORKDIR /app

# ---- Copy project files ----
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# ---- Copy rest of the code ----
COPY . .

# ---- Default command (change as needed) ----
#CMD ["uvicorn", "your_module.main:app", "--host", "0.0.0.0", "--port", "8000"]
