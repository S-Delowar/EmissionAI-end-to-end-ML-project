# # ./mlflow/Dockerfile
# FROM ghcr.io/mlflow/mlflow:v2.20.2

# USER root

# # Create a non-root user (`mlflow_user` is new user-name)
# RUN adduser --disabled-password --gecos "" mlflow_user

# # Install psycopg2-binary
# RUN pip install --no-cache-dir --upgrade pip && \
#     pip install --no-cache-dir psycopg2-binary

# # Switch to the new non-root user
# USER mlflow_user



# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install MLflow and other dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir mlflow psycopg2-binary

# Expose the port MLflow runs on
EXPOSE 5000

# Command to run MLflow server
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000"]