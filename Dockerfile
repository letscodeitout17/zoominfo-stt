# Use a slim Python base image to reduce size
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy only requirements 
COPY requirements.txt .

# Install system dependencies + Python dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg curl unzip build-essential && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app
COPY tests/ ./tests

# Expose port (adjust if needed)
EXPOSE 8000

CMD ["python", "app/main.py"]
