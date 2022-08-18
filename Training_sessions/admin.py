from django.contrib import admin
from .models import Training_type,Training_session,Rpe
# Register your models here.

admin.site.register([Rpe])

@admin.register(Training_type)
class Training_typeAdmin(admin.ModelAdmin):
    list_display = ['name','description','is_active']
    ordering = ['name',]

@admin.register(Training_session)
class Training_sessionAdmin(admin.ModelAdmin):
    list_display =['user','dt_assign','done']
    ordering = ['user',]