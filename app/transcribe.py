# Importing the necessary libraries
import os
import tempfile
import whisper
from fastapi import UploadFile

# ---------------------- Model Initialization ----------------------
# Default mode is to 'base' model if not set to allow flexible configuration
MODEL_NAME = os.getenv("WHISPER_MODEL", "base")

# Loading the model at the startup to avoid loading on every request, which is expensive.
model = whisper.load_model(MODEL_NAME)

# ---------------------- Audio Transcription Function ----------------------
def transcribe_audio(file: UploadFile):
    try:
        # ---------------------- Save File Temporarily ----------------------
        # NamedTemporaryFile ensures a unique file name and safe cleanup.
        # delete=False ensures to read it again after closing.
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            contents = file.file.read()
            tmp_file.write(contents)
            tmp_path = tmp_file.name
            
         # Whisper model returns a dict containing 'text' and possibly 'language'
        result = model.transcribe(tmp_path)
        
        # Temp file clean up
        os.remove(tmp_path)

        ''' 
        Strip whitespace from transcription text
        Provide 'unknown' if language is not returned by Whisper 
        '''
        return {
            "text": result["text"].strip(),
            "language": result.get("language", "unknown")
        }
    except Exception as e:
         # Return a JSON-compatible error message
        return {"error": f"Transcription failed: {str(e)}"}