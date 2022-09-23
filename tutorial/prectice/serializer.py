from django.db import IntegrityError
from django.forms import ValidationError
from rest_framework import serializers
from .models import Task, Project




class BulkCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        result = [self.child.create(attrs) for attrs in validated_data]

        try:
            self.child.Meta.model.objects.bulk_create(result)
        except IntegrityError as e:
            raise ValidationError(e)

        return result


class TaskSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        instance = Task(**validated_data)

        if isinstance(self._kwargs["data"], dict):
            instance.save()

        return instance

   
    class Meta:
        model = Task
        fields = ("id", "name", "project", "description", "last_modified")
        read_only_fields = ("id", "last_modified")
        list_serializer_class = BulkCreateListSerializer


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
