from django.contrib import admin

# Register your models here.
from .models import Challenge,Overview,Workout,Diet

admin.site.register(Challenge)
admin.site.register(Overview)
admin.site.register(Workout)
admin.site.register(Diet)