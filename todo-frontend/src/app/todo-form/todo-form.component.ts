import { Component } from '@angular/core';
import { TodoService, Todo } from '../todo.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-todo-form',
  templateUrl: './todo-form.component.html',
  styleUrls: ['./todo-form.component.css']
})
export class TodoFormComponent {
  todo: Todo = {
    id: 0,
    title: '',
    description: '',
    done: false
  };

  constructor(private todoService: TodoService, private router: Router) { }

  addTodo(): void {
    this.todoService.addTodo(this.todo).subscribe(() => {
      this.router.navigate(['/']);
    });
  }
}
