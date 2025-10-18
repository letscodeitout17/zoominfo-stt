## ZoomInfo Speech-to-Text API

A FastAPI-based Speech-to-Text service leveraging openAI Whisper for transcribing audio files. It supports local development, Docker deployment, and ready-to-use API endpoints.

## Table of Contents

1. Prerequisites
2. Setup & Run Locally
3. Docker Deployment
4. API Usage
5. Testing 
---

## Prerequisites

Before running the project, please ensure the following are installed:

* Python 3.12 or above
* pip
* Virtual environment support ('venv')
* Docker for containerized deployment
* Git (to clone the repository)
* ffmpeg installed (required by Whisper)

---

## Setup & Run Locally

1. Clone the repository:

```bash
git clone git@github.com:letscodeitout17/zoominfo-stt.git
cd zoominfo-stt
```
2. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate 
```

3. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Run the API:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
- Access the Swagger UI at [http://localhost:8000/docs](http://13.60.21.218:8000/docs)

- Health check endpoint: [http://localhost:8000/health](http://13.60.21.218:8000/health)
---

## Docker Deployment

1. Build the Docker image:

```bash
docker build -t zoominfo-stt-repo-img .
```

2. Run the Docker container:

```bash
docker run -d -p 8000:8000 zoominfo-stt-repo-img
```
The API will be accessible at http://localhost:8000
---

## API Usage

1. Health Check

```bash
curl http://localhost:8000/health
```

Response:

```json
{
  "status": "ok"
}
```

2. Transcribe Audio

```bash
curl -X POST "http://localhost:8000/transcribe" \
  -F "file=@sample.wav"
```

Response:

```json
{
  "text": "Transcribed audio text",
  "language": "en"
}
```
---

## Testing

Run all tests using pytest:

```bash
pytest tests/
```

* Architecture Overview **

The ZoomInfo Speech-to-Text (STT) API is a lightweight FastAPI-based microservice that accepts audio files, processes them through OpenAI's Whisper model, and returns transcribed text along with detected language. The architecture is modular, testable, and cloud-ready for deployment on platforms like GitHub Actions or AWS Lambda. The system consists of three main layers:

**API Layer (main.py)**: This layer defines REST endpoints for health check and transcription.

**Service Layer (transcribe.py)**: This layer handles audio file processing, temporary file management, and calls the Whisper model.

**Tests (tests/)**: A pytest-based suite that validates API behavior, error handling, and integration between FastAPI and Whisper components.

- **Environment Variables**
 One can specify a Whisper model (default is "base"):

**Deployment Steps**
**GitHub Actions (CI/CD)**-
The repository already includes workflow support for automated testing and deployment.
If deploying manually on a server:

# On own EC2 server
ssh -i <path to the key>.pem ubuntu@13.60.21.218 

# Start the API
nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 &

If deploying via Docker:

sudo apt update
sudo apt install -y docker.io net-tools # net-tools is for netstat diagnostics
sudo usermod -aG docker ubuntu        

# Safely stop and remove container by name
sudo docker stop your-app-name 2>/dev/null || true
sudo docker rm your-app-name 2>/dev/null || true

# Run Docker container
IMAGE_TAG="ghcr.io/<the_username>/<the_image>:latest"

sudo docker run -d \
    --network host \
    --name your-app-name \
    -e HOST=0.0.0.0 \
    -e PORT=8000 \
    $IMAGE_TAG

**Example Usage**
- Health Check
curl -X GET http://13.60.21.218:8000/health
Expected Output:
{"status": "ok"}

-**Transcription Example**

Assuming you have an audio file named sample.wav:

curl -X POST "http://13.60.21.218:8000/transcribe" \
  -F "file=@sample.wav"
Example Response:

{
  "text": "Hello, welcome to ZoomInfo speech-to-text demo.",
  "language": "en"
}

💡 Notes on Trade-offs and Next Steps

**Trade-offs**

- Using Whisper locally offers flexibility but increases model load time and memory usage.
- Model is synchronous; for large files, async streaming could improve performance.
- No persistent storage — each file is processed temporarily and deleted.

**Future improvements**

- Add async streaming transcription for long audio inputs.
- Enable cloud model hosting to reduce inference latency.
- Expand test coverage to include integration and edge-case scenarios.

This README covers: prerequisites, local setup, Docker deployment, API usage, and testing.
