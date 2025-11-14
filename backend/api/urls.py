from django.urls import path,include

from . import views
#from .views import api_home/roughtly the same as above hehehe

urlpatterns=[
    path('',views.api_home),
    #path('products/',include(products.urls))--->Another method of including the api endpoit
]