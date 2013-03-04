from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.contrib import messages

from lazysignup.decorators import allow_lazy_user

from django.contrib.auth.models import *
from todo.models import Item
from todo.forms import TodoForm

# Create your views here.

def index(request):

    return render(request, 'index.html')


@allow_lazy_user
def todo(request):

    if request.method == 'GET':
        if request.user.is_authenticated():
            todo_list = Item.objects.filter(user__id=request.user.id).order_by('date_added', 'time_added').reverse()
            
            context = {"todo_list": todo_list}
            
        else:
            pass
            
    if request.method == 'POST':
        pass

    return render(request, 'todo.html', context)


def new_todo(request):

    if request.method == 'GET':
        return render(request, 'new-todo.html')

    if request.method == 'POST':
        todo_name = request.POST.get('todo_name')
        todo_description = None

        if request.user.is_authenticated():
            if request.POST.get('todo_description'):
                todo_description = request.POST.get('todo_description')
            
            t = Item(name=todo_name, description=todo_description, user=request.user)
            t.save()
            messages.add_message(request, messages.INFO, 'Todo added!')
                
            return redirect('/')
            
        else:
            todo_description = request.POST.get('todo_description')
            #request.session['todo_name'] = todo_name
            #request.session['todo_description'] = todo_description
            messages.add_message(request, messages.INFO, 'Todo added as anonymous user!')
            
            return redirect('/')


def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                messages.add_message(request, messages.INFO, 'Logged in!')
                return redirect('/')
                
            else:
                pass #return 'disabled account'
        else:
            messages.add_message(request, messages.INFO, 'Bad login')
            #return HttpResponse('bad_login')
            return redirect('/')

def logout(request):

    if request.method == 'GET':
        auth_logout(request)
        return redirect('/')

def registration(request):

    if request.method == 'GET':
        return render(request, 'registration.html')

    if request.method =='POST':
        username = request.POST.get('register_username')
        password = request.POST.get('register_password')
        
        user = User.objects.create_user(username, None, password)
        user.save();

        messages.add_message(request, messages.INFO, 'Registered!')
        
        return render(request, 'index.html')

