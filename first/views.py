from django.shortcuts import render
from django.http import HttpResponse
from .models import Students, Scores

# Create your views here.

def index(request):
    return render(request, 'first/index.html')  

def students(request):
    
    #디비에서 데이터 가져옴
    students = Students.objects.all()

    #템플릿에 적용
    return render(request, 'first/students.html',{
        'text': '안녕하세요',
        'students': students
    })

def scores(request):

    scores = Scores.objects.all()

    return render(request, 'first/scores.html', {
        'scores' : scores

    })
