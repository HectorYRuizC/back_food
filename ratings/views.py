from rest_framework import viewsets, permissions
from .models import Rating
from .serializers import RatingSerializer
from core.permissions import IsOwner
from foods.models import Food
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def rate_food(request):
    user = request.user
    food_id = request.data.get("id")
    rating_value = request.data.get("rating")

    if not food_id or rating_value is None:
        return Response({"error": "Missing food ID or rating"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        food = Food.objects.get(id=food_id)
    except Food.DoesNotExist:
        return Response({"error": "Food not found"}, status=status.HTTP_404_NOT_FOUND)

    rating_obj, created = Rating.objects.update_or_create(
        user=user,
        food=food,
        defaults={"rating": rating_value}
    )

    message = "Rating saved successfully." if created else "Rating updated successfully."
    return Response({"success": True, "message": message}, status=status.HTTP_200_OK)

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filterset_fields = ["food"]
    ordering_fields = ["timestamp", "rating"]

    def get_queryset(self):
        # Cada usuario ve sus ratings
        return Rating.objects.filter(user=self.request.user).select_related("food")
