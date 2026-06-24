# Use the official python:3.12-slim image as the base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY version_info.py .

# Command to execute when the container starts
CMD ["python", "version_info.py"]
