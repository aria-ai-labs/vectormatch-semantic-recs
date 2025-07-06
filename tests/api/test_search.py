from fastapi.testclient import TestClient
from main import app

def test_search():
    c = TestClient(app)
    r = c.post("/v1/search", json={"text": "anxiety therapy near me"})
    assert r.status_code == 200
    assert "results" in r.json()