from flaskapp import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the API!" in response.data

def test_search_success(client):
    response = client.get('/search?person=John')
    assert response.status_code == 200
    assert response.is_json
    assert response.json == {"id": 1, "name": "John", "age": 25}

def test_search_failure(client):
    response = client.get('/search?person=Mary')
    assert response.status_code == 400
    assert response.is_json
    assert response.json == {"error": "No matching data found."}

def test4():
    response = app.test_client().get("/search?person=Ducanh")
    # assert b'{"error":"No matching data found."}\n' in response.data
    assert response.status_code == 400 


response = app.test_client().get('/search?person=ducanh')
print(response.data)