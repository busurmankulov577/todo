from django.shortcuts import render, HttpResponse
from .models import ToDo

def homepage(requests):
    return render(requests, "index.html")

def go(request):
    return HttpResponse("THIS is MY first Page")

def test(requests):
    todo_list = ToDo.objects.all()
    return render(requests, "test.html",{"todo_list":todo_list})

def second(request):
    return HttpResponse("test 2 page")

def addtxt(request):
    return render(request,"add.html")

def change(request):
    return render(request,"change.html")

def delete(request):
    return render(request,"delete.html")
# Create your views here.
