from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Welcome to Django Course!!!'
    return render(request, 'index.html', {
        'title' : title
    })

def about(request):
    username = 'chen'
    return render(request, 'about.html', {
        'username': username
    })

def hi(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects 
    })

def tasks(request):
    # task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks/task.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html',{
        'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=request.POST['project'])
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
        'form': CreateNewProject()
    })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html',{
        'project': project,
        'tasks': tasks
    })

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = not task.done
    task.save()
    return redirect('tasks')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks')