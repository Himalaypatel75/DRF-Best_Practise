from datetime import timezone
from unittest import signals
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    last_modified = models.DateTimeField(auto_now=True)


class Task(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=200)
    last_modified = models.DateTimeField(auto_now=True)
