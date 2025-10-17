# Importing the necessary libraries
import sys
import os

# Add the parent directory to sys.path to allow importing 'app' module
# This is necessary when running tests from a subdirectory.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------------------- Test Framework Imports ----------------------
import pytest
from fastapi.testclient import TestClient
from app.main import app


# ---------------------- Test Fixtures ----------------------
@pytest.fixture
def client():
    """
    Pytest fixture to provide a reusable FastAPI test client.
    Returns:
        TestClient: A client that can be used to make HTTP requests
                    to the FastAPI app during tests.
    """
    return TestClient(app)