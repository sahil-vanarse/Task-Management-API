"""
Admin configuration for the Task model in the Django admin interface.

This module registers the Task model with the Django admin site and customizes
the admin interface for managing tasks.

The TaskAdmin class inherits from django.contrib.admin.ModelAdmin and provides
the following customizations:

- list_display: Specifies the fields to be displayed in the list view of tasks.
  In this case, it shows the 'name', 'created_at', and 'status' fields.

- search_fields: Allows searching for tasks by 'name' and 'description'.
  This enables quick filtering of tasks based on user input.

- list_filter: Adds filters to the right sidebar of the list view, allowing
  administrators to filter tasks by 'status' and 'task_type'.

Usage:
To use this admin configuration, ensure that the Task model is defined in
the models.py file and that this admin.py file is located in the same app
directory. Once registered, the Task model will be accessible in the Django
admin interface with the specified customizations.

"""
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'status')
    search_fields = ('name', 'description')
    list_filter = ('status', 'task_type')
