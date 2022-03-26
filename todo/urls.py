from django.urls import path
from .views import TodoList, TodoDetail, DetailView
# from . import views

urlpatterns = [
  path("", TodoList.as_view(), name="list"),
  path("detail/<int:pk>", TodoDetail.as_view(), name="detail"),
  # path("", views.index),
]