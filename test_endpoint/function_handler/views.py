import json

from django.http import JsonResponse
from rest_framework.decorators import api_view

from function_handler.services.handlers import *


@api_view(['POST'])
def api_function_2(request):
    if request.method == 'POST':
        a, b = request.data
        return JsonResponse(function_2(a, b), safe=False)


@api_view(['POST'])
def api_function_3(request):
    if request.method == 'POST':
        return JsonResponse('function3!', safe=False)
