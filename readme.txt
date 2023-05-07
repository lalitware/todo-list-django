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