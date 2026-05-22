from . import views
from django.urls import path

urlpatterns = [
    path('',views.todo_list),
    path('create/',views.todocreate),
    path('update/<int:k>/',views.todoupdate),
    path('patch/<int:k>/',views.todopatch),
    path('delete/<int:k>/',views.tododelete),
    ]
