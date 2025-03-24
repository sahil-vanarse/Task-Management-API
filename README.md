# 🚀 Task Management API

Welcome to the **Task Management API**! This Django REST Framework application enables users to manage tasks efficiently, assign them to others, and retrieve tasks based on assignments.

---

## 📌 Table of Contents
- [📥 Installation](#-installation)
- [🚀 Running the Project](#-running-the-project)
- [📡 API Endpoints](#-api-endpoints)
  - [📝 Task APIs](#-task-apis)
  - [👤 User APIs](#-user-apis)
- [🔍 Sample API Requests](#-sample-api-requests)
- [🔑 Test Credentials](#-test-credentials)

---

## 📥 Installation

### 1️⃣ Clone the Repository
```sh
git clone <repository-url>
cd task_manager
```

### 2️⃣ Set Up a Virtual Environment *(optional but recommended)*
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies
```sh
pip install django djangorestframework
```

### 4️⃣ Apply Migrations
```sh
python manage.py migrate
```

### 5️⃣ Create a Superuser *(for accessing the admin interface)*
```sh
python manage.py createsuperuser
```

---

## 🚀 Running the Project

### Start the Development Server
```sh
python manage.py runserver
```

### Access the API
🌐 Open your browser and visit: **[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)**

---

## 📡 API Endpoints

### 📝 Task APIs
- **Create a Task** → `POST /api/tasks/`
- **List All Tasks** → `GET /api/tasks/`
- **Retrieve a Specific Task** → `GET /api/tasks/{task_id}/`
- **Update a Task** → `PUT /api/tasks/{task_id}/`
- **Delete a Task** → `DELETE /api/tasks/{task_id}/`
- **Assign Users to a Task** → `POST /api/tasks/{task_id}/assign/`
- **Get Tasks for a Specific User** → `GET /api/tasks/user/{user_id}/`

### 👤 User APIs
- **List All Users and Their Assigned Tasks** → `GET /api/users/`
- **Retrieve a Specific User and Their Assigned Tasks** → `GET /api/users/{user_id}/`

---

## 🔍 Sample API Requests

### ➕ Create a Task
#### **Request:**
```http
POST /api/tasks/
Content-Type: application/json
```
```json
{
  "name": "Implement User Authentication",
  "description": "Develop a secure user authentication system.",
  "task_type": "Development",
  "status": "Pending",
  "assigned_users": [1, 2]  // Replace with actual user IDs
}
```

#### **Response:**
```json
{
  "id": 1,
  "name": "Implement User Authentication",
  "description": "Develop a secure user authentication system.",
  "task_type": "Development",
  "status": "Pending",
  "created_at": "2023-10-01T12:00:00Z",
  "assigned_users": [1, 2]
}
```

### 📋 List All Users
#### **Request:**
```http
GET /api/users/
```

#### **Response:**
```json
[
  {
    "id": 1,
    "username": "user1",
    "email": "user1@example.com",
    "tasks": []
  },
  {
    "id": 2,
    "username": "user2",
    "email": "user2@example.com",
    "tasks": [
      {
        "id": 1,
        "name": "Implement User Authentication",
        "description": "Develop a secure user authentication system.",
        "task_type": "Development",
        "status": "Pending"
      }
    ]
  }
]
```

---

## 🔑 Test Credentials
- **Admin Username:** `admin`
- **Admin Password:** *your_password_here* *(set during superuser creation)*

---

Name : Sahil Vanarse
Email : sahilvanarse13@gmail.com
Contact : 8530038434
