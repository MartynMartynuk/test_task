from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def api_function_2(request):
    if request.method == 'POST':
        return JsonResponse(request.data, safe=False)


@api_view(['POST'])
def api_function_3(request):
    if request.method == 'POST':
        return JsonResponse('function3!', safe=False)
