from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel


User=get_user_model()

class Gender(models.TextChoices):
    MALE='Male',_("Male")
    FEMALE='Female',_("Female")
    OTHER='Other',_("Other")
    
    
class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name=_('phone number'),default="+917898756663",max_length=30)
    about_me = models.TextField(verbose_name=_('About Me '),default="Say something about yourself")
    aadhar = models.CharField(max_length=255,null=True,blank=True)
    profile_image = models.ImageField(upload_to='profile_images',null=True,blank=True)
    gender = models.CharField(choices=Gender.choices,default=Gender.OTHER,max_length=20)
    country = CountryField(default='India',null=False,blank=False)
    city = models.CharField(max_length=255,null=True,blank=True)
    is_buyer = models.BooleanField(default=False,verbose_name=_('Buyer'),help_text=_('Are Looking for Buy a property'))
    is_seller = models.BooleanField(default=False,verbose_name=_('Seller'),help_text=_('Are Looking to Sell a property'))
    is_agent = models.BooleanField(default=False,verbose_name=_('Agent'),help_text=_('Are an Agent'))
    top_agent = models.BooleanField(default=False,verbose_name=_('Top Agent'))
    rating = models.DecimalField(max_digits=4,null=True,blank=True,decimal_places=2)
    num_reviews = models.IntegerField(verbose_name=_('Number of Review '),default=0,null=True,blank=True)


    def __str__(self) -> str:
        return f'{self.user.email} profile'