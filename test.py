from flaskapp import app

def test1():
    response = app.test_client().get("/")
    assert response.status_code == 200

def test2():
    response = app.test_client().get("/search")
    assert response.status_code == 200 
def test_db():
    response = app.test_client().get("/search")

def test3():
    response = app.test_client().get("/search?person=John")
    assert b'{"age":25,"id":1,"name":"John"}\n' in response.data

def test4():
    response = app.test_client().get("/search?person=Ducanh")


response = app.test_client().get('/search?person=ducanh')
print(response.data)