import os
import requests
import asyncio
import requests
from django.http.response import JsonResponse
import httpx

# # Synchronous way of uploading the file
# def push_files_to_api(api_endpoint, source_folder):
#     try:
#         files = os.listdir(source_folder)

#         for file in files:
#             file_path = os.path.join(source_folder, file)

#             if os.path.isfile(file_path):

#                 with open(file_path, 'rb') as f:
#                     files = {'file': (file, f)}
#                     response = requests.post(api_endpoint, files=files)
                    
#                     if response.status_code == 200:
#                         print(f"File {file} uploaded successfully.")
#                     else:
#                         return JsonResponse({'error' : "Failed to upload {file}", "response" : response}, status = 500)
#         return JsonResponse({'message': 'all files uploaded successfully'})
#     except Exception as e:
#         return JsonResponse({'error' : str(e)})

async def upload_file(session, file_name, url):
    with open(file_name, 'rb') as file:
        files = {'file': (file_name, file, 'multipart/form-data')}
        response = await session.post(url, files=files)
        return response.status_code

# Uploading all files asynchronously
async def main(files_to_upload,upload_url):
    files = os.listdir(files_to_upload)
    files_list = []
    for file in files:
        file_path = os.path.join(files_to_upload, file)

        if os.path.isfile(file_path):
            files_list.append(file_path)

    async with httpx.AsyncClient() as client:
        tasks = [upload_file(client, file_name, upload_url) for file_name in files_list]
        results = await asyncio.gather(*tasks)

        for idx, status_code in enumerate(results):
            # if status_code !=200:
            #     return JsonResponse({'error': 'File {files_to_upload[idx]} upload status: {status_code}'})
            print(f"File {files_to_upload[idx]} upload status: {status_code}")
    return JsonResponse({'message' : 'Upload completed async'}, status = 200)
