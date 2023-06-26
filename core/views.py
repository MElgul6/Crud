from django.shortcuts import render, redirect
from .models import Task
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Q
#from .forms import TaskForm

def index(request):
    tasks=Task.objects.order_by("id").all()
    return render(request,'index.html',{"tasks":tasks})

def create_task(request): 
    task = Task(name=request.POST['name'],surname=request.POST['surname'], patronymic=request.POST['patronymic'])
    task.save()
    return redirect('/index/')

def update_task(request,id):
    if request.method == "POST":
        task=Task.objects.get(id=id)

        task.name = request.POST.get('name')
        task.surname = request.POST.get('surname')
        task.patronymic = request.POST.get('patronymic')
    
        task.save()
        
    return render(request,'index1.html')
   
def search_task(request):
    data = request.POST.get("query")
    tasks = Task.objects.filter(Q(name=data) | Q(surname=data) | Q(patronymic=data))
    print(tasks)
    return render(request,'index.html',{"tasks":tasks})




def activation(request,id):
    if request.method == "POST":
        task=Task.objects.get(id=id)
        is_active=request.POST.get("is_active")
        if is_active == "on":
              task.is_active = True
        else:
            task.is_active = False
        task.save()
    tasks=Task.objects.order_by("id").all()
        
    return render(request,'index.html',{"tasks":tasks})

