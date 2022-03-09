from django.contrib import admin

# Register your models here.
from src.apps.app2.models import App2Model


@admin.register(App2Model)
class AppAdmin(admin.ModelAdmin):
    list_fields=['__all__']