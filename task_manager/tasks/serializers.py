"""
serializers.py

This module defines the TaskSerializer for the task_manager application.

The TaskSerializer is a subclass of the ModelSerializer provided by Django REST Framework. It is used to serialize and deserialize Task instances, allowing for easy conversion between complex data types, such as querysets and model instances, and Python data types that can then be easily rendered into JSON or other content types.

Attributes:
- model (Task): The model that this serializer is associated with, which is the Task model defined in models.py.
- fields (list): A list of fields to be included in the serialized representation. The value '__all__' indicates that all fields in the Task model should be included.

Usage:
The TaskSerializer can be used in views to validate and save incoming data for creating or updating Task instances, as well as to convert Task instances into JSON format for API responses.

Example:
To create a new task, you can instantiate the serializer with the request data:
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
"""

from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'