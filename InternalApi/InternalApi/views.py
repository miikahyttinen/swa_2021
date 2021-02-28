import os

import requests
from django.http import HttpResponse
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def index(request):
    return HttpResponse("Hello, world. You're at the InternalApi index.")


def sportradar(request):
    data = requests.get("https://api.sportradar.com/tennis-t2/en/players/rankings.json?api_key=" + API_KEY)
    return HttpResponse(data)
