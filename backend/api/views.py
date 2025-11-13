import json
from django.forms.models import model_to_dict#module that provides tools for creating forms directly from Django models
#from django.http import JsonResponse,HttpResponse
#Above import is unnecessary bcoz DRF provides the response that automatically renders res according to the format needed 

#convertind django view-->RF view
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

#@api_view(["GET"]) #you can specify the req methods you want the view to handle in here 

#01.0 Let's see how post works
@api_view(["POST"])
def api_home(request,*args,**kwargs):
    """
    DRF API View
    ---
    data=ProductSerializer(instance/model_data).data
      is cleaner & faster than 
    data=model_to_dict(instance/model_data,fields=['id','title','sale_price'])

    """
   # model_data=Product.objects.all().order_by("?").first()

   #using serializer to access model data
    #instance=Product.objects.all().order_by("?").first()


    #data={}
    #if instance:
        #00.The hard way 

        # data['title'] =model_data.title
        # data['content']=model_data.content
        # data['price']=model_data.price

        #01. clean way
        #the fields param allows you to specify what you want title,price both or all
        #data=model_to_dict(instance,fields=['id','title','sale_price'])

        #03. using a serializer
        #data=ProductSerializer(instance).data
    #a http res
    #ret # def get_discount(self):
    #     return "122"urn HttpResponse(json_data_str,headers={"content-type":"application/json"})
    
    #json res
    #return JsonResponse(data)

    #DRF res 
    #return Response(data)
    #------------------------------------POST METHOD ---------------------------------
    serializer=ProductSerializer(data=request.data )
    if serializer.is_valid():
        instance=serializer.save()
        print(serializer.data)

        instance=serializer.data
        return Response(instance)