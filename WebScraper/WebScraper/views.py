import requests
from WebScraper import processor
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the WebScraper index.")


def data(request):
    raw_data = requests.get('http://tennisabstract.com/reports/atp_elo_ratings.html')
    processed = processor.process_data(raw_data)
    return JsonResponse(processed, safe=False)
