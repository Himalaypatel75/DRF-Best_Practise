from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import ThumbnailSerializer, ThumbnailDeleteSerializer
from .models import Thumbnail
# Create your views here.


class ThumbnailListAPIView(ListCreateAPIView):
    serializer_class = ThumbnailSerializer
    queryset = Thumbnail.objects.all()



class ThumbnailUpdateListAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ThumbnailDeleteSerializer
    queryset = Thumbnail.objects.all()