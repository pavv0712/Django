from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.index, name = 'index'),
    path('favorite', views.favorite, name = 'favorite'),
    path('todo', views.todo, name = 'todo')
    ]