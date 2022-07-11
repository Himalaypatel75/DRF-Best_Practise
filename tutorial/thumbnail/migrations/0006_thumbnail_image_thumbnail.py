# Generated by Django 3.2.8 on 2022-06-24 16:21

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnail', '0005_remove_thumbnail_image_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnail',
            name='image_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='mediafiles'),
        ),
    ]
