from django.shortcuts import render, HttpResponse, redirect
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


def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    title=form["book.title"]
    subtitle =form["book.subtitle"]
    description = form["book.description"]
    price = form["book.price"]
    genre = form["book.genre"]
    author = form["book.author"]
    year = form["book.year"][:10]
    books = Book(title=title,subtitle=subtitle,description=description,price=price,genre=genre,author=author,year=year)
    books.save()
    return redirect(book)

def delete_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)


def mark_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def delete_book(request,id):
    books = Book.objects.get(id=id)
    books.delete()
    return redirect(book)

def mark_book(request,id):
    books = Book.objects.get(id=id)
    books.is_favorite = True
    books.save()
    return redirect(book)

def unmark_book(requests,id):
    books = Book.objects.get(id=id)
    books.is_favorite = False
    books.save()
    return redirect(book)
    

def details(request):
    details_book = Book.objects.all()
    return render(request, "book_detail.html",{"book_list": details_book})



def DetailsBook(request,id):
    book_object = Book.objects.get(id=id)
    return render (request,"book_detail.html",{"book_object": book_object})

