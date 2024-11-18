from django.urls import path
from django.conf import settings
from django.shortcuts import render

urlpatterns = [
    #path('yourfile', lambda a:render(a, 'yourfile.html'), 'yourfile'),
    path('test', lambda a:render(a, 'test.html'), name='test'),
]
