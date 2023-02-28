from rest_framework import status as status_
from rest_framework.decorators import api_view
from rest_framework.response import Response
from function_handler.serializers import *
from function_handler.services.handlers import *


@api_view(['POST'])
def api_function_2(request):
    """
    Api реализация function-2
    """
    if request.method == 'POST':
        a_serializer = ASerializer(data=request.data[0])
        b_serializer = BSerializer(data=request.data[1])
        if a_serializer.is_valid() and b_serializer.is_valid():
            return Response(function_2(dict(a_serializer.data), dict(b_serializer.data)),
                            status=status_.HTTP_200_OK)


@api_view(['POST'])
def api_function_3(request, pk_a, pk_b):
    """
    Api реализация function-3
    :param pk_a: id объекта А
    :param pk_b: id объекта В
    """
    if request.method == 'POST':
        try:
            a = A.objects.get(pk=pk_a)
            b = B.objects.get(pk=pk_b)
        except:
            return Response(status=status_.HTTP_406_NOT_ACCEPTABLE)
        a_dict = dict(value=a.value, color=a.color)
        b_dict = dict(function=b.function, value=b.value)
        c_dict = function_2(a_dict, b_dict)
        c_serializer = CSerializer(data=c_dict)
        if c_serializer.is_valid():
            c_serializer.save()
            return Response(c_serializer.data, status=status_.HTTP_201_CREATED)
        return Response(c_serializer.errors, status=status_.HTTP_409_CONFLICT)


@api_view(['POST'])
def api_poster(request):
    """
    Дополнительная функция добавления объектов А и В в БД
    """
    if request.method == 'POST':
        a_serializer = ASerializer(data=request.data)
        b_serializer = BSerializer(data=request.data)
        if a_serializer.is_valid():
            a_serializer.save()
            return Response(a_serializer.data, status=status_.HTTP_201_CREATED)
        elif b_serializer.is_valid():
            b_serializer.save()
            return Response(b_serializer.data, status=status_.HTTP_201_CREATED)
        return Response(status=status_.HTTP_400_BAD_REQUEST)
