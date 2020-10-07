from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='password-home'),
    path('list', views.list, name='password-list'),
]
