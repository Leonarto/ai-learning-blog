from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return JsonResponse({
        "text": "Hello Matt",
        "id": "cualquier-wea-id"
    })