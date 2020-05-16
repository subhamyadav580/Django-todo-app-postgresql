from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('todo/',views.todo,name='todo'),
    path('',views.todolist,name='todolist'),
    path('/delete_todo/<int:todos_id>/',views.delete_todo,name='delete_todo'),
]
