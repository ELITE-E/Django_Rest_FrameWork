from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Product

#3.35---->External validation using a serializer 
# def validate_title(value):
#     qs=Product.objects.values(title_iexact=value)
#     if qs.exists():
#         return serializers.ValidationError(f"{value} is already a product name.")
#     return value

def validate_title_no_hello(value):
    if "hello" in value.lower():
        return serializers.ValidationError(f"Hello is not allowed ")
    return value

#Another way of validating the uniqueness of a val (---using Unique validator from rf)
unique_product_title=UniqueValidator(queryset=Product.objects.all())