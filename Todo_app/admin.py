from django.contrib import admin
from .models import Todo
# Register your models here

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title','description','due_date', 'priority', 'created_at']
    # Filter
    search_fields = ['title',]
    list_filter = ['completed', 'priority']
