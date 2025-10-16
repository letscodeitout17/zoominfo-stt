# Using Python 3.12 slim image
FROM python:3.12-slim

# Setting working directory
WORKDIR /app

# Installing system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg curl unzip build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copying requirements for caching
COPY requirements.txt .

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install CPU-only PyTorch and Torchaudio
RUN pip install --no-cache-dir torch==2.9.0 torchaudio==2.9.0 -f https://download.pytorch.org/whl/cpu/torch_stable.html
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]