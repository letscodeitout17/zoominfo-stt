from unittest.mock import patch, MagicMock
def test_transcribe_success(client, tmp_path):
    dummy_audio = tmp_path / "dummy.wav"
    dummy_audio.write_bytes(b"fake audio bytes")

    mock_result = {"text": "Hello world", "language": "en"}
    with patch("app.transcribe.model.transcribe", return_value=mock_result):
        with open(dummy_audio, "rb") as f:
            response = client.post("/transcribe", files={"file": ("dummy.wav", f, "audio/wav")})

    assert response.status_code == 200
    assert response.json()["text"] == "Hello world"
    assert response.json()["language"] == "en"