from django.urls import path
from django.conf import settings
from django.shortcuts import render

#def yourfile(request):return render(request, 'yourfile.html')
def test(request):return render(request, 'test.html')

urlpatterns = [
    #path('yourfile', yourfile, 'yourfile'),
    path('test', test, name='test'),
]
