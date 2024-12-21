from django.urls import path
from django.shortcuts import render

from .views import api_enabled_html, basic_view

from config.settings.mcs_console import ENABLED_HTML, SERVER_NAME

urlpatterns = [
    path('api/enabled_html/', api_enabled_html),
    path('<str:template_name>', basic_view),
]
