# Generated by Django 3.2.8 on 2022-07-11 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulkexample', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
