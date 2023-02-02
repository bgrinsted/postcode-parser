# docker build -t postcode-parser .

# Use official Python runtime as base image
FROM python:3.9-slim

# Set working directory within container
WORKDIR /app

# Copy repository to container
COPY . .

# Install required dependencies
RUN pip install -r requirements.txt


# Run app when the container starts
CMD ["python", "./main.py"]
