from django.contrib import admin
from .models import Task

# To override the admin panel display
class TaskAdmin(admin.ModelAdmin):
  # to add column
  list_display = ('task', 'is_completed', 'updated_at')
  # to add search functionality
  search_fields = ('task',)

# Register your models here.
admin.site.register(Task, TaskAdmin)