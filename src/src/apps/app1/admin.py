from django.contrib import admin

# Register your models here.
from src.apps.app1.models import App1Model


@admin.register(App1Model)
class AppAdmin(admin.ModelAdmin):
    list_fields=['__all__']