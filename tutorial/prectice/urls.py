from django.urls import path, include  
from .views import TaskCreateView  
  
urlpatterns = [  
    path('task/', TaskCreateView.as_view(), name='taskcreate')  
]  