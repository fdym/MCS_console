from django.http import JsonResponse
from django.shortcuts import render, redirect

from config.settings.mcs_console import ENABLED_HTML, SERVER_NAME

# Create your views here.

def api_enabled_html(request): return JsonResponse(ENABLED_HTML)

def basic_view(request, template_name:str):
    if template_name.endswith('.html'):
        return redirect('/' + template_name.replace('.html', ''))
    elif template_name == 'search':
        full_name = template_name + '.html'
        return render(request, full_name, {'title': 'Search page', 'server_name': SERVER_NAME})
    else:
        full_name = template_name + '.html'
        return render(request, full_name, {'title': ENABLED_HTML[full_name], 'server_name': SERVER_NAME})
