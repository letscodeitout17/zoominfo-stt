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
Access the **Swagger UI** at [http://localhost:8000/docs](http://localhost:8000/docs)
Health check endpoint: [http://localhost:8000/health](http://localhost:8000/health)
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
The API will be accessible at [http://localhost:8000](http://localhost:8000)
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

This README covers: prerequisites, local setup, Docker deployment, API usage, and testing.
