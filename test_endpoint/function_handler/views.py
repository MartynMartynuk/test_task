import json

from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view

from function_handler.models import *
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


@api_view(['PUT'])
def api_putter(request):
    if request.method == 'PUT':
        object_type, obj = request.data
        status = 200
        try:
            if object_type['type'] == 'A':
                A.objects.create(value=obj['value'], color=obj['color'])
            elif object_type['type'] == 'B':
                B.objects.create(function=obj['function'], value=obj['value'])
            else:
                status = 400
        except:
            status = 405
        return HttpResponse(status=status)
