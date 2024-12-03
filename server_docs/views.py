from django.http import JsonResponse

from config.settings import ENABLED_HTML

# Create your views here.

def api_enabled_html(request): return JsonResponse(ENABLED_HTML)
