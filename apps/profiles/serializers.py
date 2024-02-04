from rest_framework import serializers
from .models import *


class ProfileSerializerPost(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

class ProfileSerializerGet(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'
        depth =1
        