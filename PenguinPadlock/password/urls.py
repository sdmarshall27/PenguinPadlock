from django.urls import path
from .views import PasswordListView, PasswordCreateView, PasswordUpdateView, PasswordDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='password-home'),
    path('list', views.list, name='password-list'),
    path('list2', PasswordListView.as_view(), name='password-list2'),
    path('new', PasswordCreateView.as_view(), name='password-new'),
    path('update/<int:pk>/', PasswordUpdateView.as_view(), name='password-update'),
    path('delete/<int:pk>/', PasswordDeleteView.as_view(), name='password-delete'),
]
