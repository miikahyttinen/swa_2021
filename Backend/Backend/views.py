from django.contrib.sites import requests
from django.http import HttpResponse, JsonResponse
import requests
import json


def index(request):
    return HttpResponse("Hello, world. You're at the Backend index.")


def getMockData(request):
    req_1 = requests.get("http://localhost:8001/sportradar/")
    req_2 = requests.get("http://localhost:8002/tweets/")
    req_3 = requests.get("http://localhost:8003/tennisabstract")
    data = {
        'sportradar': req_1.content,
        'tweets': req_2.content,
        'tennisabstract': req_3.content
    }
    return JsonResponse(data)
    response = jsonify(data)
    # TODO: aggregate data
    # response = jsonify(data)
    # response.status_code = 200
    # print(data)
    # return JsonResponse(data)
    return HttpResponse("Imagine the data here")
