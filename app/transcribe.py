import os
import tempfile
import whisper
from fastapi import UploadFile

MODEL_NAME = os.getenv("WHISPER_MODEL", "base")
model = whisper.load_model(MODEL_NAME)

def transcribe_audio(file: UploadFile):
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            contents = file.file.read()
            tmp_file.write(contents)
            tmp_path = tmp_file.name
        result = model.transcribe(tmp_path)
        os.remove(tmp_path)

        return {
            "text": result["text"].strip(),
            "language": result.get("language", "unknown")
        }
    except Exception as e:
        return {"error": f"Transcription failed: {str(e)}"}