import pytest
from foods.models import Category, Food

@pytest.mark.django_db
def test_list_foods_public(client):
    cat = Category.objects.create(name="Cat")
    Food.objects.create(title="F1", category=cat)
    resp = client.get("/api/foods/items/")
    assert resp.status_code == 200
