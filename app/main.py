# Importing the necessary libraries
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.transcribe import transcribe_audio

# Initialize the FastAPI application
app = FastAPI(title="ZoomInfo Speech-to-Text API")

# ---------------------- Health Check Endpoint ----------------------
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# ---------------------- Transcription Endpoint ----------------------
@app.post("/transcribe")
async def transcribe_endpoint(file: UploadFile = File(...)):
    if not file:
        return JSONResponse(status_code=400, content={"error": "No file uploaded"})

    result = transcribe_audio(file)
    return JSONResponse(content=result)