from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login


from todo.models import Item
from todo.forms import TodoForm

# Create your views here.

def index(request):
    #return HttpResponse("Hello world :(")
    
    todo_list = Item.objects.all()[:5]

    context = {"todo_list": todo_list}

    return render(request, 'index.html', context)


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


def list_todo(request):
    todo_list = Item.objects.all()[:5]

    context = {"todo_list": todo_list}

    return render(request, 'index.html', context)
    

def new_todo(request):
    if request.method == 'GET':
        form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form_name = form.cleaned_data['name']
            form_description = form.cleaned_data['description']
            form_date_due = form.cleaned_data['date_due']
            i = Item(name = form_name, description = form_description, date_due = form_date_due)
            i.save()
            return HttpResponseRedirect('/admin/')
        else:
            form = TodoForm()

    return render(request, 'todo.html', { 'form': form })
