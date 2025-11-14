from rest_framework import generics

from .serializers import ProductSerializer
from .models import Product


class  ProductDetailAPIView(generics.RetrieveAPIView):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer


product_detail_view=ProductDetailAPIView.as_view()
    #for specific fields you pass the/it's  pk (primarykey)

# Create your views here.
