# Stage 1: Build Stage
FROM python:3.11-slim AS build-stage

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Stage 2: Production Stage (Smaller final image)
FROM python:3.11-slim AS production-stage

# Set environment variables for production
ENV APP_ENV=production \
    DB_HOST=localhost \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies (including executables) from the build stage to avoid re-installation
COPY --from=build-stage /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build-stage /usr/local/bin /usr/local/bin
COPY --from=build-stage /app /app

# Ensure .env is not included (should also be in .dockerignore for safety)
RUN rm -f .env

# Define a health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:8000/health || exit 1

# Expose the application port
EXPOSE 8000

# Use a non-root user for better security
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
