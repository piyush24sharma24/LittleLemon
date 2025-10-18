from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.menu_list, name='menu-list'),
]
