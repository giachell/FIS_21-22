"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'netflixapp'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('tabular', views.tabular, name='tabular'),
    path('add-movie', views.add_movie, name='add_movie'),
    path('delete', views.delete_movie, name='delete_movie'),
    path('edit', views.edit_movie, name='edit_movie'),
]