def test_transcribe_no_file(client):
    response = client.post("/transcribe", files={})
    assert response.status_code == 400
    assert "No file uploaded" in response.text