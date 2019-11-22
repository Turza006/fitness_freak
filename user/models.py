from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length =50,null=True,blank=True)
    password = models.CharField(max_length=50,null=True,blank=True)
    number = models.CharField(max_length=50,null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    pro_pic = models.ImageField()
    u_id = models.IntegerField(primary_key=True,null=False)
    
    def __str__(self):
        return self.u_id