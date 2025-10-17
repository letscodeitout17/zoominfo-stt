# Importing the necessary libraries
from fastapi.testclient import TestClient
from app.main import app

# ---------------------- Test Functions ----------------------
# Test the /health endpoint of the FastAPI application. This endpoint is expected to return a simple JSON indicating the service status.
def test_health_check():
    client = TestClient(app)
    
    # Send a GET request to the /health endpoint
    response = client.get("/health")
    
    # Assert that the response body on the status code 200
    assert response.status_code == 200
    
    # Assert that the response body contains the expected JSON
    assert response.json() == {"status": "ok"}