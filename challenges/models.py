from django.db import models

# Create your models here.
class Challenge(models.Model):
    challenge_name = models.CharField(max_length=50,null=True,blank=True)
    short_desc = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.challenge_name
    
class Overview(models.Model):
    challenge_name = models.ForeignKey(Challenge,on_delete=models.CASCADE,null=False)
    desc = models.CharField(max_length=20000,null=True,blank=True)
    workout_split = models.CharField(max_length=1000000,null=True,blank=True)
    calorie_intake = models.CharField(max_length=100000,null=True,blank=True)
    nutrition = models.CharField(max_length=100000,null=True,blank=True)
    def __str__(self):
        return self.challenge_name
    
class Workout(models.Model):
    challenge_name = models.ForeignKey(Challenge,on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length=50,null=True,blank=True)
    sets = models.CharField(max_length=10,null=True,blank=True)
    repetitions = models.CharField(max_length=10,null=True,blank=True)
    rest_time = models.CharField(max_length=10,null=True,blank=True)
    img1Path = models.ImageField(null=True,blank=True)
    img2Path = models.ImageField(null=True,blank=True)
    instruction = models.CharField(max_length=10,null=True,blank=True)
    muscle_group = models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return self.name
class Diet(models.Model):
    challenge_name = models.ForeignKey(Challenge, on_delete=models.CASCADE, null=False)
    img = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.challenge_name