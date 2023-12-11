from django.http.request import HttpRequest
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse, JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('middleware was called')
        response = self.get_response(request)
        return response 
    
    def process_view(request, view_func, view_args, view_kwargs):
        return 