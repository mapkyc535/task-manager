from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='list'),
    path('add/', add, name='add'),
    path('search/', search, name='search'),
    path('perform/', perform, name='perform'),
    path('delete/', delete, name='delete'),
]