from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

class CustomUserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=['email','password','first_name','last_name']
        extra_kwargs={
            'password':{'write_only':True}
        }
        
    def validate_password(self,value):
        validate_password(value)
        return value
    
    def create(self, validated_data):
        user =get_user_model()(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'
        depth=1