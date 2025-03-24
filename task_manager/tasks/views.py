"""
views.py

This module defines the TaskViewSet and UserViewSet for the task_manager application, which handle the API endpoints related to tasks and users.

The TaskViewSet provides the following functionalities:
- **create**: Allows the creation of a new task. It validates the incoming data using the TaskSerializer and saves the task if valid, returning the created task data with a 201 status code. If the data is invalid, it returns the errors with a 400 status code.
- **assign**: Assigns users to a specific task identified by its primary key (pk). It updates the task's assigned users based on the provided user IDs in the request data and returns a 204 status code upon success.
- **list**: Retrieves and returns a list of all tasks in the system, serialized into a JSON format.
- **retrieve**: Fetches a specific task by its primary key (pk) and returns its serialized data. If the task does not exist, it returns a 404 status code.
- **get_tasks_for_user**: Retrieves all tasks assigned to a specific user identified by their user ID and returns the serialized task data.

The UserViewSet provides the following functionalities:
- **list**: Retrieves and returns a list of all users along with their assigned tasks. Each user's data includes their ID, username, email, and a list of tasks serialized into JSON format.
- **retrieve**: Fetches a specific user by their primary key (pk) and returns their data along with the tasks assigned to them. If the user does not exist, it returns a 404 status code.

This module utilizes Django REST Framework's viewsets to streamline the creation of API endpoints and manage the serialization of data for both tasks and users.
"""
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class TaskViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def assign(self, request, pk=None):
        task = Task.objects.get(pk=pk)
        users = request.data.get('users', [])
        task.assigned_users.set(users)
        task.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get_tasks_for_user(self, request, user_id=None):
        tasks = Task.objects.filter(assigned_users__id=user_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        user_data = []
        
        for user in users:
            tasks = Task.objects.filter(assigned_users=user)
            task_serializer = TaskSerializer(tasks, many=True)
            user_data.append({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'tasks': task_serializer.data
            })
        
        return Response(user_data)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            tasks = Task.objects.filter(assigned_users=user)
            task_serializer = TaskSerializer(tasks, many=True)
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'tasks': task_serializer.data
            }
            return Response(user_data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)