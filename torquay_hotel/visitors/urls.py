from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('visitors_home/', views.visitors_home, name='visitors_home'),
    path("vacancies/", views.vacancies, name='vacancies'),
]