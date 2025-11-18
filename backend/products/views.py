from rest_framework import generics

from rest_framework.response import Response
#from django.http import Http404
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .serializers import ProductSerializer
from .models import Product


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    A combination of List + crete api view 
    """
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def product_create(self,serializer):
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        price=serializer.validated_data.get('price')
        serializer.save(content=content)


product_list_create_view=ProductListCreateAPIView.as_view()

class  ProductDetailAPIView(generics.RetrieveAPIView):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #for specific fields you pass the/it's  pk (primarykey)

product_detail_view=ProductDetailAPIView.as_view()

class  ProductListAPIView(generics.ListAPIView):
    """
    But we wont use it 
    """
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

product_list_view=ProductListAPIView.as_view()

#1.44.36--->Using function based views for create ,retreive and list 

# In this section we just saw 2 types of views in play FBVs and CBVs .The former excels at lightweight tasks,is simpler,easy on begginers but
# the latter is more robust ,suited for complex systems,handles common CRUD operations and errors out tof the box

@api_view(['POST','GET'])
def product_alt_view(request,pk=None,*args,**kwargs):
    method=request.method

    if method =='GET':
        #get products>>list 
        if pk is not None:
            #detail view
            #01.A way of doing it (Error and object are isolated )
            # queryset=Product.objects.filter(pk=pk)
            # if not queryset.exists():
            #     raise Http404
            # data=ProductSerializer(queryset).data
            # return Response(data=data)

            #02.Another way (error 404 is bundled together with request )
            obj=get_object_or_404(Product,pk=pk)
            data=ProductSerializer(obj,many=False).data
            return Response(data=data)
        else:
            #List view
            queryset=Product.objects.all()
            data=ProductSerializer(queryset,many=True).data
            return Response(data=data)
        
    if method=='POST':
        
        #create an item in the DB that it queryset=Product.objects.filter(pk=pk)
            # if not queryset.exists():
            #     raise Http404
            # data=ProductSerializer(queryset).data
            # return Response(data=data)queryset=Product.objects.filter(pk=pk)
            # if not queryset.exists():
            #     raise Http404
            # data=ProductSerializer(queryset).data
            # return Response(data=data)

        serializer=ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            #
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content') or None
            if content is None:
                content=title
            serializer.save(content=content)
            print(serializer.data)
            return Response(serializer.data)
        return Response({"Invalid":"Not data",status:400})