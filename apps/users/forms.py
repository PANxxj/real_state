from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields=['email','first_name','last_name']
        error_class='error'
        
        
class UserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=['email','first_name','last_name']
        error_class='error'