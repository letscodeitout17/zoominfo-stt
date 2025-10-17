# Importing the necessary libraries
import os
import pytest
from app.transcribe import transcribe_audio

# Constant: Path to a sample audio file for testing transcription
SAMPLE_AUDIO = os.path.join(os.path.dirname(__file__), "sample.wav")

# ---------------------- Test Functions ----------------------
def test_transcribe_audio_file_exists():
    """Checking that the sample audio file exists."""
    assert os.path.exists(SAMPLE_AUDIO), f"{SAMPLE_AUDIO} not found"


def test_transcribe_audio_runs():
    """
    Testing that the transcribe_audio function executes successfully 
    and returns a non-empty dictionary.
    This test verifies:
        1. The sample audio file exists, otherwise it skips the test
        2. The result is a dictionary
        3. The dictionary contains at least one key-value pair
    """
    if not os.path.exists(SAMPLE_AUDIO):
        pytest.skip("Sample audio file missing")

    result = transcribe_audio(SAMPLE_AUDIO)
    # Check that the result is a dictionary
    assert isinstance(result, dict)
    
    # Check that the dictionary is not empty
    assert len(result) > 0