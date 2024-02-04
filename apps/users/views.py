from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login,logout,authenticate
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import send_mail
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework.authtoken.models import Token

# from rest_framework.


class CreateUser(CreateAPIView):
    authentication_classes=[]
    def post(self,request):
        try:
            ser = CustomUserCreationSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({'Message':"ok"},status=status.HTTP_201_CREATED)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('eroror',e)
            return Response({"Message":'error'},status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt     
class UserLogin(APIView):
    authentication_classes=[]
    permission_classes=[]
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        try:
            user=authenticate(request,email=email,password=password)
            if user:
                login(request,user)
                refresh=RefreshToken.for_user(user)
                user_data=CustomUserSerializer(user)
                # token = Token.objects.create(user=user)
                return Response({'refresh_token':str(refresh),'access':str(refresh.access_token),'user':user_data.data},status=status.HTTP_200_OK)
                # return Response({'token':token.key,'user':user_data.data},status=status.HTTP_200_OK)
            return Response({"Message":"wrong Credentials"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('error',e)
            return Response({"Message":"wrong Credentials"},status=status.HTTP_400_BAD_REQUEST) 