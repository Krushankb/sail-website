from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sail-home'),
    path('about/', views.about, name='sail-about'),
    path('staff/', views.staff, name='sail-staff'),
    path('teachers/', views.teachers, name='sail-teacher'),
]
