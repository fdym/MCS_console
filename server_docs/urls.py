from django.urls import path
from django.conf import settings
from django.shortcuts import render

from config.settings import ENABLED_HTML,SERVER_NAME

urlpatterns = []

for i in ENABLED_HTML.keys():
    urlpatterns.append(path(
        i.replace('.html', ''),
        lambda request:render(request, i, {'title': ENABLED_HTML[i], 'server_name': SERVER_NAME})
    ))
