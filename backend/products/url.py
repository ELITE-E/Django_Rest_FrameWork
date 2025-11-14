from django.urls import path

from . import views

urlpattern=[

#path('<int:pk>',views.ProductDetailAPIView.as_view())

path('<int:pk>/',views.product_detail_view)

]