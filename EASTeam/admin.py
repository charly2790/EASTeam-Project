from django.contrib import admin
from .models import Settings

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_per_page = 20
    search_fields =['title','description']
