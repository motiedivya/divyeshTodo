# app/routes.py
from flask import request, jsonify, current_app as app
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, get_jwt, JWTManager
from . import db
from .models import TodoItem, User, TokenBlacklist

jwt = JWTManager(app)

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = TodoItem.query.all()
    return jsonify([{
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'done': todo.done,
        'created': todo.created,
        'edited': todo.edited
    } for todo in todos])

@app.route('/todos', methods=['POST'])
@jwt_required()
def add_todo():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    new_todo = TodoItem(title=data['title'], description=data.get('description', ''), user_id=current_user_id)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({
        'message': 'Todo created successfully',
        'id': new_todo.id,
        'title': new_todo.title,
        'description': new_todo.description,
        'done': new_todo.done,
        'created': new_todo.created,
        'edited': new_todo.edited
    }), 201

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
    return jsonify({
        'message': 'Todo updated successfully',
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'done': todo.done,
        'created': todo.created,
        'edited': todo.edited
    })

@app.route('/todos/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_todo(id):
    current_user_id = get_jwt_identity()
    todo = TodoItem.query.filter_by(id=id, user_id=current_user_id).first_or_404()
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted successfully'})

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

@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    db.session.add(TokenBlacklist(jti=jti))
    db.session.commit()
    return jsonify({'message': 'User logged out successfully'}), 200

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    token = TokenBlacklist.query.filter_by(jti=jti).first()
    return token is not None
