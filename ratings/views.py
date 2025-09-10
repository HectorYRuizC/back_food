from rest_framework import viewsets, permissions
from .models import Rating
from .serializers import RatingSerializer
from core.permissions import IsOwner

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filterset_fields = ["food"]
    ordering_fields = ["timestamp", "rating"]

    def get_queryset(self):
        # Cada usuario ve sus ratings
        return Rating.objects.filter(user=self.request.user).select_related("food")
