from django.urls import path
from . import views

urlpatterns = [
    path('addTask', views.add_task, name='addTask'),
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:pk>', views.mark_as_undone, name='mark_as_undone'),
]
