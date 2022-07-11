from email.policy import default
from django.db import models
from imagekit import ImageSpec
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class Thumbnail(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null = True)
    image_thumbnail = ProcessedImageField(upload_to='mediafiles',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60}, null = True)

 