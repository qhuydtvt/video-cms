# Generated by Django 2.0 on 2017-12-15 00:26

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vid', '0002_auto_20171215_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='media/videos'), upload_to=''),
        ),
    ]
