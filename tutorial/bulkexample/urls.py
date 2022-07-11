from django.urls import path, include  
from .views import ProductView, ProductGetView, ProductUpdateView

  
urlpatterns = [  
    path('product', ProductView.as_view(), name='product') , 
    path('product/update', ProductUpdateView.as_view(), name='product_update') , 
    path('get_product', ProductGetView.as_view(), name='get_product') , 
    # path('email', SendingEmail.as_view(), name='send_email') 
]  