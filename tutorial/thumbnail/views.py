from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import ThumbnailSerializer, ThumbnailDeleteSerializer
from .models import Thumbnail
# Create your views here.


class ThumbnailListAPIView(ListCreateAPIView):
    serializer_class = ThumbnailSerializer
    queryset = Thumbnail.objects.all()

    # def post(self, request, *args, **kwargs):
    #     data = request.data.get('items', request.data)
    #     many = isinstance(data, list)
    #     print (data, many)
    #     return self.create(request, *args, **kwargs)

class ThumbnailUpdateListAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ThumbnailDeleteSerializer
    queryset = Thumbnail.objects.all()