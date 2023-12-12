from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def employee(request):
    try:
        if request.method == 'GET':
            pass
        elif request.method == 'POST':
            pass
        elif request.method == 'PUT':
            pass
        elif request.method == 'DELETE':
            pass
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)