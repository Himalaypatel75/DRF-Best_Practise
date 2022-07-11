from django.urls import path, include  
from .views import ProductView, ProductGetView

  
urlpatterns = [  
    path('product', ProductView.as_view(), name='product') , 
    path('get_product', ProductGetView.as_view(), name='get_product') , 
    # path('email', SendingEmail.as_view(), name='send_email') 
]  