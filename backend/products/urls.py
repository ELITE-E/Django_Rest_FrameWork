from django.urls import path

from . import views

urlpatterns=[
    #Working with DRF based views
#path('',views.product_list_create_view),
#path('<int:pk>',views.product_detail_view)

    #Working with function based views
path('',views.product_alt_view),
path('<int:pk>/',views.product_alt_view)

]