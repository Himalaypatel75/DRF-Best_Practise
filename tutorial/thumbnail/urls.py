from django.urls import path, include  
from .views import ThumbnailListAPIView, ThumbnailUpdateListAPIView

  
urlpatterns = [  
    path('add', ThumbnailListAPIView.as_view(), name='thumbnail'),
    path('add/<int:pk>', ThumbnailUpdateListAPIView.as_view(), name='update_thumb')  
]  