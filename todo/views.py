from django.http import HttpResponse
from django.template import Context, loader

from todo.models import Item

# Create your views here.

def index(request):
    return HttpResponse("Hello world :(")
    '''
    todo_list = Item.objects.order_by('-name')[:5]
    template = loader.get_template('index.html')
    context = Context({
            'todo_list': todo_list,
            })
    output = '\n, '.join([t.name for t in todo_list])
    return HttpResponse(template.render(context))
    '''
