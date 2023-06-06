
from fastapi.testclient import TestClient
from schemas.user import userEntity, usersEntity
from config.database import con
from app import app

client = TestClient(app)
data={
    "first_name":"Alexandra",
    "last_name":"Canon",
    "password":"prueba",
    "email": "test_user@example.com",
    "phone":14785236912
}
def test_create_user():
    response = client.post("/usuarios", json=data)
    assert response.status_code == 200
    assert response.json()["email"] == data.get('email')
    
def test_list_users():
    response = client.get("/usuarios")
    assert response.status_code == 200
    assert response.json() == usersEntity(con.local.user.find())
    
    
def test_email():
    url="/usuarios/"+data.get('email')
    response = client.get(url)
    assert response.status_code == 200
    assert response.json()["email"] == data.get('email')