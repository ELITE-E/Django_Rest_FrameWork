from django.urls import path

from . import views
#from .views import api_home/roughtly the same as above hehehe

urlPatterns=[
    path('',views.api_home)
]