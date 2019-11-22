from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(primary_key=True,max_length=2000,null=False)
    def __str__(self):
        return self.id

class Sub_Category(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False)
    sub_Catagory = models.CharField(max_length=1000,null=False,blank=False)
    s_id = models.IntegerField(null=False)

    def __str__(self):
        return self.s_id

class Routine(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    sets = models.CharField(max_length=10,null=True,blank=True)
    repetitions = models.CharField(max_length=10,null=True,blank=True)
    rest_time = models.CharField(max_length=10,null=True,blank=True)
    img1Path = models.ImageField(null=True,blank=True)
    img2Path = models.ImageField(null=True,blank=True)
    instruction = models.CharField(max_length=10,null=True,blank=True)
    s_id = models.ForeignKey(Sub_Category,on_delete=models.CASCADE,null=False)

    
    
    
    def __str__(self):
        return self.name
