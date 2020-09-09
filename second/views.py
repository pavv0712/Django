from django.shortcuts import render
from django.http import HttpResponse
from .models import Favorite, Todo

# Create your views here.

def favorite(request):
    
    favorite = Favorite.objects.all()

    return render(request, 'second/favorite.html', {
        'favorite' : favorite

    })

def todo(request):
    
    todo = Todo.objects
    
    # if 'group' in request.GET:
    #     todo = todo.filter(group__name=request.GET['group'])
    
    # if 'end_date' in request.GET:
    #      todo = todo.filter(end_date__gte=request.GET['end_date'])

    # return render(request, 'second/todo.html', {
    #     'text' : '나의 할 일',
    #     'todo' : todo.all()       
        
    # }) 
    todo_pending = todo.filter(status='pending')
    todo_inprogress = todo.filter(status='inprogress')
    todo_end = todo.filter(status='end')

    return render(request, 'second/todo.html', {

        'todo_pending' : todo_pending,
        'todo_inprogress' : todo_inprogress,
        'todo_end' : todo_end
    })

def index(request):
    return render(request, 'second/index.html')  

