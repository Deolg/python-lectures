"""
Landing's module urls
"""
from django.urls import path

from . import views

# pylint: disable=invalid-name
app_name = 'home'

# pylint: disable=invalid-name
urlpatterns = [
    path('', views.index, name='home'),
]
