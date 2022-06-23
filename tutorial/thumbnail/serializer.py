from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from .models import Thumbnail
from rest_framework import serializers

class ThumbnailSerializer(ModelSerializer):
    # image_thumbnail = SerializerMethodField()
    image_thumbnail = serializers.ImageField(read_only=True)
    class Meta:
        model = Thumbnail
        fields = ('id','name','image','image_thumbnail')

    # def get_ThumbNail_images(self, obj):
    #     qs = Thumbnail.objects.all()[0]
    #     thumb = qs.image_thumbnail.url
    #     return thumb


class ThumbnailDeleteSerializer(ModelSerializer):

    class Meta:
        model = Thumbnail
        fields = '__all__'
