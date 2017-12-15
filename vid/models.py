from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=60)
    video = models.FileField()
    image = models.FileField(null=True, blank=True)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.title
