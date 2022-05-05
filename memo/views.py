from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'memo/index.html')

def top(request):
    return render(request,'memo/top.html')