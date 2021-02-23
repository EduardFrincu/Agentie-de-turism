from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('destinations/', views.destinatie, name='destinatie'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutPage, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('my_account/', views.my_account, name = 'my_account'),
    path('rezervare/',views.rezervare, name = 'rezervare')

]