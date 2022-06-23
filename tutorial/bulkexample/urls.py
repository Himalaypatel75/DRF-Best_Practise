from django.urls import path, include  
from .views import ProductView  , SendingEmail

  
urlpatterns = [  
    path('product', ProductView.as_view(), name='product') , 
    path('email', SendingEmail.as_view(), name='send_email') 
]  