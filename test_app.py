# test_hello_add.py
from app import app

def test_hello():
    response = app.test_client().get('/hello')
    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>'
    
def test_hello_with_accept_header():
    response = app.test_client().get('/hello', headers={'accept': 'application/json'})
    print(response)
    assert response.status_code == 200
    response.json["message"]=='Hello, World'
   