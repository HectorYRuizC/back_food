import pytest
from django.contrib.auth import get_user_model

@pytest.fixture
def user(db):
    User = get_user_model()
    return User.objects.create_user(username="u1", email="u1@test.com", password="pass1234")

@pytest.fixture
def staff(db):
    User = get_user_model()
    return User.objects.create_user(username="staff", email="s@test.com", password="pass1234", is_staff=True)
