from django.shortcuts import render, HttpResponse


def homepage(requests):
    return HttpResponse("Hello beatifull world")

def go(request):
    return HttpResponse("THIS is MY first Page")

def test(requests):
    return render(requests, "test.html")

# Create your views here.
