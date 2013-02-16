from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from django.contrib.auth.models import *
from todo.models import Item
from todo.forms import TodoForm

# Create your views here.

def index(request):

    todo_list = Item.objects.all()[:5]

    context = {"todo_list": todo_list}

    return render(request, 'index.html', context)


def todo(request):

    if request.method == 'GET':
        todo_list = Item.objects.all()

        context = {"todo_list": todo_list}

    if request.method == 'POST':
        pass

    return render(request, 'todo.html', context)


def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method =='POST':
        pass

    return render(request, 'login.html')

def new_todo(request):

    if request.method == 'GET':
        return render(request, 'new-todo.html')

    if request.method == 'POST':
        todo_name = request.POST.get('todo_name')
        todo_description = None
        if request.POST.get('todo_description'):
            todo_description = request.POST.get('todo_description')

        t = Item(name=todo_name, description=todo_description, user=User.objects.get(username='admin'))
        t.save()

        return redirect('/')

