from django.shortcuts import render
from django.http import HttpResponse

def taskList(request):
    return HttpResponse('To Do list')

# Create your views here.
