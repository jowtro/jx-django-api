from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from datetime import datetime
# from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(data['username'],
                                            password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)},
                                status=status.HTTP_201_CREATED)
        except IntegrityError:
            return JsonResponse({'error':
                                 'That username has already been taken. Please choose a new username'},
                                status=400)


@csrf_exempt
def login(request):
    """DEPRECATED
    Login without check if token has expired

    Args:
        request

    Returns:
        JsonResponse: JSON response
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error': 'Could not login. Please check username and password'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except Exception:
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)},
                                status=status.HTTP_200_OK)


class ObtainExpiringAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            token, created =  Token.objects.get_or_create(user=serializer.validated_data['user'])

            if not created:
                # update the created time of the token to keep it valid
                token.created = datetime.utcnow()
                token.save()

            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

