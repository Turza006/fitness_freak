from django.db import models

# Create your models here.
class Category(models.Model):
    diet_category = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.diet_category


class Details(models.Model):
    diet_category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False)
    question = models.CharField(max_length=150, null=True,blank=True)
    answer = models.CharField(max_length=100000,null=True,blank=True)

    def __str__(self):
        return self.diet_category


class Food(models.Model):
    img = models.ImageField(null=True)
    diet_category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.diet_category

class Blog(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    subtitle = models.CharField(max_length=200,null=True,blank=True)
    link = models.CharField(max_length=200,null=True,blank=True)
    diet_category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False)


    def __str__(self):
        return self.diet_category