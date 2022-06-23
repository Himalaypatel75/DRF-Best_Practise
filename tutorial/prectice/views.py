from django.forms import ValidationError
from django.shortcuts import render
from .serializer import TaskSerializer
from rest_framework import generics
from .models import Project

# Create your views here.

class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(TaskCreateView, self).get_serializer(*args, **kwargs)

        

    def post(self, request, *args, **kwargs):

        project = Project.objects.get(id=kwargs["project_id"])

        if isinstance(request.data, list):
            for item in request.data:
                item["project"] = project
        else:
            raise ValidationError("Invalid Input")

        return super(TaskCreateView, self).post(request, *args, **kwargs)