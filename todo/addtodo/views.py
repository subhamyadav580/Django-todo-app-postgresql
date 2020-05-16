from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.


def todo(request):
    if request.method == 'POST':
        todos = Todo(todo = request.POST['content'])
        todos.save();
    return redirect('/')
def todolist(request):
    all_todo = {'todohistory' : Todo.objects.all()}    
    return render(request, 'todo.html',all_todo)

def delete_todo(request,todos_id):
    todo_delete = Todo.objects.get(id=todos_id)
    todo_delete.delete()
    return redirect('/')