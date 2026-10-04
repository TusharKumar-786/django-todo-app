from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/',views.add_todo,name='add'),
    path('update-todo/<id>/', views.update_todo, name='update_todo'),
    path('update-completed/<id>/', views.update_completed, name='update_completed'),
    path('delete-todo/<id>', views.delete_todo, name='delete_todo'),
    path('logout/', views.logout_page, name='logout_page'),
    ]
