from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [ 
   path('', views.login, name='login'),  # Define the 'login' URL pattern
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('logout', views.logout, name='logout'),

]