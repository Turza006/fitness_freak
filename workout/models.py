from django.db import models

class Category(models.Model):
    category = models.CharField(primary_key=True,null=False,max_length=2000)
    def __str__(self):
        return self.id
# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    sets = models.CharField(max_length=10,null=True,blank=True)
    repetitions = models.CharField(max_length=10,null=True,blank=True)
    rest_time = models.CharField(max_length=10,null=True,blank=True)
    img1Path = models.ImageField(null=True,blank=True)
    img2Path = models.ImageField(null=True,blank=True)
    instruction = models.CharField(max_length=10,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False)
    w_id = models.IntegerField(primary_key=True,null=False)
    
    
    
    
    def __str__(self):
        return self.w_id