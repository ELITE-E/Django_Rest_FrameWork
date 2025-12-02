from django.urls import path

from . import views

urlpatterns=[
    #Working with DRF based views
    #path ("",views.product_details_view)
path('',views.product_mixin_view),#Mixins in action 

#1.55--->Creating the update and delete APIViews url
path('<int:pk>/update/',views.product_update_view),
path('<int:pk>/delete/',views.product_delete_view),
#path('<int:pk>,views.product_detail_view)

path('<int:pk>',views.product_mixin_view)#Mixins in action fo pk 

    #Working with function based views
#path('',views.product_alt_view),
#path('<int:pk>/',views.product_alt_view)

]