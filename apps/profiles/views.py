from rest_framework import status
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import send_mail
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.users.models import *
# from rest_framework.authentication import tok

class AgentListView(ListAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Profile.objects.filter(is_agent=True)
    serializer_class=ProfileSerializerGet

class TopAgentListView(ListAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Profile.objects.filter(top_agent=True)
    serializer_class=ProfileSerializerGet

class GetProfile(APIView):
    def get(self,request):
        print('......................',self.request.user)
        
        try:
            user=Profile.objects.get(user=request.user)
            ser=ProfileSerializerGet(user,context={'request':request})
            return Response(ser.data,status=status.HTTP_200_OK)
        except Exception as e:
            print('error',e)
            return Response({"Message":"errrrrrror"},status=status.HTTP_400_BAD_REQUEST)
        
class UpdateProfile(APIView):
    def put(self,request):
        try:
            profile=Profile.objects.get(user=request.user)
            ser=ProfileSerializerPost(profile,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                return Response({"Message":"ok"},status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('error',e)
            return Response({"Message":"errrrrrror"},status=status.HTTP_400_BAD_REQUEST)
        