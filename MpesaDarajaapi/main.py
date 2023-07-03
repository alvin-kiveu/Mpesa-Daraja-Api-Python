import requests
from django.http import JsonResponse


def main (request):
    return JsonResponse({'error': 'This is the main page'})  # Return JSON response