def test_transcribe_no_file(client):
    response = client.post("/transcribe", files={})
    assert response.status_code == 422  # FastAPI validation error for missing required field