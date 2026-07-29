from django.urls import path
from . import views

app_name = 'club'


urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'about/', views.about, name='about'),
    path(r'team/', views.team, name='team'),
    path(r'events/', views.events, name='events'),
    path(r'contact/', views.contact, name='contact'),
    path(r'gallery/', views.gallery, name='gallery'),


]