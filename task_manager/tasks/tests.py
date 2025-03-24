# tasks/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Task

class TaskAPITests(APITestCase):

    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(username='user1', password='password1', email='user1@example.com')
        self.user2 = User.objects.create_user(username='user2', password='password2', email='user2@example.com')

        # Create a test task
        self.task = Task.objects.create(
            name="Test Task",
            description="This is a test task.",
            task_type="Development",
            status="Pending"
        )
        self.task.assigned_users.add(self.user1)

    def test_create_task(self):
        url = reverse('task-list') 
        data = {
            "name": "New Task",
            "description": "Description of new task.",
            "task_type": "Development",
            "status": "Pending",
            "assigned_users": [self.user1.id, self.user2.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)  

    def test_list_tasks(self):
        url = reverse('task-list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  

    def test_retrieve_task(self):
        url = reverse('task-detail', args=[self.task.id])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.task.name)

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task.id])  
        data = {
            "name": "Updated Task",
            "description": "Updated description.",
            "task_type": "Development",
            "status": "In Progress",
            "assigned_users": [self.user1.id]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, "Updated Task")

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)  

class UserAPITests(APITestCase):

    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(username='user1', password='password1', email='user1@example.com')
        self.user2 = User.objects.create_user(username='user2', password='password2', email='user2@example.com')

    def test_list_users(self):
        url = reverse('user-list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  

    def test_retrieve_user(self):
        url = reverse('user-detail', args=[self.user1.id])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user1.username)
