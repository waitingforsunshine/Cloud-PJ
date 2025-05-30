from app import app

def test_index():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

if __name__ == '__main__':
    test_index()
    print("Index page returns 200 OK")
