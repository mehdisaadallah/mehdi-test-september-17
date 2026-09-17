#write a test case for the app.py

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_total_revenue(client):
    response = client.get("/total_revenue")
    assert response.status_code == 200
    data = response.get_json()
    assert "total_revenue" in data
    assert isinstance(data["total_revenue for all the regions is the following the following amount"], int)

def test_highest_region(client):
    response = client.get("/highest_region")
    assert response.status_code == 200
    data = response.get_json()
    assert "region" in data
    assert "total_sales" in data
    assert isinstance(data["total_sales"], int)