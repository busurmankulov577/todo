from django.shortcuts import render, HttpResponse


def homepage(requests):
    return render(requests, "index.html")

def go(request):
    return HttpResponse("THIS is MY first Page")

def test(requests):
    return render(requests, "test.html")

def second(request):
    return HttpResponse("test 2 page")

# Create your views here.
