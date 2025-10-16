import os
import pytest
from app.transcribe import transcribe_audio

SAMPLE_AUDIO = os.path.join(os.path.dirname(__file__), "sample.wav")

def test_transcribe_audio_file_exists():
    """Check that the sample audio file exists."""
    assert os.path.exists(SAMPLE_AUDIO), f"{SAMPLE_AUDIO} not found"

def test_transcribe_audio_runs():
    """Check that transcribe_audio runs and returns a string."""

    if not os.path.exists(SAMPLE_AUDIO):
        pytest.skip("Sample audio file missing")

    result = transcribe_audio(SAMPLE_AUDIO)
    assert isinstance(result, str)
    assert len(result) > 0