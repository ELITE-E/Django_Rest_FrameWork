from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title_no_hello,unique_product_title

class ProductSerializer(serializers.ModelSerializer):
    #Just demonstrates renaming of product attributes inside a serializer
    my_discount =serializers.SerializerMethodField(read_only=True)

    #3.30---->allow access details of each product in the  in the ListApiView
    detail_url=serializers.SerializerMethodField(read_only=True)

    #3.35----->Access of an external serialize validation
    title=serializers.CharField(validators=[validate_title_no_hello,
                                            unique_product_title])
    class Meta:
        model=Product
        fields=[
             'pk',
             'user',
             'detail_url',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

#3.45---->Custom validation inside a serializer
    # def validate_title(self,value):
    #     qs=Product.objects.filter(title_iexact=value)
    #     if qs.exists():
    #          raise serializers.ValidationError(f"{value} is alredy a product name")
         

    def get_detail_url(self,obj):
         request=self.context.get('request')  
         if request is None:
              return None
         return reverse('products-detail',kwargs={'pk':obj.pk},request=request)
    
    def get_my_discount(self,obj):
          if hasattr(obj,'id') is None:
               return None
          if isinstance(obj,Product) is None:
               return None
          return obj.get_discount()
#     A serializer converts:

# Python objects / model instances → JSON (for API responses)

# JSON data → Python objects / model instances (for API requests)

# So it’s like a translator between the Django world and the API world.