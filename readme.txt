Aim : To make to do list app using django framework.
Instructor: Rathan Kumar Udemy

Steps:
  1. Create directory of the project.
  2. Create environment -> python -m venv env
  3. activate virtual environment -> source env/bin/activate
  4. install django -> pip install django
  5. check the installation -> pip freeze
  6. create django project -> django-admin startproject todo_main .
  7. check the project -> python manage.py runserver
  8. run the migrate command to get default db tables -> python manage.py migrate
  9. create super user -> python manage.py createsuperuser
  10. check by login in the browser -> /admin
  11. create path for home page ->
    a. create views.py module in todo_main package and define home function
    b. import views module in urls.py
    c. add path("", views.home) in urls.py in urlpattern list
  12. create home template
    a. create templates directory in root directory
    b. create a template home.html
    c. from django.shortcuts import render
    d. return render(request, 'home.html') in home function.
    e. add 'templates' in DIRS list of TEMPLATES variable in settings.py module.
      TEMPLATES = [
        {
          ...
          "DIRS": ['templates'],
  13. Steps to load static file(images, js, css):
    a. Create a directory 'static' in the main package(todo_main).
    b. Create 'css' or 'images' or 'js' or all three directories in 'static' to include them.
    c. Add the below variables in the settings.py of the project.
        STATIC_ROOT = BASE_DIR /'static'
        STATICFILES_DIRS = [
          'mysite/static'
        ]
    d. load static in the template {% load static %}.
    e. In href or src of the html tag add {% static 'css/style.css' %}

  14. Create an app todo to store the task.
    a. python manage.py startapp todo
    b. register the app in settings.py in the INSTALLED_APPS list.
    c. create database tables in models.py of the app.
      i. make Task class having two fields task, is_completed(by default false), created_at, updated_at
      ii. register the model in admin.py -> admin.site.register(Task) and import Task from .models
      iii Generate sql queries this will create a migration file -> python manage.py makemigrations
      iv. Run migration to create tables -> python manage.py migrate
    
  15. List the completed tasks:
    a. write filter query in home function of views.py module in main package.
      -> Task.objects.filter(is_completed=False)
      -> using order clause Task.objects.filter(is_completed=False).order_by('updated_at)
    b. pass the variable to the render function as argument to use it in template.
    c. use forloop to display all the tasks.
  
  16. Steps to update the admin panel table.
    a. create a class in admin.py
      i. to add column -> list_display = ('task', 'is_completed', 'updated_at').
      ii. to add search functionality -> search_fields('task',)
    b. register it in the admin.py

  17. Add task to database from frontend:
    a. add path in the urlpatterns in urls.py of main package -> path('todo/', include('todo.urls'))
    b. create urls.py module in todo app.
    c. define path and views in urls.py of todo app
      urlpatterns = [
        path('addTask', views.addTask, name='addTask')
      ]
    d. define addTask in views.py of todo app.
    e. add the url name to form action.
    f. pass csrf token in the form-> {% csrf_token %} -> Django generate csrf token to keep data secure.
    g. In addTask function run create query and redirect to the home page.
      task = request.POST['task']
      Task.objects.create(task=task)
      return redirect('home')

  18. Listing of completed task:
    a. write filter query in views.py of main package -> completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    b. render it in home.html by passing the variable to the template
    c. use forloop to display all the completed_tasks

  19. Mark as done and mark as undone feature:
    a. create a url path in urlpattern in urls.py of todo app.
      path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
      path('mark_as_done/<int:pk/>', views.mark_as_done, name='mark_as_done'),
    b. create mark_as_done and mark_as_undone function in views.py of todo app.
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

