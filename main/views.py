from django.shortcuts import render, HttpResponse
from .models import ToDo
from .models import Book

def homepage(requests):
    return render(requests, "index.html")

def go(request):
    return HttpResponse("THIS is MY first Page")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html",{"todo_list":todo_list})
def book(request):
    book_list = Book.objects.all()
    return render(request,"book.html",{"book_list":book_list})
def second(request):
    return HttpResponse("test 2 page")

def addtxt(request):
    return render(request,"add.html")

def change(request):
    return render(request,"change.html")

def delete(request):
    return render(request,"delete.html")
# Create your views here.
