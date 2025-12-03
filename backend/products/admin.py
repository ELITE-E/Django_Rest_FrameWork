from django.contrib import admin

# Register your models here.
from .models import Product
#2.23---->User group permissions using DjangoModelsPermission
admin.site.register(Product)