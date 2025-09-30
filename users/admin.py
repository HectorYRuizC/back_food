from django.contrib import admin
from .models import User, Rol

admin.site.register(Rol)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff','rol')

