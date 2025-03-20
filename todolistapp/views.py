from asyncio import tasks

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task, Taskers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm


# Create your views here.
"""authentication view functions"""
# User registration (sign up)
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        # check if the form entries are valid
        if form.is_valid():
            # capturing the details for the registration and saving them to db
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'todolistapp/register.html', {'form' : form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user() # user exists in db we get the record object
            login(request, user)
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'todolistapp/login.html', {'form' : form})

def logout_user(request):
    logout(request)
    return redirect('login')



"""these functionalities take care of CRUD :-)"""


@login_required(login_url='login')
def task_list(request):

    # [] empty list is a default if tasks are empty
    # tasks = request.session.get('tasks', []) # collects tasks
    # Fetching tasks from db
    tasks = Task.objects.all()
    taskers = Taskers.objects.all()
    # render returns a html template

    return render(request, 'todolistapp/task_list.html', {"tasks" : tasks, "taskers":taskers})
def add_tasker(request):
    """add a new tasker"""
    if request.method == "POST":
        username = request.POST.get('user_tasker')
        email =request.POST.get('user_email')

        #save to db table
        if username:
            Taskers.objects.create(username=username, email=email)
    return redirect('task_list')

def add_task(request):
    """add a new task to db table"""
    if request.method == "POST":
        title = request.POST.get("task")
        tasker_id = request.POST.get("tasker")
        print(title,tasker_id)
        # save to db
        if title:
            #validating the id entered
            tasker = Taskers.objects.get(id=tasker_id) if tasker_id else None
            Task.objects.create(title=title,taskers=tasker)
            messages.success(request, 'Tasker and task added successfully')
        else:
            messages.error(request, 'Please enter a valid tasker')

    return redirect('task_list')

# def add_task(request):
#     """adds new task"""
#     if request.method == 'POST':
#         task = request.POST.get('task')
#         # checking if task is captured
#         if task:
#             # fetch existing tasks
#             tasks = request.session.get('tasks', [])
#             # add the new task to above list
#             tasks.append({'task': task, 'done': False})
#             # save new list to the current session
#             request.session['tasks'] = tasks
#             # notify user
#             messages.success(request, 'Task added successfully')
#         else:
#             messages.error(request, 'Task not found')
#     # redirect is different from render, render loads the template. Redirect simply change the web address to the given location
#     return redirect('task_list')

def delete_task(request,task_id):
    """delete task from db table"""
    Task.objects.filter(id=task_id).delete()
    return redirect('task_list')




# def delete_task(request, index):
#     """deletes task at the given index"""
#     tasks = request.session.get('tasks', [])
#     if 0 <= index < len(tasks):
#         del tasks[index]
#         # save the new task
#         request.session['tasks'] = tasks
#         messages.success(request, 'Task deleted')
#     else:
#         messages.error(request, 'Task not found')
#     return redirect('task_list')


def mark_complete(request,task_id):
    """mark task as complete in db table"""
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')
# def mark_complete(request, index):
#     """marks task complete"""
#     tasks = request.session.get('tasks', [])
#     if 0 <= index < len(tasks):
#         tasks[index]['done'] = True
#         request.session['tasks'] = tasks
#         messages.success(request, 'Task marked as completed')
#     else:
#         messages.error(request, 'Task not found')
#     return redirect('task_list')
#
