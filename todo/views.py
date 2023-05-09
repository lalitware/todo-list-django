from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from django.http import HttpResponse


# function to add task.
def add_task(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


# function to mark a task as done.
def mark_as_done(request, pk):
    # fetch the data if it exists other wise give 404 error.
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


# function to mark a task as undone.
def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


# function to edit task.
def edit_task(request, pk):
    task_data = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        updated_task = request.POST['updated_task']
        # return HttpResponse(updated_task)
        task_data.task = updated_task
        task_data.save()
        return redirect('home')
    elif request.method == 'GET':
        context = {
            'task_data': task_data
        }
        return render(request, 'edit_task.html', context)


# function to delete a task
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task:
        task.delete()
    return redirect('home')
