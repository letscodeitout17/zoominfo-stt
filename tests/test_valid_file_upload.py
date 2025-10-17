# Importing the necessary libraries
from unittest.mock import patch, MagicMock
def test_transcribe_success(client, tmp_path):
    """
    Test the /transcribe endpoint for a successful transcription.
    This test uses a dummy audio file and mocks the Whisper model's 
    transcribe method to avoid running actual model inference, ensuring 
    fast and deterministic tests.
    """
    # Create a dummy audio file in a temporary directory
    dummy_audio = tmp_path / "sample.wav"
    dummy_audio.write_bytes(b"fake audio bytes")

    # Define the mocked transcription result
    mock_result = {"text": "Hello world", "language": "en"}
    
    # Patch the Whisper model's transcribe method to return the mock result
    with patch("app.transcribe.model.transcribe", return_value=mock_result):
        # Open the dummy file and make a POST request to /transcribe
        with open(dummy_audio, "rb") as f:
            response = client.post("/transcribe", files={"file": ("sample.wav", f, "audio/wav")})

    # Assert the endpoint returned HTTP 200 OK
    assert response.status_code == 200
    
    # Assert the response JSON contains the expected transcription text
    assert response.json()["text"] == "Hello world"
    
    # Assert the response JSON contains the expected language
    assert response.json()["language"] == "en"