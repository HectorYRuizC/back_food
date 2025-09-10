from foods.models import Category, Ingredient, Food

def test_food_m2m(db):
    c = Category.objects.create(name="Main")
    i = Ingredient.objects.create(name="Tomato")
    f = Food.objects.create(title="Salad", category=c)
    f.ingredients.add(i)
    assert f.ingredients.count() == 1
