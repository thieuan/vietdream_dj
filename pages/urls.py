from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gioi-thieu/', views.about, name='about'),
    path('dich-vu/', views.services, name='services'),
    path('du-an/', views.projects, name='projects'),
    path('du-an/<slug:project_slug>/', views.project_detail, name='project_detail'),
    path('tin-tuc/', views.news, name='news'),
    path('lien-he/', views.contact, name='contact'),
]
