from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo
# from django.http import HttpResponse
# Create your views here.
class TodoList(ListView):
  model = Todo
  context_object_name = "tasks"

class TodoDetail(DetailView):
  model = Todo
  context_object_name = "task"

class TodoCreate(CreateView):
  model = Todo
  fields = "__all__"
  success_url = reverse_lazy("list")
  
class TodoUpdate(UpdateView):
  model = Todo
  fields = "__all__"
  success_url = reverse_lazy("list")
  
class TodoDelete(DeleteView):
  model = Todo
  context_object_name = "task"
  success_url = reverse_lazy("list")
# def index(request):
#   return HttpResponse("<H1>Hello World</H1>")
