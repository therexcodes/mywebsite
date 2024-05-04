from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service', views.service, name='service'),
    path('about', views.about,  name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('subscribe', views.subscribe, name='subscribe')
]
