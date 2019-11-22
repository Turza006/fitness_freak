from django.db import models
from user.models import User
from django.utils import timezone

# Create your models here.
#date,title,desc,
class Transformation(models.Model):
    u_id = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    date = models.DateTimeField(default=timezone.datetime.now())
    title = models.CharField(max_length=100,null=True,blank=True)
    desc = models.CharField(max_length=1000000,null=True,blank=True)
    
    
    def __str__(self):
        return self._id