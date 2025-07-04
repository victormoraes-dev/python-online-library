from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_author_successfully():

    payload = {
        "name": "Victor",
        "email": "victor@email.com",
        "description": "Autor dedicado à escrita."
    }

    response = client.post("/authors/", json=payload)
    assert response.status_code == 201
    assert response.json()["error_message"] is None 
    assert response.json()["data"]['message'] == "Author created successfully" 

def test_invalid_email():
    
    payload = {
        "name": "Victor",
        "email": "invalid_email",
        "description": "Autor dedicado à escrita."
    }
    
    response = client.post("/authors/", json=payload)
    assert response.status_code == 422
    assert "data" not in response.json()
    assert response.json()["error_message"]["message"] == "value is not a valid email address: An email address must have an @-sign."

def test_missing_name_should_fail():
    payload = {
        "email": "victor@email.com",
        "description": "Valid description"
    }

    response = client.post("/authors/", json=payload)
    assert response.status_code == 422
    assert "data" not in response.json()    
    assert response.json()["error_message"]["message"] == "Field required"

def test_description_too_long_should_fail():
    
    payload = {
        "name": "Victor",
        "email": "victor@email.com",
        "description": "x" * 401
    }

    response = client.post("/authors/", json=payload)
    assert response.status_code == 422
    assert "data" not in response.json()
    assert response.json()["error_message"]["message"] == "String should have at most 400 characters"


def test_missing_email_should_fail():
    
    payload = {
        "name": "Victor",
        "description": "Valid description"
    }

    response = client.post("/authors/", json=payload)
    assert response.status_code == 422
    assert "data" not in response.json()
    assert response.json()["error_message"]["message"] == "Field required"