from django.contrib import admin
from django.urls import path
from .import views
from .views import TodoListView,TodoDetailView,TodoCreateView,TodoUpdateView,TodoDeleteView

urlpatterns = [
    path('todo/new/',TodoCreateView.as_view(),name='todo-form'),
    path('todo/<int:pk>/',TodoDetailView.as_view(), name='todo-detail'),
    path('todo/',TodoListView.as_view(), name='todolist'),
    path('todo/<int:pk>/update/',TodoUpdateView.as_view(), name='todo-update'),
    path('todo/<int:pk>/delete/',TodoDeleteView.as_view(), name='todo-delete'),

]
