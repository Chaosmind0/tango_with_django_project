from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name ='about'),
    path('category/<slug:category_name_slug>/',
        views.show_category, name='show_category'),
<<<<<<< HEAD
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    
=======
    path('category/<slug:category_name_slug>/add_page/',
        views.add_page, name='add_page'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'), # New mapping!
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),

>>>>>>> 3aad359ab85a6c495c7cda84e8e25252d0da2bbd
]