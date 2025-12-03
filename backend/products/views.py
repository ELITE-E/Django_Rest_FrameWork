from rest_framework import generics,mixins,permissions,authentication

from rest_framework.response import Response
#from django.http import Http404
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .serializers import ProductSerializer
from .models import Product
from api.mixins import StaffEditorPermissionMixin#Importng the global permission in mixin format
#from ..api.permissions import IsStaffEditorPermission
from api.authentication import TokenAuthentication


class ProductListCreateAPIView(generics.ListCreateAPIView,
                               StaffEditorPermissionMixin #Accessing by a view 3.07---
                               ):
    """
    A combination of List + crete api view 
    """
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #2.30---->Custom permissions 
    #permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]=Obsolete Because of 3.07..Global mixin


    #2.16..--->Authentication& Permissions(Controlling what a user can/cant do)
    #Can be used same in mixins&generics view


    #3.01...-->(What default permissions& auths do we want in our prj.

    # Doing as this for all views is very tedious and not cool )
    #Thats where the default settings&permissions come in --->settings
    #authentication_classes=[authentication.SessionAuthentication,
                            #authentication.TokenAuthentication
                            #TokenAuthentication]
    #permission_classes=[permissions.IsAuthenticatedOrReadOnly]


    #3.07--->From previous chapter ,we set default permissions.But for each view we have tho declare 
    #a permission class.Thats where using mixins comes in 
    #permission_classes-[permissions.IsAdminUser,IsStaffEditorPermission]

    def product_create(self,serializer):
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        price=serializer.validated_data.get('price')
        serializer.save(content=content)


product_list_create_view=ProductListCreateAPIView.as_view()

class  ProductDetailAPIView(generics.RetrieveAPIView,
                            StaffEditorPermissionMixin):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #for specific fields you pass the/it's  pk (primarykey)

product_detail_view=ProductDetailAPIView.as_view()

class  ProductListAPIView(generics.ListAPIView,
                          StaffEditorPermissionMixin):
    """
    But we wont use it 
    """
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

product_list_view=ProductListAPIView.as_view()

#1.55-----> Creating the Updata and delete APIViews

class ProductUpdateAPIView(generics.UpdateAPIView,
                           StaffEditorPermissionMixin):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookupField='pk'

    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content=instance.title


product_update_view=ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

    def perform_destroy(self,instance):
        super().perform_destroy(instance)

product_delete_view=ProductDeleteAPIView.as_view()
#2.05---->Mixins and Generic APIViews
#mixins are reusable classes that provide the core logic for standard data operations 
# (CRUD: Create, Retrieve, Update, Delete) in API views, significantly reducing boilerplate code. 
    #Common DRF Mixins
    #DRF provides several built-in mixins, each corresponding to a standard HTTP verb and data operation: 
    #ListModelMixin: Handles GET requests to list a collection of records (e.g., fetching all products).
    #CreateModelMixin: Handles POST requests to create a new record (e.g., adding a new user).
    #RetrieveModelMixin: Handles GET requests to retrieve a single specific record using a lookup field (e.g., fetching a product by its ID).
    #UpdateModelMixin: Handles PUT and PATCH requests to modify an existing record.
    #DestroyModelMixin: Handles DELETE requests to remove a record. 
class ProductMixinsView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,#Cares about pk
    generics.GenericAPIView):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

    def get(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        if pk is not None:
            return  self.retreive(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    

product_mixin_view=ProductMixinsView.as_view()


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