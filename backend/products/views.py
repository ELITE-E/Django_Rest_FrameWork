from rest_framework import generics

from .serializers import ProductSerializer
from .models import Product


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    A combination of List + crete api view 
    """
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


product_list_create_view=ProductListCreateAPIView.as_view()

class  ProductDetailAPIView(generics.RetrieveAPIView):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer


product_detail_view=ProductDetailAPIView.as_view()
    #for specific fields you pass the/it's  pk (primarykey)
class  ProductListAPIView(generics.ListAPIView):
    """
    But we wont use it 
    """
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

product_list_view=ProductListAPIView.as_view()
