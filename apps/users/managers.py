from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_kwargs):
        if not email:
            raise ValueError(_("User must be set"))
        user = self.normalize_email(email)
        user = self.model(email=email,**extra_kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_kwargs):
        extra_kwargs.setdefault('is_superuser',True)
        extra_kwargs.setdefault('is_active',True)
        extra_kwargs.setdefault('is_staff',True)
        
        if extra_kwargs.get('is_superuser') is not True:
            raise ValueError(_('is super user must be true'))
        if extra_kwargs.get('is_staff') is not True:
            raise ValueError(_('is staff must be true'))
        
        return self.create_user(email,password,**extra_kwargs)