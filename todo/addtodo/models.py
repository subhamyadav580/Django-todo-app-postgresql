from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Todo(models.Model):
    todo = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.todo

    # def get_absolute_url(self):
    #     return reverse("todo-detail", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        return reverse("todolist")
