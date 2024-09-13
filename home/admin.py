from django.contrib import admin
from .models import OvozModel
# Register your models here.

@admin.register(OvozModel)
class ToDoAdmin(admin.ModelAdmin):
    list_display = [
        'user'
    ]

    list_filter = ['user'] 

