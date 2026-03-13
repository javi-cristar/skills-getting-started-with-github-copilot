from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    # Arrange: nothing to set up for this test

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Arrange
    activity = "Chess Club"
    email = "testuser@mergington.edu"

    # Act: Sign up
    resp_signup = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert resp_signup.status_code == 200

    # Act: Unregister
    resp_unreg = client.post(f"/activities/{activity}/unregister?email={email}")

    # Assert
    assert resp_unreg.status_code == 200
