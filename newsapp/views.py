from django.shortcuts import render
from django.http import HttpResponse

def word(request):
    return HttpResponse("fafsadf")

def home(request):
    return render(request,'index.html')