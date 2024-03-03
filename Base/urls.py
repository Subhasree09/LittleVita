from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('awarness/', views.awarness, name='awarness'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('doctors/', views.doctors, name='doctors'),
    path('disease/', views.disease, name='disease'),
    path('vaccine/', views.vaccine, name='vaccine'),
    path('videos/', views.videos, name='videos'),

]
