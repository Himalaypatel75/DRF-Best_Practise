from django.shortcuts import render
from pytz import timezone
 
from rest_framework import generics, status  
from rest_framework.response import Response  
  
from bulkexample import models
from .serializer import ProductSerializer
from .models import Product
from rest_framework.views import APIView
import threading
from threading import Thread
from django.core.mail import send_mail
  
# class ProductView(generics.ListCreateAPIView):  
#     queryset = models.Product.objects.all()  
#     serializer_class = ProductSerializer
  
#     def create(self, request, *args, **kwargs):  
#         serializer = self.get_serializer(data=request.data, many=True)  
#         serializer.is_valid(raise_exception=True)  
  
#         try:  
#             self.perform_create(serializer)  
#             return Response(serializer.data, status=status.HTTP_201_CREATED)  
#         except:  
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
# # Create your views here.

class ProductView(generics.ListCreateAPIView):  
    serializer_class = ProductSerializer  
    http_method_names = ["post"]
    def get_serializer(self, *args, **kwargs):  
        if isinstance(kwargs.get("data", {}), list):  
            kwargs["many"] = True  
  
        return super(ProductView, self).get_serializer(*args, **kwargs)  

    # def get(self, *args, **kwargs):
    #     # query = Product.objects.all()
    #     # # serializer = ProductSerializer(query, many=True).data
    #     return Response(status=status.HTTP_201_CREATED)  


class email_send(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run (self):
        send_mail(
            'Subject here',
            'Here is the message.',
            'no-reply@xduce.com',
            ['Himalay.patel@XDuce.com'],
            fail_silently=False,
        )
        print("aaaaaaa")

class SendingEmail(APIView):

    def get(self, *args, **kwargs):
        query = Product.objects.all()
        serializer = ProductSerializer
        email_send().start()
        print("bbbbb")
        return Response("Email send quieckly")