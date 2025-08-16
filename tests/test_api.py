from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_healthcheck():
    r = client.get("/")
    assert r.status_code == 200
    assert "Shopify Insights Fetcher" in r.json()["message"]


def test_missing_url():
    r = client.post("/insights", json={})
    assert r.status_code == 400


def test_invalid_url():
    r = client.post("/insights", json={"website_url": "https://notarealshop.com"})
    assert r.status_code in [401, 500]
