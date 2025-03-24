"""
models.py

This module defines the Task model for the task_manager application.

The Task model represents a task that can be assigned to users. It includes the following fields:

- name (CharField): A short title for the task, with a maximum length of 255 characters.
- description (TextField): A detailed description of the task.
- created_at (DateTimeField): The timestamp when the task was created, automatically set to the current date and time when the task is created.
- task_type (CharField): A field to specify the type of task, with a maximum length of 50 characters.
- completed_at (DateTimeField): The timestamp when the task was completed. This field can be null or left blank if the task is not yet completed.
- status (CharField): A field to indicate the current status of the task, with a maximum length of 50 characters.
- assigned_users (ManyToManyField): A many-to-many relationship with the User model, allowing multiple users to be assigned to a task. The related name for accessing tasks assigned to a user is 'tasks'.

The __str__ method returns the name of the task, which is used for string representation of the Task instances.

"""

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=50)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50)
    assigned_users = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.name