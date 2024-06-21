import { Component, OnInit } from '@angular/core';
import { TodoService, Todo } from '../todo.service';

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css']
})
export class TodoListComponent implements OnInit {
  todos: Todo[] = [];

  constructor(private todoService: TodoService) { }

  ngOnInit(): void {
    this.getTodos();
  }

  getTodos(): void {
    this.todoService.getTodos().subscribe(todos => this.todos = todos);
  }

  deleteTodo(id: number): void {
    this.todoService.deleteTodo(id).subscribe(() => this.getTodos());
  }

  toggleDone(todo: Todo): void {
    todo.done = !todo.done;
    this.todoService.updateTodo(todo).subscribe();
  }
}
