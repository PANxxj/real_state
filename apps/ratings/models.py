from django.db import models
from django.utils.translation import gettext_lazy as _
from real_state.settings.base import AUTH_USER_MODEL
from apps.common.models import TimeStampedUUIDModel
from apps.profiles.models import Profile


class Rating(TimeStampedUUIDModel):
    
    class Range(models.IntegerChoices):
        RATING_1 = 1,_('Poor')
        RATING_2 = 2,_('Fair')
        RATING_3 = 3,_('Good')
        RATING_4 = 4,_('Very Good')
        RATING_5 = 5,_('Excellent')
        
    rater = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name='rateings')
    agent = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,related_name='rateings')
    rating = models.IntegerField(choices=Range.choices,default=0)
    comment = models.TextField()
    
    class Meta:
        unique_together=['rater','agent']
        
        
    def __str__(self) -> str:
        return f'{self.agent} rated at {self.rating}'