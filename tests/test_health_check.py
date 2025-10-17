# test_healthcheck.py
import pytest
from httpx import AsyncClient
from app.main import health_check  

@pytest.mark.asyncio
async def test_root_endpoint():
    async with AsyncClient(app=health_check, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "OK" in response.text