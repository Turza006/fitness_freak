from django.contrib import admin

# Register your models here.
from .models import Details,Food,Blog,Category

admin.site.register(Details)
admin.site.register(Food)
admin.site.register(Blog)
admin.site.register(Category)