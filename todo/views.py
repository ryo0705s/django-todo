from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Todo
# from django.http import HttpResponse
# Create your views here.
class TodoList(ListView):
  model = Todo
  context_object_name = "tasks"

class TodoDetail(DetailView):
  model = Todo
  context_object_name = "task"
# def index(request):
#   return HttpResponse("<H1>Hello World</H1>")
