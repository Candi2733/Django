from django.shortcuts import render
from django.http.response import JsonResponse
import os
from .functions import main
import asyncio

# Create your views here.
async def home(request):
    api_endpoint = 'http://127.0.0.1:8000/file_upload'
    source_folder = '/home/devum/files'
    # value = push_files_to_api(api_endpoint, source_folder)
    async_func = await main(source_folder, api_endpoint)
    return async_func

def file_upload(request):
    try:
        if request.method == 'POST' and request.FILES.get('file'):
            file = request.FILES['file']
            file_path = '/home/devum/files1'
            file_extension = os.path.splitext(file.name)[1] 
            print(file, file_extension)
            destination_folder = os.path.join(file_path, file_extension[1:].upper() + "_Files")

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            with open(os.path.join(destination_folder, file.name), 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            return JsonResponse({'message' : 'Uploaded successfully'}, status = 200)
        return JsonResponse({'error' : 'Method not allowed'}, status = 404)
    except Exception as e:
        return JsonResponse({'error' : str(e)}, status=500)
        