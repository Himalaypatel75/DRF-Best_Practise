from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Thumbnail(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null = True)
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})

