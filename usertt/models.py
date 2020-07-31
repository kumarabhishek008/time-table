from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    
class timetablecolumn(models.Model):

    user = models.ManyToManyField(User)
  
    c1=models.CharField(max_length=2000000,default="---")

    
    def __str__(self):
        return self.c1



    
    

    
    