# app/routes.py
from flask import request, jsonify
from . import db
from .models import TodoItem
from flask import current_app as app

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
def add_todo():
    data = request.get_json()
    new_todo = TodoItem(title=data['title'], description=data.get('description', ''))
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'message': 'Todo created successfully'}), 201

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    todo = TodoItem.query.get_or_404(id)
    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.done = data.get('done', todo.done)
    db.session.commit()
    return jsonify({'message': 'Todo updated successfully'})

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = TodoItem.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted successfully'})
