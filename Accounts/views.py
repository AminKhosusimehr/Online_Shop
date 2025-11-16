
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, RegisterSerializer
from rest_framework import generics , status
from rest_framework.response import Response

from .tasks import send_welcome_email
from Utils.messages import title,text

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_welcome_email.delay(title , text , request.data['email'])

            return Response("User created!" , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)
