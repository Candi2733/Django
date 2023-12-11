from django.http import JsonResponse
import jwt
from datetime import datetime
from basic_features.settings import SECRET_KEY

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print('Middleware was called')
        response = self.get_response(request)
        return response 
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path not in ['/', '/sign_up', '/login']:
            return self.token_validation(request)
        # print('middleware ended')
        return None
    
    def token_validation(self, request):
        try:
            if 'Authorization' in request.headers:
                auth_header = request.headers['Authorization']
                token = auth_header.split(' ')[1]
                # print(token)
            else:
                return JsonResponse({'error': 'Authorization Header missing'}, status=400)
            
            decoded_data = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=["HS256"])
            # print(decoded_data)
            # if datetime.fromtimestamp(decoded_data['exp']) < datetime.utcnow():
            #     print(1)
            #     return JsonResponse({'error': 'Token has expired'}, status=401)
            # print(2)
            request.email = decoded_data['email']
            return None
        
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
