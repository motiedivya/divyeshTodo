# app/routes.py
from flask import request, jsonify, current_app as app
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from . import db
from .models import TodoItem, User

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = TodoItem.query.all()
    return jsonify([{
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'done': todo.done
    } for todo in todos])

@app.route('/todos', methods=['POST'])
@jwt_required()
def add_todo():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    new_todo = TodoItem(title=data['title'], description=data.get('description', ''), user_id=current_user_id)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'message': 'Todo created successfully'}), 201

@app.route('/todos/<int:id>', methods=['PUT'])
@jwt_required()
def update_todo(id):
    current_user_id = get_jwt_identity()
    data = request.get_json()
    todo = TodoItem.query.filter_by(id=id, user_id=current_user_id).first_or_404()
    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.done = data.get('done', todo.done)
    db.session.commit()
    return jsonify({'message': 'Todo updated successfully'})

@app.route('/todos/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_todo(id):
    current_user_id = get_jwt_identity()
    todo = TodoItem.query.filter_by(id=id, user_id=current_user_id).first_or_404()
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted successfully'})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200
