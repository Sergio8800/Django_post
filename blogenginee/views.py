# from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    # return HttpResponse('<h1> Hello world<h1>')
    return render(request, 'templates/blog/index.html')

