from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from uuid import uuid4
from django.utils.translation import gettext_lazy as _
import datetime

class CustomUser(AbstractBaseUser,PermissionsMixin):
    pkid=models.BigAutoField(primary_key=True,editable=False)
    id = models.UUIDField(default=uuid4,editable=False,unique=True)
    email=models.EmailField(unique=True,verbose_name=_('Email Address'))
    first_name=models.CharField(max_length=255,verbose_name=_('First Name'))
    last_name=models.CharField(max_length=255,verbose_name=_('Last Name'))
    date_joined=models.DateTimeField(default=datetime.datetime.now())
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    
    REQUIRED_FIELDS=[]
    USERNAME_FIELD='email'
    
    objects=CustomUserManager()
    
    class Meta:
        verbose_name=_('CustomUser')
        verbose_name_plural=_('CustomUsers')
    
    def __str__(self) -> str:
        return f'{self.email}'
    
    @property
    def get_full_name(self):
        return f'{self.first_name.title()} {self.last_name.title()}'
    
    def get_short_name(self):
        return f'{self.email}'
    