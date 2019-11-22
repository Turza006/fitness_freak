from django.db import models
from user.models import User
from workout.models import Workout
from django.utils import timezone
# Create your models here.
class Pick(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    w_id = models.ForeignKey(Workout,on_delete=models.CASCADE,null=False)
    date = models.DateTimeField(default=timezone.datetime.now())
    reps = models.CharField(max_length=1000,null=True,blank=True)
    sets = models.CharField(max_length=1000,null=True,blank=True)


    def __str__(self):
        return self.date