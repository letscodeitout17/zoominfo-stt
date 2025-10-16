# Use a slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# 1. Install system dependencies with single RUN command and immediate cleanup
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy requirements before installing
COPY requirements.txt .

# Upgrade pip and install CPU-only PyTorch/Torchaudio
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir torch torchaudio \
       --index-url https://download.pytorch.org/whl/cpu \
    && pip install --no-cache-dir -r requirements.txt \
    # Aggressively remove cached files after installation
    && rm -rf /root/.cache/pip

# Copy the rest of your application code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]