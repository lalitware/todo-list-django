from django.shortcuts import redirect
from .models import Task
# Create your views here.
def addTask(request):
  task = request.POST['task']
  Task.objects.create(task=task)
  return redirect('home')