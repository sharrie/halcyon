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
        form = LoginForm()

    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                else:
                    pass
                    # Return a 'disabled account' error message
            else:
                pass
                # Return an 'invalid login' error message.

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

