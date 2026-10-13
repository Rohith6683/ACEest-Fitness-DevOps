import pytest
from app import app, members


@pytest.fixture
def client():
    members.clear()
    with app.test_client() as test_client:
        yield test_client
    members.clear()


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["application"] == "ACEest Fitness & Gym"


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_list_members_empty(client):
    response = client.get("/members")
    assert response.status_code == 200
    assert response.get_json() == []


def test_add_member(client):
    response = client.post(
        "/members",
        json={"name": "Rohith", "plan": "Monthly"}
    )
    assert response.status_code == 201
    assert response.get_json()["name"] == "Rohith"


def test_reject_invalid_member(client):
    response = client.post(
        "/members",
        json={"name": "", "plan": "Monthly"}
    )
    assert response.status_code == 400


def test_get_missing_member(client):
    response = client.get("/members/999")
    assert response.status_code == 404
