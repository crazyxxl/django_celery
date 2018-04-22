# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers.serializers import UserSerializer
from utils.jwtutils import generate_token, ver_token
from .models import *

# Create your views here.


@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    result = User.objects.filter(username=username, password=password)[0]
    if result:
        serializer = UserSerializer(result)
        return Response(ver_token(generate_token(result)), status=status.HTTP_200_OK)
    else:
        return Response("username or password is wrong", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register(request):
    check_result, user = user_register_data_valid(request.data)
    print(check_result)
    if not check_result:
        return Response("account exist", status=status.HTTP_400_BAD_REQUEST)
    else:
        user.save()
    return Response("register successful", status=status.HTTP_200_OK)


def user_register_data_valid(data):
    if User.objects.filter(account=data.get("account")):
        return False, None
    else:
        user = User(username=data.get("username"),
                    password=data.get("password"),
                    account=data.get("account"),
                    stat=data.get("stat")
                    )
        return True, user
