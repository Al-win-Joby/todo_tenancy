from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Task
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
# Create your views here.

def loginfunction(request):     
    return render(request,'login.html')     

def signup(request):
    return render(request,'signup.html')    

def loggedup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)       
            return redirect('home')
        else:
            
            return redirect('login')


def home(request):
    if request.user.is_authenticated:
        tasks=Task.objects.filter(user=request.user)
        return render(request,'home.html',{'tasks':tasks})
    
    else:         
        return redirect('login')

def signedup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        password2=request.POST.get('confirm-password')
        if not User.objects.filter(username=username).exists():
            user=User.objects.create_user(username=username,password=password)
            #user=User.objects.get(username="ee")
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    else:
            return redirect('login')


def logoutfunction(request):
    logout(request)
    return redirect('login')


def add1(request):
    if request.method == 'POST':
        text=request.POST['todoText']
        print(text)
        user= request.user
        task=Task()
        task.user=user
        task.title=text
        task.save()
        return JsonResponse({'status':True})


def checkbox(request):
    if request.method=='POST':
        id=request.POST['id']
        task=Task.objects.get(id=id)
        if task.complete==True:
            task.complete=False
        else:
            task.complete=True
        
        task.save()
        return JsonResponse({'status':True})

def deleted(request):
    id = request.POST['id']
    Task.objects.get(id=id).delete()
    print("deleted ")
    return JsonResponse({'status':True})
    