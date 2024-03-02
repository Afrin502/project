from django.shortcuts import render,HttpResponse
from hello.models import Contect

# Create your views here.
def index(request):
    return render(request,'index.html')
def contect(request):
    if request.method =="POST":
        name=request.POST.get('name')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        address=request.POST.get('address')
        contect=Contect(name=name,lastname=lastname,email=email,password=password,address=address)
        contect.save()
    return render(request,'contect.html')

