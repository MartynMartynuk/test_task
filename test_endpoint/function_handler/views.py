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
        if is_valid(request.data):
            id_a = request.data['id_a']
            id_b = request.data['id_b']
            try:
                a = A.objects.get(pk=id_a)
                b = B.objects.get(pk=id_b)
            except:
                return HttpResponse(status=406)
            a_dict = dict(value=a.value, color=a.color)
            b_dict = dict(function=b.function, value=b.value)
            c_dict = function_2(a_dict, b_dict)
            C.objects.create(value=c_dict['value'])
            return JsonResponse(c_dict, safe=True)
        else:
            return HttpResponse(status=400)


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
