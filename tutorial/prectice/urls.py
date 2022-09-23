from django.urls import path, include  
from .views import TaskCreateView  , ProjectList
  
urlpatterns = [  
    path('task/', TaskCreateView.as_view(), name='taskcreate'),
    path('list/', ProjectList.as_view(), name='list_project'),
]  