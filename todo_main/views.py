from django.shortcuts import render
from todo.models import Task


def home(request):
    # filter is used to fetch multiple data with condition
    # add order_by clause to sort the data by any field, - is for descending order. 
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks': tasks
    }
    return render(request, 'home.html', context)
