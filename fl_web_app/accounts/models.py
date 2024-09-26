from django.contrib.auth.models import User
from django.db import models
from core.models import Tblmacchine



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)      
    macchinario = models.ForeignKey(Tblmacchine, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
