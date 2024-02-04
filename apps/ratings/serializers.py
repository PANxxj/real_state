from rest_framework import serializers
from .models import *


class RatingSerializerPost(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields='__all__'

class RatingSerializerGet(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields='__all__'
        depth =1
        