from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Avg
from foods.models import Food
from .models import RecommendationSession, SessionItem
from .serializers import RecommendationSessionSerializer
from core.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommendation_packs(request):
    """Return all recommendation sessions for the current user,
    where each session includes an array of foods with their predicted ratings."""
    sessions = RecommendationSession.objects.filter(user=request.user).prefetch_related("items__food")

    result = []
    for session in sessions:
        foods = [
            {
                "title": item.food.title,
                "predicted_rating": item.predicted_rating
            }
            for item in session.items.all()# type: ignore[attr-defined]
        ]
        result.append({
            "id": session.id,# type: ignore[attr-defined]
            "created_at": session.created_at.strftime("%d/%m/%Y"),
            "foods": foods
        })

    return Response(result)


class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = RecommendationSessionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    ordering_fields = ["created_at"]

    def get_queryset(self):
        qs = RecommendationSession.objects.all().prefetch_related("items__food")
        if self.request.user.is_superuser: # type: ignore[attr-defined]
            return qs
        return qs.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_destroy(self, instance):
        self.check_object_permissions(self.request, instance)
        return super().perform_destroy(instance)

    @action(detail=True, methods=["post"], url_path="generate")
    def generate_recommendations(self, request, pk=None):
        """
        Genera recomendaciones para esta sesión.
        Lógica temporal: comidas top-rated o aleatorias.
        En el futuro, conectar aquí el modelo real.
        """
        session = self.get_object()

        # Comidas más valoradas o aleatorias
        foods = (
            Food.objects.annotate(avg_rating=Avg("ratings__rating"))
            .order_by("-avg_rating")[:5]
        )
        if not foods.exists():
            foods = Food.objects.all().order_by("?")[:5]

        created_items = []
        for food in foods:
            item, created = SessionItem.objects.get_or_create(session=session, food=food)
            if created:
                created_items.append(food.title)

        return Response({
            "session_id": session.id,
            "recommendations_added": created_items,
            "message": "Recomendaciones generadas exitosamente"
        }, status=status.HTTP_200_OK)
