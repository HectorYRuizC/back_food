from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Avg
from foods.models import Food
from .models import RecommendationSession, SessionItem
from .serializers import RecommendationSessionSerializer
from core.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from .ml_service import train_model, recommend_for_user
from ratings.models import Rating


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

    def get_queryset(self):
        qs = RecommendationSession.objects.all().prefetch_related("items__food")
        if self.request.user.is_superuser:
            return qs
        return qs.filter(user=self.request.user)

    @action(detail=True, methods=["post"], url_path="generate")
    def generate_recommendations(self, request, pk=None):
        """
        Genera recomendaciones personalizadas basadas en el modelo entrenado con la BD.
        Verifica primero si el usuario ha calificado comidas.
        """
        session = self.get_object()
        user = request.user

        # --- 1️⃣ Verificar si el usuario tiene calificaciones previas
        has_ratings = Rating.objects.filter(user=user).exists()
        if not has_ratings:
            return Response({
                "can_generate": False,
                "message": "Debes calificar algunas comidas antes de obtener recomendaciones."
            }, status=status.HTTP_400_BAD_REQUEST)

        # --- 2️⃣ Entrenar modelo con datos actuales de la BD
        try:
            model, user2idx, food2idx, dataset = train_model()
        except Exception as e:
            print("⚠️ Error al entrenar el modelo:", e)
            return Response({
                "can_generate": False,
                "message": f"Error durante el entrenamiento del modelo: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if model is None or dataset is None:
            return Response({
                "can_generate": False,
                "message": "No hay datos suficientes para entrenar el modelo."
            }, status=status.HTTP_400_BAD_REQUEST)

        # --- 3️⃣ Obtener recomendaciones personalizadas
        try:
            recommended_foods = recommend_for_user(
                user=user,
                model=model,
                dataset=dataset,
                n_recommendations=4
            )
        except Exception as e:
            print("⚠️ Error al generar recomendaciones:", e)
            return Response({
                "can_generate": False,
                "message": f"Error al generar recomendaciones: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # --- 4️⃣ Guardar los resultados en la sesión
        created_items = []
        for food_data in recommended_foods:
            food = get_object_or_404(Food, id=food_data["id"])
            item, created = SessionItem.objects.get_or_create(
                session=session,
                food=food,
                defaults={"predicted_rating": food_data["predicted_rating"]}
            )
            if created:
                created_items.append(food.title)

        # --- 5️⃣ Respuesta final
        return Response({
            "can_generate": True,
            "session_id": session.id,
            "recommendations": recommended_foods,
            "message": f"Recomendaciones generadas exitosamente ({len(created_items)} agregadas)."
        }, status=status.HTTP_200_OK)