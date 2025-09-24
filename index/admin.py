from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'completed', 'date', 'user']
    list_filter = ['completed', 'date']
    search_fields = ['title', 'user__name']
    ordering = ['-date']