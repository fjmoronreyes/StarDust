# Dockerfile for StarDust
# Base image with Python
FROM python:3.11-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies (kept minimal on purpose)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy source code
COPY src/ ./src/
COPY README.md LICENSE ./

# Install StarDust in editable mode (future-proof)
# pyproject.toml will come back later
# RUN pip install -e .

# Default command (overridden in CI or compose)
CMD ["python", "-c", "print('StarDust container ready')"]
