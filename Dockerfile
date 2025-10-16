# Using Python 3.12 slim image
FROM python:3.12-slim

# Setting working directory
WORKDIR /app

# Installing system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Copying requirements for caching
COPY requirements.txt .

# Upgrading pip
RUN pip install --no-cache-dir --upgrade pip

# installing torch cpu version
RUN pip install --no-cache-dir torch torchaudio \
    --index-url https://download.pytorch.org/whl/cpu

# Step 3: Install all other Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Exposing port 8000
EXPOSE 8000

# Defining the command to run your application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]