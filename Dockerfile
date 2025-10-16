# Using Python 3.12 slim image
FROM python:3.12-slim

# Setting working directory
WORKDIR /app

# Installing system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ffmpeg \
        curl \
        unzip \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copying requirements for caching
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]