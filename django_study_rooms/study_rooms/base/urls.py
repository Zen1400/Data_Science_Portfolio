from django.urls import path
from . import views


urlpatterns = [
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registeruser, name = 'register'),
    path('login/', views.loginpage, name = 'login'),
    path('', views.home, name = 'home'),
    path('room/<str:n>', views.room, name = 'room'),
    path('profile/<str:id>', views.userprofile, name='user-profile'),
    path('create-room/', views.createroom, name='create-room'),
    path('update-room/<str:n>/', views.updateroom, name='update-room'),
    path('delete-room/<str:n>/', views.deleteroom, name = 'delete-room'),
    path('create-topic/', views.createtopic, name = 'create-topic'),
    path('delete-message/<str:n>/', views.deletemessage, name = 'delete-message'),
    path('edit-message/<str:n>', views.editmessage, name = 'edit-message'),
]
