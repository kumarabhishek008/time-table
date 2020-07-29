from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    
class timetablecolumn(models.Model):
    week_choice = (('MONDAY','MONDAY'),('TUESDAY','TUESDAY'),('WEDNESDAY','WEDNESDAY'),('THURSDAY','THURSDAY'),
                   ('FRIDAY','FRIDAY'),('SATURDAY','SATURDAY'),('SUNDAY','SUNDAY'))
    rowchoice = (('first','first'),('second','second'),('third','third'),('fourth','fourth'),('fifth','fifth'),
                 ('sixth','sixth'))
    subject = (('SUB1','SUB1'),('SUB2','SUB2'),('SUB3','SUB3'),('SUB4','SUB4'),('SUB5','SUB5'),
               ('counselling class','counselling class'),('library','library'),('seminar','seminar'),('---','---'),('lunch','lunch'),
               ('lab','lab'),('SWA','SWA'))
    row = models.CharField(max_length=15,choices=rowchoice)
    c1=models.CharField(max_length=20,default="---",choices=week_choice)
    c2=models.CharField(max_length=20,default="---",choices=subject)
    c3=models.CharField(max_length=20,default="---",choices=subject)
    c4=models.CharField(max_length=20,default="---",choices=subject)
    c5=models.CharField(max_length=20,default="---",choices=subject)
    c6=models.CharField(max_length=20,default="---",choices=subject)
    c7=models.CharField(max_length=20,default="---",choices=subject)
    c8=models.CharField(max_length=20,default="---",choices=subject)
    c9=models.CharField(max_length=20,default="---",choices=subject)
    def __str__(self):
        return self.c1


'''class usertable(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    time_table = models.ForeignKey(timetablecolumn,on_delete=models.CASCADE,default=None)'''

    
    