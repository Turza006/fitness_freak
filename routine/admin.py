from django.contrib import admin

from .models import Routine,Category,Sub_Category
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Routine)