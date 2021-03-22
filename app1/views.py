from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Myfun(request):

    
    return HttpResponse('Hiiiiiiiii')

def Home(request): 
    a=23
    return render(request,'home.html',{'test':'Hello Django'})

def Store(request):  
    return HttpResponse('store')