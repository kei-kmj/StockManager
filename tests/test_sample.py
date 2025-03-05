from fastapi.testclient import TestClient

from app.db.models import User
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/users")

    assert response.status_code == 200


def test_create_user(db):

    user = User(name="test", nickname="yumi", email="<EMAIL>")
    db.add(user)
    db.commit()

    result = db.query(User).filter(User.name == "test").first()
    assert result == user
    assert result.id == 1

    total_users = db.query(User).count()
    assert total_users == 1

