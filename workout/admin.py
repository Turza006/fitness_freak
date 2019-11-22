from django.contrib import admin

# Register your models here.
from .models import Workout,Category

admin.site.register(Workout)
admin.site.register(Category)