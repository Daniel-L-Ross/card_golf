from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import json

@csrf_exempt
def login_user(request):
    '''
    Handles the authentication of a user
    Template code copied from Nashville Software School bootcamp projects
    Method arguments:
      request -- The full HTTP request object
    '''

    req_body = json.loads(request.body.decode())

    if request.method == 'POST':

        email = req_body['email']
        password = req_body['password']
        user = User.objects.get(email=email)
        username = user.username
        authenticated_user = authenticate(username=username, password=password)

        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)

            data = json.dumps({"valid": True, "token": token.key, "username": username})
            return HttpResponse(data, content_type='application/json')

        else:
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')

@csrf_exempt
def register_user(request):
    '''Handles the creation of a new user for authentication
    Template code copied from Nashville Software School bootcamp projects
    
    Method arguments:
      request -- The full HTTP request object
    '''

    req_body = json.loads(request.body.decode())

    new_user = User.objects.create_user(
        username=req_body['username'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name']
    )

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)

    username = new_user.username

    data = json.dumps({"valid": True, "token": token.key, "username": username})
    return HttpResponse(data, content_type='application/json')