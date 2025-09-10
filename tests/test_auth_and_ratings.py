import pytest
from django.urls import reverse
from foods.models import Category, Food

@pytest.mark.django_db
def test_jwt_and_protected_endpoints(client, user):
    # login -> token
    resp = client.post(reverse("token_obtain"), {"username": "u1", "password": "pass1234"})
    assert resp.status_code == 200
    token = resp.json()["access"]
    auth = {"HTTP_AUTHORIZATION": f"Bearer {token}"}

    # crear rating (protegido)
    cat = Category.objects.create(name="Cat")
    food = Food.objects.create(title="F1", category=cat)
    r = client.post("/api/ratings/", {"food": food.id, "rating": 5}, **auth)
    assert r.status_code == 201

    # acceder sin token debe fallar
    r2 = client.get("/api/ratings/")
    assert r2.status_code == 401
