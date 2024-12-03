from django.urls import path
from django.shortcuts import render

from .views import api_enabled_html

from config.settings import ENABLED_HTML, SERVER_NAME

def render_builder(template_name: str, context: dict):
    return lambda request:render(request, template_name, context)


urlpatterns = [
    path('api/enabled_html/', api_enabled_html)
]

for i in ENABLED_HTML.keys():
    urlpatterns.append(path(
        i.replace('.html', ''),
        render_builder(i, {'title': ENABLED_HTML[i], 'server_name': SERVER_NAME})
    ))
