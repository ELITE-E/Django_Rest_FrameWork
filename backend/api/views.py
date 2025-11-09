import json
from django.forms.models import model_to_dict#module that provides tools for creating forms directly from Django models
#from django.http import JsonResponse,HttpResponse

#convertind django view-->RF view
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product

@api_view(["GET"]) #you can specify the req methods you want the view to handle in here 
def api_home(request,*args,**kwargs):
    """
    DRF API View

    """
    model_data=Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        #00.The hard way 

        # data['title'] =model_data.title
        # data['content']=model_data.content
        # data['price']=model_data.price

        #01. clean way
        #the fields param allows you to specify what you want title,price both or all
        data=model_to_dict(model_data,fields=['id','title'])
    #a http res
    #return HttpResponse(json_data_str,headers={"content-type":"application/json"})
    
    #json res
    #return JsonResponse(data)

    #DRF res 
    return Response(data)