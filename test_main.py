from fastapi import FastAPI
from testapi.testclient import TestClient
from main import app



client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API.  Call/Search or /wiki"}