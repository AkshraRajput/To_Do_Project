from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import todo_table

# Create your views here.

def home(request):
    task_data = todo_table.objects.all()
    return render(request, 'home.html',{"data" : task_data })


def add_task(request):
    if request.method == "POST":
        Title = request.POST.get('title')
        Description = request.POST.get('description')
        todo_table.objects.create(
            Title = Title, 
            Description = Description)
        return redirect('home')
    return render(request, 'add_task.html')


def edit_task(request,id):
    task_data = todo_table.objects.get(id=id)
    if request.method == 'POST':
        Title = request.POST.get('title')
        Description = request.POST.get('description')

        if Title and Description:
            task_data.Title = Title
            task_data.Description = Description
            task_data.save()
            return redirect('home')

    return render(request, 'edit_task.html',{'task_data' : task_data})


def delete_task(request, id):
    task_data = todo_table.objects.get(id=id)
    task_data.delete()
    return redirect('home')


def task_completed(request, id):
    task_id = todo_table.objects.get(id=id)

    if request.method == "POST":
        task_id.Done = request.POST.get('checkbox') == "True"
        task_id.save()

    return redirect('home')

