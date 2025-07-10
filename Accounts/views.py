from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from Accounts.serializers import RegisterSerializer


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self , request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = {
        "message" : "User created successfully",
        "user" : {
            "username" :  serializer.data["username"],
            "email": serializer.data["email"],
            }
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

