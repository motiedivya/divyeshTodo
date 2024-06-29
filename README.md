# Flask Todo API

A simple Todo API built with Flask, SQLAlchemy, and Flask-JWT-Extended for user authentication. This project demonstrates how to create a RESTful API with authentication, CRUD operations, and deploy it on PythonAnywhere.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [API Endpoints](#api-endpoints)
- [Running the Application](#running-the-application)
- [Testing with Postman](#testing-with-postman)
- [Deployment](#deployment)
- [License](#license)

## Project Overview

This project provides a backend API for managing todo items. It supports user registration, login, and CRUD operations on todo items. Authentication is handled using JSON Web Tokens (JWT).

## Features

- User registration and login with JWT authentication.
- CRUD operations for todo items.
- Each user can manage their own todos.
- Secure endpoints with JWT authentication.
- Deployed on PythonAnywhere.

## Setup and Installation

### Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Flask-Migrate
- Flask-CORS

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file and add the following environment variables:

   ```plaintext
   SECRET_KEY=your-secret-key
   SQLALCHEMY_DATABASE_URI=sqlite:///todo.db
   JWT_SECRET_KEY=your-jwt-secret-key
   ```

5. **Initialize the Database**

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

## API Endpoints

### User Authentication

- **Register**
  - `POST /register`
  - Request Body: `{ "username": "user1", "password": "password123" }`
  - Response: `201 Created`

- **Login**
  - `POST /login`
  - Request Body: `{ "username": "user1", "password": "password123" }`
  - Response: `{ "access_token": "your_jwt_token" }`

### Todo Management

- **Get All Todos**
  - `GET /todos`
  - Response: `[{ "id": 1, "title": "Buy groceries", "description": "Milk, eggs, bread", "done": false }]`

- **Create Todo**
  - `POST /todos`
  - Headers: `Authorization: Bearer <your_jwt_token>`
  - Request Body: `{ "title": "Buy groceries", "description": "Milk, eggs, bread" }`
  - Response: `201 Created`

- **Update Todo**
  - `PUT /todos/<id>`
  - Headers: `Authorization: Bearer <your_jwt_token>`
  - Request Body: `{ "title": "Updated title", "description": "Updated description", "done": true }`
  - Response: `200 OK`

- **Delete Todo**
  - `DELETE /todos/<id>`
  - Headers: `Authorization: Bearer <your_jwt_token>`
  - Response: `200 OK`

## Running the Application

1. **Start the Flask Application**

   ```bash
   python run.py
   ```

2. **Access the Application**

   The API will be available at `http://localhost:5000`.

## Testing with Postman

1. **Register a User**
   - Method: `POST`
   - URL: `http://localhost:5000/register`
   - Headers: `Content-Type: application/json`
   - Body: `{ "username": "user1", "password": "password123" }`

2. **Login**
   - Method: `POST`
   - URL: `http://localhost:5000/login`
   - Headers: `Content-Type: application/json`
   - Body: `{ "username": "user1", "password": "password123" }`
   - Copy the `access_token` from the response.

3. **Create a Todo**
   - Method: `POST`
   - URL: `http://localhost:5000/todos`
   - Headers:
     - `Content-Type: application/json`
     - `Authorization: Bearer <your_jwt_token>`
   - Body: `{ "title": "Buy groceries", "description": "Milk, eggs, bread" }`

4. **Get All Todos**
   - Method: `GET`
   - URL: `http://localhost:5000/todos`
   - Headers: `Authorization: Bearer <your_jwt_token>`

5. **Update a Todo**
   - Method: `PUT`
   - URL: `http://localhost:5000/todos/<id>`
   - Headers:
     - `Content-Type: application/json`
     - `Authorization: Bearer <your_jwt_token>`
   - Body: `{ "title": "Updated title", "description": "Updated description", "done": true }`

6. **Delete a Todo**
   - Method: `DELETE`
   - URL: `http://localhost:5000/todos/<id>`
   - Headers: `Authorization: Bearer <your_jwt_token>`

## Deployment

### Deploying to PythonAnywhere

1. **Sign Up / Log In** to PythonAnywhere.

2. **Create a New Web App**:
   - Go to the "Web" tab.
   - Click "Add a new web app".

3. **Select Manual Configuration**:
   - Choose "Manual configuration".
   - Select the correct Python version.

4. **Clone Your Repository on PythonAnywhere**:
   - Open a Bash console.
   - Navigate to your home directory and clone your repo:

     ```bash
     cd ~
     git clone https://github.com/yourusername/your-repo-name.git
     cd your-repo-name
     ```

5. **Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

6. **Configure WSGI File**:
   - Go to the "Web" tab.
   - Click on the WSGI file link.
   - Edit the WSGI file to point to your Flask application:

     ```python
     import sys
     import os

     # Add your project directory to the sys.path
     project_home = u'/home/yourusername/your-repo-name'
     if project_home not in sys.path:
         sys.path = [project_home] + sys.path

     # Activate your virtual env
     activate_this = os.path.expanduser(project_home + '/venv/bin/activate_this.py')
     exec(open(activate_this).read(), dict(__file__=activate_this))

     # Import Flask app
     from app import create_app
     application = create_app()
     ```

7. **Reload Your Web App**:
   - Go to the "Web" tab.
   - Click the "Reload" button.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.