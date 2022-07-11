# Generated by Django 3.2.8 on 2022-06-24 12:07

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnail',
            name='image_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default=None, null=True, upload_to='mediafiles'),
        ),
    ]