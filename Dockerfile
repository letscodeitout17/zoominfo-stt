FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg curl unzip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire app
COPY . .

# Expose port
EXPOSE 8000

# Run the app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]