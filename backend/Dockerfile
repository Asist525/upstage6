# Backend Dockerfile
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libmagic1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install uv for faster dependency management (if used in project)
RUN pip install uv

# Copy dependency files
COPY pyproject.toml uv.lock* ./

# Install dependencies
RUN uv pip install --system -e .

# Copy application code (except what's in .dockerignore)
COPY . .

# Ensure .env is NOT in the image to prevent overriding Docker env vars
RUN rm -f .env

# Create directory for data and uploads
RUN mkdir -p data/uploads

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
