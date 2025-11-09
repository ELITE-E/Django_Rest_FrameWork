from django.urls import path

from . import views
#from .views import api_home/roughtly the same as above hehehe

urlpatterns=[
    path('',views.api_home),
]