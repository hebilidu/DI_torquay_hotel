from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('visitors_home/', views.visitors_home, name='visitors_home'),
    path('add_guest/', views.GuestCreateView.as_view(), name='addguest'),
    path('list_guests/', views.GuestListView.as_view(), name='listguests'),
    path('add_message/<int:pk>', views.MessageCreateView.as_view(), name='addmessage'),
    path("vacancies/", views.vacancies, name='vacancies'),
]