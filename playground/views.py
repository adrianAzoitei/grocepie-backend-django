from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# view functions are better thought of as request handlers

def say_hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello World')

def show_hello(request: HttpRequest) -> HttpResponse:
    return render(request, 'hello.html')

def show_hello_dynamic(request: HttpRequest) -> HttpResponse:
    return render(request, 'hello_dynamic.html', {'name': 'Adrian'})