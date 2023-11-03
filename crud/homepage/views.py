import json
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.core import serializers
from .models import User

def helloworld(request):
    return HttpResponse("Hello World!")

def index(request):
    data = User.objects.all()
    serialized_data = serializers.serialize('json', data)
    deserialized_data = json.loads(serialized_data)
    return JsonResponse({'data': deserialized_data}, safe=False)


def add_user(request):
    return render(request, 'form.html')

def edit_user(request, emailid):
    try:
        user = User.objects.get(email=emailid)
        user_data = {
            'email': user.email,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'phone': user.phone,
            'dob': user.dob,
            'address': user.address
        }
        return JsonResponse({'data': user_data})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

def save_user(request):
    try:
        if request.method == 'POST':
            user_data = json.loads(request.body)
            email = user_data.get('email')
            fname = user_data.get('firstname')
            lname = user_data.get('lastname')
            mob = int(user_data.get('phone'))
            dob = user_data.get('dob')
            address = user_data.get('address')

            try:
                user, created = User.objects.get_or_create(email=email)
                user.firstname = fname
                user.lastname = lname
                user.phone = mob
                user.dob = dob
                user.address = address

                user.save()
                return JsonResponse({'message': 'User data saved successfully'})

            except IntegrityError as e:
                return JsonResponse({'error': 'Database error: ' + str(e)}, status=500)
            # user, created = User.objects.get_or_create(email=email)

            # user.firstname = fname
            # user.lastname = lname
            # user.phone = mob
            # user.dob = dob
            # user.address = address

            # user.save()

            # return JsonResponse({'message': 'User data saved successfully'})
        else:
            return JsonResponse({'error': 'Method Not Allowed'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def delete_user(request, emailid):
    user = User.objects.get(email=emailid)
    user.delete()
    return JsonResponse({'message': 'User data deleted successfully'})

def check_email(request):
    user_data = json.loads(request.body)
    email = user_data.get('email')
    print(f"Received email: {email}")
    exists = User.objects.filter(email=email).exists()
    print(f"Email exists: {exists}")
    return JsonResponse({'exists': exists})
