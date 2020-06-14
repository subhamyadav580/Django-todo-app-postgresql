from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Todo
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.


def todo(request):
    if request.method == 'POST':
        todos = Todo(todo=request.POST['content'])
        todos.save()
    return redirect('/todo')


def todolist(request):
    all_todo = {
        'todohistory': Todo.objects.all()
    }
    return render(request, 'todo.html', all_todo)


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'todohistory'
    template_name = 'todo.html'

    def get_queryset(self):
        return Todo.objects.filter(
            author=self.request.user
        )



class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_detail.html'


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['todo']
    template_name = 'todo_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo
    fields = ['todo']
    template_name = 'todo_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.author:
            return True
        return False


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    template_name = 'todo_confirm_delete.html'
    success_url = '/todo'

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.author:
            return True
        return False


def delete_todo(request, todos_id):
    todo_delete = Todo.objects.get(id=todos_id)
    todo_delete.delete()
    return redirect('/')
