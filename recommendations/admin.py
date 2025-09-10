from django.contrib import admin
from .models import RecommendationSession, SessionItem

admin.site.register(RecommendationSession)
admin.site.register(SessionItem)
