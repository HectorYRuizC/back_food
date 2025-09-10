from django.db import models
from django.conf import settings
from foods.models import Food

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ratings")
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="ratings")
    rating = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "food")

    def __str__(self): return f"{self.user} -> {self.food}: {self.rating}"
