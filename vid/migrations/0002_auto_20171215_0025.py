# Generated by Django 2.0 on 2017-12-15 00:25

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/videos'), upload_to=''),
        ),
    ]